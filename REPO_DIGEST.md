# Parenthood: The Atlas — Repository Digest

Snapshot of `ralfcam/parenthood-atlas` as of 2026-09-15. This file is a map for humans and agents: what the repo is, where canonical vs staging work lives, how content is supposed to move, and what is currently inconsistent.

This is a **markdown knowledge base and book workbench**, not an application. There is no runtime, package manager, test suite, or CI.

---

## 1. What this repository is

**Parenthood: The Atlas** is a longitudinal evidence atlas of developmental science from roughly one year before conception through age 3.

Mission (from `README.md`): determine what can be concluded, with reasonable confidence, about how biological, psychological, relational, social, and educational conditions influence early development — and what, if anything, those conclusions justify families, institutions, and societies doing.

The project never collapses three categories:

| Category | Meaning |
|---|---|
| **Science** | What can be observed, measured, tested, replicated, and reasonably inferred |
| **Interpretation** | How evidence should be understood, contextualized, and translated |
| **Art** | Judgment, relationships, values, culture, individuality, uncertainty, lived experience |

Scientific findings do not automatically generate parenting prescriptions. The book is a field guide / natural-history atlas, not a parenting manual.

GitHub description: *Knowledge base and versioned research atlas for Parenthood: The Atlas — developmental science from preconception through age 3.*

---

## 2. Mental model: three layers

```
preliminary/          staging workbench (not OKF, not voice-checked)
  MANIFEST.md         inventory of every uploaded file
  triage/             chapter-level extraction plans (Part I: Ch. 1–5, 7)
  research/           archival dossiers, plans, syntheses
  research/extraction/  atomic claims and evidence maps
  drafts-chapters/    full chapter prose still in composition
  drafts-chapters/reviews/  structural/voice notes (do not overwrite drafts)

evidence-cards/       canonical knowledge base (OKF v0.2, draft status)
SOURCES.md            single point of truth for cited sources
CONTRIBUTING.md       evidence-evaluation methodology

chapters/             canonical manuscript (seed outlines only so far)
COMPOSITION.md        book grammar (voice, chapter rhythm, claim calibration)
style/                voice checklist, forbidden phrases, anomaly bank
```

Promotion is one-way:

1. Research notes in `preliminary/research/` → atomic claims in `research/extraction/` → OKF evidence card in `evidence-cards/` + register sources in `SOURCES.md` + log in `CHANGELOG.md`.
2. Chapter drafts in `preliminary/drafts-chapters/` → review notes in `drafts-chapters/reviews/` → curated copy to `chapters/` only after linked cards are audited.

Do not treat `preliminary/` as published. Do not treat `evidence-cards/` cards as settled: every card is still `status: draft`. YAML `confidence` now matches in-body grades; that is not the same as `status: stable`.

---

## 3. Directory map

```
README.md                 Mission, governing rules
index.md                  OKF v0.2 bundle root
SPEC.md                   Pointer to the external OKF v0.2 spec
REPO_DIGEST.md            This map
CONTRIBUTING.md           Evidence-card methodology
CHANGELOG.md              Knowledge-base version history
COMPOSITION.md            Book compositional grammar
SOURCES.md                Master source catalog (62 verified)
evidence-cards/           31 draft cards + template + index
chapters/                 Working 15-chapter TOC; curated Ch. 2, 6, and 7; seed sketches for Ch. 2 and 4
style/                    Voice/style constraints for manuscript prose
preliminary/              Staging area (research notes + chapter drafts)
```

There is no `.cursor/`, `package.json`, Dockerfile, or test suite. `SPEC.md` exists as a pointer to the external OKF v0.2 specification.

---

## 4. How to work in this repo

### Adding or revising an evidence card

1. Copy `evidence-cards/_TEMPLATE.md` (OKF frontmatter is in the template).
2. Keep the body to ~200–400 words unless deeper analysis is warranted.
3. If a card anchors a chapter, CONTRIBUTING also asks for `atlas_domains` and `chapter_hooks`. New Chapter 2 cards have these fields; most first-pass cards still do not.
4. List the card in `evidence-cards/index.md`.
5. Register every source in `SOURCES.md` in the same commit (verified table + frontmatter `sources` array, or Unresolved Citations).
6. Log the change in `CHANGELOG.md` under `[Unreleased]` as Added / Revised / Retracted / Structure.

### Promoting a chapter

1. Draft in `preliminary/drafts-chapters/`.
2. Run `style/voice-checklist.md` (all boxes must pass).
3. Avoid phrases in `style/forbidden-phrases.md`.
4. Calibrate claim strength to certainty grades using `COMPOSITION.md` Appendix A.
5. Write a curated copy into `chapters/` (do not overwrite archival drafts).
6. Link relevant evidence cards.
7. Write a review note in `preliminary/drafts-chapters/reviews/`.
8. Log in `CHANGELOG.md`.

### Evidence rules that override prose instincts

From `CONTRIBUTING.md` / `README.md`:

- State the **narrowest** claim the evidence supports.
- Distinguish association, prediction, contribution, causation, prevention, and determinism.
- Match recommendation strength to confidence.
- When genetically informed designs substantially attenuate an observational association, treat confounding as the default explanation.
- Report attenuation: largely confounded (>50%), partially confounded (20–50%), robust (<20%).
- Do not assume early effects persist.
- Do not average effects across incompatible designs.
- Screens: never treat "screen time" as a unitary exposure.
- Interventions: separate efficacy, effectiveness, scalability, and institutional dependence.

Certainty grades: High / Moderate / Low / Very Low.

---

## 5. Knowledge base inventory

OKF bundle root: `index.md` (`okf_version: "0.2"`).

Thirty-one cards, all `status: draft`. YAML `confidence` is aligned with in-body grades. Cards still need a completed catalog-wide retraction search before `stable`. A first selected-card re-audit is in `preliminary/research/extraction/selected-cards--replication-bias-reaudit.md` and a catalog-wide Crossref/PubMed lookup is in `preliminary/research/extraction/catalog-wide-retraction-search.md`; both moved **none** to `stable`. See `evidence-cards/index.md` for the full list. Chapter 2 has draft cards for C01–C12. Chapter 3 has transition, SSC, crying, feeding-coordination, and preterm cards. Chapter 4 has co-regulation and deprivation cards (sleep/attachment reconciled, not rewritten). Chapter 6 has a contingency-learning card. Chapter 7 has perceptual-narrowing, statistical-segmentation, conversational-turns, and dual-language cards (screens reconciled).

The eight first-pass cards plus C05/C07 remain as in the previous digest table. New Chapter 2 cards: `prenatal-developmental-timing.md`, `placenta-as-mediator.md`, `prenatal-neural-construction.md`, `fetal-autonomic-maturation.md`, `prenatal-iodine-thyroid.md`, `prenatal-alcohol-fasd.md`, `prenatal-tobacco-birthweight.md`, `prenatal-environmental-mixtures.md`, `fetal-growth-not-destiny.md`.

| File | Domain | YAML / in-body grade | Narrowest current claim |
|---|---|---|---|
| `prenatal-maternal-stress-anxiety.md` | pregnancy / stress | `low-to-moderate` | Observational prenatal stress/anxiety associations largely attenuate under genetically informed designs |
| `prenatal-auditory-learning.md` | pregnancy / language | `moderate` (Low for lasting cognitive advantage) | Late-pregnancy speech can shape newborn preference; not lasting cognitive advantage |
| `prenatal-folate-ntd.md` | pregnancy / nutrition | `high` (Low for other anomalies / IQ) | Periconceptional folic acid substantially reduces NTD risk |
| `breastfeeding-cognitive-development.md` | feeding | `moderate` | PROBIT RCT + sibling comparisons: small, verbal-concentrated, fading effect |
| `early-childcare-quality.md` | childcare | `moderate` | NICHD SECCYD: modest quality–cognition links; parenting predicts more |
| `screen-time-language-development.md` | screens / language | `low-to-moderate` | Weak-to-moderate observational associations; decompose content, co-use, context |
| `responsive-caregiving-attachment-interventions.md` | attachment | `moderate-to-high-sensitivity; moderate-attachment` | Short sensitivity RCTs move sensitivity more than attachment security |
| `infant-sleep-training.md` | sleep | `low-to-moderate` | RCTs/cohorts: no measured attachment or behavioral harm through age 6 |
| `self-regulation-delay-of-gratification.md` | executive function | `moderate-to-high-overstatement-of-original` | 2018 NICHD replication: original marshmallow-test predictor claim mostly confounded |
| `preschool-early-education-rct.md` | early learning | `moderate-historical; low-generalization` | Small high-fidelity 1960s–70s RCTs show persistent adult gains; modern at-scale programs are a different claim |
| `infant-contingency-learning.md` | early learning | `high-controlled; low-transfer` | Mobile paradigm: action–outcome learning under control, not adult-like cause |
| `neonatal-cardiopulmonary-transition.md` | birth | `high-sequence; moderate-timing` | Birth reorganizes gas exchange and circulation; not a personality forecast |
| `skin-to-skin-immediate-physiology.md` | birth / feeding | `moderate-breastfeeding; low-infant-physiology` | Healthy-newborn SSC: breastfeeding 1–4 months Moderate; infant physiology Low |
| `infant-caregiver-coregulation.md` | regulation | `moderate-existence; low-to-moderate-mechanism` | Bidirectional co-regulation; nurturing care is an ecology |
| `severe-institutional-deprivation.md` | attachment / social | `high-danger; moderate-to-high-placement` | BEIP family placement after severe deprivation ≠ ordinary parenting |
| `infant-perceptual-narrowing.md` | language | `high-lab; moderate-timetable` | First-year phonetic attunement; not a sealed deadline |
| `infant-statistical-speech-segmentation.md` | language | `high-lab; low-transfer` | Transitional-probability segmentation in the lab, not household vocabulary |
| `conversational-turns-language.md` | language | `moderate-prediction; low-causation` | Turns at 18–24 months predict later language better than word counts |
| `dual-language-does-not-confuse.md` | language | `high-no-confusion; moderate-individual-trajectories` | Dual exposure as such does not confuse; not an automatic cognitive bonus |
| `infant-crying-as-signal.md` | birth / regulation | `moderate-signal; low-acoustic-decoding` | Crying is a graded distress signal, not a cause-code |
| `suck-swallow-breathe-coordination.md` | birth / feeding | `high-coordination; moderate-practice-effects` | Oral feeding requires asynchronous maturational coordination |
| `preterm-cognition-group-risk.md` | birth | `moderate-group; low-individual` | Preterm group SMD about −0.57; not an individual sentence |

### Declared but missing evidence cards

From `evidence-cards/index.md` "Not Yet Started":

- Preconception exposures (parental age, paternal contributions, periconceptional nutrition beyond folate)
- Birth (mode of delivery and birth experience still held; skin-to-skin, crying, feeding coordination, and preterm group risk now have cards)
- Play (unstructured/free play, pretend play, outdoor play)
- Social development beyond attachment (peers, siblings, daycare socialization)

Priority domains in `README.md` that still lack cards include preconception, play, and several feeding/language/stress subtopics beyond the thirty-one current cards.

### Sources

`SOURCES.md` is the catalog of record:

- **62 verified** resources with URLs, mirrored in the file's OKF `sources` array
- **12 first-pass unresolved citations resolved** (two were already in the verified table; two titles were corrected to the matching papers). Resolution log lives under Unresolved Citations.
- Catalog itself is `status: draft`. A catalog-wide Crossref/PubMed retraction lookup found no retraction/EoC titles among DOI-resolved records; 20 older IDs still lack a recovered DOI. None promoted to `stable`.

---

## 6. Manuscript: working TOC is 15 chapters

**Decision (2026-09-15):** the book follows the 15-chapter draft sequence. Recorded in `chapters/_OUTLINE.md`. The 8-chapter seed is a compositional sketch, not the TOC.

### Seed sketches (still useful as 10-step checklists)

`chapters/01-first-environment.md` is a 10-step sketch. `chapters/02-first-environment.md` is the curated proof-of-voice chapter. `chapters/04-regulatory-relationship.md` is the Ch. 4 seed sketch (relocated from `02-regulatory-relationship.md`). `chapters/06-the-mind-in-motion.md` is the curated Chapter 6 expansion. `chapters/07-the-birth-of-language.md` is the curated Chapter 7 copy.

| Canonical file | Maps to working TOC | Status |
|---|---|---|
| `chapters/01-first-environment.md` | Draft Ch. 2, *The First Environment* | Seed outline; not the promoted chapter |
| `chapters/02-first-environment.md` | Working TOC Ch. 2 | Curated, voice-checked; archival draft untouched |
| `chapters/04-regulatory-relationship.md` | Draft Ch. 4, *The Regulatory Relationship* | Seed outline; not promoted |
| `chapters/06-the-mind-in-motion.md` | Working TOC Ch. 6 | Curated expansion; archival draft untouched |
| `chapters/07-the-birth-of-language.md` | Working TOC Ch. 7 | Curated, voice-checked; archival draft untouched |

`COMPOSITION.md` Appendix B target: 2,500–4,000 words per finished chapter.

### Preliminary full drafts (the working book)

`preliminary/drafts-chapters/` holds long prose drafts (~1.6k–5.5k words). Filenames are inconsistent (spaces, mixed case, some missing `.md`). The closing draft is `chapter 15` (heading: Chapter 15, *Three Years: What Has Been Built?*). There is no Chapter 16.

| File | Title (from heading) | Words (approx.) |
|---|---|---|
| `chapter 1` | Before the Child Is Born | 4,000 |
| `chapter 2` | The First Environment | 4,300 |
| `chapter 3` | The Great Transition | 5,500 |
| `chapter 4` | The Regulatory Relationship | 4,600 |
| `chapter 5` | Becoming a Mind | 4,900 |
| `chapter 6` | The Mind in Motion | 1,625 archival; curated copy in `chapters/` ~2,700 |
| `chapter 7` | The Birth of Language | 4,908 archival; curated copy in `chapters/` ~3,785 |
| `chapter 8.md` | The Expanding World | 3,900 |
| `Chapter 9.md` | The Emotional Revolution | 4,600 |
| `Chapter 10.md` | Boundaries, Behavior, and the First Rules | 5,100 |
| `chapter 11` | The Developing Executive | 3,900 |
| `chapter 12` | Play, Imagination, and Meaning | 3,400 |
| `chapter 13` | The Ecology of Development | 4,100 |
| `chapter 14` | What Actually Works? | 4,400 |
| `chapter 15` | Three Years: What Has Been Built? | 4,200 |

None of the archival files have been overwritten. Curated, voice-checked copies exist for Chapter 2, Chapter 6, and Chapter 7. Some drafts contain leftover citation artifacts such as `:contentReference[oaicite:…]`.

Seed filenames still say `01` / `02` because they were written against the old numbering. Do not promote them as Chapter 1 and 2 of the book.

---

## 7. Preliminary research workbench

`preliminary/research/` is the literature staging area. Most files are `.docx`. A few are markdown/text.

Paired with the 15-chapter draft sequence:

| Chapter | Research file(s) |
|---|---|
| 1 | `Chapter 1 Research Dossier.docx` |
| 2 | `Chapter 2 Research Dossier — The First Environment.docx`; `The First Environment_ The Biological Architecture of Early Development.docx`; `Prenatal Biology Research Plan.docx` |
| 3 | `Chapter 3 — The Great Transition  Preliminary Research Plan.docx`; `The Great Transition_ Birth as a Developmental Continuum.docx` |
| 4 | `Chapter 4 — The Regulatory Relationship.docx`; `The Regulatory Relationship_ The Relational Foundation of Human Development.docx` |
| 5 | `Chapter 5 Preliminary Research Plan.docx`; `Chapter 5 Preliminary Research Dossier_ Becoming a Mind.docx` (~3.0 MB); `Infant Cognitive Development Research Plan.docx` (~2.9 MB) |
| 6 | `Chapter 6 Preliminary Research Dossier.docx` |
| 7 | `Chapter 7 — The Birth of Language.docx`; `The Birth of Language_ A Comprehensive Research Synthesis.docx` (~2.9 MB) |
| 8 | `Chapter 8 Preliminary Research Plan — The Expanding World.docx`; `The Expanding World_ Moving Beyond the Primary Dyad in Early Human Development.docx` (~2.9 MB) |
| 9 | `Chapter 9 Preliminary Research Plan — The Emotional Revolution.docx`; `Developmental Emotion Regulation Research.docx` |
| 10 | `Chapter 10 Preliminary Research Dossier.docx`; `Early Behavioral Regulation Research Plan.docx` (~2.9 MB) |
| 11 | `Chapter 11 — The Developing Executive.docx` |
| 12 | `Chapter 12 Preliminary Research Plan.docx`; `Childhood Play Research Plan.docx` |
| 13 | `Chapter 13 — The Ecology of Development  Preliminary Research Plan.docx`; `Ecology of Development Research Plan.docx` (~2.9 MB) |
| 14 | `Chapter 14 Research Architecture  What Actually Works.docx`; `Early Childhood Interventions Evidence Review.docx` (~3.1 MB) |
| 15 | `Chapter 15 Research Dossier  Three Years — What Has Been Built.md`; `Developmental Synthesis at Age Three.txt` |

Cross-cutting: `Child Development Research Synthesis.docx`, `Early Human Development Book Research.docx`.

Several ~3 MB `.docx` files likely contain embedded media. They are not machine-traversable as OKF. Convert into evidence cards before treating claims as part of the knowledge base.

---

## 8. Compositional grammar (book layer)

`COMPOSITION.md` is the governing literary framework. Compressed formula:

1. Begin with something ordinary.
2. Reveal that it is stranger than it appears.
3. Investigate it scientifically.
4. Expose the mechanisms.
5. Define the limits of knowledge.
6. Reconnect it to the larger developmental system.
7. Return to the child.

Default chapter rhythm (Appendix B): Phenomenon → Puzzle → Case → Question → Competing Explanations → Mechanism → Evidence → Boundary → System → Return.

Voice: calm, curious, empirically disciplined, narratively intelligent, philosophically reflective, anti-deterministic. Author role: cartographer / investigator / guide — not guru, coach, or detached academic.

The book must never become: a parenting instruction manual, optimization literature, parental-guilt literature, neuroscience sensationalism, unevidenced evolutionary storytelling, ideological advocacy, or certainty masquerading as expertise.

Supporting files:

- `style/voice-checklist.md` — pre-commit review for chapter drafts
- `style/forbidden-phrases.md` — "you should", "optimal", "critical window" (unless High + persistence shown), "science says", etc.
- `style/anomaly-bank.md` — 10 opening-hook observations

Claim-strength table: High → "evidence shows"; Moderate → "suggests/likely"; Low → "is associated with"; Very Low → "unclear/conflicting".

---

## 9. Git history and current status

Default branch: `main`.

The repo was initialized 2026-09-14 (KB structure, 8 evidence cards, OKF retrofit, `SOURCES.md`, compositional grammar) and expanded 2026-09-14/15 with `preliminary/` research dossiers and chapter drafts 1–15. The closing draft was originally committed as `chapter 16` and later renamed to `chapter 15` to match its heading.

`CHANGELOG.md` records the knowledge-base bootstrap, the corpus-governance layer (PR #1), and the 2026-09-15 source-audit package (new cards, citation resolutions, TOC decision, SPEC stub, Ch. 14 triage).

---

## 10. Known gaps and agent hazards

1. **Working TOC is 15 chapters.** See `chapters/_OUTLINE.md`. Seed sketches: `01-first-environment.md` (Ch. 2) and `04-regulatory-relationship.md` (Ch. 4). Curated copies: `02-first-environment.md`, `06-the-mind-in-motion.md`, `07-the-birth-of-language.md`.
2. **Chapter 6 archival remains thin** (~1,625 words). A curated copy in `chapters/06-the-mind-in-motion.md` is now in the Appendix B range. Chapter 7 has a curated copy (~3,785 words); archival ~4,908 remains untouched.
3. **`_TEMPLATE.md` now has OKF frontmatter.** Keep it in sync when live-card fields change.
4. **`atlas_domains` / `chapter_hooks`** are on the newer cards; most first-pass cards still omit them.
5. **Draft citation artifacts.** `chapter 14` has 29 `:contentReference[oaicite:…]` leftovers; listed as a promotion blocker in `preliminary/triage/ch14-what-actually-works--triage.md`. Do not overwrite the archival draft.
6. **Binary research files.** Most of `preliminary/research/` is `.docx`; grep/search will miss them.
7. **Catalog-wide retraction lookup has begun** (Crossref/PubMed). No retraction/EoC titles among DOI-resolved records; 20 older IDs still lack a recovered DOI; Retraction Watch dump not done. None moved to `stable`.
8. **No tests or lint.** Quality control is methodological (CONTRIBUTING + voice checklist), not automated.
9. **Do not invent prescriptions.** If evidence does not justify an action, say so.
10. **Screen-time card citation mismatch.** Frontmatter currently points at a 2023 *Child Development* vocabulary meta-analysis while the body leads with Madigan 2020 *JAMA Pediatrics*. Recorded in the Chapter 7 map; not repaired.

---

## 11. Suggested next work

Done in this package: Chapter 7 language claims as draft cards (screens reconciled, not rewritten); curated voice-checked Chapter 7; catalog-wide Crossref/PubMed retraction lookup with none to `stable`; remaining Chapter 3 crying, feeding-coordination, and prematurity cards.

Highest-leverage remaining knowledge-base work:

- Recover DOIs for the twenty catalog IDs still unchecked by Crossref, and query Retraction Watch, before any card moves to `stable`.
- Remaining Ch. 4 feeding-as-regulation claim, if a curated Chapter 3 or 4 is next. Chapter 3 C04/C05/C07 now have cards; mode of delivery still held; C03 neonatal perception still open.
- Source-audit remaining Chapter 7 dossier cards (joint attention, gesture, babbling, parent-implemented interventions) if Chapter 7 needs a second evidence pass.
- Source-audit remaining Chapter 6 dossier cards (embodied action, exploration, causal representation, imitation) if Chapter 6 needs a second evidence pass.

Highest-leverage remaining manuscript work:

- Voice-check and promote a curated Chapter 3 (*The Great Transition*) now that crying, feeding coordination, and prematurity have cards.
- Voice-check Chapter 5 (*Becoming a Mind*) or Chapter 4 as the next proof-of-voice candidate.
- Normalize remaining draft filenames on **curated copies only**.

---

## 12. Quick start for a new agent

1. Read `README.md`, `CONTRIBUTING.md`, then this digest.
2. If changing evidence: start from `preliminary/MANIFEST.md` and `preliminary/research/extraction/`; never skip `SOURCES.md` + `CHANGELOG.md`.
3. If changing chapters: treat `chapters/` as canonical and `preliminary/drafts-chapters/` as staging; write reviews in `drafts-chapters/reviews/` rather than overwriting archival drafts.
4. If the task is research synthesis, start from existing cards and `SOURCES.md` before opening the `.docx` dossiers.
5. Preserve Science / Interpretation / Art. When unsure, write a narrower claim.
