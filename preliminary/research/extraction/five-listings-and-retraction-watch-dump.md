# Five remaining listings repaired, and a Retraction Watch dump

Date: 2026-09-15. **No card is moved to `status: stable`.**

Extends `doi-recovery-retraction-watch.md` and `catalog-wide-retraction-search.md`. That DOI-recovery pass left **five listings** without a journal DOI, including a mismatched `hiscock-2016`. This pass repairs those listings and runs a catalog-wide Retraction Watch–coverage dump (Crossref update metadata, which now ingests Retraction Watch, plus OpenAlex `is_retracted`, plus PubMed publication types). OpenRetractions (`openretractions.com`) remains unreachable in this environment (DNS failure).

## Repair of the five listings

| ID | Repair | Journal DOI? |
|---|---|---|
| `nichd-seccyd-2006` | Identified as the January 2006 NICHD findings booklet, **NIH Publication No. 05-4318**. Official PDF URL kept. Grey literature; no Crossref DOI exists. Journal papers remain `nichd-effectsizes-2006`, `nichd-age15`, `belsky-2007-cd`. | No (and none expected) |
| `who-anc-2016` | Resource now WHO IRIS handle **10665/250796** (ISBN 9789241549912). NCBI Bookshelf NBK409109. No Crossref DOI. | No (and none expected) |
| `who-nurturing-care-2018` | Resource now WHO IRIS handle **10665/272603** (ISBN 9789241514064). No Crossref DOI. | No (and none expected) |
| `kramer-1987-lbw` | Resource now WHO IRIS handle **10665/264515**; PMID 3322602; PMC2491072. PubMed publication types: Journal Article, Review — not retraction. No DOI in idconv or Crossref. | No (confirmed absent) |
| `hiscock-2016` | **Retired.** The catalog URL was a 2020 *MCN* handler and did not identify a 2016 *Pediatrics* meta-analysis of 52 RCTs. Replaced by `mindell-2006-sleep`, `gradisar-2016-pediatrics`, and `bilgin-wolke-2020`. | N/A (ID withdrawn) |

### `hiscock-2016` replacement (sleep card citation-repaired)

| New ID | What it actually is | Role on `infant-sleep-training.md` |
|---|---|---|
| `mindell-2006-sleep` DOI 10.1093/sleep/29.10.1263 | AASM review of **52 studies** (n>2,500), nine Level I RCTs. Efficacy of behavioral treatment for bedtime problems and night wakings. | Efficacy context. **Not** a harm meta-analysis and **not** 2016 *Pediatrics*. |
| `gradisar-2016-pediatrics` DOI 10.1542/peds.2015-1486 | 2016 *Pediatrics* RCT, **n=43**. Attachment and behavior at 12 months; cortisol. | The actual 2016 *Pediatrics* paper. |
| `bilgin-wolke-2020` DOI 10.1111/jcpp.13223 | Observational **n=178** dyads; cry-it-out report vs attachment at 18 months. | The N=178 attachment study. **Not** an RCT. |

The sleep card’s **Low-to-Moderate** no-measured-harm claim is unchanged. Price 2012 remains the five-year RCT follow-up. Williamson 2019 remains not-an-RCT. The false “2016 Pediatrics meta-analysis (52 RCTs, >10,000 infants)” sentence is removed. This is a citation repair, not a new theory of sleep training.

## Retraction Watch dump

**Scope.** Every verified `SOURCES.md` ID with a recoverable DOI, including newly added sleep and Chapter 5 DOIs. Grey-literature IDs (NICHD booklet, two WHO documents, Kramer 1987) have no Crossref retraction object; Kramer was PubMed-checked.

**Methods.**

1. Crossref `works/{doi}` for `update-to` / `relation` whose type or label indicates retraction, withdrawal, or expression of concern.
2. OpenAlex `is_retracted` (Retraction Watch–informed).
3. PubMed esummary `pubtypes` where a PMID/PMC exists.
4. OpenRetractions: DNS failure, same as the prior pass.

**Results.**

| Check | Result |
|---|---|
| Unique DOIs queried (doi.org catalog + recovered PMC/Wiley DOIs + new sleep/Ch. 5 DOIs) | 60+ |
| OpenAlex `is_retracted = true` | **0** |
| Crossref retraction / EoC / withdrawal flags | **0** |
| PubMed retraction / retracted-publication / expression-of-concern PTs | **0** |
| Cochrane `update-to: new_version` | 2 (`deregil-2015-cochrane`, `moore-2016-ssc`) — successor review versions, not retractions |
| `partanen-2013` idconv DOI | Still maps PMC3847147 to BMC Research Notes `10.1186/1756-0500-6-358`. **Wrong.** Card cites Partanen 2013 *PNAS*. Not treated as a retraction. |
| Sibling-comparison Crossref 404 on `10.1111/j.1475-6773.2004.00453.x` | OpenAlex `is_retracted = false`. ID remains verified via PMC. |

New DOIs this package (`mindell-2006-sleep`, `gradisar-2016-pediatrics`, `bilgin-wolke-2020`, `aslin-2007-look`, `colombo-2001-attention`, `baillargeon-1987-object`, `mundy-newell-2007-ja`): Crossref `update-to` none; OpenAlex not retracted.

## Decision

- **Zero cards set to `status: stable`.** A completed Retraction Watch–coverage dump is necessary and still not sufficient. Replication/attenuation classification is not catalog-wide; YAML/in-body grade match and “What This Does Not Mean” matching identification remain outstanding for promotion.
Grey literature is now *identified*, not missing. Absence of a journal DOI on WHO/NIH reports is a resolved catalog state. A 2026-09-16 hygiene note in `SOURCES.md` records the same four live IDs plus the retired `hiscock-2016` ID; none of the four is retired. They should not be load-bearing primary IDs for a first `stable` card.
- `hiscock-2016` is gone from the catalog of record.
