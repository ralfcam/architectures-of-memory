#!/usr/bin/env python3
"""Audiobook Web Player & Marketing Portal Generator for Realized Press Imprint.

Centralizes the standalone HTML5 audiobook web player across all series and volumes,
serving as the foundational architecture for the owned marketing and serial-membership site.

Modes:
  1. Single-Book Mode:
     python scripts/render_audiobook_player.py series/parenthood-atlas
  2. Centralized Imprint Portal Mode:
     python scripts/render_audiobook_player.py --imprint [--output site]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

from merge_book_chapters import iter_chapter_files, repo_root, resolve_book_path, transform_audiobook

WPM_SPEAKING_RATE = 150
DEFAULT_GITHUB_REPO = "ralfcam/realized-press"


def extract_chapter_title(md_path: Path) -> str:
    content = md_path.read_text(encoding="utf-8")
    m = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
    if m2:
        return m2.group(1).strip()
    return md_path.stem.replace("-", " ").title()


def extract_clean_text(md_path: Path) -> str:
    content = md_path.read_text(encoding="utf-8")
    spoken = transform_audiobook(content)
    spoken = re.sub(r"^---+\s*$", "", spoken, flags=re.MULTILINE)
    spoken = re.sub(r"^#\s+(.+)$", r"<h3>\1</h3>", spoken, flags=re.MULTILINE)
    spoken = re.sub(r"^##\s+(.+)$", r"<h4>\1</h4>", spoken, flags=re.MULTILINE)
    spoken = re.sub(r"^###\s+(.+)$", r"<h5>\1</h5>", spoken, flags=re.MULTILINE)
    spoken = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", spoken)
    spoken = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", spoken)
    spoken = re.sub(r"`([^`]+)`", r"<code>\1</code>", spoken)
    paras = [p.strip() for p in spoken.split("\n\n") if p.strip()]
    html_paras = []
    for p in paras:
        if p.startswith("<h"):
            html_paras.append(p)
        else:
            html_paras.append(f"<p>{html.escape(p)}</p>")
    return "\n".join(html_paras)


def collect_book_data(book_path: Path, series_title: str, series_subtitle: str, release_tag: str, repo: str) -> dict:
    chapters_dir = book_path / "chapters"
    audio_dir = book_path / "audiobook"
    book_title = book_path.name.replace("-", " ").title()
    subtitle = series_subtitle

    # Check for series.yaml title if single-volume
    s_yaml = book_path / "series.yaml"
    if s_yaml.exists():
        import yaml
        try:
            cfg = yaml.safe_load(s_yaml.read_text(encoding="utf-8")) or {}
            book_title = cfg.get("title", book_title)
            subtitle = cfg.get("subtitle", subtitle)
        except Exception:
            pass

    # Check for book outline or README title
    outline_file = book_path / "outline.md"
    if outline_file.exists():
        content = outline_file.read_text(encoding="utf-8")
        m = re.search(r"^#\s+Book\s+\d+\s+[—–-]\s*(.+)$", content, flags=re.MULTILINE)
        if m:
            book_title = m.group(1).strip()
        m_sub = re.search(r"^\*\*Subtitle:\*\*\s*(.+)$", content, flags=re.MULTILINE)
        if m_sub:
            subtitle = m_sub.group(1).strip()

    md_files = iter_chapter_files(chapters_dir) if chapters_dir.is_dir() else []
    chapters = []
    for idx, f in enumerate(md_files, 1):
        content = f.read_text(encoding="utf-8")
        words = len(content.split())
        title = extract_chapter_title(f)
        stem = f.stem
        has_mp3 = (audio_dir / f"{stem}.mp3").exists()
        has_wav = (audio_dir / f"{stem}.wav").exists()
        online_url = f"https://github.com/{repo}/releases/download/{release_tag}/{stem}.mp3"
        local_url = f"{stem}.mp3" if has_mp3 else f"{stem}.wav"
        
        # Read transcript excerpt / HTML
        clean_html = extract_clean_text(f)

        chapters.append({
            "num": idx,
            "stem": stem,
            "title": title,
            "words": words,
            "minutes": f"{words / WPM_SPEAKING_RATE:.1f}",
            "hasLocalMp3": has_mp3,
            "hasLocalWav": has_wav,
            "onlineUrl": online_url,
            "localUrl": local_url,
            "transcriptHtml": clean_html,
        })

    return {
        "id": book_path.name,
        "title": book_title,
        "subtitle": subtitle,
        "seriesTitle": series_title,
        "releaseTag": release_tag,
        "chapters": chapters,
        "hasAudio": any(c["hasLocalMp3"] or c["hasLocalWav"] for c in chapters) or (release_tag == "v1.0-rc1" and book_path.name == "parenthood-atlas"),
    }


def scan_all_imprint_books(root: Path, repo: str) -> list[dict]:
    import yaml
    catalog = []
    series_dir = root / "series"
    if not series_dir.is_dir():
        return catalog

    for s in sorted(series_dir.iterdir()):
        if not s.is_dir():
            continue
        s_yaml = s / "series.yaml"
        s_cfg = {}
        if s_yaml.exists():
            try:
                s_cfg = yaml.safe_load(s_yaml.read_text(encoding="utf-8")) or {}
            except Exception:
                pass
        series_title = s_cfg.get("title", s.name.replace("-", " ").title())
        series_subtitle = s_cfg.get("subtitle", "Autonomous Nonfiction Publishing Imprint")

        # Check multi-book vs single-book
        sub_books = [b for b in sorted(s.iterdir()) if b.is_dir() and b.name.startswith("book-")]
        if sub_books:
            for b in sub_books:
                release_tag = "aom-v1.0"
                catalog.append(collect_book_data(b, series_title, series_subtitle, release_tag, repo))
        else:
            release_tag = "v1.0-rc1" if s.name == "parenthood-atlas" else "v1.0"
            catalog.append(collect_book_data(s, series_title, series_subtitle, release_tag, repo))

    return catalog


def render_portal_html(catalog: list[dict], repo: str) -> str:
    catalog_json = json.dumps(catalog, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Realized Press — Imprint Audiobook Portal & Marketing Hub</title>
  <meta name="description" content="Official Audiobook Web Player, Serial Preprints, and Public Evidence Briefs from Realized Press imprint.">
  <style>
    :root {{
      --bg: #0b0f14;
      --card-bg: #141a22;
      --card-hover: #1c232f;
      --border: #26303d;
      --gold: #d29922;
      --gold-light: #f1e05a;
      --gold-dim: rgba(210, 153, 34, 0.15);
      --text: #e6edf3;
      --text-muted: #8b949e;
      --accent: #2f81f7;
      --success: #3fb950;
      --sidebar-w: 320px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Top Navigation */
    .navbar {{
      background: #080c10;
      border-bottom: 1px solid var(--border);
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #fff;
    }}
    .brand-mark {{
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, var(--gold), #9e6a03);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      color: #000;
    }}
    .brand-text h1 {{
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: -0.01em;
    }}
    .brand-text p {{
      font-size: 0.72rem;
      color: var(--gold);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      font-weight: 600;
    }}
    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 6px;
      transition: all 0.2s;
    }}
    .nav-link:hover {{
      color: #fff;
      background: var(--card-bg);
    }}
    .nav-link.btn-gold {{
      background: var(--gold);
      color: #000;
      font-weight: 600;
    }}
    .nav-link.btn-gold:hover {{
      background: var(--gold-light);
    }}

    /* Main Layout */
    .main-layout {{
      display: flex;
      flex: 1;
      max-width: 1440px;
      margin: 0 auto;
      width: 100%;
      padding-bottom: 110px;
    }}

    /* Sidebar Catalog */
    .catalog-sidebar {{
      width: var(--sidebar-w);
      border-right: 1px solid var(--border);
      background: #0a0e13;
      padding: 24px 16px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      flex-shrink: 0;
    }}
    .section-label {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 10px;
      padding-left: 8px;
    }}
    .book-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .book-nav-item {{
      background: transparent;
      border: 1px solid transparent;
      border-radius: 8px;
      padding: 10px 12px;
      text-align: left;
      cursor: pointer;
      color: var(--text);
      display: flex;
      flex-direction: column;
      gap: 2px;
      transition: all 0.2s;
    }}
    .book-nav-item:hover {{
      background: var(--card-bg);
      border-color: var(--border);
    }}
    .book-nav-item.active {{
      background: var(--gold-dim);
      border-color: var(--gold);
    }}
    .book-nav-series {{
      font-size: 0.7rem;
      color: var(--gold);
      font-weight: 600;
      text-transform: uppercase;
    }}
    .book-nav-title {{
      font-size: 0.92rem;
      font-weight: 600;
      color: #fff;
    }}
    .book-nav-meta {{
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      gap: 8px;
    }}

    /* Content Area */
    .content-area {{
      flex: 1;
      padding: 32px 36px;
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }}

    /* Book Hero */
    .book-hero {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px 28px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 24px;
    }}
    .hero-meta {{
      flex: 1;
    }}
    .hero-badge {{
      display: inline-block;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      color: var(--gold);
      background: var(--gold-dim);
      padding: 3px 10px;
      border-radius: 999px;
      margin-bottom: 8px;
      border: 1px solid rgba(210, 153, 34, 0.25);
    }}
    .hero-title {{
      font-size: 1.8rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }}
    .hero-subtitle {{
      font-size: 0.95rem;
      color: var(--text-muted);
      max-width: 700px;
      margin-bottom: 16px;
    }}
    .hero-tags {{
      display: flex;
      gap: 10px;
      font-size: 0.78rem;
      color: var(--text-muted);
      align-items: center;
    }}
    .hero-controls {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 10px;
      flex-shrink: 0;
    }}
    .source-selector {{
      display: inline-flex;
      background: #0b0f14;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 3px;
    }}
    .source-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.78rem;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .source-btn.active {{
      background: var(--gold);
      color: #000;
    }}

    /* View Switcher: Playlist vs Reader */
    .view-tabs {{
      display: flex;
      gap: 12px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }}
    .tab-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 0.92rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }}
    .tab-btn:hover {{
      color: #fff;
    }}
    .tab-btn.active {{
      color: var(--gold);
      background: var(--gold-dim);
    }}

    /* Chapter List */
    .playlist {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .chapter-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .chapter-card:hover {{
      border-color: var(--gold);
      background: var(--card-hover);
    }}
    .chapter-card.active-track {{
      border-color: var(--gold);
      background: var(--gold-dim);
    }}
    .ch-left {{
      display: flex;
      align-items: center;
      gap: 16px;
      flex: 1;
      min-width: 0;
    }}
    .ch-num {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--gold);
      width: 28px;
      text-align: center;
      flex-shrink: 0;
    }}
    .ch-title {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .ch-meta {{
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      gap: 10px;
    }}
    .ch-right {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }}
    .pill {{
      font-size: 0.72rem;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 600;
    }}
    .pill-live {{
      background: rgba(63, 185, 80, 0.15);
      color: var(--success);
      border: 1px solid rgba(63, 185, 80, 0.3);
    }}
    .pill-queue {{
      background: rgba(139, 148, 158, 0.12);
      color: var(--text-muted);
      border: 1px solid var(--border);
    }}
    .btn-play-sm {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--gold);
      color: #000;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.15s ease;
    }}
    .btn-play-sm:hover {{
      transform: scale(1.08);
    }}
    .btn-play-sm:disabled {{
      background: #21262d;
      color: #484f58;
      cursor: not-allowed;
      transform: none;
    }}

    /* Synchronized Reader Pane */
    .reader-pane {{
      display: none;
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 36px 44px;
      max-width: 820px;
      margin: 0 auto;
      font-size: 1.05rem;
      line-height: 1.75;
      color: #d1d7e0;
    }}
    .reader-pane.active {{
      display: block;
    }}
    .reader-pane h3 {{
      font-size: 1.6rem;
      color: #fff;
      margin: 24px 0 12px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }}
    .reader-pane h4 {{
      font-size: 1.25rem;
      color: var(--gold);
      margin: 20px 0 8px;
    }}
    .reader-pane p {{
      margin-bottom: 16px;
    }}
    .reader-pane strong {{
      color: #fff;
    }}

    /* Marketing & Patreon Tier Blueprint */
    .patreon-blueprint {{
      background: #0e141c;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px 28px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .patreon-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .patreon-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
    }}
    .tier-cards {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }}
    .tier-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .tier-card h4 {{
      color: var(--gold);
      font-size: 0.95rem;
    }}
    .tier-card p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .tier-links {{
      margin-top: auto;
      padding-top: 8px;
      font-size: 0.8rem;
    }}
    .tier-links a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .tier-links a:hover {{
      text-decoration: underline;
    }}

    /* Persistent Dock Player */
    .player-dock {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #070a0e;
      border-top: 1px solid var(--border);
      padding: 12px 24px;
      box-shadow: 0 -8px 30px rgba(0,0,0,0.7);
      z-index: 1000;
    }}
    .dock-inner {{
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .dock-main {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .dock-info {{
      flex: 1;
      min-width: 0;
    }}
    .dock-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .dock-sub {{
      font-size: 0.74rem;
      color: var(--gold);
    }}
    .dock-ctrls {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-dock {{
      background: transparent;
      border: none;
      color: var(--text);
      font-size: 0.95rem;
      cursor: pointer;
      padding: 6px 8px;
      border-radius: 6px;
      transition: color 0.15s;
    }}
    .btn-dock:hover {{
      color: var(--gold);
    }}
    .btn-dock-play {{
      background: var(--gold);
      color: #000;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      font-weight: 700;
    }}
    .btn-dock-play:hover {{
      background: var(--gold-light);
    }}
    .dock-speed {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 0.78rem;
      border-radius: 6px;
      padding: 4px 6px;
      cursor: pointer;
    }}
    .dock-progress {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}
    .bar-bg {{
      flex: 1;
      height: 6px;
      background: #1c232d;
      border-radius: 3px;
      cursor: pointer;
      position: relative;
    }}
    .bar-fill {{
      height: 100%;
      background: var(--gold);
      border-radius: 3px;
      width: 0%;
      transition: width 0.1s linear;
    }}

    @media (max-width: 900px) {{
      .main-layout {{ flex-direction: column; }}
      .catalog-sidebar {{ width: 100%; border-right: none; border-bottom: 1px solid var(--border); }}
      .content-area {{ padding: 20px; }}
    }}
  </style>
</head>
<body>
  <nav class="navbar">
    <a href="#" class="brand">
      <div class="brand-mark">R</div>
      <div class="brand-text">
        <h1>Realized Press</h1>
        <p>Book Writing Environment & Multi-Series Imprint</p>
      </div>
    </a>
    <div class="nav-actions">
      <a href="https://github.com/{repo}/releases/tag/v1.0-rc1" target="_blank" class="nav-link">Release v1.0-rc1</a>
      <a href="https://github.com/{repo}" target="_blank" class="nav-link">GitHub Repository</a>
      <a href="https://linear.app/realized/team/ARC/projects/all" target="_blank" class="nav-link btn-gold">Linear ARC Track</a>
    </div>
  </nav>

  <div class="main-layout">
    <!-- Sidebar: Multi-Series Catalog -->
    <aside class="catalog-sidebar">
      <div>
        <div class="section-label">Select Series & Volume</div>
        <div class="book-list" id="book-nav-list">
          <!-- Populated by JS -->
        </div>
      </div>

      <div style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border); font-size: 0.75rem; color: var(--text-muted);">
        <p><strong>Epistemic Contract:</strong> OKF v0.2 atomic evidence cards, 3-lens calibration, 0% padding guarantee.</p>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="content-area">
      <!-- Book Hero Section -->
      <section class="book-hero">
        <div class="hero-meta">
          <div class="hero-badge" id="hero-badge">Series Title</div>
          <h2 class="hero-title" id="hero-title">Book Title</h2>
          <p class="hero-subtitle" id="hero-subtitle">Subtitle</p>
          <div class="hero-tags" id="hero-tags">
            <span id="hero-stat-chapters">0 chapters</span>
            <span>•</span>
            <span id="hero-stat-words">0 words</span>
            <span>•</span>
            <span id="hero-stat-audio">Audio available</span>
          </div>
        </div>
        <div class="hero-controls">
          <div class="source-selector">
            <button class="source-btn active" id="btn-src-online" onclick="setSource('online')">Cloud Stream</button>
            <button class="source-btn" id="btn-src-local" onclick="setSource('local')">Local Audio</button>
          </div>
        </div>
      </section>

      <!-- View Selector (Playlist vs Reader Mode) -->
      <div class="view-tabs">
        <button class="tab-btn active" id="tab-playlist" onclick="switchView('playlist')">Chapter Audio Playlist</button>
        <button class="tab-btn" id="tab-reader" onclick="switchView('reader')">Synchronized Chapter Reader</button>
      </div>

      <!-- Playlist View -->
      <section class="playlist" id="playlist-view">
        <!-- Rendered by JS -->
      </section>

      <!-- Reader View -->
      <section class="reader-pane" id="reader-view">
        <div id="reader-content">
          Select a chapter to read alongside the audio narration.
        </div>
      </section>

      <!-- Marketing & Serial-Membership Foundation -->
      <section class="patreon-blueprint">
        <div class="patreon-header">
          <h3 class="patreon-title">Realized Press Reader Community & Serialization Blueprint</h3>
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 600;">Owned Marketing Site Foundation</span>
        </div>
        <div class="tier-cards">
          <div class="tier-card">
            <h4>1. Public Evidence Briefs</h4>
            <p>Freely available 2-page synthesis briefs distilled from stable OKF v0.2 cards for top-of-funnel organic search.</p>
            <div class="tier-links">
              <a href="https://github.com/{repo}/releases/download/v1.0-rc1/parenthood-atlas-evidence-briefs-compendium.pdf" target="_blank">Download Compendium PDF →</a>
            </div>
          </div>
          <div class="tier-card">
            <h4>2. Core Serial Chapters & Audio</h4>
            <p>Early access chapter preprints, audio drops (Gemini Flash TTS), and developmental fact-check dossiers.</p>
            <div class="tier-links">
              <a href="https://github.com/{repo}/releases/download/v1.0-rc1/01-before-the-child-is-born.mp3" target="_blank">Stream Ch 1 MP3 →</a>
            </div>
          </div>
          <div class="tier-card">
            <h4>3. Insider Reader Edition</h4>
            <p>Complete unpaded review editions (PDF + EPUB 3) and direct feedback loop into Amazon KDP release locks.</p>
            <div class="tier-links">
              <a href="https://github.com/{repo}/releases/download/v1.0-rc1/parenthood-atlas-reader-edition.pdf" target="_blank">Reader Edition PDF →</a>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>

  <!-- Persistent Bottom Player Dock -->
  <footer class="player-dock">
    <div class="dock-inner">
      <div class="dock-main">
        <div class="dock-info">
          <div class="dock-title" id="dock-title">Select a track to play</div>
          <div class="dock-sub" id="dock-sub">Gemini 2.5 Flash TTS Narration</div>
        </div>
        <div class="dock-ctrls">
          <button class="btn-dock" onclick="skip(-15)" title="Rewind 15 seconds">↺ 15s</button>
          <button class="btn-dock btn-dock-play" id="btn-dock-play" onclick="togglePlay()">▶</button>
          <button class="btn-dock" onclick="skip(15)" title="Fast-forward 15 seconds">15s ↻</button>
          <select class="dock-speed" id="dock-speed" onchange="setSpeed(this.value)">
            <option value="0.75">0.75x</option>
            <option value="1.0" selected>1.0x</option>
            <option value="1.25">1.25x</option>
            <option value="1.5">1.5x</option>
            <option value="1.75">1.75x</option>
            <option value="2.0">2.0x</option>
          </select>
        </div>
      </div>
      <div class="dock-progress">
        <span id="time-cur">0:00</span>
        <div class="bar-bg" id="bar-bg" onclick="seek(event)">
          <div class="bar-fill" id="bar-fill"></div>
        </div>
        <span id="time-total">0:00</span>
      </div>
    </div>
  </footer>

  <audio id="audio" preload="metadata"></audio>

  <script>
    const catalog = {catalog_json};
    let currentBookIdx = 0;
    let currentChapterIdx = 0;
    let streamMode = 'online';
    let currentView = 'playlist';

    const audio = document.getElementById('audio');
    const dockTitle = document.getElementById('dock-title');
    const dockSub = document.getElementById('dock-sub');
    const dockPlay = document.getElementById('btn-dock-play');
    const timeCur = document.getElementById('time-cur');
    const timeTotal = document.getElementById('time-total');
    const barFill = document.getElementById('bar-fill');

    function init() {{
      // Prefer parenthood-atlas as first book if present
      const pIdx = catalog.findIndex(b => b.id === 'parenthood-atlas');
      if (pIdx >= 0) currentBookIdx = pIdx;

      renderBookNav();
      selectBook(currentBookIdx);
    }}

    function renderBookNav() {{
      const navList = document.getElementById('book-nav-list');
      navList.innerHTML = '';
      catalog.forEach((b, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'book-nav-item' + (idx === currentBookIdx ? ' active' : '');
        btn.onclick = () => selectBook(idx);
        btn.innerHTML = `
          <span class="book-nav-series">${{b.seriesTitle}}</span>
          <span class="book-nav-title">${{b.title}}</span>
          <span class="book-nav-meta">
            <span>${{b.chapters.length}} ch</span>
            ${{b.hasAudio ? '<span>• Audio live</span>' : ''}}
          </span>
        `;
        navList.appendChild(btn);
      }});
    }}

    function selectBook(idx) {{
      currentBookIdx = idx;
      currentChapterIdx = 0;
      renderBookNav();
      const book = catalog[idx];

      document.getElementById('hero-badge').innerText = book.seriesTitle;
      document.getElementById('hero-title').innerText = book.title;
      document.getElementById('hero-subtitle').innerText = book.subtitle;
      document.getElementById('hero-stat-chapters').innerText = `${{book.chapters.length}} chapters`;
      const totalWords = book.chapters.reduce((sum, c) => sum + c.words, 0);
      document.getElementById('hero-stat-words').innerText = `${{totalWords.toLocaleString()}} words`;
      document.getElementById('hero-stat-audio').innerText = book.hasAudio ? 'Audio Narration Active' : 'Narration Queued';

      renderPlaylist();
      if (book.chapters.length > 0) {{
        loadTrack(0, false);
      }}
    }}

    function renderPlaylist() {{
      const book = catalog[currentBookIdx];
      const container = document.getElementById('playlist-view');
      container.innerHTML = '';

      if (book.chapters.length === 0) {{
        container.innerHTML = `<div style="padding: 32px; text-align: center; color: var(--text-muted); background: var(--card-bg); border-radius: 8px;">Chapters currently in research & drafting phase.</div>`;
        return;
      }}

      book.chapters.forEach((ch, idx) => {{
        const isAvailable = streamMode === 'online' ? (ch.stem === '01-before-the-child-is-born' || ch.hasLocalMp3) : (ch.hasLocalMp3 || ch.hasLocalWav);
        const card = document.createElement('div');
        card.className = 'chapter-card' + (idx === currentChapterIdx && !audio.paused ? ' active-track' : '');
        card.onclick = () => {{
          loadTrack(idx, isAvailable);
          if (currentView === 'reader') updateReader();
        }};
        card.innerHTML = `
          <div class="ch-left">
            <div class="ch-num">${{String(ch.num).padStart(2, '0')}}</div>
            <div>
              <div class="ch-title">${{ch.title}}</div>
              <div class="ch-meta">
                <span>${{ch.words.toLocaleString()}} words</span>
                <span>•</span>
                <span>~${{ch.minutes}} min</span>
              </div>
            </div>
          </div>
          <div class="ch-right">
            ${{isAvailable
              ? '<span class="pill pill-live">Audio Ready</span>'
              : '<span class="pill pill-queue">Queued</span>'}}
            <button class="btn-play-sm" ${{!isAvailable ? 'disabled' : ''}}>
              ${{idx === currentChapterIdx && !audio.paused ? '⏸' : '▶'}}
            </button>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function loadTrack(idx, autoPlay = false) {{
      currentChapterIdx = idx;
      const book = catalog[currentBookIdx];
      const ch = book.chapters[idx];
      if (!ch) return;

      dockTitle.innerText = `${{String(ch.num).padStart(2, '0')}}. ${{ch.title}} — ${{book.title}}`;
      const url = streamMode === 'online' ? ch.onlineUrl : ch.localUrl;
      audio.src = url;
      dockSub.innerText = streamMode === 'online' ? `Online Cloud Stream (${{ch.stem}}.mp3)` : `Local Audio Master`;

      if (autoPlay) {{
        audio.play().catch(e => console.log('Autoplay handled:', e));
      }}
      renderPlaylist();
      updateReader();
    }}

    function togglePlay() {{
      if (!audio.src) {{
        loadTrack(0, true);
        return;
      }}
      if (audio.paused) {{
        audio.play();
      }} else {{
        audio.pause();
      }}
    }}

    function skip(sec) {{
      if (audio.duration) {{
        audio.currentTime = Math.max(0, Math.min(audio.duration, audio.currentTime + sec));
      }}
    }}

    function setSpeed(spd) {{
      audio.playbackRate = parseFloat(spd);
    }}

    function setSource(mode) {{
      streamMode = mode;
      document.getElementById('btn-src-online').classList.toggle('active', mode === 'online');
      document.getElementById('btn-src-local').classList.toggle('active', mode === 'local');
      renderPlaylist();
      if (audio.src) {{
        loadTrack(currentChapterIdx, !audio.paused);
      }}
    }}

    function switchView(view) {{
      currentView = view;
      document.getElementById('tab-playlist').classList.toggle('active', view === 'playlist');
      document.getElementById('tab-reader').classList.toggle('active', view === 'reader');
      document.getElementById('playlist-view').style.display = view === 'playlist' ? 'flex' : 'none';
      document.getElementById('reader-view').classList.toggle('active', view === 'reader');
      if (view === 'reader') updateReader();
    }}

    function updateReader() {{
      const book = catalog[currentBookIdx];
      const ch = book.chapters[currentChapterIdx];
      if (!ch) return;
      document.getElementById('reader-content').innerHTML = `
        <div style="margin-bottom: 24px; padding-bottom: 12px; border-bottom: 1px solid var(--border);">
          <span style="font-size: 0.8rem; color: var(--gold); text-transform: uppercase; font-weight: 700;">Chapter ${{ch.num}} of ${{book.chapters.length}}</span>
          <h2 style="font-size: 2rem; color: #fff; margin-top: 4px;">${{ch.title}}</h2>
          <div style="font-size: 0.85rem; color: var(--text-muted);">${{ch.words.toLocaleString()}} words · ${{book.title}}</div>
        </div>
        ${{ch.transcriptHtml}}
      `;
    }}

    function formatTime(s) {{
      if (isNaN(s)) return "0:00";
      const m = Math.floor(s / 60);
      const rem = Math.floor(s % 60);
      return `${{m}}:${{rem < 10 ? '0' : ''}}${{rem}}`;
    }}

    function seek(e) {{
      const rect = document.getElementById('bar-bg').getBoundingClientRect();
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
      timeCur.innerText = formatTime(audio.currentTime);
      timeTotal.innerText = formatTime(audio.duration);
      if (audio.duration) {{
        barFill.style.width = `${{(audio.currentTime / audio.duration) * 100}}%`;
      }}
    }});

    audio.addEventListener('ended', () => {{
      const book = catalog[currentBookIdx];
      if (currentChapterIdx + 1 < book.chapters.length) {{
        loadTrack(currentChapterIdx + 1, true);
      }}
    }});

    init();
  </script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Render interactive HTML5 audiobook web player & imprint portal.")
    parser.add_argument("book", nargs="?", default=None, type=Path, help="Specific book directory (optional)")
    parser.add_argument("--imprint", action="store_true", help="Generate centralized imprint-wide multi-series portal")
    parser.add_argument("--output", default="site", help="Output directory for imprint portal (default: site)")
    parser.add_argument("--release-tag", default="v1.0-rc1", help="GitHub Release tag for online streaming (default: v1.0-rc1)")
    parser.add_argument("--repo", default=DEFAULT_GITHUB_REPO, help="GitHub repository (owner/repo)")
    args = parser.parse_args()

    root = repo_root()

    if args.imprint or args.book is None:
        catalog = scan_all_imprint_books(root, args.repo)
        portal_html = render_portal_html(catalog, args.repo)

        out_dir = root / args.output
        out_dir.mkdir(parents=True, exist_ok=True)
        portal_file = out_dir / "index.html"
        portal_file.write_text(portal_html, encoding="utf-8")

        # Also write to docs/ for zero-config GitHub Pages
        docs_dir = root / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)
        docs_file = docs_dir / "index.html"
        docs_file.write_text(portal_html, encoding="utf-8")

        print(f"[imprint] Rendered Centralized Imprint Portal & Web Player across {len(catalog)} volumes:")
        for b in catalog:
            print(f"  - {b['seriesTitle']}: {b['title']} ({len(b['chapters'])} chapters)")
        print(f"Outputs written to:")
        print(f"  - {portal_file}")
        print(f"  - {docs_file}")
        return

    # Book-specific mode
    book_path = resolve_book_path(root, args.book)
    catalog = [collect_book_data(book_path, book_path.name.title(), "Field Guide & Reference", args.release_tag, args.repo)]
    book_html = render_portal_html(catalog, args.repo)

    pub_dir = book_path / "publishing"
    aud_dir = book_path / "audiobook"
    pub_dir.mkdir(parents=True, exist_ok=True)
    aud_dir.mkdir(parents=True, exist_ok=True)

    out1 = pub_dir / "audiobook-player.html"
    out2 = aud_dir / "index.html"
    out1.write_text(book_html, encoding="utf-8")
    out2.write_text(book_html, encoding="utf-8")

    print(f"[book] Wrote single-book player to:")
    print(f"  - {out1}")
    print(f"  - {out2}")


if __name__ == "__main__":
    main()
