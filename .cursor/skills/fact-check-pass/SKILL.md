---
name: fact-check-pass
description: Sweeps a chapter for assertive claims, cross-references research notes, updates fact-check tables, and opens Linear fact-check issues for gaps. Use when the user asks to fact-check, verify citations, audit sources, or close citation debt on a chapter.
---

# Fact-check pass

## Inputs

- Path to chapter: `book-0X-*/chapters/NN-slug.md`
- Matching notes glob: `book-0X-*/research/notes/chNN-*.md`

## Steps

1. **Extract** numbered assertive claims (dates, “first”, “proved”, quotes, causal claims).
2. **Map** each claim to a passage in `research/notes/` or mark **unmapped**.
3. **Update** `book-0X-*/research/fact-checks/chNN.md` — table rows: claim, source, verified (`yes`/`no`/`partial`), notes.
4. **Linear** — For each `no` or `partial`, open issue: team **ARC**, project **Architectures of Memory — Series**, labels **`fact-check`** + **`book-0X`**, title `Fact-check: <short claim>`, body with claim + chapter path + suggested query.
5. **Chapter** — Replace bare assertions with footnotes where mapping exists; leave `[citation needed]` only where issues are open.

## Output

- Summary comment: counts of verified / partial / open; list of new Linear issue ids.
