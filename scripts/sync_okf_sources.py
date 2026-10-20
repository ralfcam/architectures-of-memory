#!/usr/bin/env python3
"""Synchronize OKF v0.2 SOURCES.md catalogs and BibTeX sources.bib across all series and books."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sync_parenthood_atlas_to_bib() -> int:
    pa_dir = ROOT / "series" / "parenthood-atlas"
    sources_md = pa_dir / "SOURCES.md"
    if not sources_md.exists():
        return 0
    text = sources_md.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    fm = parts[1] if len(parts) >= 3 else ""
    entries = re.findall(
        r"-\s+id:\s*(\S+)\s*\n\s*resource:\s*(\S+)\s*\n\s*title:\s*\"([^\"]+)\"",
        fm,
    )
    bib_lines = ["% Auto-synchronized from SOURCES.md (OKF v0.2 Source Catalog)\n"]
    for sid, url, title in entries:
        year_m = re.search(r"\b(19\d\d|20\d\d)\b", title + " " + sid)
        year = year_m.group(1) if year_m else "2024"
        doi_m = re.search(r"10\.\d{4,9}/[^\s\"<>]+", url)
        doi_field = f"  doi = {{{doi_m.group(0)}}},\n" if doi_m else ""
        bib_lines.append(
            f"@misc{{{sid},\n"
            f"  title = {{{title}}},\n"
            f"  year = {{{year}}},\n"
            f"{doi_field}"
            f"  url = {{{url}}}\n"
            f"}}\n"
        )
    out_bib = pa_dir / "sources.bib"
    out_bib.write_text("\n".join(bib_lines), encoding="utf-8")
    print(f"[sync] Wrote {len(entries)} BibTeX entries to {out_bib.relative_to(ROOT)}")
    return len(entries)


def sync_architectures_bib_to_okf() -> int:
    total = 0
    aom_dir = ROOT / "series" / "architectures-of-memory"
    if not aom_dir.exists():
        return 0
    for book_dir in sorted(aom_dir.glob("book-*")):
        bib_path = book_dir / "research" / "sources.bib"
        if not bib_path.exists():
            continue
        bib_text = bib_path.read_text(encoding="utf-8")
        raw_entries = re.findall(r"@\w+\{([^,]+),([^@]+)", bib_text, re.S)
        yaml_sources = []
        md_bullets = []
        for key, body in raw_entries:
            key = key.strip()
            title_m = re.search(r"title\s*=\s*\{([^\}]+)\}", body)
            year_m = re.search(r"year\s*=\s*\{?(\d{4})\}?", body)
            doi_m = re.search(r"doi\s*=\s*\{([^\}]+)\}", body)
            url_m = re.search(r"url\s*=\s*\{([^\}]+)\}", body)
            title = title_m.group(1).strip() if title_m else key
            year = year_m.group(1).strip() if year_m else "n.d."
            if doi_m:
                res = f"https://doi.org/{doi_m.group(1).strip()}"
            elif url_m:
                res = url_m.group(1).strip()
            else:
                res = f"https://scholar.google.com/scholar?q={key}"
            safe_title = title.replace('"', "'")
            yaml_sources.append(
                f"  - id: {key}\n    resource: {res}\n    title: \"{safe_title} ({year})\""
            )
            md_bullets.append(f"- **`{key}`** ({year}): {title} — <{res}>")
        okf_md = (
            "---\n"
            "type: Source Catalog\n"
            f"title: \"Master Source Catalog — {book_dir.name}\"\n"
            "description: \"OKF v0.2 Source Catalog synchronized with research/sources.bib.\"\n"
            "tags: [bibliography, provenance, okf]\n"
            "status: stable\n"
            "generated: { by: agent:antigravity, at: 2026-10-20T22:45:00Z }\n"
            "stale_after: 2027-10-20T00:00:00Z\n"
            "sources:\n"
            + ("\n".join(yaml_sources) if yaml_sources else "  []")
            + "\n---\n\n"
            f"# Master Source Catalog (`{book_dir.name}`)\n\n"
            + ("\n".join(md_bullets) if md_bullets else "_No entries yet._")
            + "\n"
        )
        out_md = book_dir / "research" / "SOURCES.md"
        out_md.write_text(okf_md, encoding="utf-8")
        print(f"[sync] Wrote {len(raw_entries)} OKF sources to {out_md.relative_to(ROOT)}")
        total += len(raw_entries)
    return total


if __name__ == "__main__":
    sync_parenthood_atlas_to_bib()
    sync_architectures_bib_to_okf()
