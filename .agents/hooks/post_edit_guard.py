#!/usr/bin/env python3
"""Antigravity lifecycle hook enforcing the Definitive Tool Routing Protocol (Books 2–5):

1. Blocks/warns on raw `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs in notes/fact-checks/chapters.
2. Enforces Mandatory Bibliographic Lock: checks that any DOI (`10.xxxx/...`) or `arXiv:xxxx.xxxxx` cited in
   `research/notes/*.md`, `research/fact-checks/*.md`, or `chapters/*.md` is locked in `book-0X-*/research/sources.bib`
   via `academic-bib` (`crossref_lookup` / `arxiv_search` -> `add_bibtex_entry`).
3. Enforces Pre-PR Manuscript Gate on `chapters/*.md`: checks `[citation needed]` markers, section-level metaphor
   collisions (max 1 controlling metaphor per section), and inline vs. `## Notes` footnote definitions.
4. Enforces `structure` workflow reminder on `book-*/outline.md` edits.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MARKER = "[citation needed]"
REDIRECT_MARKER = "vertexaisearch.cloud.google.com/grounding-api-redirect/"
STATE_FILE = Path(__file__).resolve().parent / ".pending_notice.txt"

DOI_RE = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b")
ARXIV_RE = re.compile(r"\barXiv:(\d{4}\.\d{4,5})\b", re.IGNORECASE)
INLINE_FN_RE = re.compile(r"(?<!^)\[\^([^\]]+)\](?!:)")
DEF_FN_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
HEADING_RE = re.compile(r"^(##+)\s+(.+)$", re.MULTILINE)

METAPHOR_PATTERNS: dict[str, re.Pattern[str]] = {
    "gradient-as-debt": re.compile(r"\b(gradient as debt|accumulating debt|chain rule as debt|compounding debt)\b", re.IGNORECASE),
    "gate-as-judgment": re.compile(r"\b(gate as judgment|forget gate|selective gating|gating judgment)\b", re.IGNORECASE),
    "attention-as-valuation": re.compile(r"\b(attention as valuation|weighted valuation|value judgment made at scale)\b", re.IGNORECASE),
    "window-as-horizon": re.compile(r"\b(window as horizon|context window|finite horizon)\b", re.IGNORECASE),
    "forgetting-as-design": re.compile(r"\b(forgetting as design|selective forgetting|happy forgetting|adaptive forgetting)\b", re.IGNORECASE),
}


def _find_book_dir(path: Path) -> Path | None:
    for parent in [path] + list(path.parents):
        if parent.name.lower().startswith("book-") and parent.is_dir():
            return parent
    return None


def _is_book_chapter(path: Path) -> bool:
    parts = [p.lower() for p in path.parts]
    return any(p.startswith("book-") for p in parts) and "chapters" in parts and path.suffix.lower() == ".md"


def _is_research_md(path: Path) -> bool:
    parts = [p.lower() for p in path.parts]
    return (
        any(p.startswith("book-") for p in parts)
        and "research" in parts
        and ("notes" in parts or "fact-checks" in parts)
        and path.suffix.lower() == ".md"
    )


def _is_book_outline(path: Path) -> bool:
    parts = [p.lower() for p in path.parts]
    return path.name.lower() == "outline.md" and any(p.startswith("book-") for p in parts)


def _check_bibliographic_lock(path: Path, text: str) -> list[str]:
    book_dir = _find_book_dir(path)
    if not book_dir:
        return []
    bib_path = book_dir / "research" / "sources.bib"
    bib_text = bib_path.read_text(encoding="utf-8", errors="replace").lower() if bib_path.is_file() else ""

    raw_dois = {d.rstrip(".,;:)]>*") for d in DOI_RE.findall(text)}
    # Ignore truncated example prefixes like 10.1080 without suffix
    valid_dois = {d for d in raw_dois if "/" in d and len(d.split("/", 1)[1]) >= 3}
    missing_dois = sorted(d for d in valid_dois if d.lower() not in bib_text)

    arxiv_ids = {a for a in ARXIV_RE.findall(text)}
    missing_arxiv = sorted(a for a in arxiv_ids if a.lower() not in bib_text)

    warnings: list[str] = []
    if missing_dois or missing_arxiv:
        items = [f"DOI:{d}" for d in missing_dois[:5]] + [f"arXiv:{a}" for a in missing_arxiv[:5]]
        warnings.append(
            f"Routing Protocol (Step 4 — Bibliographic Lock): `{path.name}` cites {', '.join(items)} "
            f"which are not yet in `{book_dir.name}/research/sources.bib`. Run `academic-bib` "
            "(`crossref_lookup` / `arxiv_search` -> `add_bibtex_entry`) to lock verified BibTeX."
        )
    return warnings


def _check_chapter_gates(path: Path, text: str) -> list[str]:
    notices: list[str] = []
    count = text.lower().count(MARKER)
    if count:
        lines = [i + 1 for i, line in enumerate(text.splitlines()) if MARKER in line.lower()][:5]
        notices.append(
            f"Citation Gate: `{path.name}` has {count} `{MARKER}` marker(s) (first line(s): {lines}). "
            "Resolve or track in `research/fact-checks/` before merge."
        )

    defs = set(DEF_FN_RE.findall(text))
    body_before_notes = text.split("## Notes")[0] if "## Notes" in text else text
    inlines = set(INLINE_FN_RE.findall(body_before_notes))
    missing_defs = sorted(inlines - defs)
    unused_defs = sorted(defs - inlines)
    if missing_defs:
        notices.append(f"Footnote Gate: `{path.name}` has inline footnote(s) missing definitions in `## Notes`: {missing_defs}.")
    if unused_defs:
        notices.append(f"Footnote Gate: `{path.name}` has unused footnote definition(s) in `## Notes`: {unused_defs}.")

    matches = list(HEADING_RE.finditer(body_before_notes))
    for idx, m in enumerate(matches):
        sec_title = m.group(2).strip()
        if sec_title.lower().startswith("notes"):
            continue
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body_before_notes)
        sec_body = body_before_notes[start:end]
        matched = [name for name, pat in METAPHOR_PATTERNS.items() if pat.search(sec_body)]
        if len(matched) > 1:
            notices.append(
                f"Metaphor Gate: `{path.name}` section '{sec_title}' mixes multiple controlling metaphors "
                f"({', '.join(matched)}). Series bible allows at most 1 controlling metaphor per section."
            )
    return notices


def handle_post_tool_use(payload: dict) -> None:
    tool_call = payload.get("toolCall") or {}
    args = tool_call.get("args") or {}
    raw_path = args.get("Path") or args.get("path") or args.get("file_path") or ""
    if not raw_path:
        print("{}", flush=True)
        return

    path = Path(raw_path)
    notices: list[str] = []

    if (_is_book_chapter(path) or _is_research_md(path)) and path.is_file():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            if REDIRECT_MARKER in text.lower():
                notices.append(
                    f"Routing Protocol Violation: `{path.name}` contains raw `{REDIRECT_MARKER}` redirect URL(s). "
                    "Replace with canonical DOIs/URLs via `academic-bib` or `perplexity_search`."
                )
            notices.extend(_check_bibliographic_lock(path, text))
            if _is_book_chapter(path):
                notices.extend(_check_chapter_gates(path, text))
        except OSError:
            pass

    if _is_book_outline(path):
        notices.append(
            f"Outline Gate: `{path.as_posix()}` was edited — ensure a Linear issue with the `structure` label "
            "exists and cross-references in `chapters/` and `research/notes/` remain aligned."
        )

    if notices:
        try:
            existing = STATE_FILE.read_text(encoding="utf-8") if STATE_FILE.is_file() else ""
            combined = (existing + "\n" + "\n".join(notices)).strip()
            STATE_FILE.write_text(combined, encoding="utf-8")
        except OSError:
            pass

    print("{}", flush=True)


def handle_post_invocation() -> None:
    if not STATE_FILE.is_file():
        print("{}", flush=True)
        return
    try:
        msg = STATE_FILE.read_text(encoding="utf-8").strip()
        STATE_FILE.unlink(missing_ok=True)
    except OSError:
        print("{}", flush=True)
        return

    if not msg:
        print("{}", flush=True)
        return

    print(
        json.dumps(
            {
                "injectSteps": [
                    {
                        "ephemeralMessage": msg,
                    }
                ]
            }
        ),
        flush=True,
    )


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "post-tool"
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    if mode == "post-invocation":
        handle_post_invocation()
    else:
        handle_post_tool_use(payload)


if __name__ == "__main__":
    main()
