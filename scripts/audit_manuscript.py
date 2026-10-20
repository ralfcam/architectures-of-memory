#!/usr/bin/env python3
"""Manuscript & Continuity Auditor for Architectures of Memory.

Performs:
1. Metaphor collision analysis per chapter section (series-bible rule: 1 controlling metaphor/section)
2. Footnote integrity & cross-chapter label collision detection
3. Character continuity & first-mention tracking (against characters.md)
4. Residual fact-check & [citation needed] debt summary
5. Optional long-context Gemini holistic review (--gemini, requires GEMINI_API_KEY)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

METAPHOR_PATTERNS: dict[str, re.Pattern[str]] = {
    "gradient-as-debt": re.compile(r"\b(gradient as debt|accumulating debt|chain rule as debt|compounding debt)\b", re.IGNORECASE),
    "gate-as-judgment": re.compile(r"\b(gate as judgment|forget gate|selective gating|gating judgment)\b", re.IGNORECASE),
    "attention-as-valuation": re.compile(r"\b(attention as valuation|weighted valuation|value judgment made at scale)\b", re.IGNORECASE),
    "window-as-horizon": re.compile(r"\b(window as horizon|context window|finite horizon)\b", re.IGNORECASE),
    "forgetting-as-design": re.compile(r"\b(forgetting as design|selective forgetting|happy forgetting|adaptive forgetting)\b", re.IGNORECASE),
}

INLINE_FN_RE = re.compile(r"(?<!^)\[\^([^\]]+)\](?!:)")
DEF_FN_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
HEADING_RE = re.compile(r"^(##+)\s+(.+)$", re.MULTILINE)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_characters(root: Path) -> list[tuple[str, str]]:
    """Return list of (full_heading, surname_key) from characters.md."""
    char_file = root / "characters.md"
    if not char_file.is_file():
        return []
    out: list[tuple[str, str]] = []
    for line in char_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            raw = line.removeprefix("### ").strip()
            clean = re.sub(r"\s*\([^)]*\)", "", raw).strip()
            parts = [p.strip() for p in re.split(r"&|,", clean) if p.strip()]
            for p in parts:
                surname = p.split()[-1]
                out.append((p, surname))
    return out


def split_sections(md_text: str) -> list[tuple[str, str]]:
    """Return list of (section_title, section_body) for a chapter."""
    matches = list(HEADING_RE.finditer(md_text))
    if not matches:
        return [("Body", md_text)]
    sections: list[tuple[str, str]] = []
    for idx, m in enumerate(matches):
        title = m.group(2).strip()
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        sections.append((title, md_text[start:end]))
    return sections


def run_gemini_review(root: Path, book_path: Path, chapters: list[Path]) -> str:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "_Skipped (`GEMINI_API_KEY` not set in environment)._"

    bible = (root / "series-bible.md").read_text(encoding="utf-8") if (root / "series-bible.md").is_file() else ""
    chars = (root / "characters.md").read_text(encoding="utf-8") if (root / "characters.md").is_file() else ""
    outline = (book_path / "outline.md").read_text(encoding="utf-8") if (book_path / "outline.md").is_file() else ""
    manuscript = "\n\n---\n\n".join(f.read_text(encoding="utf-8") for f in chapters)

    prompt = (
        "You are the Series Editor for 'The Architectures of Memory'.\n"
        "Evaluate the complete book manuscript below against the Series Bible, Characters guide, and Book Outline.\n"
        "Provide a concise, high-signal markdown audit covering:\n"
        "1. Voice & Tone Consistency (analytic, non-triumphalist, concrete scenes)\n"
        "2. Three-Lens Balance (technical -> organizational -> philosophical transitions)\n"
        "3. Cross-Chapter Argument Progression & Redundancies\n"
        "4. Top 5 Specific Line/Section Edit Recommendations\n\n"
        f"## SERIES BIBLE\n{bible}\n\n## CHARACTERS\n{chars}\n\n## BOOK OUTLINE\n{outline}\n\n## MANUSCRIPT\n{manuscript}"
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            candidates = data.get("candidates") or []
            if candidates:
                parts = (candidates[0].get("content") or {}).get("parts") or []
                return "".join(p.get("text", "") for p in parts).strip()
            return "_Gemini returned no candidates._"
    except Exception as exc:
        return f"_Gemini API call failed: {exc}_"


def audit_book(book_path: Path, use_gemini: bool = False) -> str:
    root = repo_root()
    chapters_dir = book_path / "chapters"
    chapters = sorted(chapters_dir.glob("*.md")) if chapters_dir.is_dir() else []
    if not chapters:
        return f"# Audit Report: `{book_path.name}`\n\nNo chapters found in `{chapters_dir}`.\n"

    characters = load_characters(root)
    char_mentions: dict[str, list[str]] = defaultdict(list)
    fn_defs_across_book: dict[str, list[str]] = defaultdict(list)

    chapter_rows: list[str] = []
    metaphor_collisions: list[str] = []
    fn_issues: list[str] = []
    citation_needed_total = 0

    for ch in chapters:
        text = ch.read_text(encoding="utf-8")
        words = len(text.split())
        cn_count = text.lower().count("[citation needed]")
        citation_needed_total += cn_count

        defs = set(DEF_FN_RE.findall(text))
        body_before_notes = text.split("## Notes")[0] if "## Notes" in text else text
        inlines = set(INLINE_FN_RE.findall(body_before_notes))

        for d in defs:
            fn_defs_across_book[d].append(ch.name)

        missing_defs = sorted(inlines - defs)
        unused_defs = sorted(defs - inlines)
        if missing_defs:
            fn_issues.append(f"- `{ch.name}`: inline footnote(s) missing definition: `{missing_defs}`")
        if unused_defs:
            fn_issues.append(f"- `{ch.name}`: defined footnote(s) never cited inline: `{unused_defs}`")

        sections = split_sections(body_before_notes)
        for sec_title, sec_body in sections:
            if sec_title.lower().startswith("notes"):
                continue
            matched = [name for name, pat in METAPHOR_PATTERNS.items() if pat.search(sec_body)]
            if len(matched) > 1:
                metaphor_collisions.append(
                    f"- `{ch.name}` → **{sec_title}**: multiple controlling metaphors (`{', '.join(matched)}`)"
                )

        for full_name, surname in characters:
            if re.search(rf"\b{re.escape(surname)}\b", body_before_notes):
                char_mentions[full_name].append(ch.stem[:2])

        chapter_rows.append(f"| `{ch.name}` | {words:,} | {len(defs)} | {cn_count} |")

    duplicate_fns = {k: v for k, v in fn_defs_across_book.items() if len(v) > 1}

    fc_dir = book_path / "research" / "fact-checks"
    open_fc_items: list[str] = []
    if fc_dir.is_dir():
        for fc in sorted(fc_dir.glob("*.md")):
            for i, line in enumerate(fc.read_text(encoding="utf-8").splitlines(), 1):
                if re.search(r"^\s*-\s*\[ \]", line):
                    open_fc_items.append(f"- `{fc.name}:{i}`: {line.strip()}")

    bib_path = book_path / "research" / "sources.bib"
    bib_entries = 0
    if bib_path.is_file():
        bib_entries = len(re.findall(r"^@\w+\s*\{", bib_path.read_text(encoding="utf-8"), re.MULTILINE))

    lines = [
        f"# Manuscript & Continuity Audit — `{book_path.name}`",
        "",
        "## 1. Overview Metrics",
        f"- **Chapters audited:** {len(chapters)}",
        f"- **Total words:** {sum(len(c.read_text(encoding='utf-8').split()) for c in chapters):,}",
        f"- **Unresolved `[citation needed]` markers in prose:** {citation_needed_total}",
        f"- **BibTeX entries in `research/sources.bib`:** {bib_entries}",
        "",
        "| Chapter | Words | Footnotes | `[citation needed]` |",
        "| :--- | ---: | ---: | ---: |",
        *chapter_rows,
        "",
        "## 2. Metaphor Collision Check (Rule: Max 1 Controlling Metaphor / Section)",
    ]
    if metaphor_collisions:
        lines.extend(metaphor_collisions)
    else:
        lines.append("- **Pass:** No multi-metaphor collisions detected within any single chapter section.")

    lines.extend(["", "## 3. Footnote Integrity & Cross-Chapter Collisions"])
    if fn_issues:
        lines.extend(fn_issues)
    else:
        lines.append("- **Pass:** Every chapter's inline `[^key]` matches its local `## Notes` definitions.")

    if duplicate_fns:
        lines.append(
            f"- **Notice ({len(duplicate_fns)} shared footnote keys across chapters):** "
            + ", ".join(f"`[^{k}]` ({', '.join(v)})" for k, v in sorted(duplicate_fns.items()))
        )

    lines.extend(
        [
            "",
            "## 4. Character Continuity Map (`characters.md`)",
            "| Character | First Mention | Chapters Appearing |",
            "| :--- | :--- | :--- |",
        ]
    )
    for full_name, _ in characters:
        chs = char_mentions.get(full_name, [])
        if chs:
            lines.append(f"| {full_name} | Ch.{chs[0]} | {', '.join(f'Ch.{c}' for c in chs)} |")

    lines.extend(["", "## 5. Residual Fact-Check Action Items (`research/fact-checks/*.md`)"])
    if open_fc_items:
        lines.extend(open_fc_items)
    else:
        lines.append("- **Pass:** No unchecked items in `research/fact-checks/`.")

    if use_gemini:
        lines.extend(["", "## 6. Long-Context Gemini 2.5 Pro Editorial Review", ""])
        lines.append(run_gemini_review(root, book_path, chapters))

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit a book manuscript for continuity, metaphors, and citations.")
    parser.add_argument("book", type=Path, help="Book directory (e.g. book-01-vanishing-signal)")
    parser.add_argument("--output", type=Path, default=None, help="Optional file path to write markdown report")
    parser.add_argument("--gemini", action="store_true", help="Run long-context Gemini 2.5 Pro holistic review")
    args = parser.parse_args()

    root = repo_root()
    book_path = args.book.resolve() if args.book.is_absolute() else (root / args.book).resolve()
    if not book_path.is_dir():
        print(f"error: directory not found: {book_path}", file=sys.stderr)
        sys.exit(1)

    report = audit_book(book_path, use_gemini=args.gemini)
    if args.output:
        out_path = args.output.resolve() if args.output.is_absolute() else (root / args.output).resolve()
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote audit report to {out_path}")
    else:
        sys.stdout.buffer.write(report.encode("utf-8"))


if __name__ == "__main__":
    main()
