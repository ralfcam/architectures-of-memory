# Selected-card replication / bias re-audit (first pass)

Date: 2026-09-15. **No card is moved to `status: stable`.** This note began the re-audit flagged after PR #3. A catalog-wide Crossref/PubMed retraction lookup is now in [`catalog-wide-retraction-search.md`](catalog-wide-retraction-search.md). No retraction or expression-of-concern titles were found among DOI-resolved records; Cochrane `update-to` flags are new review versions, not retractions. That still does not promote any card to `stable`.

Scope: folate, FASD, iodine, prenatal stress, attachment-intervention, plus a status check on the new Ch. 3–4–6 cards. Sleep training was citation-reconciled in PR #2 and is listed only for status.

## Decision rule used here

A card may move to `stable` only after:

1. Sources remain resolvable.
2. No retraction or expression-of-concern was found for the primary ID (catalog-wide Crossref/PubMed lookup now exists; 15 of 20 previously unchecked IDs now have recovered DOIs; five still lack a journal DOI; Retraction Watch dump not a complete database export).
3. Replication or genetically informed attenuation has been classified (robust / partial / largely confounded) where that design class exists.
4. In-body grade still matches YAML `confidence`.
5. “What This Does Not Mean” still matches the identification.

None of the selected cards clear all five for promotion to `stable` in this pass.

## Selected cards

| Card | Why selected | What this pass found | Still `draft` because |
|---|---|---|---|
| `prenatal-folate-ntd.md` | High-grade RCT claim; temptation to treat as settled | De-Regil 2015 Cochrane and MRC 1991 remain the identification. No retraction of those trials located in this pass. Dose and fortified-population questions remain open. | No catalog-wide retraction audit; later-cognition still Low; first-occurrence evidence thinner than recurrence. |
| `prenatal-alcohol-fasd.md` | High FASD claim; high over-translation risk | Hoyme 2016 remains a diagnostic-guideline synthesis, not an exposure RCT. Any-sip still Low. | Clinical teratology ≠ completed bias review of epidemiologic low-dose literature. |
| `prenatal-iodine-thyroid.md` | High severe / Low mild split | Zimmermann 2008 and Morreale de Escobar 2004 still support the severe/T4 story. Mild-replete IQ claims remain Low. | Severe-end reviews are not a replete-population RCT package. |
| `prenatal-maternal-stress-anxiety.md` | Genetically informed attenuation already on the card | MoBa, MCS sibling, JAACAP meta, and children-of-twins IDs still resolve. Attenuation still **largely confounded (>50%)** for typical-range prenatal-specific claims. | Card body still says “initial literature pass”; disaster/clinical trauma boundary untested here. |
| `responsive-caregiving-attachment-interventions.md` | Would be a candidate for `stable` if this were only an efficacy meta-analysis | Bakermans 2003 still the core RCT synthesis (d≈0.33 sensitivity; d≈0.20 attachment). Long-run child outcomes and non-Western effectiveness remain open. | No updated meta-analysis registered this pass; distal outcomes Low-to-Moderate. |
| `infant-sleep-training.md` | Adjacent Ch. 4 card | Citations already reconciled (Price 2012; Williamson 2019 not an RCT). | Underpowered for rare harms; not a completed safety guarantee. |

## New cards this package and later first-pass cards

The five cards from the Chapter 3–4–6 package (`neonatal-cardiopulmonary-transition`, `skin-to-skin-immediate-physiology`, `infant-caregiver-coregulation`, `severe-institutional-deprivation`, `infant-contingency-learning`) remain first-pass source audits. The seven cards added with Chapter 7 and remaining Chapter 3 claims, plus the Chapter 4 feeding-as-regulation card, are also first-pass. They are **not** re-audit candidates yet.

## Explicit non-promotions

- Zero cards set to `status: stable`.
- YAML `confidence` is not a stability claim.
- Catalog-wide Crossref/PubMed lookup: [`catalog-wide-retraction-search.md`](catalog-wide-retraction-search.md). DOI recovery / Retraction Watch pass: [`doi-recovery-retraction-watch.md`](doi-recovery-retraction-watch.md). Still not sufficient for `stable` (five IDs lack a journal DOI; replication/attenuation not classified catalog-wide).

## Next re-audit candidates (not done here)

PROBIT breastfeeding-IQ, Watts 2018 marshmallow replication, Perry/Abecedarian historical RCTs, and INTERGROWTH as a measurement standard rather than an outcome card.
