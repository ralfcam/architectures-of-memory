# Repository Digest — Realized Press (`ralfcam/realized-press`)

Cold-start orientation map for human collaborators and AI agents working in the **Realized Press** multi-series editorial monorepo (`https://github.com/ralfcam/realized-press`).

---

## 1. Monorepo Architecture

This repository unites two nonfiction book series under a single **Open Knowledge Format (OKF v0.2)**, **5-Step MCP Tool Routing**, and **Multi-Format Publishing (Markdown / Reader Edition PDF+HTML / Gemini TTS Audiobook)** harness:

| Series | Root Path | Linear Project (Team `ARC`) | Epistemic Three-Lens Method | Current Status |
| :--- | :--- | :--- | :--- | :--- |
| **Series 1: *Architectures of Memory*** | [`series/architectures-of-memory/`](series/architectures-of-memory/) | `Architectures of Memory — Series` (`3cae0985-8124-4f85-a959-6216cb041c81`) | **Technical $\to$ Organizational $\to$ Philosophical** | **Book 1 (`book-01-vanishing-signal`)**: Complete 16-chapter manuscript, fact-checked, BibTeX-locked, merged MD/PDF/TTS ready. **Books 2–5**: Outlined, `sources.bib` + `evidence-cards/` seeded. |
| **Series 2: *Parenthood: The Atlas*** | [`series/parenthood-atlas/`](series/parenthood-atlas/) | `Parenthood: The Atlas — Series` (Team `ARC`) | **Science $\to$ Interpretation $\to$ Art** | **`v0.3` Release Slice**: 15 curated chapters (`chapters/01-*.md` … `15-*.md`), 64 OKF v0.2 `evidence-cards/*.md`, `SOURCES.md` + `sources.bib`, Reader Edition PDF/HTML & TTS ready. |

---

## 2. Canonical Root Harness Map

- [`AGENTS.md`](AGENTS.md) — Master agent instructions, Linear IDs, and Definitive 5-Step Tool Routing Protocol.
- [`SPEC.md`](SPEC.md) — Open Knowledge Format (OKF v0.2) specification for `evidence-cards/` and `SOURCES.md` / `sources.bib`.
- [`COMPOSITION.md`](COMPOSITION.md) — Three-Lens crosswalk, Anomaly-driven chapter grammar, and Grade-to-Verb prose calibration.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — Evidence grading rules, confounding attenuation standards, and Five-Rule Promotion Gate.
- [`templates/evidence-card-template.md`](templates/evidence-card-template.md) — Canonical 9-section OKF v0.2 Evidence Card template.
- [`style/`](style/) — Shared `forbidden-phrases.md`, `voice-checklist.md`, and `anomaly-bank.md`.
- [`scripts/`](scripts/) — Unified CLI and CI tools:
  - [`scripts/mcp_academic_bib.py`](scripts/mcp_academic_bib.py) — `academic-bib` MCP server & CLI (`crossref_lookup`, `arxiv_search`, `openalex_work`, `add_bibtex_entry`).
  - [`scripts/five_rule_check.py`](scripts/five_rule_check.py) — Mechanical 5-rule checker for OKF v0.2 `evidence-cards/*.md` with optional `--online-retraction-check` via Crossref/OpenAlex.
  - [`scripts/audit_manuscript.py`](scripts/audit_manuscript.py) — Cross-chapter continuity, metaphor collision, footnote integrity, forbidden-phrase, and grade-verb auditor.
  - [`scripts/merge_book_chapters.py`](scripts/merge_book_chapters.py) — Merges book chapters into full print Markdown and TTS-stripped audiobook transcripts.
  - [`scripts/render_publishing_pdfs.py`](scripts/render_publishing_pdfs.py) — Compiles deterministic **Reader Edition PDF + standalone HTML** with SHA-256 verification.
  - [`scripts/generate_audiobook_tts.py`](scripts/generate_audiobook_tts.py) — Synthesizes chapter audio via Gemini 2.5 Flash TTS.

---

## 3. Common `make` Commands

```bash
# Audit manuscript continuity, footnotes, metaphors & forbidden phrases
make audit BOOK=series/architectures-of-memory/book-01-vanishing-signal
make audit BOOK=series/parenthood-atlas

# Run OKF v0.2 Five-Rule Evidence Card check (add ONLINE=1 for live Crossref/OpenAlex retraction check)
make five-rule BOOK=series/parenthood-atlas
make five-rule BOOK=series/architectures-of-memory/book-01-vanishing-signal

# Compile merged Markdown + TTS transcript
make merge BOOK=series/architectures-of-memory/book-01-vanishing-signal
make merge BOOK=series/parenthood-atlas

# Render deterministic Reader Edition PDF + HTML
make pdf BOOK=series/architectures-of-memory/book-01-vanishing-signal
make pdf BOOK=series/parenthood-atlas

# Estimate duration / dry-run Gemini TTS Audiobook
make audiobook-dry-run BOOK=series/architectures-of-memory/book-01-vanishing-signal
make audiobook-dry-run BOOK=series/parenthood-atlas
```
