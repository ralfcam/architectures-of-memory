#!/usr/bin/env python3
"""Gemini TTS / Audiobook Synthesis Pipeline for Multi-Series Editorial Monorepo.

Transforms book chapters into clean spoken transcripts (stripping YAML frontmatter,
footnotes, Sources, and Notes), segments into semantic blocks, packs whole blocks
into TTS chunks without splitting, estimates speaking duration (--dry-run),
synthesizes 24kHz WAV audio files via Gemini 2.5 TTS, encodes MP3s, and outputs
zero-drift ground-truth audio timing sidecars (*.timings.json).
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import urllib.request
import wave
from pathlib import Path

from audio_sync_utils import (
    BYTES_PER_SECOND,
    SAMPLE_RATE,
    WPM_SPEAKING_RATE,
    build_timings_manifest,
    extract_semantic_blocks,
    pack_semantic_blocks,
    save_timings_manifest,
)
from merge_book_chapters import iter_chapter_files, repo_root, resolve_book_path


def synthesize_chunk_pcm(text: str, voice: str, model: str, api_key: str) -> bytes:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Narrate the following nonfiction audiobook passage in a measured, "
                            "clear, analytic, and engaging documentary tone:\n\n" + text
                        )
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {
                    "prebuiltVoiceConfig": {
                        "voiceName": voice,
                    }
                }
            },
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("No candidates returned from Gemini TTS API.")
    parts = (candidates[0].get("content") or {}).get("parts") or []
    for p in parts:
        inline = p.get("inlineData") or {}
        if inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError("No inlineData audio returned in Gemini response.")


def write_wav(out_path: Path, pcm_bytes: bytes, sample_rate: int = SAMPLE_RATE) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit linear PCM
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)


def load_dotenv(root: Path) -> None:
    env_path = root / ".env"
    if env_path.is_file():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip("'\"")
                if k and k not in os.environ:
                    os.environ[k] = v


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Gemini TTS audiobook generator with zero-drift timing sidecars.")
    parser.add_argument("book", type=Path, help="Book directory (e.g. series/architectures-of-memory/book-01-vanishing-signal or series/parenthood-atlas)")
    parser.add_argument("--chapter", default=None, help="Filter to a specific chapter prefix (e.g. '01' or '07')")
    parser.add_argument("--voice", default="Kore", help="Gemini prebuilt voice name (default: Kore)")
    parser.add_argument("--model", default="gemini-2.5-flash-preview-tts", help="Gemini TTS model")
    parser.add_argument("--max-chars", type=int, default=3500, help="Max characters per TTS request chunk")
    parser.add_argument("--dry-run", action="store_true", help="Estimate duration, blocks & chunk counts without calling API")
    parser.add_argument("--encode-mp3-only", action="store_true", help="Encode existing WAVs in audiobook/ to MP3 without calling Gemini")
    args = parser.parse_args()

    root = repo_root()
    load_dotenv(root)
    book_path = resolve_book_path(root, args.book)
    chapters_dir = book_path / "chapters"
    out_dir = book_path / "audiobook"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.encode_mp3_only:
        ffmpeg_bin = shutil.which("ffmpeg")
        if not ffmpeg_bin:
            print("error: ffmpeg not found in PATH.", file=sys.stderr)
            sys.exit(1)
        wav_files = sorted(out_dir.glob("*.wav"))
        if not wav_files:
            print("no WAV files found in audiobook/ to encode.", file=sys.stderr)
            sys.exit(0)
        for w in wav_files:
            mp3 = out_dir / f"{w.stem}.mp3"
            print(f"Encoding {w.name} -> {mp3.name}...")
            subprocess.run([ffmpeg_bin, "-y", "-i", str(w), "-codec:a", "libmp3lame", "-b:a", "128k", str(mp3)], check=True)
        # Refresh player
        render_script = root / "scripts" / "render_audiobook_player.py"
        if render_script.exists():
            subprocess.run([sys.executable, str(render_script), str(book_path)])
        return

    if not chapters_dir.is_dir():
        print(f"error: chapters directory not found: {chapters_dir}", file=sys.stderr)
        sys.exit(1)

    md_files = iter_chapter_files(chapters_dir)
    if args.chapter:
        prefix = args.chapter.zfill(2)
        md_files = [f for f in md_files if f.name.startswith(prefix)]

    if not md_files:
        print("error: no matching chapter files found.", file=sys.stderr)
        sys.exit(1)

    total_words = 0
    total_blocks = 0
    total_chunks = 0
    rows: list[tuple[str, int, int, int, float]] = []

    for f in md_files:
        content = f.read_text(encoding="utf-8")
        blocks = extract_semantic_blocks(content)
        chunks = pack_semantic_blocks(blocks, max_chars=args.max_chars)
        words = sum(b["words"] for b in blocks)
        minutes = words / WPM_SPEAKING_RATE
        total_words += words
        total_blocks += len(blocks)
        total_chunks += len(chunks)
        rows.append((f.name, words, len(blocks), len(chunks), minutes))

    print(f"# Audiobook TTS Plan — {book_path.name} (Voice: {args.voice})")
    print(f"{'Chapter':<38} {'Words':>7} {'Blocks':>7} {'Chunks':>7} {'Est. Min':>9}")
    print("-" * 73)
    for name, words, n_blocks, n_chunks, mins in rows:
        print(f"{name:<38} {words:>7,d} {n_blocks:>7,d} {n_chunks:>7,d} {mins:>8.1f}m")
    print("-" * 73)
    total_min = total_words / WPM_SPEAKING_RATE
    print(f"{'TOTAL':<38} {total_words:>7,d} {total_blocks:>7,d} {total_chunks:>7,d} {total_min:>8.1f}m ({total_min / 60:.2f} hrs)")

    if args.dry_run:
        return

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("\nerror: set GEMINI_API_KEY in environment to synthesize audio (or use --dry-run).", file=sys.stderr)
        sys.exit(1)

    ffmpeg_bin = shutil.which("ffmpeg")
    for f in md_files:
        content = f.read_text(encoding="utf-8")
        blocks = extract_semantic_blocks(content)
        chunks = pack_semantic_blocks(blocks, max_chars=args.max_chars)
        pcm_all = bytearray()
        chunk_durations_sec: list[float] = []
        chunk_pcm_bytes: list[int] = []

        for idx, chunk in enumerate(chunks, 1):
            print(f"Synthesizing {f.stem} [chunk {idx}/{len(chunks)}] ({chunk['total_words']} words, {len(chunk['blocks'])} blocks)...")
            pcm = synthesize_chunk_pcm(chunk["spoken_text"], voice=args.voice, model=args.model, api_key=api_key)
            dur = len(pcm) / BYTES_PER_SECOND
            chunk_durations_sec.append(dur)
            chunk_pcm_bytes.append(len(pcm))
            pcm_all.extend(pcm)
            print(f"  -> Received {len(pcm):,d} PCM bytes ({dur:.2f}s narration)")

        wav_path = out_dir / f"{f.stem}.wav"
        write_wav(wav_path, bytes(pcm_all))
        print(f"Wrote master WAV: {wav_path}")

        # Build and save zero-drift timings sidecar JSON
        manifest = build_timings_manifest(f.stem, chunks, chunk_durations_sec, chunk_pcm_bytes)
        timings_path = out_dir / f"{f.stem}.timings.json"
        save_timings_manifest(manifest, timings_path)
        print(f"Wrote zero-drift ground-truth timings sidecar: {timings_path}")

        if ffmpeg_bin:
            mp3_path = out_dir / f"{f.stem}.mp3"
            res = subprocess.run(
                [ffmpeg_bin, "-y", "-i", str(wav_path), "-codec:a", "libmp3lame", "-b:a", "128k", str(mp3_path)],
                capture_output=True,
            )
            if res.returncode == 0:
                print(f"Wrote web-streamable MP3: {mp3_path}")

    # Re-render audio player
    render_script = root / "scripts" / "render_audiobook_player.py"
    if render_script.exists():
        subprocess.run([sys.executable, str(render_script), str(book_path)])


if __name__ == "__main__":
    main()
