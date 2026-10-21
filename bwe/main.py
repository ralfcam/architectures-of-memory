# bwe/main.py
import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from jinja2_fragments.fastapi import Jinja2Blocks

from bwe.db import get_db, init_db
from bwe.schema import validate_series_yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BWE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
SERIES_DIR = REPO_ROOT / "series"
SITE_DIR = BWE_DIR / "site"

# Ensure scripts directory is importable for data synthesis
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from render_audiobook_player import DEFAULT_GITHUB_REPO, scan_all_imprint_books

app = FastAPI(title="Realized Press — BWE & Serial Portal (P-ARC-18)")
templates = Jinja2Blocks(directory=str(REPO_ROOT / "bwe" / "templates"))

# Mount documentation if present
if (REPO_ROOT / "docs").exists():
    app.mount("/docs-static", StaticFiles(directory=str(REPO_ROOT / "docs")), name="docs")


@app.on_event("startup")
def on_startup() -> None:
    init_db(REPO_ROOT)


@app.get("/", response_class=HTMLResponse)
async def root_redirect(request: Request):
    """Root entrypoint landing on the unified Imprint Hub."""
    return await imprint_site_home(request)


# -------------------------------------------------------------------------
# PILLAR 1 (ARC-55): IMPRINT SITE & AUDIOBOOK HUB (FASTAPI + HTMX)
# -------------------------------------------------------------------------


@app.get("/site", response_class=HTMLResponse)
@app.get("/site/", response_class=HTMLResponse)
async def imprint_site_home(request: Request):
    """
    ARC-55: Serves the Imprint Audiobook Portal & Marketing Hub under the
    unified FastAPI + HTMX stack with aligned navigation and live catalog data.
    """
    catalog = scan_all_imprint_books(REPO_ROOT, DEFAULT_GITHUB_REPO)
    catalog_json = json.dumps(catalog)
    return templates.TemplateResponse(
        "site.html",
        {
            "request": request,
            "catalog": catalog,
            "catalog_json": catalog_json,
            "active_tab": "site",
        },
    )


# Static file mounts for audio binaries and PDFs (registered after HTML route)
if SITE_DIR.exists():
    app.mount("/site-static", StaticFiles(directory=str(SITE_DIR)), name="site-static")
    app.mount("/site", StaticFiles(directory=str(SITE_DIR)), name="site-files")


# -------------------------------------------------------------------------
# PILLAR 1 (ARC-55): SERIAL READER, FOOTNOTE ISOLATION & ARC-53 FEEDBACK
# -------------------------------------------------------------------------


@app.get("/read/{series_slug}/{chapter_slug}", response_class=HTMLResponse)
async def read_chapter(request: Request, series_slug: str, chapter_slug: str):
    """Serves the bidirectional audio-synced chapter reader with isolated footnotes."""
    md_candidates = list((SERIES_DIR / series_slug).glob(f"**/chapters/{chapter_slug}.md"))
    if not md_candidates:
        raise HTTPException(status_code=404, detail="Chapter not found")
    md_path = md_candidates[0]
    raw_md = md_path.read_text(encoding="utf-8")

    # Split prose from ## Notes so footnotes can be fetched via HTMX without page jump
    prose_part, _, notes_part = raw_md.partition("## Notes")
    timings_path = SERIES_DIR / series_slug / "audiobook" / f"{chapter_slug}.timings.json"
    timings = json.loads(timings_path.read_text(encoding="utf-8")) if timings_path.exists() else []

    return templates.TemplateResponse(
        "portal.html",
        {
            "request": request,
            "series_slug": series_slug,
            "chapter_slug": chapter_slug,
            "prose": prose_part,
            "timings": timings,
        },
    )


@app.get("/hx/footnote/{series_slug}/{chapter_slug}/{footnote_id}", response_class=HTMLResponse)
async def inspect_footnote(request: Request, series_slug: str, chapter_slug: str, footnote_id: str):
    """
    ARC-55 & ARC-58: Returns a single chapter-local footnote into the side drawer
    without interrupting paragraph audio playback, and logs citation telemetry.
    """
    md_candidates = list((SERIES_DIR / series_slug).glob(f"**/chapters/{chapter_slug}.md"))
    if not md_candidates:
        raise HTTPException(status_code=404, detail="Chapter not found")
    raw_md = md_candidates[0].read_text(encoding="utf-8")

    pattern = rf"\[\^{re.escape(footnote_id)}\]:\s*(.+?)(?=\n\[\^|\n## |\Z)"
    match = re.search(pattern, raw_md, flags=re.DOTALL)
    note_text = match.group(1).strip() if match else "Footnote definition not found in ## Notes."

    with get_db() as conn:
        conn.execute(
            "INSERT INTO citation_telemetry (series_slug, chapter_slug, footnote_id) VALUES (?, ?, ?)",
            (series_slug, chapter_slug, footnote_id),
        )

    return templates.TemplateResponse(
        "partials/footnote_drawer.html",
        {"request": request, "footnote_id": footnote_id, "note_text": note_text},
    )


@app.post("/hx/feedback", response_class=HTMLResponse)
async def submit_reader_feedback(
    series_slug: str = Form(...),
    chapter_slug: str = Form(...),
    block_id: str = Form(""),
    category: str = Form("epistemic-clarity"),
    comment: str = Form(...),
):
    """ARC-53: Replaces manual CSV feedback entry with instant HTMX inline capture."""
    with get_db() as conn:
        conn.execute(
            """INSERT INTO reader_feedback (series_slug, chapter_slug, block_id, category, comment)
               VALUES (?, ?, ?, ?, ?)""",
            (series_slug, chapter_slug, block_id, category, comment),
        )
    return HTMLResponse(
        '<div class="p-3 text-sm bg-emerald-950 text-emerald-200 rounded border border-emerald-700">'
        '&check; Feedback logged for ARC-53 triage. Thank you.</div>'
    )


# -------------------------------------------------------------------------
# PILLAR 2 (ARC-56): EPISTEMIC IDE, LIVE AUDITS & INCREMENTAL TTS STREAM
# -------------------------------------------------------------------------


@app.get("/ide", response_class=HTMLResponse)
async def epistemic_ide_home(request: Request):
    """ARC-56: Renders the full 3-column Epistemic IDE workbench."""
    with get_db() as conn:
        rows = conn.execute(
            "SELECT series_slug, book_slug, card_slug, title, substr(body, 1, 240) AS snippet "
            "FROM evidence_cards_fts LIMIT 15"
        ).fetchall()
    return templates.TemplateResponse(
        "ide.html",
        {"request": request, "cards": rows, "query": ""},
    )


@app.get("/ide/search-cards", response_class=HTMLResponse)
async def search_evidence_cards(request: Request, q: str = ""):
    """Instant FTS5 search across all OKF v0.2 Evidence Cards."""
    with get_db() as conn:
        if not q.strip():
            rows = conn.execute(
                "SELECT series_slug, book_slug, card_slug, title, substr(body, 1, 240) AS snippet "
                "FROM evidence_cards_fts LIMIT 15"
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT series_slug, book_slug, card_slug, title, snippet(evidence_cards_fts, 4, '<mark>', '</mark>', '...', 24) AS snippet "
                "FROM evidence_cards_fts WHERE evidence_cards_fts MATCH ? LIMIT 20",
                (f'"{q}"*',),
            ).fetchall()
    return templates.TemplateResponse(
        "ide.html",
        {"request": request, "cards": rows, "query": q},
        block_name="card_results",
    )


@app.post("/ide/audit", response_class=HTMLResponse)
async def run_epistemic_audit(
    request: Request,
    script_name: str = Form(...),
    target_path: str = Form(...),
):
    """
    ARC-56: Invokes five_rule_check.py, audit_manuscript.py, or audit_epub.py
    and swaps the structured audit output directly into the IDE panel.
    """
    allowed_scripts = {
        "five_rule_check": SCRIPTS_DIR / "five_rule_check.py",
        "audit_manuscript": SCRIPTS_DIR / "audit_manuscript.py",
        "audit_epub": SCRIPTS_DIR / "audit_epub.py",
    }
    if script_name not in allowed_scripts:
        raise HTTPException(status_code=400, detail="Unsupported audit script")

    proc = subprocess.run(
        [sys.executable, str(allowed_scripts[script_name]), target_path],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=60,
    )
    return templates.TemplateResponse(
        "partials/audit_results.html",
        {
            "request": request,
            "script_name": script_name,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        },
    )


@app.get("/ide/tts-stream/{series_slug}/{chapter_slug}")
async def stream_tts_synthesis(series_slug: str, chapter_slug: str):
    """
    ARC-62 / ARC-56: Streams live paragraph-by-paragraph Gemini TTS synthesis
    and SHA-256 PCM cache hits (.cache/tts_pcm/) over Server-Sent Events (SSE).
    """

    async def event_generator():
        # Match series directory (e.g. series/parenthood-atlas)
        series_target = f"series/{series_slug}"
        # Extract 2-digit chapter prefix if present (e.g. '01' from '01-before-the-child-is-born')
        ch_prefix = chapter_slug.split("-")[0] if "-" in chapter_slug else chapter_slug

        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            str(SCRIPTS_DIR / "generate_audiobook_tts.py"),
            series_target,
            "--chapter",
            ch_prefix,
            cwd=str(REPO_ROOT),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        assert proc.stdout is not None
        async for line in proc.stdout:
            clean = line.decode("utf-8", errors="replace").rstrip()
            yield f"event: tts-log\ndata: <div class='font-mono text-xs py-0.5'>{clean}</div>\n\n"
        rc = await proc.wait()
        status = "COMPLETE (Zero Drift)" if rc == 0 else f"FAILED (exit {rc})"
        yield f"event: tts-done\ndata: <span class='font-bold'>{status}</span>\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
