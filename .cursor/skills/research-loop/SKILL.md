---
name: research-loop
description: Runs the Linear to Perplexity/Academic-Bib/Context7 to GitHub research loop for a book chapter. Use when the user asks to research, gather sources for, run Perplexity on, or complete a research issue for any chapter in the Architectures of Memory series.
---

# Research loop (Definitive Tool Routing Protocol)

## Inputs to confirm

- Book folder: `book-0X-*` (e.g. `book-01-vanishing-signal`, `book-02-forget-gate`)
- Chapter number and slug for the output filename (e.g. `ch01-six-years-thesis-to-paper`)
- Linear issue id (e.g. `ARC-50`) or title to find/create

## Steps

1. **Linear (`linear` MCP)** — Ensure an issue exists on team **ARC**, project **Architectures of Memory — Series**, with labels **`research`** + **`book-0X`**, appropriate **milestone** for that book, **Todo** or **In Progress**, **High** if it unblocks drafting. Paste or refine the query set in the issue body if empty.
2. **Execute Definitive Tool Routing Protocol:**
   - **Historical / Archival Survey:** Run `perplexity_research` (or `perplexity_ask` for targeted 2–3 paper lookups).
   - **Vendor Statistics / Contested Claims:** Run `perplexity_reason` to separate peer-reviewed findings from secondary citation decay.
   - **Pre-DOI Literary / Print Loci:** Pair `perplexity_search` with Gemini `search_web`.
   - **Live Technical SDKs / Vector Stores / Privacy Libraries:** Run `context7` (`resolve-library-id` → `query-docs`).
   - **Mandatory Bibliographic Lock:** Pass every cited academic paper or preprint through `academic-bib` (`crossref_lookup`, `arxiv_search`, `openalex_work`) and persist to `book-0X-*/research/sources.bib` via `add_bibtex_entry`. Never commit `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs.
3. **GitHub** — Create `book-0X-*/research/notes/chNN-slug.md` using the template from `.agents/rules/research-notes.md`. Set **Linear Issue** to the real id.
4. **Fact-check stub** — Append or create `book-0X-*/research/fact-checks/chNN.md` for claims that need primary sources.
5. **Branch + PR** — Branch `research/chNN-slug` (or `research/topic-slug`). Open PR via `gh pr create`; link PR in a Linear comment on the issue.
6. **Close** — When notes are merged and complete, move issue to **Done** and reference the merge commit.

## Definition of done

- [ ] Note file committed with queries, findings, verified claims, open questions
- [ ] All academic DOIs and arXiv preprints verified via `academic-bib` and saved to `book-0X-*/research/sources.bib`
- [ ] Zero `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs in the note
- [ ] No factual sentence in Findings without a source pointer
- [ ] PR merged or ready for review
