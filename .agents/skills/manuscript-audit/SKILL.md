---
name: manuscript-audit
description: >-
  Audits a book directory for series-bible compliance, metaphor collisions, footnote
  integrity, character introduction continuity, fact-check debt, and optional long-context
  Gemini review. Use when the user asks to audit a manuscript, check continuity across
  chapters, lint footnotes/metaphors, or populate sources.bib.
---

# Manuscript & Continuity Audit

## Steps

1. **Deterministic Structural Audit:**
   Run [audit_manuscript.py](../../../scripts/audit_manuscript.py) on the target book folder:
   ```powershell
   python scripts/audit_manuscript.py book-01-vanishing-signal
   ```
   Optional JSON or Markdown report output:
   ```powershell
   python scripts/audit_manuscript.py book-01-vanishing-signal --output book-01-vanishing-signal/audit-report.md
   ```
2. **Long-Context Gemini Editorial Review (Optional):**
   When `GEMINI_API_KEY` is set, run with `--gemini` to evaluate voice, three-lens rhythm, and philosophical depth across the full book in a single 1M-token context window:
   ```powershell
   python scripts/audit_manuscript.py book-01-vanishing-signal --gemini
   ```
3. **Review Findings:**
   - **Metaphor Collisions:** Sections containing more than one controlling series metaphor (`debt`, `gate`, `valuation`, `horizon`, `forgetting`).
   - **Footnote Integrity:** Missing definitions, unused definitions, or cross-chapter duplicate keys that collide in `*-full.md`.
   - **Character Continuity:** First-mention tracking for figures in [characters.md](../../../characters.md).
   - **Fact-Check Debt:** Unchecked `- [ ]` items or `no`/`partial` rows in `research/fact-checks/*.md`.
