#!/usr/bin/env python3
"""Gemini TTS / Audiobook Synthesis Pipeline for Architectures of Memory.

Transforms book chapters into clean spoken transcripts (stripping footnotes, Sources,
and Notes), chunks by section/paragraph, estimates speaking duration (--dry-run), and
synthesizes 24kHz WAV audio files via Gemini 2.5 TTS (--chapter or full book).
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.request
import wave
from pathlib import Path

from merge_book_chapters import transform_audiobook

WPM_SPEAKING_RATE = 150  # Standard nonfiction audiobook narration pace


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def clean_markdown_for_speech(md_text: str) -> str:
    text = transform_audiobook(md_text)
    # Remove horizontal rules
    text = re.sub(r"^---+\s*$", "", text, flags=re.MULTILINE)
    # Convert headings into clean spoken transitions
    text = re.sub(r"^#\s+(.+)$", r"\1.\n", text, flags=re.MULTILINE)
    text = re.sub(r"^##+\s+(.+)$", r"\n\1.\n", text, flags=re.MULTILINE)
    # Strip bold/italic/code markers while preserving words
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(text: str, max_chars: int = 3500) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for p in paragraphs:
        if current_len + len(p) + 2 > max_chars and current:
            chunks.append("\n\n".join(current))
            current = [p]
            current_len = len(p)
        else:
            current.append(p)
            current_len += len(p) + 2
    if current:
        chunks.append("\n\n".join(current))
    return chunks


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


def write_wav(out_path: Path, pcm_bytes: bytes, sample_rate: int = 24000) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit linear PCM
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Gemini TTS audiobook generator for Architectures of Memory.")
    parser.add_argument("book", type=Path, help="Book directory (e.g. book-01-vanishing-signal)")
    parser.add_argument("--chapter", default=None, help="Filter to a specific chapter prefix (e.g. '01' or '07')")
    parser.add_argument("--voice", default="Kore", help="Gemini prebuilt voice name (default: Kore)")
    parser.add_argument("--model", default="gemini-2.5-flash-preview-tts", help="Gemini TTS model")
    parser.add_argument("--max-chars", type=int, default=3500, help="Max characters per TTS request chunk")
    parser.add_argument("--dry-run", action="store_true", help="Estimate duration & chunk counts without calling API")
    args = parser.parse_args()

    root = repo_root()
    book_path = args.book.resolve() if args.book.is_absolute() else (root / args.book).resolve()
    chapters_dir = book_path / "chapters"
    if not chapters_dir.is_dir():
        print(f"error: chapters directory not found: {chapters_dir}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(chapters_dir.glob("*.md"))
    if args.chapter:
        prefix = args.chapter.zfill(2)
        md_files = [f for f in md_files if f.name.startswith(prefix)]

    if not md_files:
        print("error: no matching chapter files found.", file=sys.stderr)
        sys.exit(1)

    total_words = 0
    total_chunks = 0
    rows: list[tuple[str, int, int, float]] = []

    for f in md_files:
        spoken = clean_markdown_for_speech(f.read_text(encoding="utf-8"))
        words = len(spoken.split())
        chunks = chunk_text(spoken, max_chars=args.max_chars)
        minutes = words / WPM_SPEAKING_RATE
        total_words += words
        total_chunks += len(chunks)
        rows.append((f.name, words, len(chunks), minutes))

    print(f"# Audiobook TTS Plan — {book_path.name} (Voice: {args.voice})")
    print(f"{'Chapter':<44} {'Words':>7} {'Chunks':>7} {'Est. Min':>9}")
    print("-" * 71)
    for name, words, n_chunks, mins in rows:
        print(f"{name:<44} {words:>7,d} {n_chunks:>7,d} {mins:>8.1f}m")
    print("-" * 71)
    total_min = total_words / WPM_SPEAKING_RATE
    print(f"{'TOTAL':<44} {total_words:>7,d} {total_chunks:>7,d} {total_min:>8.1f}m ({total_min / 60:.2f} hrs)")

    if args.dry_run:
        return

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("\nerror: set GEMINI_API_KEY in environment to synthesize audio (or use --dry-run).", file=sys.stderr)
        sys.exit(1)

    out_dir = book_path / "audiobook"
    for f in md_files:
        spoken = clean_markdown_for_speech(f.read_text(encoding="utf-8"))
        chunks = chunk_text(spoken, max_chars=args.max_chars)
        pcm_all = bytearray()
        for idx, ch_text in enumerate(chunks, 1):
            print(f"Synthesizing {f.stem} [chunk {idx}/{len(chunks)}]...")
            pcm_all.extend(synthesize_chunk_pcm(ch_text, voice=args.voice, model=args.model, api_key=api_key))
        wav_path = out_dir / f"{f.stem}.wav"
        write_wav(wav_path, bytes(pcm_all))
        print(f"Wrote {wav_path}")


if __name__ == "__main__":
    main()
