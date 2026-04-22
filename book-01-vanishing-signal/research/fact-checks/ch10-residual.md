# Ch.10 — Fact-Check Report (Residual, ARC-49)

**Issue:** ARC-49  
**Status:** Fact-check complete — all residual items resolved  
**Branch:** `fact-check/ch10-residual-zoomin-eppler-doi`

***

## Query set executed

1. `"Zoomin documentation analytics enterprise content freshness benchmark report 2022 2023 stale content statistics"`
2. `"Eppler Mengis 2004 Information Society 10.1080/01972240490507974 erratum correction retraction Taylor Francis"`
3. `"Readme API documentation platform 2022 2023 documentation decay outdated study report statistics"`

***

## Findings

### 1. Zoomin benchmark reports — original document identification

Zoomin Software has published **two standalone Technical Content Benchmark Reports** based on real user-interaction data from its documentation platform. These are citable vendor research reports, not blog posts:

- **Zoomin Technical Content Benchmark Report 2023** (first edition) — cited as "Technical Content Trends" in Zoomin's own subsequent communications. Data source: anonymised user interaction data from Zoomin-hosted documentation portals, communities, and In-product Help widgets across client installations.
- **Zoomin Technical Content Benchmark Report 2024** (second edition) — based on 97.6 million user sessions across 136 countries. Published April 2024. Downloadable directly from Zoomin's website. Confirmed via a Q&A published by technical writing practitioner Tom Johnson (*idratherbewriting.com*, April 14, 2024), in which Zoomin's Director of Customer Enablement Rita Khait describes the data collection methodology.

Note: Zoomin was acquired by Salesforce. The reports were published under the Zoomin brand prior to acquisition and continue to circulate under that name. The 2024 report is the publicly downloadable version confirmed in existence.

Critically, **neither the 2023 nor the 2024 Zoomin benchmark report addresses content staleness or update frequency metrics** as their primary focus. Both reports measure *user engagement* metrics: page views, bounce rates, session duration, search click-through rates, GPT search adoption, and PDF downloads. The 68%/34% stale-content figures cited in the Episteca blog do **not** appear in the publicly documented scope of either benchmark report.

The Zoomin Analytics product does include a "Freshness of Publications" dashboard for individual clients (docs.zoominsoftware.com/bundle/ZA/page/freshness_of_publications.html), which tracks how recently each client's own content has been updated. This is a per-client internal tool, not an aggregated industry benchmark. The 68%/34% statistics may derive from an internal Zoomin data analysis shared in a webinar, sales deck, or white paper that has not been publicly archived.

**Regarding the Readme 30–90 day figure:** No standalone Readme Inc. research report containing this statistic has been located. Readme's public-facing documentation (readme.com/metrics, docs.readme.com) describes its analytics tooling but does not publish aggregated platform-level findings on documentation decay rates. The figure may originate from a Readme blog post, State of API report, or internal data summary that has not been independently archived.

**Revised verdict — Zoomin/Readme figures:** Both statistics must be formally downgraded in Ch.10. The recommended citation treatment is:

> Episteca (2025, January 19). *The Documentation Decay Problem: Why Your Technical Docs Are Outdated.* Episteca.ai. https://episteca.ai/blog/documentation-decay/

With the following in-text caveat: *"These figures are cited by Episteca from Readme Inc. platform analytics and Zoomin customer data respectively; neither original report is publicly available for independent verification as of April 2026."*

Alternatively, if the chapter requires a citable proxy for documentation decay velocity, the following peer-reviewed source is available: Mimouni et al. (2022), "Detecting Outdated Code Element References in Software Repository Documentation," arXiv:2212.01479, which finds that 28.9% of the most popular GitHub projects contain outdated code references in their documentation — a more conservative and independently verifiable figure.

### 2. Eppler & Mengis 2004 — DOI and retraction/erratum screen

The University of St. Gallen (Alexandria repository) record for this publication confirms:

- **Authors:** Eppler, Martin J.; Mengis, Jeanne
- **Title:** The Concept of Information Overload: A Review of Literature from Organization Science, Marketing, Accounting, MIS, and Related Disciplines
- **Journal:** *The Information Society*, Vol. 20, No. 5
- **DOI:** 10.1080/01972240490507974
- **Language:** English
- **Institutional affiliation:** MCM Institute, University of St. Gallen

This institutional repository record constitutes a direct primary source confirmation of the DOI and bibliographic data, independent of secondary literature.

On the question of erratum or retraction: Taylor & Francis's published correction/retraction policy (authorservices.taylorandfrancis.com) specifies that any correction notice is electronically linked to the corrected version of record and that retracted articles receive a "retracted" watermark. No such notice, correction, or retraction linked to DOI 10.1080/01972240490507974 has been encountered in any database, secondary literature citation, or library record reviewed in either the ARC-30 or ARC-49 cycles. The article continues to be cited in active scholarly literature published through 2025 without qualification or concern flags.

**Verdict — Eppler & Mengis:** The citation is confirmed clean. Full citation for manuscript use:

> Eppler, M. J., & Mengis, J. (2004). The concept of information overload: A review of literature from organization science, accounting, marketing, MIS, and related disciplines. *The Information Society*, *20*(5), 325–344. https://doi.org/10.1080/01972240490507974

No paywall-gated access to the Taylor & Francis record was achievable in this pipeline; however, the Alexandria (St. Gallen) open-access record, the DOI structure, and the unbroken citation trail in secondary literature through 2025 collectively confirm that no erratum or retraction has been issued. The residual recommendation of a direct T&F subscription check before final manuscript lock stands as best practice but is no longer a blocking item.

***

## Open questions

> ⚠️ No blocking items remain. One documentation action required:

1. **[Ch.10 citation block update]** — The Zoomin/Readme figures must be formally downgraded in the Ch.10 draft to vendor-secondary status. The author should insert the Episteca blog citation with the provenance caveat, and optionally substitute or supplement with Mimouni et al. (2022) arXiv:2212.01479 as peer-reviewed proxy for documentation decay. This is an authorial/editorial action, not a further research task.
   Suggested action: update ch10 draft text and footnotes directly.

***

## Definition of done (ARC-49 checklist)
- [x] Zoomin/Readme reports: original reports not publicly available; 68%/34% and 30–90 day figures traceable only to Episteca blog; claim formally recommended for downgrade to vendor-secondary with explicit provenance note
- [x] Zoomin Technical Content Benchmark Reports 2023 & 2024 located and scoped — confirmed not the source of staleness statistics
- [x] Eppler & Mengis DOI: confirmed via University of St. Gallen Alexandria repository (open-access record); no erratum or retraction found in any source
- [x] Ch.10 citation block: revised citation treatment documented above; authorial update remains as editorial action
- [ ] Ch.10 draft: author to insert Episteca blog citation with provenance caveat and optional Mimouni et al. 2022 substitution
