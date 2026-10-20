---
trigger: glob
globs: "series/**/chapters/*.md"
description: Chapter drafting conventions across Architectures of Memory and Parenthood: The Atlas.
---

# Chapter Drafting Conventions (Multi-Series)

Applies to: `series/architectures-of-memory/book-*/chapters/*.md` and `series/parenthood-atlas/chapters/*.md`

- **Compositional Grammar:** Follow [`COMPOSITION.md`](../../COMPOSITION.md) and the book's `outline.md` (or `chapters/_OUTLINE.md`).
  - **Series 1 (*Architectures of Memory*):** Use the **Technical $\to$ Organizational $\to$ Philosophical** three-lens rhythm ([`series-bible.md`](../../series/architectures-of-memory/series-bible.md)).
  - **Series 2 (*Parenthood: The Atlas*):** Use the **Science $\to$ Interpretation $\to$ Art** three-lens rhythm ([`series/parenthood-atlas/COMPOSITION.md`](../../series/parenthood-atlas/COMPOSITION.md)).
- **Anomaly + Mechanism:** Open with a concrete historical scene, engineering failure mode, or developmental anomaly ([`style/anomaly-bank.md`](../../style/anomaly-bank.md)); decompose the mechanism in prose before introducing abstract interpretations.
- **Grade-Calibrated Verbs & Citations:**
  - Match verb strength to the underlying OKF v0.2 Evidence Card (`evidence-cards/*.md`): *High* $\to$ **shows**; *Moderate* $\to$ **suggests**; *Low* $\to$ **is associated with**.
  - Unsupported claims must be marked `[citation needed]` and logged in `research/fact-checks/`. Lock verified BibTeX keys in `sources.bib` and `SOURCES.md` via `python scripts/sync_okf_sources.py`.
- **Metaphors & Forbidden Phrases:** At most **one** controlling metaphor per section; zero phrases from [`style/forbidden-phrases.md`](../../style/forbidden-phrases.md).
- **Characters:** Before naming historical figures in Series 1, align with [`series/architectures-of-memory/characters.md`](../../series/architectures-of-memory/characters.md).
