---
name: research-loop
description: Runs the Linear to Perplexity to GitHub research loop for a book chapter. Use when the user asks to research, gather sources for, run Perplexity on, or complete a research issue for any chapter in the Architectures of Memory series.
---

# Research loop

## Inputs to confirm

- Book folder: `book-0X-*` (e.g. `book-01-vanishing-signal`)
- Chapter number and slug for the output filename (e.g. `ch01-rosenblatt-perceptron`)
- Linear issue id (e.g. `ARC-1`) or title to find/create

## Steps

1. **Linear** — Ensure an issue exists on team **ARC**, project **Architectures of Memory — Series**, with labels **`research`** + **`book-0X`**, appropriate **milestone** for that book, **Todo** or **In Progress**, **High** if it unblocks drafting. Paste or refine the Perplexity query set in the issue body if empty.
2. **Perplexity** — Run each query from the issue; keep URLs and titles in the findings.
3. **GitHub** — Create `book-0X-*/research/notes/chNN-slug.md` using the template from `.cursor/rules/research-notes.mdc`. Set **Linear Issue** to the real id (e.g. `ARC-1`).
4. **Fact-check stub** — Append or create `book-0X-*/research/fact-checks/chNN.md` for claims that need primary sources.
5. **Branch + PR** — Branch `research/chNN-slug` (or `research/topic-slug`). Open PR; link PR in a Linear comment on the issue.
6. **Close** — When notes are merged and complete, move issue to **Done** and reference the merge commit.

## Definition of done

- [ ] Note file committed with queries, findings, verified claims, open questions
- [ ] No factual sentence in Findings without a source pointer
- [ ] PR merged or ready for review
