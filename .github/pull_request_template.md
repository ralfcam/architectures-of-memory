## Summary

<!-- What this PR changes (one short paragraph) -->

## Scope

- **Series / Book folder:** `series/architectures-of-memory/book-0X-…/` or `series/parenthood-atlas/`
- **Chapter / Evidence Card / Artifact:** <!-- e.g. chapters/01-slug.md, evidence-cards/slug.md, research/notes/ch01-slug.md -->
- **Linear (`ARC`):** <!-- ARC-NN link -->

## Checklist

- [ ] Linear issue linked above (`research` / `draft` / `edit` / `fact-check` / `structure`)
- [ ] All new/modified academic sources verified via `academic-bib` MCP, persisted to `sources.bib`, and synchronized to `SOURCES.md` (`python scripts/sync_okf_sources.py`)
- [ ] OKF v0.2 Evidence Cards (`evidence-cards/*.md`) pass `python scripts/five_rule_check.py <book-dir> --online-retraction-check`
- [ ] Manuscript continuity, footnote, metaphor & forbidden-phrase audit passes (`python scripts/audit_manuscript.py <book-dir> --strict`)
- [ ] Voice and grade-calibrated verbs align with [COMPOSITION.md](../COMPOSITION.md) and [style/forbidden-phrases.md](../style/forbidden-phrases.md)
- [ ] If `outline.md` / `_OUTLINE.md` changed: `structure` issue opened and cross-refs updated

## Reviewer notes

<!-- Risks, open questions, or sections that need a second pair of eyes -->
