"""Cursor afterFileEdit hook: remind about structure workflow when outline.md changes."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _is_book_outline(path: Path) -> bool:
    parts = path.parts
    if path.name != "outline.md":
        return False
    return any(p.startswith("book-") for p in parts)


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
    if not _is_book_outline(path):
        print("{}", flush=True)
        return

    msg = (
        "Outline edited — consider opening a Linear issue with the `structure` label "
        "and updating cross-references in `chapters/` and `research/notes/` if chapter "
        "numbering or titles changed."
    )
    print(msg, file=sys.stderr)
    print(json.dumps({"additional_context": msg}), flush=True)


if __name__ == "__main__":
    main()
