# Replication note — first `stable` physiology/lab candidates

Date: 2026-09-16. This note is the re-audit required before any `status: stable` flip. It covers the three strongest candidates named in `stable-promotion-candidates.md`. Other listed cards (`looking-time-as-measurement.md`, `infant-perceptual-narrowing.md`, timing/neural/contingency) stay `draft`.

Five promotion rules (from `catalog-wide-replication-attenuation.md`):

1. Sources remain resolvable.
2. No retraction or expression-of-concern for the primary ID.
3. Replication or GI attenuation has been classified where that design class exists.
4. In-body grade still matches YAML `confidence`.
5. “What This Does Not Mean” still matches the identification.

Grey-literature IDs (`who-anc-2016` and other WHO/NIH/Kramer listings) are not load-bearing primary IDs for a first `stable` card.

---

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
