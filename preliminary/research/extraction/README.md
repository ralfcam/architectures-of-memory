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
- [Chapter 1 Evidence Map](ch01-before-the-child--evidence-map.md) — framing claims; paternal-age card; timing/neural/folate/stress linked.
- [Chapter 3 Evidence Map](ch03-great-transition--evidence-map.md) — transition physiology, bounded skin-to-skin, crying, feeding coordination, preterm group risk.
- [Chapter 3 Evidence Map](ch03-great-transition--evidence-map.md) — transition physiology, bounded skin-to-skin, crying, feeding coordination, preterm group risk.
- [Chapter 4 Evidence Map](ch04-regulatory-relationship--evidence-map.md) — co-regulation, deprivation, and feeding-as-regulation; sleep/attachment reconciled.
- [Chapter 5 Evidence Map](ch05-becoming-a-mind--evidence-map.md) — looking-time, attention, object permanence, joint attention; narrowing/statistical/contingency reconciled.
- [Chapter 7 Evidence Map](ch07-birth-of-language--evidence-map.md) — perceptual narrowing, statistical segmentation, conversational turns, dual language, pointing, babbling; screens ID-repaired; parent-implemented language card added; joint attention is a Ch. 5 card.
- [Chapter 8 Evidence Map](ch08-expanding-world--evidence-map.md) — social referencing, networks, peers; childcare/BEIP reconciled.
- [Chapter 9 Evidence Map](ch09-emotional-revolution--evidence-map.md) — still-face, temperament, inhibition; co-regulation/delay reconciled.
- [Chapter 11 Evidence Map](ch11-developing-executive--evidence-map.md) — EF unity/diversity and inhibitory control; Watts delay reconciled.
- [Chapter 12 Evidence Map](ch12-play-imagination--evidence-map.md) — symbolic play and Lillard overclaim.
- [Stable-promotion candidates](stable-promotion-candidates.md) — physiology/lab path; three narrow claims `stable`.
- [Stable-candidate replication note](stable-candidates--replication-note.md) — five-rule re-audit; folate, Saffran, neonatal transition.
- [Preconception extraction plan](preconception--extraction-plan.md) — first dedicated domain plan; Kong card exists.
- [Play extraction plan](play--extraction-plan.md) — Chapter 12; two first-pass cards exist.
- [Social-beyond-attachment extraction plan](social-beyond-attachment--extraction-plan.md) — Chapters 8–11 remainder.
- [Selected-card re-audit](selected-cards--replication-bias-reaudit.md) — first replication/bias pass; none to `stable` in that pass.
- [Catalog-wide replication / attenuation](catalog-wide-replication-attenuation.md) — every live card classified; three later `stable` flips.
- [Catalog-wide retraction search](catalog-wide-retraction-search.md) — Crossref/PubMed lookup; Cochrane `new_version` is not retraction.
- [DOI recovery and Retraction Watch](doi-recovery-retraction-watch.md) — 15 of 20 previously unchecked IDs recovered; five listings later repaired.
- [Five listings and Retraction Watch dump](five-listings-and-retraction-watch-dump.md) — `hiscock-2016` retired; dump finds no retractions.
