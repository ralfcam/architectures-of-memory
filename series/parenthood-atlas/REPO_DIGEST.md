# Parenthood: The Atlas — Repository Digest

Snapshot of `ralfcam/parenthood-atlas` as of 2026-09-16. This file is a map for humans and agents: what the repo is, where canonical vs staging work lives, how content is supposed to move, and what is currently inconsistent.

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

evidence-cards/       canonical knowledge base (72 OKF v0.2 cards: 12 stable, 60 draft)
SOURCES.md            single point of truth for cited sources (127 verified sources)
CONTRIBUTING.md       evidence-evaluation methodology

chapters/             canonical manuscript (15 curated chapters, 41,342 words)
COMPOSITION.md        book grammar (voice, chapter rhythm, claim calibration)
style/                voice checklist, forbidden phrases, anomaly bank
```

Promotion is one-way:

1. Research notes in `preliminary/research/` → atomic claims in `research/extraction/` → OKF evidence card in `evidence-cards/` + register sources in `SOURCES.md` + log in `CHANGELOG.md`.
2. Chapter drafts in `preliminary/drafts-chapters/` → review notes in `drafts-chapters/reviews/` → curated copy to `chapters/` only after linked cards are audited.

Do not treat `preliminary/` as published. Do not treat `evidence-cards/` cards as settled unless `status: stable`. Three physiology/lab cards are `stable` for a *narrow* claim only. YAML `confidence` matching in-body grades is not the same as `status: stable`.

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
SOURCES.md                Master source catalog (114 verified)
evidence-cards/           68 cards (7 `stable` for a narrow claim; 61 `draft`) + template + index
chapters/                 Working 15-chapter TOC; curated Ch. 1–15
style/                    Voice/style constraints for manuscript prose
.cursor/                  Project rules, pinned research MCP config, permissions
.github/                  Issue templates + read-only five-rule comment workflow
scripts/                  `five_rule_check.py`; deterministic publishing renderer
requirements-publishing.txt
                          Pinned `fpdf2` / `pypdf` publishing dependencies
preliminary/              Staging area (research notes + chapter drafts + publishing packets)
```

There is no `package.json`, Dockerfile, or test suite. `SPEC.md` exists as a pointer to the external OKF v0.2 specification.

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

Sixty-five cards remain `status: draft` plus three `stable` physiology/lab cards (68 total). YAML `confidence` is aligned with in-body grades. A first selected-card re-audit, a catalog-wide Crossref/PubMed lookup, a DOI-recovery pass, a Retraction Watch dump, a catalog-wide replication/attenuation classification, and a 2026-09-16 replication note moved **three narrow claims** to `stable`. First-pass Part II, Chapter 15 waypoint, and remaining-domain cards stay `draft`. See `evidence-cards/index.md` for the full list. `v0.1` is tagged on `main` at `c7c2a7a`. `v0.2` is tagged on `main` at `9bbc2d9`. `v0.3` is tagged on `main` at `21d1a0d`.

The eight first-pass cards plus C05/C07 remain as in the previous digest table. New Chapter 2 cards: `prenatal-developmental-timing.md`, `placenta-as-mediator.md`, `prenatal-neural-construction.md`, `fetal-autonomic-maturation.md`, `prenatal-iodine-thyroid.md`, `prenatal-alcohol-fasd.md`, `prenatal-tobacco-birthweight.md`, `prenatal-environmental-mixtures.md`, `fetal-growth-not-destiny.md`.

| File | Domain | YAML / in-body grade | Narrowest current claim |
|---|---|---|---|
| `prenatal-maternal-stress-anxiety.md` | pregnancy / stress | `low-to-moderate` | Observational prenatal stress/anxiety associations largely attenuate under genetically informed designs |
| `prenatal-auditory-learning.md` | pregnancy / language | `moderate` (Low for lasting cognitive advantage) | Late-pregnancy speech can shape newborn preference; not lasting cognitive advantage |
| `prenatal-folate-ntd.md` | pregnancy / nutrition | `high-ntd; low-other-anomalies-cognition` | **`stable`**: periconceptional folic acid substantially reduces NTD risk |
| `breastfeeding-cognitive-development.md` | feeding | `moderate` | PROBIT RCT + sibling comparisons: small, verbal-concentrated, fading effect |
| `early-childcare-quality.md` | childcare | `moderate` | NICHD SECCYD: modest quality–cognition links; parenting predicts more |
| `screen-time-language-development.md` | screens / language | `low-to-moderate` | Weak-to-moderate observational associations; decompose content, co-use, context |
| `responsive-caregiving-attachment-interventions.md` | attachment | `moderate-to-high-sensitivity; moderate-attachment` | Short sensitivity RCTs move sensitivity more than attachment security |
| `infant-sleep-training.md` | sleep | `low-to-moderate` | RCTs/cohorts: no measured attachment or behavioral harm through age 6 |
| `self-regulation-delay-of-gratification.md` | executive function | `moderate-to-high-overstatement-of-original` | 2018 NICHD replication: original marshmallow-test predictor claim mostly confounded |
| `preschool-early-education-rct.md` | early learning | `moderate-historical; low-generalization` | Small high-fidelity 1960s–70s RCTs show persistent adult gains; modern at-scale programs are a different claim |
| `infant-contingency-learning.md` | early learning | `high-controlled; low-transfer` | **`stable`**: mobile paradigm action–outcome learning under control, not adult-like cause |
| `neonatal-cardiopulmonary-transition.md` | birth | `high-sequence; moderate-timing` | **`stable`**: birth reorganizes gas exchange and circulation; not a personality forecast |
| `skin-to-skin-immediate-physiology.md` | birth / feeding | `moderate-breastfeeding; low-infant-physiology` | Healthy-newborn SSC: breastfeeding 1–4 months Moderate; infant physiology Low |
| `infant-caregiver-coregulation.md` | regulation | `moderate-existence; low-to-moderate-mechanism` | Bidirectional co-regulation; nurturing care is an ecology |
| `severe-institutional-deprivation.md` | attachment / social | `high-danger; moderate-to-high-placement` | BEIP family placement after severe deprivation ≠ ordinary parenting |
| `infant-perceptual-narrowing.md` | language | `high-lab; moderate-timetable; low-sealed-deadline` | **`stable`**: first-year phonetic attunement (Werker & Tees / Kuhl); not a sealed deadline |
| `infant-statistical-speech-segmentation.md` | language | `high-lab; low-transfer` | **`stable`**: transitional-probability segmentation in the lab, not household vocabulary |
| `conversational-turns-language.md` | language | `moderate-prediction; low-causation` | Turns at 18–24 months predict later language better than word counts |
| `dual-language-does-not-confuse.md` | language | `high-no-confusion; moderate-individual-trajectories` | Dual exposure as such does not confuse; not an automatic cognitive bonus |
| `infant-crying-as-signal.md` | birth / regulation | `moderate-signal; low-acoustic-decoding` | Crying is a graded distress signal, not a cause-code |
| `suck-swallow-breathe-coordination.md` | birth / feeding | `high-coordination; moderate-practice-effects` | Oral feeding requires asynchronous maturational coordination |
| `preterm-cognition-group-risk.md` | birth | `moderate-group; low-individual` | Preterm group SMD about −0.57; not an individual sentence |
| `responsive-feeding-as-regulation.md` | regulation / feeding | `moderate-framework; low-growth-program` | Cue-based bidirectional feeding; not a weight or IQ program |
| `looking-time-as-measurement.md` | cognition / methods | `high-method; low-rich-interpretation` | A look indexes discrimination or attention, not a rich concept; remains `draft` |
| `infant-attention-as-gatekeeper.md` | cognition | `moderate-functions; low-trait` | Attention is a family of processes, not a character verdict |
| `object-permanence-looking-vs-search.md` | cognition | `moderate-looking-sensitivity; low-complete-concept` | Looking-time occlusion sensitivity ≠ search ≠ a finished object concept |
| `joint-attention-shared-reference.md` | cognition / social | `moderate-construct; low-isolated-training` | Shared reference is real; not a language guarantee |
| `infant-pointing-as-shared-reference.md` | language / social | `moderate-reference; low-product` | Pointing predicts language; baby-sign products are a different claim |
| `infant-babbling-as-exploration.md` | language | `high-canonical-stage; low-iq-verdict` | Canonical babbling is exploration; not an IQ or parenting score |

### Declared but missing evidence cards

From `evidence-cards/index.md` "Not Yet Started":

- Preconception: Kong paternal-age card exists; `preconception-nutrition-beyond-folate.md` now covers other nutrients without inheriting folate’s NTD grade; sperm-epigenetic stories still excluded
- Birth (mode of delivery and birth experience still held)
- Play (symbolic/pretend, Lillard, and outdoor/risky cards exist; guided-play efficacy still thinner)
- Social development beyond attachment (Warneken helping card now exists)
- Ecology (income/cash, MTO, leave, and food-insecurity cards exist)
- Age-3 waypoint (three cards plus curated Chapter 15)

Priority domains that still lack *full* dedicated families include guided-play efficacy, mode of delivery, and sperm-epigenetic claims (excluded). Sixty-eight cards are live; seven are `stable` for a narrow claim.

### Sources

`SOURCES.md` is the catalog of record:

- **114 verified** resources with URLs, mirrored in the file's OKF `sources` array
- **12 first-pass unresolved citations resolved** (two were already in the verified table; two titles were corrected to the matching papers). Resolution log lives under Unresolved Citations.
- Catalog itself is `status: draft`. The five remaining no-DOI listings are repaired (`hiscock-2016` retired). A Retraction Watch dump found no retraction/EoC titles among DOI-resolved records. Replication/attenuation is classified catalog-wide. `madigan-2020` ID repaired. Seven *narrow* physiology/lab claims promoted to `stable`. `kuhl-1992` added this pass.

---

## 6. Manuscript: working TOC is 15 chapters

**Decision (2026-09-15):** the book follows the 15-chapter draft sequence. Recorded in `chapters/_OUTLINE.md`. The 8-chapter seed is a compositional sketch, not the TOC.

### Canonical `chapters/` files

`chapters/01-before-the-child-is-born.md` is the curated Chapter 1 copy. The leftover Ch. 2 seed sketch was removed. `chapters/02-first-environment.md` is the curated Chapter 2 copy. `chapters/03-the-great-transition.md` is the curated Chapter 3 copy. `chapters/04-regulatory-relationship.md` is the curated Chapter 4 copy. `chapters/05-becoming-a-mind.md` is the curated Chapter 5 copy. `chapters/06-the-mind-in-motion.md` is the curated Chapter 6 expansion. `chapters/07-the-birth-of-language.md` is the curated Chapter 7 copy. `chapters/08-the-expanding-world.md` through `chapters/13-the-ecology-of-development.md` are curated Part II copies (v0.2 manuscript slice, tagged at `9bbc2d9`). `chapters/14-what-actually-works.md` is a staging copy with citation artifacts stripped. `chapters/15-three-years.md` is the curated Chapter 15 copy (v0.3 manuscript center, tagged at `21d1a0d`).

| Canonical file | Maps to working TOC | Status |
|---|---|---|
| `chapters/01-before-the-child-is-born.md` | Working TOC Ch. 1 | Curated, voice-checked; archival draft untouched |
| `chapters/02-first-environment.md` | Working TOC Ch. 2 | Curated, voice-checked; archival draft untouched |
| `chapters/03-the-great-transition.md` | Working TOC Ch. 3 | Curated, voice-checked; archival draft untouched |
| `chapters/04-regulatory-relationship.md` | Working TOC Ch. 4 | Curated, voice-checked; replaced prior seed; archival draft untouched |
| `chapters/05-becoming-a-mind.md` | Working TOC Ch. 5 | Curated, voice-checked; archival draft untouched |
| `chapters/06-the-mind-in-motion.md` | Working TOC Ch. 6 | Curated expansion; archival draft untouched |
| `chapters/07-the-birth-of-language.md` | Working TOC Ch. 7 | Curated, voice-checked; archival draft untouched |
| `chapters/14-what-actually-works.md` | Working TOC Ch. 14 | Curated, voice-checked; artifacts stripped; Appendix B range; archival untouched |
| `chapters/08-the-expanding-world.md` | Working TOC Ch. 8 | Curated, voice-checked; archival draft untouched |
| `chapters/09-the-emotional-revolution.md` | Working TOC Ch. 9 | Curated, voice-checked; archival draft untouched |
| `chapters/10-boundaries-behavior.md` | Working TOC Ch. 10 | Curated, voice-checked; archival draft untouched |
| `chapters/11-the-developing-executive.md` | Working TOC Ch. 11 | Curated, voice-checked; archival draft untouched |
| `chapters/12-play-imagination.md` | Working TOC Ch. 12 | Curated, voice-checked; archival draft untouched |
| `chapters/13-the-ecology-of-development.md` | Working TOC Ch. 13 | Curated, voice-checked; archival draft untouched |
| `chapters/15-three-years.md` | Working TOC Ch. 15 | Curated, voice-checked; archival draft untouched |

`COMPOSITION.md` Appendix B target: 2,500–4,000 words per finished chapter.

### Preliminary full drafts (the working book)

`preliminary/drafts-chapters/` holds long prose drafts (~1.6k–5.5k words). Filenames are inconsistent (spaces, mixed case, some missing `.md`). The closing draft is `chapter 15` (heading: Chapter 15, *Three Years: What Has Been Built?*). There is no Chapter 16.

| File | Title (from heading) | Words (approx.) |
|---|---|---|
| `chapter 1` | Before the Child Is Born | 4,000 |
| `chapter 2` | The First Environment | 4,300 |
| `chapter 3` | The Great Transition | 5,497 archival; curated copy in `chapters/` ~2,597 |
| `chapter 4` | The Regulatory Relationship | 4,561 archival; curated copy in `chapters/` ~2,518 |
| `chapter 5` | Becoming a Mind | 4,900 archival; curated copy in `chapters/` ~2,537 |
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

None of the archival files have been overwritten. Curated, voice-checked copies exist for Chapters 1–15. Some drafts contain leftover citation artifacts such as `:contentReference[oaicite:…]`.

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

Squash-merged into `main`, in order: **#1, #2, #3, #5, #6, #7, #8**. There is no squash commit for [PR #4](https://github.com/ralfcam/parenthood-atlas/pull/4). [PR #9](https://github.com/ralfcam/parenthood-atlas/pull/9) is this package (replication classification, Madigan ID repair, remaining Chapter 7 cards); it was opened from `main` at #7 and then merged with #8 so the history note and the catalog work sit on one branch.

| PR | Merge commit on `main` | What landed |
|---|---|---|
| [#1](https://github.com/ralfcam/parenthood-atlas/pull/1) | `7dc288a` | Corpus manifest, Chapter 2 evidence map, digest |
| [#2](https://github.com/ralfcam/parenthood-atlas/pull/2) | `a2a97b3` | Chapter 2 C05/C07, citation resolutions, 15-chapter TOC, SPEC stub |
| [#3](https://github.com/ralfcam/parenthood-atlas/pull/3) | `c13f0e6` | Remaining Chapter 2 claims, template sync, Ch. 3–4 triage, curated Chapter 2 |
| [#4](https://github.com/ralfcam/parenthood-atlas/pull/4) | **never merged** | Closed superseded. Unique files reached `main` via #5. |
| [#5](https://github.com/ralfcam/parenthood-atlas/pull/5) | `4bba8a7` | Chapter 7 language cards, remaining Chapter 3 cards, catalog-wide retraction search, **and** the PR #4 payload (stacked branch) |
| [#6](https://github.com/ralfcam/parenthood-atlas/pull/6) | `89658b7` | DOI recovery; curated Chapters 3 and 4 |
| [#7](https://github.com/ralfcam/parenthood-atlas/pull/7) | `e379de8` | Five-listing repair, Retraction Watch dump, curated Chapter 5 |
| [#8](https://github.com/ralfcam/parenthood-atlas/pull/8) | `97544c7` | Recorded that PR #4 was never merged; do not merge it |
| [#9](https://github.com/ralfcam/parenthood-atlas/pull/9) | `6275ad4` | Catalog-wide replication/attenuation; Madigan 2020 vs Jing 2023 ID repair; pointing and babbling cards |
| [#10](https://github.com/ralfcam/parenthood-atlas/pull/10) | `499414c` | Curated Chapter 1; Chapter 8 first cards; remaining Ch. 6/7 extraction |
| [#11](https://github.com/ralfcam/parenthood-atlas/pull/11) | `da2fc75` | Part II Ch. 9/11/12 triage; Chapter 14 trim; three narrow `stable` flips |
| [#12](https://github.com/ralfcam/parenthood-atlas/pull/12) | `c7c2a7a` | Part II Ch. 8 remainder, 10, 13; Chapters 6–7 update; v0.1 slice defined (`v0.1` tagged here) |
| [#13](https://github.com/ralfcam/parenthood-atlas/pull/13) | `f6011b7` | Tag plan for v0.1; Chapter 15 triage and three waypoint cards; v0.2 slice defined |
| [#14](https://github.com/ralfcam/parenthood-atlas/pull/14) | `9bbc2d9` | Curated Chapters 8–13; v0.2 tagged here; v0.3 slice defined |
| [#15](https://github.com/ralfcam/parenthood-atlas/pull/15) | `21d1a0d` | Curated Chapter 15; remaining-domain cards; v0.3 tagged here |

**Do not merge PR #4.** Its branch `cursor/ch3-ch4-ch6-7d96` (`79419f7`) was the base for the Chapter 7 branch. When #5 squash-merged onto `main` after #3, Git included every file unique to #4. GitHub left PR #4 OPEN until [PR #8](https://github.com/ralfcam/parenthood-atlas/pull/8) closed it without merging. A three-dot merge of #4 onto current `main` would still replay stale digest/catalog counts and the Chapter 4 seed against the later curated Chapter 4.

Later packages that treated “PR #4 merged” as true were describing content on `main`, not a GitHub merge of that pull request.

`CHANGELOG.md` records the knowledge-base bootstrap, the corpus-governance layer (PR #1), and the 2026-09-15 source-audit packages (new cards, citation resolutions, TOC decision, SPEC stub, Ch. 14 triage, and the stacked #4/#5 landing).

---

## 10. Known gaps and agent hazards

1. **Working TOC is 15 chapters.** See `chapters/_OUTLINE.md`. Curated copies exist for all 15 working-TOC chapters. Leftover `01-first-environment.md` seed removed.
2. **Chapter 6 archival remains thin** (~1,625 words). A curated copy in `chapters/06-the-mind-in-motion.md` is now in the Appendix B range. Chapter 7 has a curated copy (~3,785 words); archival ~4,908 remains untouched. Chapter 3 curated copy ~2,597 words (archival ~5,497). Chapter 4 curated copy ~2,518 words; archival ~4,561 remains untouched. Chapter 5 curated copy ~2,537 words (archival ~4,900). Chapter 1 curated copy ~2,900 words (archival ~3,985).
3. **`_TEMPLATE.md` now has OKF frontmatter.** Keep it in sync when live-card fields change.
4. **`atlas_domains` / `chapter_hooks`** are on the newer cards; most first-pass cards still omit them.
5. **Draft citation artifacts.** Archival `chapter 14` still has 29 `:contentReference[oaicite:…]` leftovers. Curated `chapters/14-what-actually-works.md` strips them and is in the Appendix B range. Do not overwrite the archival draft.
6. **Binary research files.** Most of `preliminary/research/` is `.docx`; grep/search will miss them.
7. **Catalog-wide retraction lookup is complete for DOI-resolved records** (Crossref + OpenAlex `is_retracted` + PubMed PTs). No retraction/EoC titles. Cochrane `new_version` flags remain successor reviews. Grey-literature IDs (NICHD 05-4318, two WHO IRIS handles, Kramer 1987) have no journal DOI and are now identified rather than missing. `hiscock-2016` retired. Replication/attenuation is classified catalog-wide; **seven narrow physiology/lab claims are `stable`**. `madigan-2020` now points at the 2020 *JAMA Pediatrics* meta-analysis.
8. **No tests or lint.** Quality control is methodological (CONTRIBUTING + voice checklist), not automated.
9. **Do not invent prescriptions.** If evidence does not justify an action, say so.
10. **PR #4 is closed, not merged.** Unique deliverables already sit on `main` via the #5 squash. See section 9.
11. **`hiscock-2016` identification mismatch is repaired.** The ID is retired. Sleep card now cites Mindell 2006, Gradisar 2016, and Bilgin & Wolke 2020 plus Price 2012. Harm claim still `draft`.

---

## 11. Suggested next work

Done in this package: harness after PR #17 — `.cursor/rules/` (four `.mdc` files), exact-version research MCP packages with exact read-only tools allowlisted for unattended use (not an absolute deny policy), secured issue templates/five-rule comment workflow (no auto-merge), internal Evidence Brief #1 (2-page PDF), Chapter 1 preprint PDF with PsyArXiv/OSF posting notes (no live deposit). Org-level Issue Fields blocked: owner is a User, not an Organization. Catalog unchanged: 68 cards (7 `stable`; 61 `draft`); 114 sources. Do not tag `v0.4`.

Reader Edition 0.1 package: private-circulation 84-page PDF plus HTML proof and extraction report, frozen to post-PR-#18 `main` commit `9f3b151`. It includes all 15 curated chapters in explicit order with reader note, contents, evidence/uncertainty note, feedback guide, and colophon. Physical proof copies and reader responses are not represented as completed. This publishing artifact changes no chapters, cards, grades, or sources and is not `v0.4`.

Highest-leverage remaining work:

- Guided-play efficacy; mode of delivery and neonatal perception (held); dedicated WM/shifting; routines/modeling.
- Looking-time remains held as a physiology/lab candidate (linking-hypothesis debate; methods essay).
- GI classification still “not classified” on many first-pass observational cards.
- Chapter 2 curated copy remains ~2,358 words (slightly under Appendix B); not padded.
- Run and record both Reader Edition physical proof copies before private sharing; synthesize de-identified feedback before any prose revision.
- Public Evidence Briefs after 10–12 `stable` cards; Ch. 1 preprint DOI only after a human PsyArXiv/OSF deposit.
- Org-level Issue Fields if the repo moves under a GitHub Organization.

---

## 12. Quick start for a new agent

1. Read `README.md`, `CONTRIBUTING.md`, then this digest. Project rules live in `.cursor/rules/`.
2. If changing evidence: start from `preliminary/MANIFEST.md` and `preliminary/research/extraction/`; never skip `SOURCES.md` + `CHANGELOG.md`.
3. If changing chapters: treat `chapters/` as canonical and `preliminary/drafts-chapters/` as staging; write reviews in `drafts-chapters/reviews/` rather than overwriting archival drafts.
4. If the task is research synthesis, start from existing cards and `SOURCES.md` before opening the `.docx` dossiers.
5. Preserve Science / Interpretation / Art. When unsure, write a narrower claim.
6. Do not set `status: stable` without the five-rule note. Do not auto-merge promotions.
