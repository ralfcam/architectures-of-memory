# Realized Press (`ralfcam/realized-press`) — Book Writing Environment & Multi-Series Imprint

**Realized Press** (`https://github.com/ralfcam/realized-press`) is a dual-engine publishing studio and **Book Writing Environment (BWE)** built on the principles of the **Software Development Lifecycle (SDLC)** and modern **IDEs**:

1. **Book Monetization & Owned Marketing Engine:** Compiles verified manuscripts directly into **Amazon KDP** assets (**6"×9" Print-on-Demand PDF** with mirrored gutter margins, **Kindle EPUB 3**, and **Gemini TTS Audiobook** — serving as the initial release channel and blueprint for multi-retailer expansion) alongside an **internally developed Marketing & Serial-Membership Web Site** modeled on Patreon (**Public Evidence Briefs**, **Interactive OKF Explorer**, **Chapter Preprints**, and **Reader Edition 0.1 PDF+HTML**).
2. **The Book Writing Environment (BWE):** An agentic authoring, verification, and publishing software harness governed by **Open Knowledge Format (OKF v0.2)** (an epistemic type system and unit-test suite for prose), a **5-step MCP Tool Routing Protocol**, real-time style/continuity linting, and CI release gates.
3. **Plug-and-Play Multi-Series Extensibility:** Declarative `series/<series-slug>/series.yaml` manifests and automated scaffolding (`scripts/init_series.py`) allow new book series and volumes to be added in seconds without changing the core harness.

See **[VISION.md](VISION.md)** for the full product, monetization, and BWE software architecture roadmap, and **[REPO_DIGEST.md](REPO_DIGEST.md)** for the cold-start inventory.

---

## 1. Imprint Catalog (`series/`)

| Series | Directory & Manifest | Three-Lens Method | Description & Current Release Slice |
| :--- | :--- | :--- | :--- |
| **Series 1: *Architectures of Memory*** | [`series/architectures-of-memory/`](series/architectures-of-memory/) ([`series.yaml`](series/architectures-of-memory/series.yaml)) | **Technical $\to$ Organizational $\to$ Philosophical** | Five-book investigation of memory, persistence, and forgetting in AI, institutions, and philosophy. **Book 1 (*The Vanishing Signal*)**: 16 chapters complete (~42,100 words), fact-checked, BibTeX-locked, KDP & Reader Edition ready. **Books 2–5**: Outlined, `sources.bib` & OKF `evidence-cards/` seeded. |
| **Series 2: *Parenthood: The Atlas*** | [`series/parenthood-atlas/`](series/parenthood-atlas/) ([`series.yaml`](series/parenthood-atlas/series.yaml)) | **Science $\to$ Interpretation $\to$ Art** | Developmental science field guide from preconception through age 3. **`v0.3` Release Slice**: 15 curated chapters (~27,200 words), 68 OKF v0.2 `evidence-cards/`, 114 verified sources, KDP & Reader Edition 0.1 ready. |

---

## 2. The Book Writing Environment (BWE) Harness

| SDLC / IDE Equivalent | Realized Press BWE Component | Purpose |
| :--- | :--- | :--- |
| **Product & Monetization Vision** | **[VISION.md](VISION.md)** | Commercial publishing model (Amazon KDP + Patreon), BWE software product architecture, and multi-series specification. |
| **Type System & Unit Tests** | **[SPEC.md](SPEC.md) & [CONTRIBUTING.md](CONTRIBUTING.md)** | Universal **OKF v0.2** specification for atomic `evidence-cards/*.md` (9 required sections, compound certainty grading, confounding attenuation, and `## What This Does Not Mean`). |
| **Language Grammar & Style Guide** | **[COMPOSITION.md](COMPOSITION.md) & [style/](style/)** | Three-Lens epistemic crosswalk, anomaly-driven chapter openings, grade-calibrated verb grammar (*shows* / *suggests* / *is associated with*), and [`style/forbidden-phrases.md`](style/forbidden-phrases.md). |
| **Dependency Lockfile & CVE Scanner** | **[scripts/mcp_academic_bib.py](scripts/mcp_academic_bib.py) & [scripts/five_rule_check.py](scripts/five_rule_check.py)** | Verifies DOIs/arXiv IDs against Crossref (`updates_or_errata`) and OpenAlex (`is_retracted`), locks `sources.bib` $\leftrightarrow$ `SOURCES.md`, and enforces the 5-rule promotion gate. |
| **Static Analyzer & IDE Linter** | **[scripts/audit_manuscript.py](scripts/audit_manuscript.py) & `.claude/hooks/post_edit_guard.py`** | Cross-chapter continuity, metaphor collision, footnote integrity, forbidden-phrase, and OKF evidence-card auditor. |
| **Multi-Target Release Compiler** | **[scripts/render_publishing_pdfs.py](scripts/render_publishing_pdfs.py) & [scripts/generate_audiobook_tts.py](scripts/generate_audiobook_tts.py)** | Compiles deterministic **Reader Edition (A4 PDF + HTML)**, **Amazon KDP 6"×9" Print Interior PDF** (`--format kdp-6x9`), **Kindle EPUB 3** (`--epub`), and **Gemini 2.5 Flash TTS Audiobooks**. |
| **Project Generator (`create-app`)** | **[scripts/init_series.py](scripts/init_series.py)** | Scaffolds new book series (`series/<slug>/series.yaml`) and book volumes with OKF v0.2 directories and seed files. |

---

## 3. Quick Commands (`Makefile`)

```bash
# Audit both flagship manuscripts (Book 1 of Architectures of Memory + Parenthood: The Atlas)
make audit-all

# Run OKF v0.2 Five-Rule check across all 74 evidence cards in both series
make five-rule-all

# Render Reader Edition (A4 PDF + standalone HTML) for Patreon / review
make pdf BOOK=series/architectures-of-memory/book-01-vanishing-signal
make pdf BOOK=series/parenthood-atlas

# Compile Amazon KDP Release Package (6"x9" Mirrored-Margin Print PDF + Kindle EPUB 3)
make kdp BOOK=series/architectures-of-memory/book-01-vanishing-signal
make kdp BOOK=series/parenthood-atlas

# Merge chapters into full Markdown and TTS-ready audiobook transcript
make merge BOOK=series/architectures-of-memory/book-01-vanishing-signal
make merge-audiobook BOOK=series/parenthood-atlas

# Estimate Gemini TTS audiobook duration
make audiobook-dry-run BOOK=series/architectures-of-memory/book-01-vanishing-signal
make audiobook-dry-run BOOK=series/parenthood-atlas

# Scaffold a brand-new series or book volume in the BWE
make new-series SERIES=systems-of-trust TITLE="Systems of Trust" LENSES="Mechanism,Institution,Ethics" NEW_BOOK=book-01-the-verification-gap
```
