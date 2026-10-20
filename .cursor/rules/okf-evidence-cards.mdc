---
trigger: glob
globs: "**/evidence-cards/**/*.md,**/SOURCES.md,**/sources.bib"
description: Enforces Open Knowledge Format (OKF v0.2) Evidence Card anatomy, the Five-Rule Promotion Gate, and dual SOURCES.md / sources.bib synchronization across all series and books.
---

# Open Knowledge Format (OKF v0.2) & Five-Rule Promotion Gate

All books across both series (`series/architectures-of-memory/book-*` and `series/parenthood-atlas/`) use **OKF v0.2** atomic `evidence-cards/*.md` governed by [`SPEC.md`](../../SPEC.md) and [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

## 1. Required 9-Section Anatomy (`templates/evidence-card-template.md`)

Every card in `evidence-cards/` (excluding `_TEMPLATE.md` and `index.md`) must include YAML frontmatter (`type: Evidence Card`, `title`, `description`, `tags`, `status: draft | stable`, `confidence`, `generated`, `stale_after`, `sources`) and these exact 9 H2 sections:

1. `## What We Know` (1–2 sentence narrowest supported conclusion)
2. `## How Confident We Are` (starts with `**Grade**: [High / Moderate / Low / Very Low]`)
3. `## Evidence and Causal Assessment`
4. `## Effect Size and Persistence`
5. `## Bias, Heterogeneity, and Confounding` (classified as `largely confounded (>50%)`, `partially confounded (20–50%)`, `robust (<20%)`, `n/a`, or `not classified`)
6. `## What Remains Uncertain`
7. `## What This Does Not Mean` (**Mandatory > 40 chars**: explicitly prohibited overreach or deterministic extrapolation)
8. `## What Action Is Reasonably Justified`
9. `## Sources`

## 2. Five-Rule Promotion Gate (`scripts/five_rule_check.py`)

Never flip `status: draft` $\to$ `status: stable` without running:
```bash
python scripts/five_rule_check.py <card-or-book-dir> --online-retraction-check
```
- **Rule 1:** Every `sources:` entry has a resolvable `http(s)` / DOI `resource` and is mirrored in `SOURCES.md` and `sources.bib` (run `python scripts/sync_okf_sources.py`).
- **Rule 2:** Zero retractions or unresolved Expressions of Concern on Crossref (`updates_or_errata`) and OpenAlex (`is_retracted`).
- **Rule 3:** Independent or conceptual replication (or formal mathematical theorem + empirical benchmark) documented.
- **Rule 4:** Exact token match between YAML `confidence:` and in-body `**Grade**:`.
- **Rule 5:** Non-empty `## What This Does Not Mean` (>40 characters).
