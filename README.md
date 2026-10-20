# Multi-Series Editorial Monorepo — *Architectures of Memory* & *Parenthood: The Atlas*

A unified, agent-native research and book-authoring monorepo housing two flagship nonfiction projects governed by **Open Knowledge Format (OKF v0.2)**, a **5-step MCP Tool Routing Protocol**, and a **Multi-Format Publishing Pipeline (Markdown, Reader Edition PDF+HTML, and Gemini TTS Audiobook)**.

---

## 1. Series Overview

| Series | Directory | Three-Lens Method | Description & Current Slice |
| :--- | :--- | :--- | :--- |
| **Series 1: *Architectures of Memory*** | [`series/architectures-of-memory/`](series/architectures-of-memory/) | **Technical $\to$ Organizational $\to$ Philosophical** | Five-book investigation of memory, persistence, and forgetting in AI, institutions, and philosophy. **Book 1 (*The Vanishing Signal*)**: 16 chapters complete, fact-checked, BibTeX-locked. **Books 2–5**: Outlined, `sources.bib` & OKF `evidence-cards/` seeded. |
| **Series 2: *Parenthood: The Atlas*** | [`series/parenthood-atlas/`](series/parenthood-atlas/) | **Science $\to$ Interpretation $\to$ Art** | Developmental science field guide from preconception through age 3. **`v0.3` Release Slice**: 15 curated chapters (`chapters/01-*.md` … `15-*.md`), 68 OKF v0.2 `evidence-cards/`, 114 verified sources, and Reader Edition 0.1 PDF/HTML. |

---

## 2. Shared Authoring, Verification & Publishing Harness

- **[SPEC.md](SPEC.md) & [CONTRIBUTING.md](CONTRIBUTING.md):** Universal **OKF v0.2** specification for atomic `evidence-cards/*.md` (9 required sections, compound certainty grading, confounding attenuation classification, and mandatory `## What This Does Not Mean` scope boundary).
- **[COMPOSITION.md](COMPOSITION.md) & [style/](style/):** Three-Lens epistemic crosswalk, anomaly-driven chapter openings, grade-calibrated verb grammar (*shows* / *suggests* / *is associated with*), and [`style/forbidden-phrases.md`](style/forbidden-phrases.md).
- **[scripts/five_rule_check.py](scripts/five_rule_check.py):** Mechanical 5-rule promotion gate for `evidence-cards/*.md`, upgraded with live Crossref (`updates_or_errata`) and OpenAlex (`is_retracted`) retraction checking (`--online-retraction-check`).
- **[scripts/audit_manuscript.py](scripts/audit_manuscript.py):** Cross-chapter continuity, metaphor collision, footnote integrity, forbidden-phrase, and OKF evidence-card auditor.
- **[scripts/render_publishing_pdfs.py](scripts/render_publishing_pdfs.py):** Deterministic `fpdf2` + `pypdf` **Reader Edition PDF + standalone HTML** renderer with SHA-256 verification.
- **[scripts/generate_audiobook_tts.py](scripts/generate_audiobook_tts.py):** Gemini 2.5 Flash TTS audiobook narrator and speaking-duration estimator.

---

## 3. Quick Commands (`Makefile`)

```bash
# Audit both flagship manuscripts (Book 1 of Architectures of Memory + Parenthood: The Atlas)
make audit-all

# Run OKF v0.2 Five-Rule check across all evidence cards in both series
make five-rule-all

# Render Reader Edition PDF + HTML for any book
make pdf BOOK=series/architectures-of-memory/book-01-vanishing-signal
make pdf BOOK=series/parenthood-atlas

# Merge chapters into full Markdown and TTS-ready transcript
make merge BOOK=series/architectures-of-memory/book-01-vanishing-signal
make merge-audiobook BOOK=series/parenthood-atlas

# Estimate Gemini TTS audiobook duration
make audiobook-dry-run BOOK=series/architectures-of-memory/book-01-vanishing-signal
make audiobook-dry-run BOOK=series/parenthood-atlas
```
