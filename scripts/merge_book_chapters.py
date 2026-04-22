#!/usr/bin/env python3
"""Merge book chapters into a single Markdown file (full manuscript or audiobook transcript)."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

INLINE_FOOTNOTE_RE = re.compile(r"\[\^[^^\]]+\]")
NOTES_HEADING_RE = re.compile(r"^## Notes\s*$", re.MULTILINE)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def transform_audiobook(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("*Sources:"):
            continue
        lines.append(line)
    body = "".join(lines)
    m = NOTES_HEADING_RE.search(body)
    if m:
        body = body[: m.start()]
    body = INLINE_FOOTNOTE_RE.sub("", body)
    return body.rstrip()


def preamble_full(book_rel: str) -> str:
    today = date.today().isoformat()
    return f"""# {book_rel} — Full manuscript

Compiled from `{book_rel}/chapters/*.md` in sorted filename order ({today}).

**Footnotes:** Each chapter defines reference-style footnotes locally. Some labels repeat across chapters; in one file, renderers may attach one definition to every use of a label.

---

"""


def preamble_audiobook(book_rel: str) -> str:
    today = date.today().isoformat()
    return f"""# {book_rel} — Audiobook transcript

Compiled from `{book_rel}/chapters/*.md` ({today}). *Sources* lines, `## Notes` sections, and inline `[^footnote]` markers are omitted for text-to-speech.

---

"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge chapters/*.md under a book-NN-* directory into one file.",
    )
    parser.add_argument(
        "book",
        type=Path,
        help="Book directory relative to repo root or absolute (e.g. book-01-vanishing-signal).",
    )
    parser.add_argument(
        "--audiobook",
        action="store_true",
        help="Strip Sources, Notes, and inline footnote calls (TTS-friendly).",
    )
    parser.add_argument(
        "--prefix",
        default=None,
        metavar="NAME",
        help="Output basename (default: book folder name). E.g. --prefix vanishing-signal",
    )
    args = parser.parse_args()

    root = repo_root()
    book_path = args.book.resolve() if args.book.is_absolute() else (root / args.book).resolve()

    if not book_path.is_dir():
        print(f"error: not a directory: {book_path}", file=sys.stderr)
        sys.exit(1)

    chapters_dir = book_path / "chapters"
    if not chapters_dir.is_dir():
        print(f"error: missing chapters/: {chapters_dir}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(chapters_dir.glob("*.md"))
    if not md_files:
        print(f"error: no *.md under {chapters_dir}", file=sys.stderr)
        sys.exit(1)

    try:
        book_rel = book_path.relative_to(root).as_posix()
    except ValueError:
        book_rel = book_path.name

    prefix = args.prefix or book_path.name
    suffix = "audiobook" if args.audiobook else "full"
    out_name = f"{prefix}-{suffix}.md"
    out_path = book_path / out_name

    sep = "\n\n---\n\n"
    preamble = preamble_audiobook(book_rel) if args.audiobook else preamble_full(book_rel)
    parts: list[str] = [preamble.rstrip("\n") + "\n\n"]

    for i, f in enumerate(md_files):
        raw = f.read_text(encoding="utf-8")
        body = transform_audiobook(raw) if args.audiobook else raw.rstrip()
        parts.append(body)
        if i < len(md_files) - 1:
            parts.append(sep)

    out_path.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {out_path} ({len(md_files)} chapters)")


if __name__ == "__main__":
    main()
