# Agent guide — Architectures of Memory

This repository is a **monorepo for a five-book series** on memory in AI, organizations, and philosophy. Workflow: **Linear (ARC)** for tasks, **GitHub** for versioned prose and research notes, **Perplexity** for structured research. See [README.md](README.md).

## File map

Each book lives under `book-XX-*/` with `outline.md`, `chapters/`, `research/notes/`, `research/fact-checks/`, `research/sources.bib`, and `drafts/`. Series-wide context: [series-bible.md](series-bible.md), [characters.md](characters.md). A combined outline snapshot: [baseline outlines.md](baseline%20outlines.md).

## Before you write

- Read [series-bible.md](series-bible.md) before **drafting** chapters.
- Read [characters.md](characters.md) before **introducing** a historical or philosophical figure.
- Match the **three-lens** method (technical / organizational / philosophical) where the outline calls for it.

## Linear (team ARC)

- **Team:** `ARC` — id `b507edbe-bdaa-4c47-8bdd-63af48774ebf`
- **Project:** `Architectures of Memory — Series` — id `3cae0985-8124-4f85-a959-6216cb041c81`
- **Book 1 milestone:** `Book 1 — The Vanishing Signal` — id `3b9c4dbb-ed86-42f1-9370-d02730fb1d7e`

Use labels `research`, `draft`, `edit`, `fact-check`, `structure`, and `book-01` … `book-05` as appropriate.

## Git workflow

- Work on a branch (`draft/ch-NN-slug`, `research/topic-slug`, `edit/ch-NN-aspect`); open a **PR** for substantive changes.
- Close Linear issues from commits when applicable: `Closes ARC-NN — short summary`

## Citations and facts

**Do not invent dates, quotes, or attributions.** If a claim is not yet sourced, mark it `[citation needed]` and capture the gap in `research/fact-checks/` or a Linear `fact-check` issue.

## Project automation

- Cursor **rules** live in `.cursor/rules/` (voice, MCP policy, glob rules for chapters, notes, outlines).
- Cursor **skills** live in `.cursor/skills/` (`research-loop`, `chapter-draft`, `fact-check-pass`).
