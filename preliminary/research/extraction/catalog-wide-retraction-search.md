# Catalog-wide retraction / expression-of-concern search

Date: 2026-09-15. **No card is moved to `status: stable`.**

This note extends `selected-cards--replication-bias-reaudit.md`. That first pass was targeted (folate, FASD, iodine, prenatal stress, attachment, sleep). This pass is a **catalog-wide** lookup of `SOURCES.md` IDs for retraction or expression-of-concern signals. It is not a completed Retraction Watch dump, not a predatory-journal audit, and not a replication classification of every card.

## Methods

1. Parsed every verified ID in `SOURCES.md` (55 IDs at the start of this pass; 7 new IDs added with the Chapter 3 remainder and Chapter 7 cards).
2. Where a DOI could be recovered from the URL or from NCBI idconv, queried Crossref `works/{doi}` for `update-to` / `relation` entries whose titles or relation types indicate retraction, withdrawal, or expression of concern.
3. Where a PMID/PMC was available, queried PubMed esummary `pubtypes` for retraction notices.

A first script that only scraped DOIs embedded in URLs was incomplete. The second script recovered **35 of 55** DOIs. A third check ran Crossref on the **seven new** DOIs registered in this package.

## Results (pre-existing 55 IDs)

| Finding | Count | Meaning |
|---|---|---|
| IDs with a recovered DOI | 35 | Crossref queried |
| IDs with no DOI in this pass | 20 | PubMed-only, PDF, WHO, NBER, ERIC, institutional PDFs |
| `pubmed-parse` flags | 24 | Script limitation (NCBI JSON shape), **not** a retraction finding |
| `crossref-update` | 2 | Cochrane living-review version updates |
| Retraction or EoC titles | **0** | None found among queried records |

The two `crossref-update` flags:

- `deregil-2015-cochrane` — De-Regil et al. periconceptional folate Cochrane review. Cochrane issues successor versions; that is not a retraction of the cited review.
- `moore-2016-ssc` — Moore et al. early skin-to-skin Cochrane review. Same class of update.

`partanen-2013` idconv once mapped PMC3847147 to BMC Research Notes `10.1186/1756-0500-6-358`. That mapping is **wrong**. The card cites Partanen et al. 2013 *PNAS* at PMC3847147. Treat the idconv DOI as unreliable; do not treat it as a retraction of the PNAS paper.

No article among the 35 DOI-resolved records was found retracted or under expression of concern.

## Results (seven IDs added this package)

Crossref `update-to` / `relation` checked; no retraction or EoC titles:

| ID | DOI | Container | Retraction/EoC |
|---|---|---|---|
| `werker-tees-1984` | 10.1016/S0163-6383(84)80022-3 | *Infant Behavior and Development* | None |
| `saffran-1996-statistical` | 10.1126/science.274.5294.1926 | *Science* | None |
| `gilkerson-2018-lena` | 10.1542/peds.2017-4276 | *Pediatrics* | None |
| `nap-2017-dll` | 10.17226/24677 | National Academies Press | None |
| `zeifman-2017-crying` | 10.1016/j.copsyc.2017.02.009 | *Current Opinion in Psychology* | None |
| `lau-2015-suck-swallow` | 10.1159/000381361 | *Annals of Nutrition and Metabolism* | None |
| `burstein-2024-preterm` | 10.1037/dev0001844 | *Developmental Psychology* | None (Crossref `update-to` is the same DOI, not a withdrawal) |

## Twenty IDs still unresolved via DOI in the first 55

These remain unchecked by Crossref because this pass did not recover a DOI from the catalog URL: `jaacap-meta-2021`, `lancet-psych-2018`, `nichd-seccyd-2006`, `nichd-effectsizes-2006`, `nichd-age15`, `bakermans-2003`, `vanijzendoorn-1995`, `dewolff-1997`, `hiscock-2016`, `preschool-scale-synthesis`, `who-anc-2016`, `kramer-2008-probit`, `der-2006-bmj`, `price-hiscock-2012`, `elango-2016-ece`, `ujhazy-2012-teratology`, `burton-2015-placenta`, `bystron-2008-cortex`, `kramer-1987-lbw`, `who-nurturing-care-2018`.

Several of those have PMIDs on the cards and were PubMed-checked for retraction pubtypes in the second script; none returned a retraction notice. WHO frameworks and institutional PDFs have no Crossref retraction object.

## Decision

- **Zero cards set to `status: stable`.**
- Clearing retraction on a subset of DOIs is necessary but not sufficient. Promotion still requires replication/attenuation classification, YAML/in-body grade match, and a “What This Does Not Mean” that matches identification.
- A later pass recovered 15 of 20 remaining DOIs and queried Retraction Watch via Crossref update metadata plus PubMed retraction publication types: [`doi-recovery-retraction-watch.md`](doi-recovery-retraction-watch.md). Still none to `stable`.
