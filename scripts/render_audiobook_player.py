#!/usr/bin/env python3
"""Audiobook Web Player Generator for Realized Press Monorepo.

Generates a standalone, responsive, modern HTML5 web player for book audiobooks.
Supports both local offline playback and direct streaming from GitHub Releases.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

from merge_book_chapters import iter_chapter_files, repo_root, resolve_book_path

WPM_SPEAKING_RATE = 150


def extract_chapter_title(md_path: Path) -> str:
    content = md_path.read_text(encoding="utf-8")
    m = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
    if m2:
        return m2.group(1).strip()
    return md_path.stem.replace("-", " ").title()


def build_player_html(
    book_title: str,
    subtitle: str,
    release_tag: str,
    github_repo: str,
    chapters: list[dict],
) -> str:
    chapters_json_entries = []
    for c in chapters:
        online_url = f"https://github.com/{github_repo}/releases/download/{release_tag}/{c['stem']}.mp3"
        chapters_json_entries.append(
            f"""    {{
      index: {c['num']},
      stem: {json_repr(c['stem'])},
      title: {json_repr(c['title'])},
      words: {c['words']},
      minutes: "{c['minutes']:.1f}",
      hasLocalMp3: {str(c['has_mp3']).lower()},
      hasLocalWav: {str(c['has_wav']).lower()},
      onlineUrl: {json_repr(online_url)},
      localUrl: {json_repr(c['local_url'])}
    }}"""
        )
    chapters_js = "[\n" + ",\n".join(chapters_json_entries) + "\n  ]"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(book_title)} — Audiobook Player</title>
  <style>
    :root {{
      --bg: #0d1117;
      --card-bg: #161b22;
      --border: #30363d;
      --gold: #d29922;
      --gold-light: #f1e05a;
      --text: #e6edf3;
      --text-muted: #8b949e;
      --accent: #2f81f7;
      --success: #3fb950;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding-bottom: 120px;
    }}
    .container {{
      max-width: 860px;
      margin: 0 auto;
      padding: 32px 20px;
    }}
    header {{
      text-align: center;
      margin-bottom: 32px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border);
    }}
    .series-badge {{
      display: inline-block;
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--gold);
      background: rgba(210, 153, 34, 0.12);
      border: 1px solid rgba(210, 153, 34, 0.3);
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    h1 {{
      font-size: 2.2rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 650px;
      margin: 0 auto 16px;
    }}
    .stream-toggle {{
      display: inline-flex;
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 4px;
      margin-top: 12px;
    }}
    .stream-toggle button {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.2s;
    }}
    .stream-toggle button.active {{
      background: var(--gold);
      color: #000;
      font-weight: 600;
    }}
    .playlist {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .chapter-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      transition: all 0.2s ease;
      cursor: pointer;
    }}
    .chapter-card:hover {{
      border-color: var(--gold);
      transform: translateY(-1px);
    }}
    .chapter-card.playing {{
      border-color: var(--gold);
      background: rgba(210, 153, 34, 0.08);
    }}
    .chapter-meta {{
      display: flex;
      align-items: center;
      gap: 16px;
      flex: 1;
      min-width: 0;
    }}
    .chapter-num {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--gold);
      width: 32px;
      text-align: center;
      flex-shrink: 0;
    }}
    .chapter-info {{
      min-width: 0;
    }}
    .chapter-title {{
      font-size: 1.05rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .chapter-stats {{
      font-size: 0.8rem;
      color: var(--text-muted);
      display: flex;
      gap: 12px;
    }}
    .card-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}
    .status-pill {{
      font-size: 0.75rem;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 600;
    }}
    .status-available {{
      background: rgba(63, 185, 80, 0.15);
      color: var(--success);
      border: 1px solid rgba(63, 185, 80, 0.3);
    }}
    .status-queued {{
      background: rgba(139, 148, 158, 0.15);
      color: var(--text-muted);
      border: 1px solid rgba(139, 148, 158, 0.3);
    }}
    .play-btn {{
      background: var(--gold);
      color: #000;
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.1rem;
      font-weight: 700;
      transition: transform 0.15s ease;
    }}
    .play-btn:hover {{
      transform: scale(1.08);
    }}
    .play-btn:disabled {{
      background: #21262d;
      color: #484f58;
      cursor: not-allowed;
      transform: none;
    }}

    /* Persistent Bottom Player Dock */
    .player-dock {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #090d13;
      border-top: 1px solid var(--border);
      padding: 12px 20px;
      box-shadow: 0 -8px 24px rgba(0,0,0,0.6);
      z-index: 1000;
    }}
    .dock-container {{
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .dock-upper {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .dock-track {{
      flex: 1;
      min-width: 0;
    }}
    .dock-track-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .dock-track-sub {{
      font-size: 0.75rem;
      color: var(--gold);
    }}
    .dock-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .dock-btn {{
      background: transparent;
      border: none;
      color: var(--text);
      font-size: 1rem;
      cursor: pointer;
      padding: 6px;
      border-radius: 6px;
    }}
    .dock-btn:hover {{
      color: var(--gold);
    }}
    .dock-btn-main {{
      background: var(--gold);
      color: #000;
      border-radius: 50%;
      width: 42px;
      height: 42px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      font-weight: 700;
    }}
    .dock-btn-main:hover {{
      background: var(--gold-light);
    }}
    .speed-select {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 0.8rem;
      border-radius: 6px;
      padding: 4px 6px;
      cursor: pointer;
    }}
    .dock-lower {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .progress-bar {{
      flex: 1;
      height: 6px;
      background: #21262d;
      border-radius: 3px;
      cursor: pointer;
      position: relative;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--gold);
      border-radius: 3px;
      width: 0%;
      transition: width 0.1s linear;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="series-badge">Realized Press Imprint · Official Audiobook</div>
      <h1>{html.escape(book_title)}</h1>
      <p class="subtitle">{html.escape(subtitle)}</p>
      <div class="stream-toggle">
        <button id="btn-stream-online" class="active" onclick="setStreamMode('online')">Stream Online (GitHub Release)</button>
        <button id="btn-stream-local" onclick="setStreamMode('local')">Local Audio</button>
      </div>
    </header>

    <div class="playlist" id="playlist">
      <!-- Populated dynamically via JS -->
    </div>
  </div>

  <div class="player-dock">
    <div class="dock-container">
      <div class="dock-upper">
        <div class="dock-track">
          <div class="dock-track-title" id="dock-title">Select a chapter to play</div>
          <div class="dock-track-sub" id="dock-status">Gemini 2.5 Flash TTS (Voice: Kore)</div>
        </div>
        <div class="dock-controls">
          <button class="dock-btn" onclick="skip(-15)" title="Rewind 15 seconds">↺ 15s</button>
          <button class="dock-btn dock-btn-main" id="dock-play" onclick="togglePlay()">▶</button>
          <button class="dock-btn" onclick="skip(15)" title="Forward 15 seconds">15s ↻</button>
          <select class="speed-select" id="speed-select" onchange="changeSpeed(this.value)">
            <option value="0.75">0.75x</option>
            <option value="1.0" selected>1.0x</option>
            <option value="1.25">1.25x</option>
            <option value="1.5">1.5x</option>
            <option value="1.75">1.75x</option>
            <option value="2.0">2.0x</option>
          </select>
        </div>
      </div>
      <div class="dock-lower">
        <span id="cur-time">0:00</span>
        <div class="progress-bar" id="progress-bar" onclick="seek(event)">
          <div class="progress-fill" id="progress-fill"></div>
        </div>
        <span id="total-time">0:00</span>
      </div>
    </div>
  </div>

  <audio id="audio-engine" preload="metadata"></audio>

  <script>
    const chapters = {chapters_js};
    let currentIdx = 0;
    let streamMode = 'online';
    const audio = document.getElementById('audio-engine');
    const dockTitle = document.getElementById('dock-title');
    const dockStatus = document.getElementById('dock-status');
    const dockPlay = document.getElementById('dock-play');
    const curTime = document.getElementById('cur-time');
    const totalTime = document.getElementById('total-time');
    const progressFill = document.getElementById('progress-fill');

    function renderPlaylist() {{
      const container = document.getElementById('playlist');
      container.innerHTML = '';
      chapters.forEach((ch, idx) => {{
        const isAvailable = streamMode === 'online' || ch.hasLocalMp3 || ch.hasLocalWav;
        const card = document.createElement('div');
        card.className = 'chapter-card' + (idx === currentIdx && !audio.paused ? ' playing' : '');
        card.onclick = () => isAvailable && playChapter(idx);
        card.innerHTML = `
          <div class="chapter-meta">
            <div class="chapter-num">${{String(ch.index).padStart(2, '0')}}</div>
            <div class="chapter-info">
              <div class="chapter-title">${{ch.title}}</div>
              <div class="chapter-stats">
                <span>${{ch.words.toLocaleString()}} words</span>
                <span>•</span>
                <span>~${{ch.minutes}} min</span>
              </div>
            </div>
          </div>
          <div class="card-actions">
            ${{isAvailable
              ? '<span class="status-pill status-available">Audio Available</span>'
              : '<span class="status-pill status-queued">Queued</span>'}}
            <button class="play-btn" ${{!isAvailable ? 'disabled' : ''}}>
              ${{idx === currentIdx && !audio.paused ? '⏸' : '▶'}}
            </button>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function setStreamMode(mode) {{
      streamMode = mode;
      document.getElementById('btn-stream-online').classList.toggle('active', mode === 'online');
      document.getElementById('btn-stream-local').classList.toggle('active', mode === 'local');
      renderPlaylist();
      if (audio.src) {{
        loadChapter(currentIdx, !audio.paused);
      }}
    }}

    function loadChapter(idx, autoPlay = false) {{
      currentIdx = idx;
      const ch = chapters[idx];
      dockTitle.innerText = `${{String(ch.index).padStart(2, '0')}}. ${{ch.title}}`;
      const url = streamMode === 'online' ? ch.onlineUrl : ch.localUrl;
      audio.src = url;
      dockStatus.innerText = streamMode === 'online' ? `Streaming via GitHub Releases (${{ch.stem}}.mp3)` : `Local Audio (${{url}})`;
      if (autoPlay) {{
        audio.play().catch(e => console.log('Autoplay deferred:', e));
      }}
      renderPlaylist();
    }}

    function playChapter(idx) {{
      if (currentIdx === idx && !audio.paused) {{
        audio.pause();
      }} else if (currentIdx === idx && audio.paused && audio.src) {{
        audio.play();
      }} else {{
        loadChapter(idx, true);
      }}
    }}

    function togglePlay() {{
      if (!audio.src) {{
        loadChapter(0, true);
        return;
      }}
      if (audio.paused) {{
        audio.play();
      }} else {{
        audio.pause();
      }}
    }}

    function skip(seconds) {{
      if (audio.duration) {{
        audio.currentTime = Math.max(0, Math.min(audio.duration, audio.currentTime + seconds));
      }}
    }}

    function changeSpeed(speed) {{
      audio.playbackRate = parseFloat(speed);
    }}

    function formatTime(s) {{
      if (isNaN(s)) return "0:00";
      const m = Math.floor(s / 60);
      const rem = Math.floor(s % 60);
      return `${{m}}:${{rem < 10 ? '0' : ''}}${{rem}}`;
    }}

    function seek(e) {{
      const rect = document.getElementById('progress-bar').getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      if (audio.duration) {{
        audio.currentTime = pos * audio.duration;
      }}
    }}

    audio.addEventListener('play', () => {{
      dockPlay.innerText = '⏸';
      renderPlaylist();
    }});

    audio.addEventListener('pause', () => {{
      dockPlay.innerText = '▶';
      renderPlaylist();
    }});

    audio.addEventListener('timeupdate', () => {{
      curTime.innerText = formatTime(audio.currentTime);
      totalTime.innerText = formatTime(audio.duration);
      if (audio.duration) {{
        progressFill.style.width = `${{(audio.currentTime / audio.duration) * 100}}%`;
      }}
    }});

    audio.addEventListener('ended', () => {{
      if (currentIdx + 1 < chapters.length) {{
        loadChapter(currentIdx + 1, true);
      }}
    }});

    // Initial render
    renderPlaylist();
    loadChapter(0, false);
  </script>
</body>
</html>
"""


def json_repr(val: str) -> str:
    import json
    return json.dumps(val)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render interactive HTML5 audiobook web player.")
    parser.add_argument("book", type=Path, help="Book directory path (e.g. series/parenthood-atlas)")
    parser.add_argument("--release-tag", default="v1.0-rc1", help="GitHub Release tag for online streaming (default: v1.0-rc1)")
    parser.add_argument("--repo", default="ralfcam/realized-press", help="GitHub repository (owner/repo)")
    args = parser.parse_args()

    root = repo_root()
    book_path = resolve_book_path(root, args.book)
    chapters_dir = book_path / "chapters"
    audio_dir = book_path / "audiobook"
    publishing_dir = book_path / "publishing"
    publishing_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

    md_files = iter_chapter_files(chapters_dir)
    if not md_files:
        print(f"error: no chapters found in {chapters_dir}", file=sys.stderr)
        sys.exit(1)

    book_title = book_path.name.replace("-", " ").title()
    subtitle = "Field Guide & Reference"
    series_yaml = book_path / "series.yaml"
    if not series_yaml.exists():
        series_yaml = book_path.parent / "series.yaml"
    if series_yaml.exists():
        import yaml
        try:
            cfg = yaml.safe_load(series_yaml.read_text(encoding="utf-8"))
            book_title = cfg.get("title", book_title)
            subtitle = cfg.get("subtitle", subtitle)
        except Exception:
            pass

    chapters_meta = []
    for idx, f in enumerate(md_files, 1):
        content = f.read_text(encoding="utf-8")
        words = len(content.split())
        title = extract_chapter_title(f)
        stem = f.stem
        has_mp3 = (audio_dir / f"{stem}.mp3").exists()
        has_wav = (audio_dir / f"{stem}.wav").exists()
        local_url = f"{stem}.mp3" if has_mp3 else f"{stem}.wav"
        chapters_meta.append({
            "num": idx,
            "stem": stem,
            "title": title,
            "words": words,
            "minutes": words / WPM_SPEAKING_RATE,
            "has_mp3": has_mp3,
            "has_wav": has_wav,
            "local_url": local_url,
        })

    html_content = build_player_html(
        book_title=book_title,
        subtitle=subtitle,
        release_tag=args.release_tag,
        github_repo=args.repo,
        chapters=chapters_meta,
    )

    out_file1 = publishing_dir / "audiobook-player.html"
    out_file2 = audio_dir / "index.html"
    out_file1.write_text(html_content, encoding="utf-8")
    out_file2.write_text(html_content, encoding="utf-8")

    print(f"Wrote Audiobook Web Player to:")
    print(f"  - {out_file1}")
    print(f"  - {out_file2}")


if __name__ == "__main__":
    main()
