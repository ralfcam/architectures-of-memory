# Corpus manifest

Inventory of every file under `preliminary/` as of 2026-09-15. Original uploads are archival. Do not rename or move them. Curated copies use the naming convention in [`README.md`](README.md).

**Chapter numbering** follows the 15-chapter draft sequence. Curated copies: `chapters/01-before-the-child-is-born.md` (Ch. 1), `chapters/02-first-environment.md` (Ch. 2), `chapters/03-the-great-transition.md` (Ch. 3), `chapters/04-regulatory-relationship.md` (Ch. 4), `chapters/05-becoming-a-mind.md` (Ch. 5), `chapters/06-the-mind-in-motion.md` (Ch. 6), `chapters/07-the-birth-of-language.md` (Ch. 7), `chapters/08-the-expanding-world.md` (Ch. 8), `chapters/09-the-emotional-revolution.md` (Ch. 9), `chapters/10-boundaries-behavior.md` (Ch. 10), `chapters/11-the-developing-executive.md` (Ch. 11), `chapters/12-play-imagination.md` (Ch. 12), `chapters/13-the-ecology-of-development.md` (Ch. 13), `chapters/14-what-actually-works.md` (Ch. 14, Appendix B range), `chapters/15-three-years.md` (Ch. 15). Leftover seed `chapters/01-first-environment.md` removed.

## Status and type vocabularies

| Field | Values |
|---|---|
| Artifact type | `research-plan`, `research-dossier`, `synthesis`, `chapter-draft`, `duplicate/alternate`, `documentation` |
| Destination | `evidence-cards/`, `chapters/`, `SOURCES.md`, `remain-preliminary` |
| Status | `unreviewed`, `triage-ready`, `extracted`, `audited`, `promoted` |
| Domains | biological, psychological, relational, social, educational |

Part I (Ch. 1–5 + 7) is `triage-ready` at the chapter level. Individual files stay `unreviewed` until extracted, except Chapter 2 research/draft files marked `extracted` after the [Chapter 2 Evidence Map](research/extraction/ch02-first-environment--evidence-map.md).

## Governance files (this package)

| ID | Path | Type | Destination | Status | Notes |
|---|---|---|---|---|---|
| G-README | `preliminary/README.md` | documentation | remain-preliminary | promoted | Workbench + naming convention |
| G-MANIFEST | `preliminary/MANIFEST.md` | documentation | remain-preliminary | promoted | This file |
| G-TRIAGE | `preliminary/triage/README.md` | documentation | remain-preliminary | promoted | Part I sequence |
| G-T01 | `preliminary/triage/ch01-framing--triage.md` | documentation | remain-preliminary | extracted | Ch. 1 extraction plan; curated copy promoted |
| G-MAP01 | `preliminary/research/extraction/ch01-before-the-child--evidence-map.md` | documentation | remain-preliminary | extracted | C01-D1 vs C01-S1 hashes; paternal-age card; four prenatal cards linked |
| G-R01 | `preliminary/drafts-chapters/reviews/ch01-curated-01-before-the-child--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 1 |
| G-T08 | `preliminary/triage/ch08-expanding-world--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 8; four cards including father/kin remainder; curated copy promoted |
| G-MAP08 | `preliminary/research/extraction/ch08-expanding-world--evidence-map.md` | documentation | remain-preliminary | extracted | Referencing, networks, peers, father/kin; childcare/BEIP reconcile |
| G-AUDIT08b | `preliminary/research/extraction/ch08-remainder--source-audit.md` | documentation | remain-preliminary | extracted | McWayne 2013; Dagan 2018 |
| G-T10 | `preliminary/triage/ch10-boundaries-behavior--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 10; compliance, aggression, punishment; curated copy promoted |
| G-MAP10 | `preliminary/research/extraction/ch10-boundaries-behavior--evidence-map.md` | documentation | remain-preliminary | extracted | EF/delay reconcile; C10-P1 not double-extracted |
| G-AUDIT10 | `preliminary/research/extraction/ch10-behavior--source-audit.md` | documentation | remain-preliminary | extracted | Kochanska 1995; Tremblay 2004; Gershoff 2016 |
| G-T13 | `preliminary/triage/ch13-ecology--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 13; income/cash and MTO; curated copy promoted |
| G-MAP13 | `preliminary/research/extraction/ch13-ecology--evidence-map.md` | documentation | remain-preliminary | extracted | Childcare/BEIP/preschool RCT reconcile |
| G-AUDIT13 | `preliminary/research/extraction/ch13-ecology--source-audit.md` | documentation | remain-preliminary | extracted | Troller-Renfree 2022; Noble 2025; Chetty 2016 |
| G-V01 | `preliminary/releases/v0.1-slice.md` | documentation | remain-preliminary | extracted | **Tagged** `v0.1` on `main` at `c7c2a7a` |
| G-V02 | `preliminary/releases/v0.2-slice.md` | documentation | remain-preliminary | extracted | **Tagged** `v0.2` on `main` at `9bbc2d9` |
| G-V03 | `preliminary/releases/v0.3-slice.md` | documentation | remain-preliminary | extracted | **Tagged** `v0.3` on `main` at `21d1a0d` |
| G-T15 | `preliminary/triage/ch15-three-years--triage.md` | documentation | remain-preliminary | extracted | Age-3 waypoint; three draft cards; curated copy promoted |
| G-MAP15 | `preliminary/research/extraction/ch15-three-years--evidence-map.md` | documentation | remain-preliminary | extracted | Continuity, self-control, resilience; Watts/BEIP/preschool RCT reconcile |
| G-AUDIT15 | `preliminary/research/extraction/ch15-three-years--source-audit.md` | documentation | remain-preliminary | extracted | Roberts 2000; Moffitt 2011; Masten 2001 |
| G-T09 | `preliminary/triage/ch09-emotional-revolution--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 9; still-face, temperament, inhibition; curated copy promoted |
| G-MAP09 | `preliminary/research/extraction/ch09-emotional-revolution--evidence-map.md` | documentation | remain-preliminary | extracted | Co-regulation/delay reconcile |
| G-AUDIT09 | `preliminary/research/extraction/ch09-emotion--source-audit.md` | documentation | remain-preliminary | extracted | Tronick; Mesman; Gartstein & Rothbart; Clauss |
| G-T11 | `preliminary/triage/ch11-developing-executive--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 11; EF construct and inhibition; curated copy promoted |
| G-MAP11 | `preliminary/research/extraction/ch11-developing-executive--evidence-map.md` | documentation | remain-preliminary | extracted | Watts delay reconcile |
| G-AUDIT11 | `preliminary/research/extraction/ch11-executive--source-audit.md` | documentation | remain-preliminary | extracted | Miyake; Garon; Carlson |
| G-T12 | `preliminary/triage/ch12-play-imagination--triage.md` | documentation | remain-preliminary | extracted | Second-wave Ch. 12; symbolic play and Lillard; curated copy promoted |
| G-MAP12 | `preliminary/research/extraction/ch12-play-imagination--evidence-map.md` | documentation | remain-preliminary | extracted | C12-P2 not double-extracted |
| G-AUDIT12 | `preliminary/research/extraction/ch12-play--source-audit.md` | documentation | remain-preliminary | extracted | Belsky & Most; Lillard 2013 |
| G-STABLE | `preliminary/research/extraction/stable-promotion-candidates.md` | documentation | remain-preliminary | extracted | Three narrow claims `stable`; others stay `draft` |
| G-STABLENOTE | `preliminary/research/extraction/stable-candidates--replication-note.md` | documentation | remain-preliminary | extracted | Five-rule re-audit |
| G-T14 | `preliminary/triage/ch14-what-actually-works--triage.md` | documentation | remain-preliminary | extracted | Artifacts stripped in curated copy; archival still has 29 crumbs |
| G-T02 | `preliminary/triage/ch02-first-environment--triage.md` | documentation | remain-preliminary | extracted | Points at Ch. 2 map |
| G-EXT | `preliminary/research/extraction/README.md` | documentation | remain-preliminary | promoted | Atomic-claim pipeline |
| G-MAP02 | `preliminary/research/extraction/ch02-first-environment--evidence-map.md` | documentation | remain-preliminary | extracted | C01–C12 `promote`; C13 interpretive on growth card |
| G-AUDIT02 | `preliminary/research/extraction/ch02-c05-c07-c06--source-audit.md` | documentation | remain-preliminary | extracted | Source audit for C05/C07/C06 |
| G-AUDIT02b | `preliminary/research/extraction/ch02-c01-c04-c08-c13--source-audit.md` | documentation | remain-preliminary | extracted | Remaining Ch. 2 claims |
| G-REV | `preliminary/drafts-chapters/reviews/README.md` | documentation | remain-preliminary | promoted | Voice-review stream |
| G-R02 | `preliminary/drafts-chapters/reviews/ch02-structural-and-voice-review.md` | documentation | remain-preliminary | extracted | Review of archival draft only |
| G-R02b | `preliminary/drafts-chapters/reviews/ch02-curated-02-first-environment--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated `chapters/02-first-environment.md` |
| G-T03 | `preliminary/triage/ch03-great-transition--triage.md` | documentation | remain-preliminary | extracted | Ch. 3 extraction plan; five cards exist; curated copy promoted; C08 held |
| G-T04 | `preliminary/triage/ch04-regulatory-relationship--triage.md` | documentation | remain-preliminary | extracted | Ch. 4 extraction plan; co-regulation, BEIP, feeding cards; curated copy promoted |
| G-MAP03 | `preliminary/research/extraction/ch03-great-transition--evidence-map.md` | documentation | remain-preliminary | extracted | C02/C04–C07 promote; C08 held |
| G-AUDIT03 | `preliminary/research/extraction/ch03-transition-physiology--source-audit.md` | documentation | remain-preliminary | extracted | Morton 2016; Moore 2016; Zeifman 2017; Lau 2015; Burstein 2024; P1≠S1 hashes |
| G-MAP04 | `preliminary/research/extraction/ch04-regulatory-relationship--evidence-map.md` | documentation | remain-preliminary | extracted | Sleep/attachment reconcile; C01/C02/C04 promote |
| G-AUDIT04 | `preliminary/research/extraction/ch04-coregulation-deprivation--source-audit.md` | documentation | remain-preliminary | extracted | Nurturing Care; Feldman; BEIP; Black & Aboud 2011 |
| G-REAUDIT | `preliminary/research/extraction/selected-cards--replication-bias-reaudit.md` | documentation | remain-preliminary | extracted | First re-audit pass; none to `stable` |
| G-REPLICATE | `preliminary/research/extraction/catalog-wide-replication-attenuation.md` | documentation | remain-preliminary | extracted | Catalog-wide replication/GI classification; none to `stable` |
| G-RETRACT | `preliminary/research/extraction/catalog-wide-retraction-search.md` | documentation | remain-preliminary | extracted | Catalog-wide Crossref/PubMed lookup; none to `stable` |
| G-DOI | `preliminary/research/extraction/doi-recovery-retraction-watch.md` | documentation | remain-preliminary | extracted | 15 of 20 DOIs recovered; RW queried; none to `stable` |
| G-RWDUMP | `preliminary/research/extraction/five-listings-and-retraction-watch-dump.md` | documentation | remain-preliminary | extracted | Five listings repaired; `hiscock-2016` retired; RW dump; none to `stable` |
| G-MAP05 | `preliminary/research/extraction/ch05-becoming-a-mind--evidence-map.md` | documentation | remain-preliminary | extracted | C01/C03/C06/C07 promote; C02/C04/C05 reconcile |
| G-AUDIT05 | `preliminary/research/extraction/ch05-cognition--source-audit.md` | documentation | remain-preliminary | extracted | Aslin; Colombo; Baillargeon; Mundy; P1≠D1≠P2 hashes |
| G-T05 | `preliminary/triage/ch05-becoming-a-mind--triage.md` | documentation | remain-preliminary | extracted | Ch. 5 extraction plan; curated copy promoted |
| G-AUDIT06 | `preliminary/research/extraction/ch06-contingency-learning--source-audit.md` | documentation | remain-preliminary | extracted | Mobile paradigm card |
| G-AUDIT06b | `preliminary/research/extraction/ch06-remaining--source-audit.md` | documentation | remain-preliminary | extracted | Embodiment, exploration, VOE, deferred imitation |
| G-AUDIT07b | `preliminary/research/extraction/ch07-parent-implemented--source-audit.md` | documentation | remain-preliminary | extracted | Heidlage 2020; Whitehurst 1988 |
| G-R14 | `preliminary/drafts-chapters/reviews/ch14-curated-14-what-actually-works--voice-review.md` | documentation | remain-preliminary | extracted | Appendix B trim pass after Part II cards |
| G-R06 | `preliminary/drafts-chapters/reviews/ch06-curated-06-the-mind-in-motion--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 6 |
| G-MAP07 | `preliminary/research/extraction/ch07-birth-of-language--evidence-map.md` | documentation | remain-preliminary | extracted | C02/C03/C05–C09 promote; screens ID-repaired |
| G-AUDIT07 | `preliminary/research/extraction/ch07-language--source-audit.md` | documentation | remain-preliminary | extracted | Werker; Saffran; Gilkerson; NAP; P1≠S1 hashes |
| G-R07 | `preliminary/drafts-chapters/reviews/ch07-curated-07-the-birth-of-language--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 7 |
| G-R03 | `preliminary/drafts-chapters/reviews/ch03-curated-03-the-great-transition--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 3 |
| G-R04 | `preliminary/drafts-chapters/reviews/ch04-curated-04-regulatory-relationship--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 4; records Ch. 4-not-Ch. 5 decision |
| G-R05 | `preliminary/drafts-chapters/reviews/ch05-curated-05-becoming-a-mind--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 5 |
| G-R08 | `preliminary/drafts-chapters/reviews/ch08-curated-08-the-expanding-world--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 8 |
| G-R09 | `preliminary/drafts-chapters/reviews/ch09-curated-09-the-emotional-revolution--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 9 |
| G-R10 | `preliminary/drafts-chapters/reviews/ch10-curated-10-boundaries-behavior--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 10 |
| G-R11 | `preliminary/drafts-chapters/reviews/ch11-curated-11-the-developing-executive--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 11 |
| G-R12 | `preliminary/drafts-chapters/reviews/ch12-curated-12-play-imagination--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 12 |
| G-R13 | `preliminary/drafts-chapters/reviews/ch13-curated-13-the-ecology-of-development--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 13 |
| G-R15 | `preliminary/drafts-chapters/reviews/ch15-curated-15-three-years--voice-review.md` | documentation | remain-preliminary | promoted | Voice review of curated Ch. 15 |
| G-AUDIT-REM | `preliminary/research/extraction/remaining-domains--source-audit.md` | documentation | remain-preliminary | extracted | Warneken, Brussoni, Carneiro, Cook, Dean |
| G-SECOND | `preliminary/research/extraction/draft-cards--second-pass-audit.md` | documentation | remain-preliminary | extracted | All 65 draft cards; no extra `stable` |
| G-CONS | `preliminary/research/extraction/cross-chapter-consistency--v03.md` | documentation | remain-preliminary | extracted | Six load-bearing terms across Ch. 1–15 |
| G-REVMS | `preliminary/research/extraction/manuscript-revision-pass--v03.md` | documentation | remain-preliminary | extracted | Transitions, S/I/A, remaining-domain naming |

## Chapter 1 — Before the Child Is Born

Window: preconception through early pregnancy / reader-contract (not a single exposure window). Domains: biological, psychological, relational, social.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C01-D1 | `research/Chapter 1 Research Dossier.docx` | research-dossier | `chapters/` + selected `evidence-cards/` | triage-ready | Primary Ch. 1 dossier. Tests bounded claim that development has antecedents before birth without parental control. |
| C01-S1 | `research/Early Human Development Book Research.docx` | synthesis | remain-preliminary | unreviewed | Alternate Ch. 1 scientific dossier; overlaps C01-D1 and C02 files (fetal movement/HRV). Treat as `duplicate/alternate` until compared. |
| C01-D | `drafts-chapters/chapter 1` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Curated copy: `chapters/01-before-the-child-is-born.md`. |

## Chapter 2 — The First Environment

Window: conception through birth (embryonic and fetal periods). Domains: biological, psychological (stress), social (exposures, care access).

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C02-D1 | `research/Chapter 2 Research Dossier — The First Environment.docx` | research-dossier | `evidence-cards/` + `SOURCES.md` + `chapters/` | extracted | Canonical Ch. 2 dossier; already proposes 10 cards. Prefer this over C02-S1 for extraction. |
| C02-S1 | `research/The First Environment_ The Biological Architecture of Early Development.docx` | synthesis | remain-preliminary | extracted | Module-style rewrite of the same territory (clock, placenta, circulation, brain, stress, nutrition, mixtures, growth). Overlaps C02-D1; keep as alternate, do not extract twice. |
| C02-P1 | `research/Prenatal Biology Research Plan.docx` | research-plan | remain-preliminary | unreviewed | Same byte size as C02-S1 (35,215) but different hash. Opening title matches C02-S1. Treat as `duplicate/alternate` until byte-level diff. |
| C02-D | `drafts-chapters/chapter 2` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Curated copy: `chapters/02-first-environment.md`. Leftover seed removed. |

## Chapter 3 — The Great Transition

Window: late fetal period through neonatal transition. Domains: biological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C03-P1 | `research/Chapter 3 — The Great Transition  Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | C02/C04–C07 cards exist; C08 mode of delivery held. Hash ≠ C03-S1. |
| C03-S1 | `research/The Great Transition_ Birth as a Developmental Continuum.docx` | synthesis | remain-preliminary | extracted | Alternate; different size/hash from C03-P1. Do not double-extract. |
| C03-D | `drafts-chapters/chapter 3` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival; not overwritten. Curated copy: `chapters/03-the-great-transition.md`. |

## Chapter 4 — The Regulatory Relationship

Window: newborn through first year (co-regulation, sleep, feeding, attachment). Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C04-D1 | `research/Chapter 4 — The Regulatory Relationship.docx` | research-dossier | `evidence-cards/` + `chapters/` | extracted | Sleep/attachment cards reconciled, not re-extracted. Feeding-as-regulation card added. Canonical curated copy: `chapters/04-regulatory-relationship.md`. |
| C04-S1 | `research/The Regulatory Relationship_ The Relational Foundation of Human Development.docx` | synthesis | remain-preliminary | extracted | Alternate; hash ≠ C04-D1. Keep; do not double-extract. |
| C04-D | `drafts-chapters/chapter 4` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival; not overwritten. Curated copy replaced the prior 10-step seed. |

## Chapter 5 — Becoming a Mind

Window: infancy (perception, attention, learning, prediction). Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C05-P1 | `research/Chapter 5 Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | Extraction source. SHA-256 `73db3356…`. C01/C03/C06/C07 cards exist. |
| C05-D1 | `research/Chapter 5 Preliminary Research Dossier_ Becoming a Mind.docx` | research-dossier | `evidence-cards/` | extracted | ~3.0 MB; hash ≠ C05-P1. Keep as alternate. |
| C05-P2 | `research/Infant Cognitive Development Research Plan.docx` | research-plan | remain-preliminary | extracted | ~2.9 MB. Hash ≠ C05-P1/D1. Do not double-extract. |
| C05-D | `drafts-chapters/chapter 5` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival; not overwritten. Curated copy: `chapters/05-becoming-a-mind.md`. |

## Chapter 6 — The Mind in Motion

Window: infancy through toddler action/learning. Domains: biological, psychological.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C06-D1 | `research/Chapter 6 Preliminary Research Dossier.docx` | research-dossier | `evidence-cards/` + `chapters/` | extracted | Contingency-learning card extracted; other dossier cards still open. |
| C06-D | `drafts-chapters/chapter 6` | chapter-draft | `chapters/` | extracted | Archival (~1,625 words) not overwritten. Curated copy: `chapters/06-the-mind-in-motion.md`. |

## Chapter 7 — The Birth of Language

Window: prenatal auditory tuning through first words/grammar. Domains: biological, psychological, relational, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C07-P1 | `research/Chapter 7 — The Birth of Language.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | Extraction source. SHA-256 `1fef9bce…`. |
| C07-S1 | `research/The Birth of Language_ A Comprehensive Research Synthesis.docx` | synthesis | `evidence-cards/` + `SOURCES.md` | extracted | Alternate (~3.0 MB); not identical to C07-P1. Do not double-extract. Overlaps existing `screen-time-language-development.md`. |
| C07-D | `drafts-chapters/chapter 7` | chapter-draft | `chapters/` | extracted | Archival (~4,908 words) not overwritten. Curated copy: `chapters/07-the-birth-of-language.md`. Pointing and babbling cards added; parent-implemented interventions still open. |

## Chapter 8 — The Expanding World

Window: late infancy through toddler extrafamilial care. Domains: relational, social, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C08-P1 | `research/Chapter 8 Preliminary Research Plan — The Expanding World.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | Extrafamilial relationships, childcare. |
| C08-S1 | `research/The Expanding World_ Moving Beyond the Primary Dyad in Early Human Development.docx` | synthesis | remain-preliminary | unreviewed | ~2.9 MB alternate; overlaps C08-P1 and existing `early-childcare-quality.md`. |
| C08-D | `drafts-chapters/chapter 8.md` | chapter-draft | `chapters/` | extracted | Has `.md` suffix unlike most drafts. Four draft cards. Curated copy: `chapters/08-the-expanding-world.md`. |

## Chapter 9 — The Emotional Revolution

Window: infancy through toddler emotion. Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C09-P1 | `research/Chapter 9 Preliminary Research Plan — The Emotional Revolution.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | SHA-256 `fde0a305324f0ac5…`. Three draft cards. |
| C09-S1 | `research/Developmental Emotion Regulation Research.docx` | research-plan | remain-preliminary | unreviewed | Cross-cutting emotion-regulation notes; also feeds Ch. 4 and 10. Do not double-extract. |
| C09-D | `drafts-chapters/Chapter 9.md` | chapter-draft | `chapters/` | extracted | Title-case filename. Archival untouched. Curated copy: `chapters/09-the-emotional-revolution.md`. |

## Chapter 10 — Boundaries, Behavior, and the First Rules

Window: toddlerhood (inhibition, rules, aggression, internalization). Domains: psychological, relational, social.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C10-D1 | `research/Chapter 10 Preliminary Research Dossier.docx` | research-dossier | `evidence-cards/` + `chapters/` | extracted | SHA-256 `79db88fd58219a26…`. Three draft cards. Overlaps Ch. 11 (executive) — reconcile only. |
| C10-P1 | `research/Early Behavioral Regulation Research Plan.docx` | research-plan | remain-preliminary | unreviewed | ~2.9 MB; overlapping regulation plan. Do not double-extract. |
| C10-D | `drafts-chapters/Chapter 10.md` | chapter-draft | `chapters/` | extracted | Title-case filename. Archival untouched. Curated copy: `chapters/10-boundaries-behavior.md`. |

## Chapter 11 — The Developing Executive

Window: toddler through age 3. Domains: biological, psychological.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C11-D1 | `research/Chapter 11 — The Developing Executive.docx` | research-dossier | `evidence-cards/` + `chapters/` | extracted | SHA-256 `07bba2a8719ac09e…`. Overlaps existing `self-regulation-delay-of-gratification.md` (reconcile only). |
| C11-D | `drafts-chapters/chapter 11` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival untouched. Curated copy: `chapters/11-the-developing-executive.md`. |

## Chapter 12 — Play, Imagination, and Meaning

Window: toddler through age 3. Domains: psychological, relational, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C12-P1 | `research/Chapter 12 Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | SHA-256 `71b833457a3b02b7…`. Two draft cards. |
| C12-P2 | `research/Childhood Play Research Plan.docx` | research-plan | remain-preliminary | unreviewed | Alternate/narrower play plan. Do not double-extract. |
| C12-D | `drafts-chapters/chapter 12` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival untouched. Curated copy: `chapters/12-play-imagination.md`. |

## Chapter 13 — The Ecology of Development

Window: whole 0–3 ecology (family, material conditions, institutions). Domains: social, educational, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C13-P1 | `research/Chapter 13 — The Ecology of Development  Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | extracted | SHA-256 `efd534f954d0a814…`. Two draft cards. |
| C13-P2 | `research/Ecology of Development Research Plan.docx` | research-plan | remain-preliminary | unreviewed | ~2.9 MB alternate. Do not double-extract. |
| C13-D | `drafts-chapters/chapter 13` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Archival untouched. Curated copy: `chapters/13-the-ecology-of-development.md`. |

## Chapter 14 — What Actually Works?

Window: intervention evidence across 0–3. Domains: educational, social, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C14-D1 | `research/Chapter 14 Research Architecture  What Actually Works.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Overlaps existing preschool RCT card and attachment-intervention card. |
| C14-S1 | `research/Early Childhood Interventions Evidence Review.docx` | synthesis | `evidence-cards/` + `SOURCES.md` | unreviewed | ~3.1 MB. Extract after Ch. 2–4 cards exist so interventions are not the first causal claims. |
| C14-D | `drafts-chapters/chapter 14` | chapter-draft | `chapters/` | extracted | **Archival still has 29 `:contentReference` leftovers.** Curated copy: `chapters/14-what-actually-works.md` (Appendix B range). Do not overwrite. |

## Chapter 15 — Three Years: What Has Been Built?

Window: age-3 waypoint (what has accumulated; what remains open). Domains: biological, psychological, relational, social, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C15-D1 | `research/Chapter 15 Research Dossier  Three Years — What Has Been Built.md` | research-dossier | `evidence-cards/` + `chapters/` | extracted | SHA-256 `b3ee7f3cbb1687e8…`. Three draft cards. Curated copy promoted. |
| C15-S1 | `research/Developmental Synthesis at Age Three.txt` | synthesis | remain-preliminary | unreviewed | Alternate age-3 synthesis. Do not double-extract. |
| C15-D | `drafts-chapters/chapter 15` | chapter-draft | `chapters/` | extracted | Renamed from `chapter 16`. Archival untouched. Curated copy: `chapters/15-three-years.md`. |

## Cross-cutting / book-level

Window: preconception through age 3. Domains: all five.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| X-S1 | `research/Child Development Research Synthesis.docx` | synthesis | remain-preliminary | unreviewed | Book-level Science/Interpretation/Art synthesis; overlaps Ch. 1 framing. |
| R-README | `research/README.md` | documentation | remain-preliminary | promoted | Staging notes. |
| D-README | `drafts-chapters/README.md` | documentation | remain-preliminary | promoted | Draft staging notes. |

## Visible overlap clusters (do not extract twice)

1. **First Environment cluster:** C02-D1, C02-S1, C02-P1, plus fetal-behavior material in C01-S1.
2. **Becoming a Mind cluster:** C05-P1, C05-D1, C05-P2.
3. **Language cluster:** C07-P1, C07-S1, plus prenatal auditory claim in Ch. 2.
4. **Expanding World / childcare:** C08-P1, C08-S1, existing early-childcare card.
5. **Regulation cluster:** C04-D1, C04-S1, C09-S1, C10-P1, existing sleep and attachment cards.
6. **Age-3 synthesis:** C15-D1, C15-S1.

## Existing evidence-card collisions

| Existing card | First colliding chapter | Action |
|---|---|---|
| `prenatal-maternal-stress-anxiety.md` | 2 | Reconciled (C06); still `status: draft` |
| `prenatal-auditory-learning.md` | 2 | Source-audited (C05); still `status: draft` |
| `prenatal-folate-ntd.md` | 2 | Source-audited (C07); still `status: draft` |
| `prenatal-developmental-timing.md` | 2 | Source-audited (C01); still `status: draft` |
| `placenta-as-mediator.md` | 2 | Source-audited (C02); still `status: draft` |
| `prenatal-neural-construction.md` | 2 | Source-audited (C03); still `status: draft` |
| `fetal-autonomic-maturation.md` | 2 | Source-audited (C04); still `status: draft` |
| `prenatal-iodine-thyroid.md` | 2 | Source-audited (C08); still `status: draft` |
| `prenatal-alcohol-fasd.md` | 2 | Source-audited (C09); still `status: draft` |
| `prenatal-tobacco-birthweight.md` | 2 | Source-audited (C10); still `status: draft` |
| `prenatal-environmental-mixtures.md` | 2 | Source-audited (C11); still `status: draft` |
| `fetal-growth-not-destiny.md` | 2 | Source-audited (C12); C13 held here; still `status: draft` |
| `infant-sleep-training.md` | 4 | Reconciled; do not re-extract; still `status: draft` |
| `responsive-caregiving-attachment-interventions.md` | 4 | Reconciled; do not re-extract; still `status: draft` |
| `neonatal-cardiopulmonary-transition.md` | 3 | Source-audited (C02); still `status: draft` |
| `skin-to-skin-immediate-physiology.md` | 3 | Source-audited (C06); still `status: draft` |
| `infant-caregiver-coregulation.md` | 4 | Source-audited (C01); still `status: draft` |
| `severe-institutional-deprivation.md` | 4 | Source-audited (C02 / BEIP); still `status: draft` |
| `infant-contingency-learning.md` | 6 | Source-audited (C01); still `status: draft` |
| `breastfeeding-cognitive-development.md` | 4 / 5 | Feeding is Ch. 4 adjacent; cognition Ch. 5 |
| `screen-time-language-development.md` | 7 | IDs repaired (Madigan 2020 vs Jing 2023); still `status: draft`. Frontmatter/body citation mismatch recorded then repaired. |
| `early-childcare-quality.md` | 8 | Second wave |
| `self-regulation-delay-of-gratification.md` | 10 / 11 | Second wave |
| `preschool-early-education-rct.md` | 14 | Second wave |
| `infant-perceptual-narrowing.md` | 7 | Source-audited (C03); still `status: draft` |
| `infant-statistical-speech-segmentation.md` | 7 | Source-audited (C02); still `status: draft` |
| `conversational-turns-language.md` | 7 | Source-audited (C07/C08); still `status: draft` |
| `dual-language-does-not-confuse.md` | 7 | Source-audited (C09); still `status: draft` |
| `infant-crying-as-signal.md` | 3 | Source-audited (C04); still `status: draft` |
| `suck-swallow-breathe-coordination.md` | 3 | Source-audited (C05); still `status: draft` |
| `preterm-cognition-group-risk.md` | 3 | Source-audited (C07); still `status: draft` |
| `responsive-feeding-as-regulation.md` | 4 | Source-audited (C04); still `status: draft` |
| `looking-time-as-measurement.md` | 5 | Source-audited (C01); still `status: draft` |
| `infant-attention-as-gatekeeper.md` | 5 | Source-audited (C03); still `status: draft` |
| `object-permanence-looking-vs-search.md` | 5 | Source-audited (C06); still `status: draft` |
| `joint-attention-shared-reference.md` | 5 / 7 | Source-audited (C07 / CH07-C04); still `status: draft` |
| `infant-pointing-as-shared-reference.md` | 7 | Source-audited (CH07-C05); still `status: draft` |
| `infant-babbling-as-exploration.md` | 7 | Source-audited (CH07-C06); still `status: draft` |
| `paternal-age-de-novo-mutations.md` | 1 | Source-audited (CH01-C06); still `status: draft` |
| `infant-social-referencing.md` | 8 | Source-audited (CH08-C02); still `status: draft` |
| `infant-multiple-caregiver-attachments.md` | 8 | Source-audited (CH08-C01); still `status: draft` |
| `toddler-peer-interaction.md` | 8 | Source-audited (CH08-C04); still `status: draft` |
| `embodied-perception-action.md` | 6 | Source-audited; still `status: draft` |
| `exploration-as-sampling.md` | 6 | Source-audited; still `status: draft` |
| `infant-physical-reasoning.md` | 6 | Source-audited; still `status: draft` |
| `deferred-imitation.md` | 6 | Source-audited; still `status: draft` |
| `parent-implemented-language.md` | 7 | Source-audited; still `status: draft` |

## Counts

- Research/synthesis/plan files: 31
- Chapter drafts: 15
- Documentation/governance (including this file): 42
- Exact byte-identical duplicates: none found. Near-duplicates: C02-P1 ~ C02-S1; several ~3 MB chapter syntheses that likely embed media.
