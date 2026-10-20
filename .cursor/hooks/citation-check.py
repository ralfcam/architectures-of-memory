"""Cursor afterFileEdit hook: enforce Definitive Tool Routing Protocol, OKF v0.2 cards & chapter gates."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / ".agents" / "hooks"))

from post_edit_guard import (  # noqa: E402
    REDIRECT_MARKER,
    _check_bibliographic_lock,
    _check_chapter_gates,
    _check_evidence_card_gates,
    _is_book_chapter,
    _is_evidence_card,
    _is_research_md,
)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        print("{}", flush=True)
        return

    raw = payload.get("file_path") or payload.get("path") or ""
    if not raw:
        print("{}", flush=True)
        return

    path = Path(raw)
    if not (_is_book_chapter(path) or _is_research_md(path) or _is_evidence_card(path)) or not path.is_file():
        print("{}", flush=True)
        return

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        print("{}", flush=True)
        return

    notices: list[str] = []
    if REDIRECT_MARKER in text.lower():
        notices.append(
            f"Routing Protocol Violation: `{path.name}` contains raw `{REDIRECT_MARKER}` redirect URL(s). "
            "Replace with canonical DOIs/URLs via `academic-bib` or `perplexity_search`."
        )
    notices.extend(_check_bibliographic_lock(path, text))
    if _is_book_chapter(path):
        notices.extend(_check_chapter_gates(path, text))
    if _is_evidence_card(path):
        notices.extend(_check_evidence_card_gates(path))

    out: dict[str, str] = {}
    if notices:
        msg = " | ".join(notices)
        print(msg, file=sys.stderr)
        out["additional_context"] = msg
    print(json.dumps(out), flush=True)


if __name__ == "__main__":
    main()
