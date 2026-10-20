# Contributing & Research Standards (OKF v0.2 + Definitive Tool Routing)

This monorepo enforces a unified **5-step Definitive Tool Routing Protocol** and **Open Knowledge Format (OKF v0.2)** evidence-evaluation methodology across both series:
- **Series 1:** *Architectures of Memory* (`series/architectures-of-memory/book-01..05-*`)
- **Series 2:** *Parenthood: The Atlas* (`series/parenthood-atlas/`)

---

## 1. Evidence Card Format (`evidence-cards/*.md`)

Every major empirical, mathematical, systems, or developmental claim is documented in `evidence-cards/` using [`templates/evidence-card-template.md`](templates/evidence-card-template.md) with these nine required sections:

1. **What We Know** — The narrowest supported conclusion, 1–2 sentences.
2. **How Confident We Are** — `**Grade**: High / Moderate / Low / Very Low` (or compound grade matching YAML `confidence`), with concise justification.
3. **Evidence and Causal Assessment** — Key studies, mathematical theorems, systems benchmarks, or syntheses; design types; replication status; causal or external-validity limitations.
4. **Effect Size and Persistence** — Quantitative bounds, spectral decay rates, latency/recall trade-offs, or standardized developmental effect sizes (with CIs and time horizon).
5. **Bias, Heterogeneity, and Confounding** — Main alternative explanations, benchmark contamination, organizational survivorship bias, or genetic/socioeconomic confounding (`largely confounded (>50%)`, `partially confounded (20–50%)`, `robust (<20%)`, or `n/a`).
6. **What Remains Uncertain** — Decision-relevant unresolved questions.
7. **What This Does Not Mean** — Explicitly prohibited overreach, anthropomorphic metaphor, or deterministic interpretation (>40 characters).
8. **What Action Is Reasonably Justified** — Proportionate engineering, architectural, organizational, or family/policy guidance—or a statement that no action follows.
9. **Sources** — Resolvable citations mirrored in `sources.bib` (BibTeX) and/or `SOURCES.md`.

---

## 2. Mechanical Five-Rule Promotion Gate (`scripts/five_rule_check.py`)

Cards begin at `status: draft` and may only be promoted to `status: stable` after passing all five rules in [`scripts/five_rule_check.py`](scripts/five_rule_check.py):

- **Rule 1 (Source Resolution):** Every `sources:` entry in YAML frontmatter has a valid `id` and resolvable `http(s)` / DOI `resource`, mirrored in `sources.bib` or `SOURCES.md`.
- **Rule 2 (No Retraction or Expression of Concern — Automated via `academic-bib` MCP):** Every DOI in `sources:` is checked against Crossref (`updates_or_errata`) and OpenAlex (`is_retracted`) via `python scripts/five_rule_check.py <path> --online-retraction-check`.
- **Rule 3 (Independent / Conceptual Replication):** At least two independent source IDs (or formal proof + empirical verification) support the narrow claim.
- **Rule 4 (YAML $\leftrightarrow$ Body Grade Parity):** The grade tokens in YAML `confidence:` match the tokens in `**Grade**:` under `## How Confident We Are`.
- **Rule 5 (Substantive WTDM Boundary):** `## What This Does Not Mean` is present and exceeds 40 characters of substantive scope-bounding prose.

---

## 3. Definitive 5-Step Tool Routing Protocol

1. **Phase 1 — Broad Historical & Archival Synthesis:** Use **`perplexity_research`** (`perplexity` MCP) for multi-paper timelines and technical report histories; use **`perplexity_ask`** for targeted 2–3 paper lookups.
2. **Phase 2 — Methodological, Confounding & Vendor-Statistic Audits:** Run **`perplexity_reason`** (`perplexity` MCP) whenever evaluating secondary vendor statistics, cohort confounding, sample populations, or contested attributions. Pair **`perplexity_search`** with **Gemini `search_web`** for pre-DOI print/archival loci.
3. **Phase 3 — Live Technical Frameworks & SDKs:** Run **`context7` MCP** (`resolve-library-id` $\to$ `query-docs`) for technical frameworks (RAG, vector databases, differential privacy, unlearning SDKs).
4. **Phase 4 — Mandatory Bibliographic Lock (`academic-bib` MCP):** Verify every cited paper via `crossref_lookup`, `arxiv_search`, or `openalex_work`, and persist to `sources.bib` via `add_bibtex_entry` (and `SOURCES.md` where applicable).
5. **Phase 5 — Pre-PR Manuscript & OKF Gate:** Run `make five-rule` and `make audit` before opening or merging any PR.
