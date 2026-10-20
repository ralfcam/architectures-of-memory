#!/usr/bin/env python3
"""Book Writing Environment (BWE) Scaffolder — Initialize a new Series or Book in Realized Press.

Usage:
  python scripts/init_series.py --series systems-of-trust --title "Systems of Trust" \
      --lenses "Mechanism,Institution,Ethics" --book book-01-the-verification-gap \
      --book-title "The Verification Gap"
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def scaffold_book(book_dir: Path, book_title: str, series_title: str, lenses: list[str], template_card: Path) -> None:
    for sub in (
        "chapters",
        "drafts",
        "evidence-cards",
        "publishing",
        "research/notes",
        "research/fact-checks",
    ):
        d = book_dir / sub
        d.mkdir(parents=True, exist_ok=True)
        gitkeep = d / ".gitkeep"
        if not any(d.iterdir()):
            gitkeep.write_text("", encoding="utf-8")

    if template_card.is_file():
        (book_dir / "evidence-cards" / "_TEMPLATE.md").write_text(
            template_card.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
    idx_path = book_dir / "evidence-cards" / "index.md"
    if not idx_path.exists():
        idx_path.write_text(
            f"# Evidence Cards (`{book_dir.name}`)\n\nOKF v0.2 atomic evidence cards anchoring *{book_title}*.\n",
            encoding="utf-8",
        )

    bib_path = book_dir / "research" / "sources.bib"
    if not bib_path.exists():
        bib_path.write_text(f"% Verified BibTeX bibliography for {book_title}\n", encoding="utf-8")

    sources_md = book_dir / "research" / "SOURCES.md"
    if not sources_md.exists():
        sources_md.write_text(
            "---\n"
            "type: Source Catalog\n"
            f'title: "Master Source Catalog — {book_dir.name}"\n'
            'description: "OKF v0.2 Source Catalog synchronized with research/sources.bib."\n'
            "tags: [bibliography, provenance, okf]\n"
            "status: draft\n"
            f"generated: {{ by: agent:bwe-scaffolder, at: {date.today().isoformat()}T00:00:00Z }}\n"
            "stale_after: 2028-01-01T00:00:00Z\n"
            "sources: []\n"
            "---\n\n"
            f"# Master Source Catalog (`{book_dir.name}`)\n\n_No entries yet._\n",
            encoding="utf-8",
        )

    outline_path = book_dir / "outline.md"
    if not outline_path.exists():
        lens_parts = "\n\n".join(
            f"## Part {i} — {lens} Lens\n\n- Ch {i:02d}: [Chapter title]"
            for i, lens in enumerate(lenses, 1)
        )
        outline_path.write_text(
            f"# {book_title}\n\n"
            f"**Series:** {series_title}\n\n---\n\n"
            f"## Premise\n\n[1-paragraph premise]\n\n---\n\n"
            f"{lens_parts}\n",
            encoding="utf-8",
        )

    readme_path = book_dir / "README.md"
    if not readme_path.exists():
        readme_path.write_text(
            f"# {book_title} (`{book_dir.name}`)\n\n"
            f"Part of **{series_title}** under **Realized Press**.\n\n"
            f"- **Three-Lens Method:** {' → '.join(lenses)}\n"
            f"- **Outline:** [`outline.md`](outline.md)\n"
            f"- **OKF v0.2 Evidence Cards:** [`evidence-cards/`](evidence-cards/)\n"
            f"- **Bibliography:** [`research/sources.bib`](research/sources.bib) & [`research/SOURCES.md`](research/SOURCES.md)\n",
            encoding="utf-8",
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new Series and/or Book in the Realized Press BWE.")
    parser.add_argument("--series", required=True, help="Series slug under series/ (e.g. systems-of-trust)")
    parser.add_argument("--title", required=True, help="Human-readable Series Title")
    parser.add_argument("--subtitle", default="", help="Optional Series Subtitle")
    parser.add_argument("--lenses", default="Mechanism,System,Meaning", help="Comma-separated 3-lens triad")
    parser.add_argument("--book", default=None, help="Optional initial book slug (e.g. book-01-slug)")
    parser.add_argument("--book-title", default=None, help="Optional initial book title")
    parser.add_argument("--dry-run", action="store_true", help="Print planned paths without writing files")
    args = parser.parse_args()

    root = repo_root()
    series_dir = root / "series" / args.series
    lenses = [x.strip() for x in args.lenses.split(",") if x.strip()]
    book_slug = args.book or "book-01-foundations"
    book_title = args.book_title or f"{args.title} — Book 1"
    book_dir = series_dir / book_slug

    if args.dry_run:
        print(f"[bwe-init dry-run] Would scaffold series at: {series_dir.relative_to(root)}")
        print(f"[bwe-init dry-run] Three-Lens triad: {' -> '.join(lenses)}")
        print(f"[bwe-init dry-run] Would scaffold book at: {book_dir.relative_to(root)}")
        return 0

    series_dir.mkdir(parents=True, exist_ok=True)
    manifest = series_dir / "series.yaml"
    if not manifest.exists():
        lens_yaml = "\n".join(
            f'    - id: "{l.lower().replace(" ", "-")}"\n      label: "{l}"'
            for l in lenses
        )
        manifest.write_text(
            'schema_version: "1.0"\n'
            'imprint: "Realized Press"\n'
            f'series_id: "{args.series}"\n'
            f'title: "{args.title}"\n'
            f'subtitle: "{args.subtitle}"\n'
            'author: "Jose Campos"\n'
            "epistemic_contract:\n"
            '  okf_version: "0.2"\n'
            "  three_lenses:\n"
            f"{lens_yaml}\n"
            "  target_chapter_words: [1500, 3500]\n"
            "monetization:\n"
            "  kdp:\n"
            '    trim_size: "6x9"\n'
            "    inside_gutter_mm: 20.0\n"
            "    outside_margin_mm: 15.0\n"
            "    top_bottom_margin_mm: 18.0\n"
            '    formats: ["paperback-pdf", "hardcover-pdf", "kindle-epub", "audiobook-wav"]\n'
            "  patreon:\n"
            "    tiers:\n"
            '      - "Public Evidence Briefs"\n'
            '      - "Chapter Preprints & Audio"\n'
            '      - "Reader Edition Slices"\n'
            "books:\n"
            f'  - id: "{book_slug}"\n'
            f'    title: "{book_title}"\n'
            '    status: "outlined"\n',
            encoding="utf-8",
        )

    bible_path = series_dir / "series-bible.md"
    if not bible_path.exists():
        bible_path.write_text(
            f"# Series Bible — {args.title}\n\n"
            f"## Three-Lens Method\n\n"
            + "\n".join(f"{i}. **{l}**" for i, l in enumerate(lenses, 1))
            + "\n\nGoverned by root [`SPEC.md`](../../SPEC.md) and [`COMPOSITION.md`](../../COMPOSITION.md).\n",
            encoding="utf-8",
        )

    scaffold_book(
        book_dir=book_dir,
        book_title=book_title,
        series_title=args.title,
        lenses=lenses,
        template_card=root / "templates" / "evidence-card-template.md",
    )
    print(f"[bwe-init] Scaffolded series '{args.title}' at {series_dir.relative_to(root)}")
    print(f"[bwe-init] Scaffolded book '{book_title}' at {book_dir.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
