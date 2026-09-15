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

Do not treat `preliminary/` as published. Do not treat `evidence-cards/` cards as settled: every card is `status: draft` and `confidence: preliminary-not-yet-graded` in frontmatter.

---

## 3. Directory map

```
README.md                 Mission, governing rules (structure section is stale)
index.md                  OKF v0.2 bundle root
REPO_DIGEST.md            This map
CONTRIBUTING.md           Evidence-card methodology
CHANGELOG.md              Knowledge-base version history
COMPOSITION.md            Book compositional grammar
SOURCES.md                Master source catalog (19 verified + 12 unresolved)
evidence-cards/           8 draft cards + template + index
chapters/                 Seed outline + 2 seed chapter outlines
style/                    Voice/style constraints for manuscript prose
preliminary/              Staging area (research notes + chapter drafts)
```

There is no `.cursor/`, `package.json`, Dockerfile, or `SPEC.md` (the last is referenced from `evidence-cards/index.md` but does not exist).

---

## 4. How to work in this repo

### Adding or revising an evidence card

1. Copy `evidence-cards/_TEMPLATE.md`.
2. Add OKF v0.2 frontmatter (`type`, `title`, `description`, `tags`, `status`, `generated`, `stale_after`, `sources`). The template body does **not** currently include frontmatter; existing cards are the working example.
3. Keep the body to ~200–400 words unless deeper analysis is warranted.
4. If the card anchors a chapter, CONTRIBUTING also asks for `atlas_domains` and `chapter_hooks` in frontmatter. **No current card has these fields.**
5. List the card in `evidence-cards/index.md`.
6. Register every source in `SOURCES.md` in the same commit (verified table + frontmatter `sources` array, or Unresolved Citations).
7. Log the change in `CHANGELOG.md` under `[Unreleased]` as Added / Revised / Retracted / Structure.

### Promoting a chapter

1. Draft in `preliminary/drafts-chapters/`.
2. Run `style/voice-checklist.md` (all boxes must pass).
3. Avoid phrases in `style/forbidden-phrases.md`.
4. Calibrate claim strength to certainty grades using `COMPOSITION.md` Appendix A.
5. Move into `chapters/` using kebab-case numbered filenames (`01-first-environment.md`).
6. Link relevant evidence cards.
7. Log in `CHANGELOG.md`.

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

All 8 cards: `status: draft`, `stale_after: 2027-03-14`, generated by `human:jose-campos` on 2026-09-14. In-body grades exist, but frontmatter still says `confidence: preliminary-not-yet-graded`. Cards still need full source retrieval, replication search, formal bias review, and a settled confidence grade.

| File | Domain | In-body grade | Narrowest current claim |
|---|---|---|---|
| `prenatal-maternal-stress-anxiety.md` | pregnancy / stress | Low-to-Moderate (confounding); Low for residual causal magnitude | Observational prenatal stress/anxiety associations largely attenuate under genetically informed designs |
| `breastfeeding-cognitive-development.md` | feeding | Moderate | PROBIT RCT + sibling comparisons: small, verbal-concentrated, fading effect |
| `early-childcare-quality.md` | childcare | Moderate | NICHD SECCYD: modest quality–cognition links; parenting predicts more |
| `screen-time-language-development.md` | screens / language | Low-to-Moderate | Weak-to-moderate observational associations; decompose content, co-use, context |
| `responsive-caregiving-attachment-interventions.md` | attachment | Moderate-to-High (sensitivity); Moderate (security) | Short sensitivity RCTs move sensitivity more than attachment security |
| `infant-sleep-training.md` | sleep | Low-to-Moderate | RCTs/cohorts: no measured attachment or behavioral harm through age 6 |
| `self-regulation-delay-of-gratification.md` | executive function | Moderate-to-High that original claim is overstated | 2018 NICHD replication: original marshmallow-test predictor claim mostly confounded |
| `preschool-early-education-rct.md` | early learning | Moderate (Perry/Abecedarian); Low to generalize | Small high-fidelity 1960s–70s RCTs show persistent adult gains; modern at-scale programs are a different claim |

### Declared but missing evidence cards

From `evidence-cards/index.md` "Not Yet Started":

- Preconception exposures (parental age, paternal contributions, periconceptional nutrition)
- Birth (mode of delivery, birth experience, skin-to-skin/bonding)
- Play (unstructured/free play, pretend play, outdoor play)
- Social development beyond attachment (peers, siblings, daycare socialization)

Priority domains in `README.md` that still lack cards include preconception, birth, play, and several feeding/language/stress subtopics beyond the eight starters.

### Sources

`SOURCES.md` is the catalog of record:

- **19 verified** resources with URLs, mirrored in the file's OKF `sources` array
- **12 unresolved** citations still needing a stable link
- Catalog itself is `status: draft`; retraction/predatory-journal audit has not been done

---

## 6. Manuscript: two competing chapter maps

This is the most important structural inconsistency in the repo.

### Map A — Canonical seed (8 chapters)

`chapters/_OUTLINE.md` plus two seed outlines. These are short 10-step checklists, not prose.

| Canonical file | Title | Status |
|---|---|---|
| `chapters/01-first-environment.md` | The First Environment | Seed outline (~270 words) |
| `chapters/02-regulatory-relationship.md` | The Regulatory Relationship | Seed outline (~250 words) |
| (unwritten) | Becoming a Mind | Listed in outline only |
| (unwritten) | The Birth of Language | Listed in outline only |
| (unwritten) | The Emotional Revolution | Listed in outline only |
| (unwritten) | The Developing Executive | Listed in outline only |
| (unwritten) | Play and Imagination | Listed in outline only |
| (unwritten) | Morality and Rules | Listed in outline only |

`COMPOSITION.md` Appendix B target: 2,500–4,000 words per finished chapter.

### Map B — Preliminary full drafts (15-chapter book)

`preliminary/drafts-chapters/` holds long prose drafts (~1.6k–5.5k words). Filenames are inconsistent (spaces, mixed case, some missing `.md`). The closing draft is `chapter 15` (heading: Chapter 15, *Three Years: What Has Been Built?*). There is no Chapter 16.

| File | Title (from heading) | Words (approx.) |
|---|---|---|
| `chapter 1` | Before the Child Is Born | 4,000 |
| `chapter 2` | The First Environment | 4,300 |
| `chapter 3` | The Great Transition | 5,500 |
| `chapter 4` | The Regulatory Relationship | 4,600 |
| `chapter 5` | Becoming a Mind | 4,900 |
| `chapter 6` | The Mind in Motion | 1,600 (shortest; likely incomplete) |
| `chapter 7` | The Birth of Language | 4,900 |
| `chapter 8.md` | The Expanding World | 3,900 |
| `Chapter 9.md` | The Emotional Revolution | 4,600 |
| `Chapter 10.md` | Boundaries, Behavior, and the First Rules | 5,100 |
| `chapter 11` | The Developing Executive | 3,900 |
| `chapter 12` | Play, Imagination, and Meaning | 3,400 |
| `chapter 13` | The Ecology of Development | 4,100 |
| `chapter 14` | What Actually Works? | 4,400 |
| `chapter 15` | Three Years: What Has Been Built? | 4,200 |

None of these have passed `style/voice-checklist.md` or been moved to `chapters/`. Some drafts contain leftover citation artifacts such as `:contentReference[oaicite:…]`.

Numbering collision: canonical Chapter 1 is "The First Environment"; the long draft treats that as Chapter 2 and inserts "Before the Child Is Born" and "The Great Transition" around it. Do not merge them without an explicit numbering decision.

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

Default branch: `main`. No other remote branches at digest time.

The repo was initialized 2026-09-14 (KB structure, 8 evidence cards, OKF retrofit, `SOURCES.md`, compositional grammar) and expanded 2026-09-14/15 with `preliminary/` research dossiers and chapter drafts 1–15. The closing draft was originally committed as `chapter 16` and later renamed to `chapter 15` to match its heading.

`CHANGELOG.md` currently records only the knowledge-base bootstrap (structure + 8 cards + OKF + `SOURCES.md`). It does **not** yet log the preliminary chapter/research upload.

There is no GitHub issue/PR metadata accessible to this agent token.

---

## 10. Known gaps and agent hazards

1. **Two chapter maps.** Canonical 8-chapter seed vs 15-chapter preliminary book. Do not renumber or promote silently.
2. **Chapter 6 is thin** (~1,600 words vs ~4k+ peers) and may be incomplete.
3. **README structure section is stale.** It lists only README / CHANGELOG / CONTRIBUTING / evidence-cards. *(Partially addressed: README now links `REPO_DIGEST.md` and lists the current tree.)*
4. **`SPEC.md` is referenced and missing.** `evidence-cards/index.md` points to an Open Knowledge Format v0.2 spec file that is not in the repo.
5. **`_TEMPLATE.md` is behind the live cards.** It lacks OKF frontmatter, `status`, `sources`, and `stale_after`.
6. **Frontmatter vs body grades disagree.** Bodies already assign grades; YAML still says `preliminary-not-yet-graded`.
7. **`atlas_domains` / `chapter_hooks` are specified but unused.**
8. **Draft citation artifacts.** At least `chapter 14` contains `:contentReference[oaicite:…]` leftovers; strip before promotion.
9. **Binary research files.** Most of `preliminary/research/` is `.docx`; grep/search will miss them.
10. **No retraction audit** on the source catalog.
11. **No tests or lint.** Quality control is methodological (CONTRIBUTING + voice checklist), not automated.
12. **Do not invent prescriptions.** If evidence does not justify an action, say so.

---

## 11. Suggested next work (not started by this digest)

Highest-leverage knowledge-base work:

- Source-audit Chapter 2 claims C05 (auditory) and C07 (folate), then reconcile the existing prenatal-stress card (C06).
- Resolve the 12 unresolved citations in `SOURCES.md` (other live cards, not Ch. 2).
- Audit the remaining 7 first-pass cards after their chapters reach triage.
- Sync `_TEMPLATE.md` with live OKF frontmatter.
- Add a real OKF spec pointer or drop the `SPEC.md` reference.

Highest-leverage manuscript work:

- Decide whether the book is the 8-chapter seed or the 15-chapter draft sequence; update `_OUTLINE.md` to match.
- Normalize remaining draft filenames (spaces, mixed case, missing `.md`).
- Voice-check and promote one proof-of-voice chapter into `chapters/`.
- Finish Chapter 6 (`The Mind in Motion`).

---

## 12. Quick start for a new agent

1. Read `README.md`, `CONTRIBUTING.md`, then this digest.
2. If changing evidence: start from `preliminary/MANIFEST.md` and `preliminary/research/extraction/`; never skip `SOURCES.md` + `CHANGELOG.md`.
3. If changing chapters: treat `chapters/` as canonical and `preliminary/drafts-chapters/` as staging; write reviews in `drafts-chapters/reviews/` rather than overwriting archival drafts.
4. If the task is research synthesis, start from existing cards and `SOURCES.md` before opening the `.docx` dossiers.
5. Preserve Science / Interpretation / Art. When unsure, write a narrower claim.
