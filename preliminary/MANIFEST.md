# Corpus manifest

Inventory of every file under `preliminary/` as of 2026-09-15. Original uploads are archival. Do not rename or move them. Curated copies use the naming convention in [`README.md`](README.md).

**Chapter numbering** follows the 15-chapter draft sequence. Canonical seed files in `chapters/` use a shorter map (seed Ch. 1 = this Ch. 2; seed Ch. 2 = this Ch. 4).

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
| G-T01 | `preliminary/triage/ch01-framing--triage.md` | documentation | remain-preliminary | triage-ready | Ch. 1 extraction plan |
| G-T02 | `preliminary/triage/ch02-first-environment--triage.md` | documentation | remain-preliminary | extracted | Points at Ch. 2 map |
| G-EXT | `preliminary/research/extraction/README.md` | documentation | remain-preliminary | promoted | Atomic-claim pipeline |
| G-MAP02 | `preliminary/research/extraction/ch02-first-environment--evidence-map.md` | documentation | remain-preliminary | extracted | First full-system test |
| G-REV | `preliminary/drafts-chapters/reviews/README.md` | documentation | remain-preliminary | promoted | Voice-review stream |
| G-R02 | `preliminary/drafts-chapters/reviews/ch02-structural-and-voice-review.md` | documentation | remain-preliminary | extracted | Review only; draft not overwritten |

## Chapter 1 — Before the Child Is Born

Window: preconception through early pregnancy / reader-contract (not a single exposure window). Domains: biological, psychological, relational, social.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C01-D1 | `research/Chapter 1 Research Dossier.docx` | research-dossier | `chapters/` + selected `evidence-cards/` | triage-ready | Primary Ch. 1 dossier. Tests bounded claim that development has antecedents before birth without parental control. |
| C01-S1 | `research/Early Human Development Book Research.docx` | synthesis | remain-preliminary | unreviewed | Alternate Ch. 1 scientific dossier; overlaps C01-D1 and C02 files (fetal movement/HRV). Treat as `duplicate/alternate` until compared. |
| C01-D | `drafts-chapters/chapter 1` | chapter-draft | `chapters/` | triage-ready | Extensionless markdown. Future copy: `ch01-before-the-child-is-born--draft-01.md`. |

## Chapter 2 — The First Environment

Window: conception through birth (embryonic and fetal periods). Domains: biological, psychological (stress), social (exposures, care access).

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C02-D1 | `research/Chapter 2 Research Dossier — The First Environment.docx` | research-dossier | `evidence-cards/` + `SOURCES.md` + `chapters/` | extracted | Canonical Ch. 2 dossier; already proposes 10 cards. Prefer this over C02-S1 for extraction. |
| C02-S1 | `research/The First Environment_ The Biological Architecture of Early Development.docx` | synthesis | remain-preliminary | extracted | Module-style rewrite of the same territory (clock, placenta, circulation, brain, stress, nutrition, mixtures, growth). Overlaps C02-D1; keep as alternate, do not extract twice. |
| C02-P1 | `research/Prenatal Biology Research Plan.docx` | research-plan | remain-preliminary | unreviewed | Same byte size as C02-S1 (35,215) but different hash. Opening title matches C02-S1. Treat as `duplicate/alternate` until byte-level diff. |
| C02-D | `drafts-chapters/chapter 2` | chapter-draft | `chapters/` | extracted | Extensionless markdown. Maps to canonical seed `chapters/01-first-environment.md` (numbering collision). |

## Chapter 3 — The Great Transition

Window: late fetal period through neonatal transition. Domains: biological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C03-P1 | `research/Chapter 3 — The Great Transition  Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | Birth as change of regulatory environment, not a reset. |
| C03-S1 | `research/The Great Transition_ Birth as a Developmental Continuum.docx` | synthesis | remain-preliminary | unreviewed | Alternate on the same theme; likely overlaps C03-P1. |
| C03-D | `drafts-chapters/chapter 3` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 4 — The Regulatory Relationship

Window: newborn through first year (co-regulation, sleep, feeding, attachment). Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C04-D1 | `research/Chapter 4 — The Regulatory Relationship.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Overlaps existing cards: sleep training, responsive caregiving/attachment. Canonical seed: `chapters/02-regulatory-relationship.md`. |
| C04-S1 | `research/The Regulatory Relationship_ The Relational Foundation of Human Development.docx` | synthesis | remain-preliminary | unreviewed | Alternate; keep until compared with C04-D1. |
| C04-D | `drafts-chapters/chapter 4` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 5 — Becoming a Mind

Window: infancy (perception, attention, learning, prediction). Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C05-P1 | `research/Chapter 5 Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | Interactionist infant-mind plan. Pair with C05-D1; do not merge into one card. |
| C05-D1 | `research/Chapter 5 Preliminary Research Dossier_ Becoming a Mind.docx` | research-dossier | `evidence-cards/` | unreviewed | ~3.0 MB; likely embedded media. Overlaps C05-P1. |
| C05-P2 | `research/Infant Cognitive Development Research Plan.docx` | research-plan | remain-preliminary | unreviewed | ~2.9 MB. Broad cognitive plan overlapping C05-P1/C05-D1. |
| C05-D | `drafts-chapters/chapter 5` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 6 — The Mind in Motion

Window: infancy through toddler action/learning. Domains: biological, psychological.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C06-D1 | `research/Chapter 6 Preliminary Research Dossier.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Second-wave relative to Part I, but needed before Ch. 7. |
| C06-D | `drafts-chapters/chapter 6` | chapter-draft | `chapters/` | unreviewed | Shortest draft (~1,600 words); likely incomplete. |

## Chapter 7 — The Birth of Language

Window: prenatal auditory tuning through first words/grammar. Domains: biological, psychological, relational, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C07-P1 | `research/Chapter 7 — The Birth of Language.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | Chapter-specific plan. |
| C07-S1 | `research/The Birth of Language_ A Comprehensive Research Synthesis.docx` | synthesis | `evidence-cards/` + `SOURCES.md` | unreviewed | ~3.0 MB comprehensive synthesis; overlaps C07-P1 and existing `screen-time-language-development.md`. |
| C07-D | `drafts-chapters/chapter 7` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 8 — The Expanding World

Window: late infancy through toddler extrafamilial care. Domains: relational, social, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C08-P1 | `research/Chapter 8 Preliminary Research Plan — The Expanding World.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | Extrafamilial relationships, childcare. |
| C08-S1 | `research/The Expanding World_ Moving Beyond the Primary Dyad in Early Human Development.docx` | synthesis | remain-preliminary | unreviewed | ~2.9 MB alternate; overlaps C08-P1 and existing `early-childcare-quality.md`. |
| C08-D | `drafts-chapters/chapter 8.md` | chapter-draft | `chapters/` | unreviewed | Has `.md` suffix unlike most drafts. |

## Chapter 9 — The Emotional Revolution

Window: infancy through toddler emotion. Domains: biological, psychological, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C09-P1 | `research/Chapter 9 Preliminary Research Plan — The Emotional Revolution.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | |
| C09-S1 | `research/Developmental Emotion Regulation Research.docx` | research-plan | remain-preliminary | unreviewed | Cross-cutting emotion-regulation notes; also feeds Ch. 4 and 10. |
| C09-D | `drafts-chapters/Chapter 9.md` | chapter-draft | `chapters/` | unreviewed | Title-case filename. |

## Chapter 10 — Boundaries, Behavior, and the First Rules

Window: toddlerhood (inhibition, rules, aggression, internalization). Domains: psychological, relational, social.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C10-D1 | `research/Chapter 10 Preliminary Research Dossier.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Overlaps Ch. 11 (executive) and existing delay-of-gratification card. |
| C10-P1 | `research/Early Behavioral Regulation Research Plan.docx` | research-plan | remain-preliminary | unreviewed | ~2.9 MB; overlapping regulation plan. |
| C10-D | `drafts-chapters/Chapter 10.md` | chapter-draft | `chapters/` | unreviewed | Title-case filename. |

## Chapter 11 — The Developing Executive

Window: toddler through age 3. Domains: biological, psychological.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C11-D1 | `research/Chapter 11 — The Developing Executive.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Overlaps existing `self-regulation-delay-of-gratification.md`. |
| C11-D | `drafts-chapters/chapter 11` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 12 — Play, Imagination, and Meaning

Window: toddler through age 3. Domains: psychological, relational, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C12-P1 | `research/Chapter 12 Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | Play is listed as a missing evidence-card topic. |
| C12-P2 | `research/Childhood Play Research Plan.docx` | research-plan | remain-preliminary | unreviewed | Alternate/narrower play plan. |
| C12-D | `drafts-chapters/chapter 12` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 13 — The Ecology of Development

Window: whole 0–3 ecology (family, material conditions, institutions). Domains: social, educational, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C13-P1 | `research/Chapter 13 — The Ecology of Development  Preliminary Research Plan.docx` | research-plan | `evidence-cards/` + `chapters/` | unreviewed | |
| C13-P2 | `research/Ecology of Development Research Plan.docx` | research-plan | remain-preliminary | unreviewed | ~2.9 MB alternate. |
| C13-D | `drafts-chapters/chapter 13` | chapter-draft | `chapters/` | unreviewed | Extensionless markdown. |

## Chapter 14 — What Actually Works?

Window: intervention evidence across 0–3. Domains: educational, social, relational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C14-D1 | `research/Chapter 14 Research Architecture  What Actually Works.docx` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Overlaps existing preschool RCT card and attachment-intervention card. |
| C14-S1 | `research/Early Childhood Interventions Evidence Review.docx` | synthesis | `evidence-cards/` + `SOURCES.md` | unreviewed | ~3.1 MB. Extract after Ch. 2–4 cards exist so interventions are not the first causal claims. |
| C14-D | `drafts-chapters/chapter 14` | chapter-draft | `chapters/` | unreviewed | Contains leftover `:contentReference[oaicite:…]` artifacts. |

## Chapter 15 — Three Years: What Has Been Built?

Window: age-3 waypoint (what has accumulated; what remains open). Domains: biological, psychological, relational, social, educational.

| ID | Path | Type | Destination | Status | Overlap / notes |
|---|---|---|---|---|---|
| C15-D1 | `research/Chapter 15 Research Dossier  Three Years — What Has Been Built.md` | research-dossier | `evidence-cards/` + `chapters/` | unreviewed | Already markdown. |
| C15-S1 | `research/Developmental Synthesis at Age Three.txt` | synthesis | remain-preliminary | unreviewed | Alternate age-3 synthesis. |
| C15-D | `drafts-chapters/chapter 15` | chapter-draft | `chapters/` | unreviewed | Renamed from `chapter 16`. Heading already said Chapter 15. |

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
| `prenatal-maternal-stress-anxiety.md` | 2 | Reconcile in Ch. 2 map before any rewrite |
| `infant-sleep-training.md` | 4 | Wait for Ch. 4 triage |
| `responsive-caregiving-attachment-interventions.md` | 4 | Wait for Ch. 4 triage |
| `breastfeeding-cognitive-development.md` | 4 / 5 | Feeding is Ch. 4 adjacent; cognition Ch. 5 |
| `screen-time-language-development.md` | 7 | Wait for Ch. 7 |
| `early-childcare-quality.md` | 8 | Second wave |
| `self-regulation-delay-of-gratification.md` | 10 / 11 | Second wave |
| `preschool-early-education-rct.md` | 14 | Second wave |

## Counts

- Research/synthesis/plan files: 31
- Chapter drafts: 15
- Documentation/governance (including this file): 11
- Exact byte-identical duplicates: none found. Near-duplicates: C02-P1 ~ C02-S1; several ~3 MB chapter syntheses that likely embed media.
