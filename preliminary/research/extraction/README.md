# Evidence-extraction pipeline

A research dossier is not an evidence card. A 200-page file should decompose into several **atomic claims**, each narrow enough to receive a certainty grade and a source trail.

Do not copy dossier prose into `evidence-cards/`. Extract, audit, then write a card from the claim record.

## Per-claim fields

For each claim, record:

1. **Claim** — the narrowest defensible statement.
2. **Outcome and window** — what is measured, at what developmental age.
3. **Exposure / intervention / context**.
4. **Study design(s)** — RCT, sibling comparison, children-of-twins, MR, cohort, natural experiment, mechanistic, animal, guideline synthesis.
5. **Effect size, precision, persistence**.
6. **Threats to inference and heterogeneity**.
7. **Sources** — exact citations and stable identifiers (DOI, PMID, URL). Unresolved citations stay unresolved until matched.
8. **Manuscript role** — `anomaly`, `mechanism`, `boundary`, `system`, or `case`.

Then label the claim:

| Label | Meaning |
|---|---|
| `promote` | Narrow claim, designs and sources are in hand; ready to draft a card after source registration in `SOURCES.md` |
| `needs-source-audit` | Claim is plausible but citations, effect sizes, or designs are unverified |
| `interpretive-only` | Useful for chapter framing; not a standalone empirical card |
| `exclude` | Too broad, deterministic, duplicative, or unsupported |

## Card grouping

Group claims into likely cards **after** they are extracted. One card = one claim family, not one chapter. Example for Chapter 2: prenatal auditory learning, prenatal stress/anxiety, maternal nutrition, teratogenic exposures, and prenatal-to-postnatal continuity are separate cards — not one “prenatal development” card.

## Destination rules

- Empirical claims → `evidence-cards/` + `SOURCES.md` in the same commit.
- Framing, voice, and Science/Interpretation/Art distinctions → `chapters/` via the draft/review stream.
- Unresolved or interpretive material → remain preliminary.

## Current maps

- [Chapter 2 Evidence Map](ch02-first-environment--evidence-map.md) — first full-system test of this pipeline.
- [Chapter 3 Evidence Map](ch03-great-transition--evidence-map.md) — transition physiology, bounded skin-to-skin, crying, feeding coordination, preterm group risk.
- [Chapter 4 Evidence Map](ch04-regulatory-relationship--evidence-map.md) — co-regulation, deprivation, and feeding-as-regulation; sleep/attachment reconciled.
- [Chapter 5 Evidence Map](ch05-becoming-a-mind--evidence-map.md) — looking-time, attention, object permanence, joint attention; narrowing/statistical/contingency reconciled.
- [Chapter 7 Evidence Map](ch07-birth-of-language--evidence-map.md) — perceptual narrowing, statistical segmentation, conversational turns, dual language; screens reconciled; joint attention now a Ch. 5 card.
- [Selected-card re-audit](selected-cards--replication-bias-reaudit.md) — first replication/bias pass; none to `stable`.
- [Catalog-wide retraction search](catalog-wide-retraction-search.md) — Crossref/PubMed lookup; none to `stable`.
- [DOI recovery and Retraction Watch](doi-recovery-retraction-watch.md) — 15 of 20 previously unchecked IDs recovered; five listings later repaired.
- [Five listings and Retraction Watch dump](five-listings-and-retraction-watch-dump.md) — `hiscock-2016` retired; dump finds no retractions; none to `stable`.
