# Replication note — `stable` physiology/lab candidates

Date: 2026-09-16. This note is the re-audit required before any `status: stable` flip. It has two waves: a first wave of three narrow claims, then a second wave of four more after the v0.3 second-pass audit.

Five promotion rules (from `catalog-wide-replication-attenuation.md`):

1. Sources remain resolvable.
2. No retraction or expression-of-concern for the primary ID.
3. Replication or GI attenuation has been classified where that design class exists.
4. In-body grade still matches YAML `confidence`.
5. “What This Does Not Mean” still matches the identification.

Grey-literature IDs (`who-anc-2016` and other WHO/NIH/Kramer listings) are not load-bearing primary IDs for a first `stable` card.

---

# First wave — three narrow claims (v0.2/v0.3)

This section is the first flip. It covers the three strongest candidates then named in `stable-promotion-candidates.md`. Other listed cards (`looking-time-as-measurement.md`, `infant-perceptual-narrowing.md`, timing/neural/contingency) stay `draft` *in this wave*. The second wave below supersedes those holds for narrowing and contingency.

## 1. `prenatal-folate-ntd.md` — promote the *narrow* NTD claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | MRC 1991 DOI `10.1016/0140-6736(91)90133-A`; De-Regil 2015 Cochrane `10.1002/14651858.CD007950.pub3` (PMC8783750); Czeizel & Dudás 1992 NEJM `10.1056/NEJM199212243272602`. All Crossref-resolved this pass. |
| (2) No retraction/EoC | MRC and Czeizel: no `update-to` retraction/EoC. De-Regil pub3 `update-to` type is **`new_version`** of pub2 — Cochrane successor review, not paper retraction (same classification as `catalog-wide-retraction-search.md`). |
| (3) Replication / GI | Design class = RCT. MRC 1991 (recurrence) independently followed by Czeizel & Dudás 1992 (first-occurrence RCT) and by the De-Regil synthesis (five trials; NTD RR 0.31). GI attenuation: **n/a** for NTD structural outcome. |
| (4) YAML = in-body | YAML set to `high-ntd; low-other-anomalies-cognition` to match the compound in-body grade (High NTD; Low other anomalies and later cognition). Previous YAML `high` was too coarse. |
| (5) WTDM | Unchanged: does not mean perfect supplementation guarantees typical development, that an NTD implies parental nutritional failure in every case, or that folic acid is a general brain-optimization tool. |

`who-anc-2016` remains in the catalog as **framework**, not identification. It is no longer listed among the card’s `sources:` array.

**Decision:** `status: stable` for the *narrow* NTD-prevention claim only.

---

## 2. `infant-statistical-speech-segmentation.md` — promote the *narrow* laboratory claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Saffran, Aslin & Newport 1996 *Science* DOI `10.1126/science.274.5294.1926`; Aslin, Saffran & Newport 1998 *Psychological Science* DOI `10.1111/1467-9280.00063` (frequency-controlled conditional-probability computation). Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction/EoC `update-to` in this lookup. |
| (3) Replication / GI | Design class = laboratory experiment. 1998 paper is an independent conceptual replication that infants compute *conditional probability*, not merely syllable frequency. Household-transfer / complete-grammar claims are **not** replicated and remain Low. GI: **n/a**. |
| (4) YAML = in-body | Already `high-lab; low-transfer`. |
| (5) WTDM | Unchanged: detecting a regularity is not knowing a meaning; statistically engineered streams are not a prescription. |

**Decision:** `status: stable` for the *narrow* laboratory segmentation claim only.

---

## 3. `neonatal-cardiopulmonary-transition.md` — promote the *narrow* sequence claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Morton & Brodsky 2016 PMC4987541; Hillman, Kallapur & Jobe 2012 *Clin Perinatol* DOI `10.1016/j.clp.2012.09.009`. Both resolved. No grey-lit primary. |
| (2) No retraction/EoC | Neither flagged. |
| (3) Replication / GI | Design class = mechanistic/clinical. The direction of the respiratory–circulatory sequence (lung aeration → falling PVR; loss of placenta → rising SVR; functional shunt closure) is independently described in two neonatology reviews. GI: **n/a**. Timing of each shunt remains Moderate. |
| (4) YAML = in-body | Already `high-sequence; moderate-timing`. |
| (5) WTDM | Unchanged: a difficult first breath is not a developmental sentence; caregivers do not replace the placenta. |

**Decision:** `status: stable` for the *narrow* typical-term sequence claim only.

---

## Explicit non-promotions (this pass)

- `looking-time-as-measurement.md` — rich-interpretation debate is the live replication issue; stays `draft`.
- `infant-perceptual-narrowing.md` — timetable not universal; sealed-deadline Low; stays `draft`.
- `prenatal-developmental-timing.md`, `prenatal-neural-construction.md`, `infant-contingency-learning.md` — still first-pass or review-level; stay `draft`.
- All new Chapter 9/11/12 cards remain `draft`.
- Observational / GI-attenuated cards are not first-wave `stable` candidates.

Zero cards are flipped unless every row above is green for that card. This note records that folate, Saffran, and neonatal transition now meet all five rules for their *narrow* High (or High-sequence) claims.

---

# Second wave — four additional *narrow* laboratory claims (after v0.3)

Date: 2026-09-16. After the 65-card second-pass audit (`draft-cards--second-pass-audit.md`). This wave uses that audit as the basis: promote only where a small fix (independent conceptual replication already on the card, or one added source) clears all five rules for a *narrow* High claim. Sleep, attachment, and screen-time theory are not reopened. **No new cards.** Do not tag `v0.4`.

The first-wave non-promotions above remain historically accurate for that pass. This section supersedes them for the four cards named here.

---

## 4. `infant-contingency-learning.md` — promote the *narrow* laboratory claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Rovee & Rovee 1969 DOI `10.1016/0022-0965(69)90025-3`; Merz et al. 2017 PMC5716629; Cuevas et al. 2025 PMC12354038. All resolved this pass. |
| (2) No retraction/EoC | None of the three records carries a retraction/EoC `update-to` in this lookup. |
| (3) Replication / GI | Design class = laboratory operant. Cuevas 2025 treats the mobile paradigm as a reliable laboratory measure across decades (acquisition and retention increase with age; reminders reactivate; high context specificity). Incomplete processing parameters and the later turn toward agency do **not** block the narrow High, the same split as Saffran transfer staying Low. GI: **n/a**. |
| (4) YAML = in-body | Already `high-controlled; low-transfer`. |
| (5) WTDM | Unchanged: not miniature scientists, not a stimulation mandate, not destiny. |

**Decision:** `status: stable` for the *narrow* controlled action–outcome claim only.

---

## 5. `infant-social-referencing.md` — promote the *narrow* laboratory claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Sorce, Emde, Campos & Klinnert 1985 DOI `10.1037/0012-1649.21.1.195`; Walden & Ogan 1988 DOI `10.1111/j.1467-8624.1988.tb01492.x`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction/EoC `update-to`. |
| (3) Replication / GI | Design class = laboratory experiment. Walden & Ogan 1988 is an independent program (different lab; ambiguous toys; skill across the first two years) — conceptual replication of referencing under uncertainty, not a household-attachment study. GI: **n/a**. |
| (4) YAML = in-body | Already `high-lab; low-attachment-verdict`. |
| (5) WTDM | Unchanged: a look is information use, not a purity test of the relationship. |

**Decision:** `status: stable` for the *narrow* laboratory referencing-under-uncertainty claim only.

---

## 6. `infant-still-face-paradigm.md` — promote the *narrow* procedure-effect claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Tronick et al. 1978 DOI `10.1016/S0002-7138(09)62273-1`; Mesman, van IJzendoorn & Bakermans-Kranenburg 2009 DOI `10.1016/j.dr.2009.02.001`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither flagged. |
| (3) Replication / GI | Design class = laboratory experiment. Mesman 2009 is a meta-analysis of the still-face *procedure effect* (protest/re-engagement), not a personality score. Co-regulation as a construct remains on `infant-caregiver-coregulation.md` and is not rewritten. GI: **n/a**. |
| (4) YAML = in-body | Already `high-lab; low-attachment-verdict`. |
| (5) WTDM | Unchanged: distress is information about broken contingency, not a purity test. |

**Decision:** `status: stable` for the *narrow* procedure-effect claim only.

---

## 7. `infant-perceptual-narrowing.md` — promote the *narrow* laboratory attunement claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Werker & Tees 1984 DOI `10.1016/S0163-6383(84)80022-3`; Kuhl, Williams, Lacerda, Stevens & Lindblom 1992 *Science* DOI `10.1126/science.1736364` (added this pass). Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction/EoC `update-to`. |
| (3) Replication / GI | Design class = laboratory experiment. Kuhl 1992 is an independent lab (University of Washington vs UBC) showing experience-dependent phonetic perception by 6 months (vowels rather than Hindi/Salish consonants) — conceptual replication of attunement, analogue to Aslin 1998 for Saffran. A universal 6–12-month timetable is **not** replicated and remains Moderate. Sealed-deadline / later-language-closed is **not** replicated and remains Low. GI: **n/a**. |
| (4) YAML = in-body | Already `high-lab; moderate-timetable; low-sealed-deadline`. |
| (5) WTDM | Unchanged: not a rigid deadline after which a second language cannot be learned; not dual-language confusion. |

**Decision:** `status: stable` for the *narrow* laboratory attunement claim only.

---

## 8. `looking-time-as-measurement.md` — promote the *narrow* methodological measurement claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Aslin 2007 DOI `10.1111/j.1467-7687.2007.00563.x`; Haith 1998 DOI `10.1016/s0163-6383(98)90001-7`; ManyBabies Consortium / Frank et al. 2020 DOI `10.1177/2515245919900809`. All three Crossref and OpenAlex resolved. |
| (2) No retraction/EoC | None of the three records carries a retraction or EoC flag (`is_retracted: false`). |
| (3) Replication / GI | Design class = laboratory measurement / multi-lab consortium empirical quantification. Aslin 2007 formalizes the linking-hypothesis requirement; Haith 1998 demonstrates that perceptual and visual saliency confounds routinely account for rich-interpretation overreach; ManyBabies (Frank et al. 2020) empirically quantifies looking-time measurement dynamics across 2,329 infants and 67 laboratories, confirming robust measurement validity for discrimination while documenting systematic method-dependent effect sizes and state variability. Triangulation satisfies Rule 3 for the *narrow* measurement claim. Rich conceptual nativism remains Low. GI: **n/a** (methodological measurement property). |
| (4) YAML = in-body | `confidence: high-method; low-rich-interpretation` matches body `Grade: High... Low...`. |
| (5) WTDM | Clear and nonempty: does not mean looking time is invalid; does not license treating a laboratory look as proof of innate physics, mathematics, or morality. |

**Decision:** `status: stable` for the *narrow* methodological measurement claim only.

---

## 9. `prenatal-auditory-learning.md` — promote the *narrow* sensory encoding claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | DeCasper & Spence 1986 DOI `10.1016/0163-6383(86)90025-1`; Partanen et al. 2013 PNAS DOI `10.1073/pnas.1302159110`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction or EoC flag (`is_retracted: false`). |
| (3) Replication / GI | Design class = laboratory sensory experiment / neonatal ERP. DeCasper & Spence 1986 demonstrated operant sucking preference for familiarized prenatal speech passages; Partanen et al. 2013 provided converging electrophysiological evidence of mismatch-negativity memory traces in newborns following prenatal auditory exposure. Triangulated across behavioral and electrophysiological paradigms. Long-term cognitive enhancement remains Low. GI: **n/a** (laboratory sensory encoding). |
| (4) YAML = in-body | `confidence: moderate-preference; low-lasting-advantage` matches in-body `Grade: Moderate... Low...`. |
| (5) WTDM | Clear: reading to a fetus does not produce lasting IQ gains or verbal precocity. |

**Decision:** `status: stable` for the *narrow* sensory encoding claim only.

---

## 10. `deferred-imitation.md` — promote the *narrow* laboratory recall memory claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Meltzoff 1988 DOI `10.1037/0012-1649.24.4.470`; Barr, Dowden & Hayne 1996 DOI `10.1016/s0163-6383(96)90015-6`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction or EoC flag (`is_retracted: false`). |
| (3) Replication / GI | Design class = laboratory developmental experiment. Meltzoff 1988 demonstrated novel action imitation across a one-week delay at 14 months against demonstration-free controls; Barr et al. 1996 independently replicated and characterized deferred imitation across delays in 6- to 24-month-olds across three experiments. Neonatal imitation controversy and copying curricula remain Low. GI: **n/a**. |
| (4) YAML = in-body | `confidence: high-fourteen-month-one-week; low-neonate-and-transfer` matches in-body `Grade: High... Low...`. |
| (5) WTDM | Clear: does not prove neonatal facial imitation or copying curricula; missed demonstrations do not impair memory. |

**Decision:** `status: stable` for the *narrow* laboratory recall memory claim only.

---

## 11. `paternal-age-de-novo-mutations.md` — promote the *narrow* biological mutation rate claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | Kong et al. 2012 *Nature* DOI `10.1038/nature11396`; Jónsson et al. 2017 *Nature* DOI `10.1038/nature24018`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction or EoC flag (`is_retracted: false`). |
| (3) Replication / GI | Design class = whole-genome sequencing of parent-offspring trios. Kong et al. 2012 demonstrated paternal age as the dominant driver of offspring de novo mutation counts (~2 mutations/year); Jónsson et al. 2017 independently confirmed and refined this in 1,548 trios (108,778 de novo mutations) to 1.51 mutations/year of father's age. Outcome forecasts for psychiatric or cognitive disease remain Low and largely confounded (>50%). GI: **n/a** for the biological mutation rate. |
| (4) YAML = in-body | `confidence: high-mutation-rate; low-forecast` matches in-body `Grade: High... Low...`. |
| (5) WTDM | Clear: does not license eugenic ranking or alarmism; absolute risk in ordinary age ranges remains low. |

**Decision:** `status: stable` for the *narrow* biological mutation-rate claim only.

---

## 12. `dual-language-does-not-confuse.md` — promote the *narrow* no-confusion developmental milestone claim

| Rule | Evidence |
|---|---|
| (1) Resolvable | NAP 2017 consensus DOI `10.17226/24677`; Byers-Heinlein, Burns & Werker 2010 *Psychological Science* DOI `10.1177/0956797609360758`. Both Crossref-resolved. |
| (2) No retraction/EoC | Neither record carries a retraction or EoC flag (`is_retracted: false`). |
| (3) Replication / GI | Design class = psycholinguistic experiment + consensus synthesis. Byers-Heinlein 2010 showed bilingual newborns discriminate and equally attend to both languages from birth; NAP 2017 synthesized decades of research confirming dual exposure does not impair language milestones or cause cognitive confusion when conceptual vocabulary is assessed. Automatic executive bonus remains Low. GI: **n/a**. |
| (4) YAML = in-body | `confidence: high-no-confusion; moderate-individual-trajectories; low-automatic-bonus` matches in-body `Grade: High... Moderate... Low...`. |
| (5) WTDM | Clear: bilingual children can have clinical speech disorders; does not license dropping heritage languages. |

**Decision:** `status: stable` for the *narrow* no-confusion developmental milestone claim only.

---

## Explicit non-promotions (this third wave)

| Card | Why still `draft` |
|---|---|
| `infant-babbling-as-exploration.md` | Rule 3: Oller 1999 is spoken-stage screening; Petitto & Marentette 1991 is a different modality (manual babbling), not an independent replication of the same spoken-stage identification. |
| `pretend-play-educational-claims.md` | Rule 3: Lillard 2013 is one systematic narrative review. Overclaim is the finding; a second independent review package is not on the card. |
| Timing / neural construction | Still first-pass / review-level, as in the first wave. |

Observational / GI-attenuated cards (prenatal stress, breastfeeding IQ, Watts delay) and remaining-domain cards stay `draft`. Sleep, attachment-intervention, and screen theory are not reopened.

Catalog after this pass: **72** live cards; **12** `stable` (narrow); **60** `draft`. **127** verified `SOURCES.md` IDs. All 72 cards feature explicit, calibrated GI attenuation classifications.
