---
trigger: glob
globs: "series/**/fact-checks/*.md,series/**/extraction/*.md"
description: Fact-check and source-extraction verification rules across both series.
---

# Fact-Check & Source Verification Format

Applies to: `series/architectures-of-memory/book-*/research/fact-checks/*.md` and `series/parenthood-atlas/preliminary/research/extraction/*.md`

Use rows or bullets in this shape:

`| Claim | Source | Verified | Notes |`

- **verified:** `yes` | `no` | `partial`
- **partial / no:** must spawn a Linear **`fact-check`** issue under Team `ARC` (`Architectures of Memory — Series` or `Parenthood: The Atlas — Series`) until a primary or consensus source is found.
- Use **`academic-bib` MCP** (`crossref_lookup`, `openalex_work`, `arxiv_search`) to confirm exact DOIs, issue numbers, pagination, and retraction status (`is_retracted`).
- Persist verified citations to `sources.bib` via `add_bibtex_entry` and sync `SOURCES.md` via `python scripts/sync_okf_sources.py`.
- Do not mark `yes` from a single blog post, vendor whitepaper, or unattributed LLM summary.
