# Agent Guide — Multi-Series Editorial Monorepo (`Architectures of Memory` & `Parenthood: The Atlas`)

This repository is a **unified multi-series nonfiction monorepo** governed by **Open Knowledge Format (OKF v0.2)**, a **5-step Definitive Tool Routing Protocol**, **Linear (`ARC`)** project tracking, and a **Multi-Format Publishing Pipeline (Markdown, Reader Edition PDF+HTML, and Gemini TTS Audiobook)**. See [README.md](README.md) and [REPO_DIGEST.md](REPO_DIGEST.md).

## 1. Symmetric Multi-Series File Map

- **Root Shared Harness:**
  - [SPEC.md](SPEC.md) — Universal Open Knowledge Format (OKF v0.2) specification.
  - [COMPOSITION.md](COMPOSITION.md) — Three-Lens crosswalk, Anomaly-driven chapter grammar, and Grade-to-Verb prose calibration.
  - [CONTRIBUTING.md](CONTRIBUTING.md) — Evidence-Card format, confounding attenuation standards, and Five-Rule Promotion Gate.
  - [REPO_DIGEST.md](REPO_DIGEST.md) — Cold-start orientation map and inventory across both series.
  - [templates/evidence-card-template.md](templates/evidence-card-template.md) — Canonical 9-section OKF v0.2 Evidence Card template.
  - [style/](style/) — Shared [forbidden-phrases.md](style/forbidden-phrases.md), [voice-checklist.md](style/voice-checklist.md), and [anomaly-bank.md](style/anomaly-bank.md).
  - [scripts/](scripts/) — Shared CLI & MCP automation (`mcp_academic_bib.py`, `five_rule_check.py`, `audit_manuscript.py`, `merge_book_chapters.py`, `render_publishing_pdfs.py`, `generate_audiobook_tts.py`, `sync_okf_sources.py`).
- **Series 1 — *Architectures of Memory* (`series/architectures-of-memory/`):**
  - Series context: [series-bible.md](series/architectures-of-memory/series-bible.md), [characters.md](series/architectures-of-memory/characters.md), [baseline outlines.md](series/architectures-of-memory/baseline%20outlines.md).
  - Five books (`book-01-vanishing-signal` … `book-05-architecture-of-forgetting`), each with `outline.md`, `evidence-cards/`, `chapters/`, `drafts/`, `research/notes/`, `research/fact-checks/`, `research/sources.bib`, and `research/SOURCES.md`.
- **Series 2 — *Parenthood: The Atlas* (`series/parenthood-atlas/`):**
  - Series context: [README.md](series/parenthood-atlas/README.md), [COMPOSITION.md](series/parenthood-atlas/COMPOSITION.md), [REPO_DIGEST.md](series/parenthood-atlas/REPO_DIGEST.md), [CHANGELOG.md](series/parenthood-atlas/CHANGELOG.md).
  - Canonical layers: `evidence-cards/` (68 OKF v0.2 cards), `chapters/` (`01-*.md` … `15-*.md` + `_OUTLINE.md`), `SOURCES.md`, `sources.bib`, `style/`, and `preliminary/` (staging drafts, extraction, triage, publishing).

## 2. Before You Write

- Read [COMPOSITION.md](COMPOSITION.md) and [style/forbidden-phrases.md](style/forbidden-phrases.md) before drafting or editing any chapter.
- **For Series 1 (*Architectures of Memory*):** Read [series/architectures-of-memory/series-bible.md](series/architectures-of-memory/series-bible.md) and [series/architectures-of-memory/characters.md](series/architectures-of-memory/characters.md); apply the **Technical $\to$ Organizational $\to$ Philosophical** three-lens method.
- **For Series 2 (*Parenthood: The Atlas*):** Read [series/parenthood-atlas/COMPOSITION.md](series/parenthood-atlas/COMPOSITION.md) and [series/parenthood-atlas/CONTRIBUTING.md](series/parenthood-atlas/CONTRIBUTING.md); apply the **Science $\to$ Interpretation $\to$ Art** three-lens method.
- Calibrate claim verbs to the underlying OKF v0.2 Evidence Card certainty grade (*High* $\to$ **shows**; *Moderate* $\to$ **suggests**; *Low* $\to$ **is associated with**).

## 3. Linear (Team `ARC`)

- **Team:** `ARC` — id `b507edbe-bdaa-4c47-8bdd-63af48774ebf` (`https://linear.app/realized/team/ARC/projects/all`)
- **Series 1 Project:** `Architectures of Memory — Series` (`P-ARC-8`) — id `3cae0985-8124-4f85-a959-6216cb041c81`
  - **Book 1 milestone:** `Book 1 — The Vanishing Signal` — id `3b9c4dbb-ed86-42f1-9370-d02730fb1d7e`
- **Series 2 Project:** `Parenthood: The Atlas — Series` (`P-ARC-17`) — id `d480b512-ba3d-45dd-9a5a-3933265cdaae`
  - **Milestones:**
    - `v0.3 — Curated 15-Chapter Baseline & Reader Edition 0.1` — id `b711f5c4-c873-4f9f-9bcc-642a6f2067f6`
    - `v0.4 — Evidence Card Expansion & GI Classification` — id `682e6eda-ace2-4366-b601-e64c1a42d917`
    - `v1.0 — Public Evidence Briefs, Print & Audiobook Release` — id `011981ab-eaea-443b-b189-d54d68290b74`

Use labels `research`, `draft`, `edit`, `fact-check`, `structure`, and `book-01` … `book-05` as appropriate.

## 4. Citations, OKF v0.2 & Definitive Tool Routing Protocol

**Do not invent dates, quotes, or attributions.** If a claim is not yet sourced, mark it `[citation needed]` and capture the gap in `research/fact-checks/` or a Linear `fact-check` issue.

All research, evidence-card authoring, verification, and drafting tasks MUST follow the **5-step Definitive Tool Routing Protocol**:

1. **Phase 1 — Broad Historical & Archival Synthesis:** Start with **`perplexity_research`** (`perplexity` MCP) for multi-paper timelines, unpublished technical report numbers, and conference/cohort histories; use **`perplexity_ask`** for targeted 2–3 paper lookups.
2. **Phase 2 — Methodological, Confounding & Vendor-Statistic Audits:** Run **`perplexity_reason`** (`perplexity` MCP) whenever evaluating secondary vendor statistics, genetically-informed (GI) cohort confounding, sample populations, or contested attributions. For pre-DOI print/literary loci, pair **`perplexity_search`** with **Gemini `search_web`**.
3. **Phase 3 — Live Technical Frameworks, Vector Stores & Privacy SDKs:** Always run **`context7` MCP** (`resolve-library-id` $\to$ `query-docs`) for technical chapters (RAG, vector databases, differential privacy, unlearning libraries).
4. **Phase 4 — Mandatory Bibliographic Lock & OKF v0.2 Evidence Cards:**
   - Pass every cited academic paper or preprint through **`academic-bib` MCP** (`crossref_lookup`, `arxiv_search`, `openalex_work`) to verify exact DOIs, volume/issue/page numbers, and retraction flags (`is_retracted`), then persist to `sources.bib` via **`add_bibtex_entry`** and sync `SOURCES.md` via `python scripts/sync_okf_sources.py`.
   - Capture empirical/benchmark claims in `evidence-cards/*.md` (9 required sections including `## What This Does Not Mean`) and verify via `python scripts/five_rule_check.py <book-dir> --online-retraction-check`.
   - Never paste raw `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs into notes, cards, or chapters.
5. **Phase 5 — Pre-PR Manuscript & OKF Gate:** Run `make five-rule BOOK=<dir>` and `make audit BOOK=<dir>` before opening any PR.

## 5. Project Automation (`Makefile` & `scripts/`)

- **OKF v0.2 Five-Rule Gate:** `python scripts/five_rule_check.py <book-dir> [--online-retraction-check]` (`make five-rule BOOK=...`).
- **Manuscript, Continuity & Style Auditor:** `python scripts/audit_manuscript.py <book-dir> [--strict]` (`make audit BOOK=...`).
- **Source Catalog Sync (`SOURCES.md` $\leftrightarrow$ `sources.bib`):** `python scripts/sync_okf_sources.py` (`make sync-sources`).
- **Merged Manuscripts (Print MD + TTS Transcript):** `python scripts/merge_book_chapters.py <book-dir> [--audiobook]` (`make merge BOOK=...`).
- **Deterministic Reader Edition PDF + HTML Renderer:** `python scripts/render_publishing_pdfs.py <book-dir>` (`make pdf BOOK=...`).
- **Audiobook TTS Generator:** `python scripts/generate_audiobook_tts.py <book-dir> --dry-run` (`make audiobook-dry-run BOOK=...` / `make audiobook-tts BOOK=...`).
