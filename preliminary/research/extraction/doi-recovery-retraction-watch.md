# DOI recovery and Retraction Watch pass

Date: 2026-09-15. **No card is moved to `status: stable`.**

Extends `catalog-wide-retraction-search.md`. That pass left **20 IDs** unchecked by Crossref because no DOI had been recovered from the catalog URL. This pass recovers DOIs where they exist, re-queries Crossref `update-to` / `relation`, searches PubMed for retraction / retracted-publication / expression-of-concern publication types, and queries Retraction Watch coverage for the recovered journal articles.

OpenRetractions (`openretractions.com`) was unreachable in this environment (DNS failure). Crossref’s works API now carries Retraction Watch–ingested update metadata; PubMed publication types were queried in parallel. Targeted Retraction Watch site search did not return retraction or EoC notices for the recovered catalog papers. An unrelated JAACAP expression of concern (Keller et al. 2001, Study 329) is **not** this catalog’s `jaacap-meta-2021` (Ahmadzadeh et al. 2021).

## Recovered DOIs (15 of 20)

| ID | Recovered DOI | Crossref `update-to` / relation | PubMed retraction PT | RW / EoC on this paper |
|---|---|---|---|---|
| `jaacap-meta-2021` | 10.1016/j.jaac.2020.12.037 | none | n/a (DOI) | None. Not Study 329. |
| `lancet-psych-2018` | 10.1016/S2215-0366(18)30225-6 | none | n/a | None |
| `nichd-effectsizes-2006` | 10.1037/0003-066X.61.2.99 | none | n/a | None |
| `nichd-age15` | 10.1111/j.1467-8624.2010.01431.x | none | n/a | None |
| `bakermans-2003` | 10.1037/0033-2909.129.2.195 | none | 0 | None |
| `vanijzendoorn-1995` | 10.1111/j.1469-7610.1995.tb01822.x | none | 0 | None |
| `dewolff-1997` | 10.1111/j.1467-8624.1997.tb04218.x | none | n/a | None |
| `kramer-2008-probit` | 10.1001/archpsyc.65.5.578 | none | 0 | None |
| `der-2006-bmj` | 10.1136/bmj.38978.699583.55 | none | 0 (PMID 18746009) | None |
| `price-hiscock-2012` | 10.1542/peds.2011-3467 | none | 0 | None |
| `elango-2016-ece` | 10.3386/w21766 | none | n/a (NBER WP) | None |
| `ujhazy-2012-teratology` | 10.2478/v10102-012-0027-0 | none | 0 | None |
| `burton-2015-placenta` | 10.1098/rstb.2014.0066 | none | 0 | None |
| `bystron-2008-cortex` | 10.1038/nrn2252 | none | 0 | None |
| `preschool-scale-synthesis` | 10.1002/pam.70031 (journal version of the ERIC working paper) | none | n/a | None |

`SOURCES.md` YAML `resource` fields for these IDs now point at `https://doi.org/…` where a DOI exists. Original pubmed/PMC/PDF URLs remain valid human links in the cards.

New ID this package: `black-aboud-2011-feeding` DOI 10.3945/jn.110.129973 — Crossref `update-to` none.

## Still no Crossref DOI (5)

| ID | Why | What was checked |
|---|---|---|
| `nichd-seccyd-2006` | NICHD government PDF report | Not a journal article |
| `who-anc-2016` | WHO guideline, ISBN 9789241549912 | No Crossref retraction object |
| `who-nurturing-care-2018` | WHO/UNICEF/World Bank framework | No Crossref retraction object |
| `kramer-1987-lbw` | *Bull World Health Organ*; PMID 3322602; PMC2491072 | PubMed PT not retraction; no DOI in idconv or Crossref |
| `hiscock-2016` | Catalog URL is a 2020 MCN handler, not a 2016 Pediatrics meta-analysis | See mismatch note. **Sleep card not rewritten.** |

## `hiscock-2016` identification mismatch (recorded, not repaired)

The card body cites “A 2016 Pediatrics meta-analysis (52 RCTs, >10,000 infants).” That figure matches **Mindell et al. 2006** *SLEEP* (52 studies, n>2,500), DOI 10.1093/sleep/29.10.1263, not a 2016 Pediatrics meta-analysis. The 2016 *Pediatrics* paper that reports attachment after behavioral sleep intervention is **Gradisar et al. 2016** RCT (n=43), DOI 10.1542/peds.2015-1486. The catalog URL points at an MCN 2020 PDF handler. Crossref query on the ID’s title string returned unrelated 2001 Hiscock papers. Price 2012 remains the identified five-year RCT follow-up. This pass does not rewrite `infant-sleep-training.md`.

## Decision

- **Zero cards set to `status: stable`.** Recovering DOIs and finding no retraction/EoC is necessary and still not sufficient. Replication/attenuation classification, YAML/in-body grade match, and “What This Does Not Mean” matching identification remain outstanding for promotion.
- Five IDs remain without a Crossref DOI (WHO, NICHD report, 1987 WHO bulletin, mismatched sleep listing).
- Cochrane living-review `update-to` flags from the prior pass (`deregil-2015-cochrane`, `moore-2016-ssc`) remain classified as new versions, not retractions.
