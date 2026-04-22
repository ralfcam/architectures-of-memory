"""Cursor afterFileEdit hook: report [citation needed] count in book chapter files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

MARKER = "[citation needed]"


def _is_book_chapter(path: Path) -> bool:
    parts = path.parts
    if not parts:
        return False
    return any(p.startswith("book-") for p in parts) and "chapters" in parts and path.suffix.lower() == ".md"


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
    if not _is_book_chapter(path):
        print("{}", flush=True)
        return

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        print("{}", flush=True)
        return

    lower = text.lower()
    needle = MARKER.lower()
    count = lower.count(needle)
    out: dict[str, str] = {}
    if count:
        lines = [i + 1 for i, line in enumerate(text.splitlines()) if needle in line.lower()][:5]
        msg = (
            f"Citation hook: `{path.name}` has {count} `{MARKER}` marker(s). "
            f"First line(s): {lines}. Resolve or track in research/fact-checks/ before merge."
        )
        print(msg, file=sys.stderr)
        out["additional_context"] = msg
    print(json.dumps(out), flush=True)


if __name__ == "__main__":
    main()
