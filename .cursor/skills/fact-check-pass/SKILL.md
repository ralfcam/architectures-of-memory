---
name: fact-check-pass
description: >-
  Sweeps a chapter for assertive claims, cross-references research notes and academic
  bibliographic databases, updates fact-check tables, and opens Linear fact-check issues
  for gaps. Use when the user asks to fact-check, verify citations, audit sources, or
  close citation debt on a chapter.
---

# Fact-Check Pass (Definitive Tool Routing Protocol)

## Inputs

- Path to chapter: `book-0X-*/chapters/NN-slug.md`
- Matching notes glob: `book-0X-*/research/notes/chNN-*.md`

## Steps

1. **Extract** numbered assertive claims (dates, “first”, “proved”, quotes, causal claims, statistics).
2. **Route Verification by Claim Type:**
   - **Academic papers / preprints:** Run **`academic-bib`** (`crossref_lookup`, `arxiv_search`, `openalex_work`) to verify exact DOI, volume, issue, pagination, and retraction status (`is_retracted`).
   - **Methodological / vendor statistics / disputed attributions:** Run **`perplexity_reason`**.
   - **Targeted factual / biographical lookups:** Run **`perplexity_ask`** (`search_context_size: "high"`).
   - **Live library / SDK claims:** Run **`context7`** (`resolve-library-id` → `query-docs`).
3. **Update** `book-0X-*/research/fact-checks/chNN.md` — table rows: claim, source, verified (`yes`/`no`/`partial`), notes.
4. **BibTeX Lock** — Persist every verified paper into `book-0X-*/research/sources.bib` via **`academic-bib`** (`add_bibtex_entry`).
5. **Linear** — For each `no` or `partial`, open issue: team **ARC**, project **Architectures of Memory — Series**, labels **`fact-check`** + **`book-0X`**, title `Fact-check: <short claim>`, body with claim + chapter path + suggested query.
6. **Chapter + Audit** — Replace bare assertions with footnotes where mapping exists; run `python scripts/audit_manuscript.py book-0X-*` to verify footnote and citation integrity.

## Output

- Summary comment: counts of verified / partial / open; list of new Linear issue ids and newly added `sources.bib` keys.
