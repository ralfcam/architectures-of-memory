---
name: chapter-draft
description: Drafts a new chapter from research notes using series voice and three-lens structure. Use when the user asks to draft, write, compose, or expand a chapter for any book in the Architectures of Memory series.
---

# Chapter draft

## Prerequisites

- `book-0X-*/research/notes/chNN-*.md` exists for the chapter (or user explicitly waives with `[citation needed]` plan)
- Linear **`draft`** issue + **`book-0X`** label (create if missing), milestone set

## Steps

1. Read [series-bible.md](../../../series-bible.md), `book-0X-*/outline.md`, all matching `research/notes/` for the chapter, and [characters.md](../../../characters.md) for everyone named.
2. Create `book-0X-*/chapters/NN-slug.md` (two-digit `NN`, kebab-case `slug` aligned with outline).
3. **Structure:** Follow outline beats; use **technical → organizational → philosophical** where the outline implies all three.
4. **Citations & `sources.bib` Lock:** Footnotes or inline pointers to research note sections; ensure every cited DOI/arXiv paper is locked in `book-0X-*/research/sources.bib` via `academic-bib` (`add_bibtex_entry`). Use `[citation needed]` only when unavoidable — then list in `research/fact-checks/chNN.md`.
5. **Pre-PR Manuscript Gate:** Run `python scripts/audit_manuscript.py book-0X-*` (`make audit BOOK=book-0X-*`) and fix any metaphor collisions or footnote mismatches before committing.
6. **Branch + PR** — `draft/ch-NN-slug`; PR description links the Linear draft issue and lists open citation gaps.

## Checklist before requesting review

- [ ] Voice matches series-bible (no triumphalism; uncertainty flagged)
- [ ] One metaphor per section (verified by `audit_manuscript.py`)
- [ ] Every date and attribution traceable or marked, and primary DOIs/arXiv IDs present in `research/sources.bib`
- [ ] `outline.md` chapter title still matches file focus
