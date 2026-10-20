# Open Knowledge Format (OKF) v0.2 — Multi-Series Specification

This monorepo conforms to **Open Knowledge Format v0.2** across all book series (`series/architectures-of-memory/` and `series/parenthood-atlas/`). The normative specification is external; this file defines how OKF v0.2 governs evidence cards and source catalogs across both series.

- Canonical spec: [GoogleCloudPlatform/open-knowledge-format `SPEC.md`](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
- Index files (`index.md`, `evidence-cards/index.md`) have no frontmatter, per OKF §8.
- Template: [`templates/evidence-card-template.md`](templates/evidence-card-template.md) (mirrored in each book's `evidence-cards/_TEMPLATE.md`).

## How this monorepo uses OKF v0.2

Every empirical, architectural, organizational, or developmental claim that anchors a chapter is captured in an atomic **Evidence Card** (`evidence-cards/<slug>.md`) backed by verified bibliographic entries in `sources.bib` (BibTeX, locked via `academic-bib` MCP) and/or `SOURCES.md` (`AuthorYear` catalog).

### Required YAML Frontmatter Fields

| Field | Role Across Both Series |
|---|---|
| `type` | `Evidence Card` or `Source Catalog` |
| `title`, `description`, `tags` | Human/agent routing; `description` states the **narrowest defensible claim** in one sentence |
| `status` | `draft` until a card passes the Five-Rule Promotion Gate (`scripts/five_rule_check.py`); `stable` after verification |
| `confidence` | Certainty grade from [`CONTRIBUTING.md`](CONTRIBUTING.md): `high`, `moderate`, `low`, `very-low`, or compound grades (e.g., `low-to-moderate`, `high-mechanism; low-org-transfer`) |
| `generated` | `{ by, at }` provenance (e.g., `{ by: agent:antigravity, at: 2026-10-20T22:00:00Z }`) |
| `stale_after` | Re-audit horizon (ISO-8601 timestamp) |
| `sources` | List of `{ id, resource, title }` entries with resolvable `https://doi.org/...` or canonical URLs |
| `series_domains` / `atlas_domains` | Domain tags mapping the card to its series chapters |
| `chapter_hooks` | `[anomaly, mechanism, boundary, technical, organizational, philosophical]` |

### Required 9-Section Card Body

All cards in `series/architectures-of-memory/book-*/evidence-cards/` and `series/parenthood-atlas/evidence-cards/` must contain the exact 9 H2 headings enforced by [`scripts/five_rule_check.py`](scripts/five_rule_check.py):

1. `## What We Know` — Narrowest supported conclusion (1–2 sentences).
2. `## How Confident We Are` — Starts with `**Grade**: [High / Moderate / Low / Very Low]` (matching YAML `confidence` tokens) + justification.
3. `## Evidence and Causal Assessment` — Study designs, mathematical proofs, benchmarks, or cohort syntheses, replication status, and causal/external-validity limitations.
4. `## Effect Size and Persistence` — Quantitative bounds, spectral decay rates, latency/accuracy trade-offs, or developmental effect sizes and time horizons.
5. `## Bias, Heterogeneity, and Confounding` — Alternative explanations, benchmark leakage, organizational selection effects, or genetic/socioeconomic confounding (`largely confounded (>50%)`, `partially confounded (20–50%)`, `robust (<20%)`, or `n/a`).
6. `## What Remains Uncertain` — Decision-relevant open questions.
7. `## What This Does Not Mean` — **Mandatory (>40 chars):** Explicitly prohibited overreach, anthropomorphic extrapolation, or deterministic interpretation.
8. `## What Action Is Reasonably Justified` — Proportionate engineering, organizational, or family/policy guidance (or statement that no action follows).
9. `## Sources` — Formatted citation list matching YAML `sources` and `sources.bib` / `SOURCES.md`.
