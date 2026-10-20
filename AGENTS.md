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

## Citations, facts & Definitive Tool Routing Protocol (Books 2–5)

**Do not invent dates, quotes, or attributions.** If a claim is not yet sourced, mark it `[citation needed]` and capture the gap in `research/fact-checks/` or a Linear `fact-check` issue.

All research, verification, and drafting tasks MUST follow the **5-step Definitive Tool Routing Protocol**:

1. **Phase 1 — Broad Historical & Archival Synthesis:** Start with **`perplexity_research`** (`perplexity` MCP) for multi-paper timelines, unpublished technical report numbers, and conference histories; use **`perplexity_ask`** for targeted 2–3 paper lookups.
2. **Phase 2 — Methodological & Vendor-Statistic Audits:** Run **`perplexity_reason`** (`perplexity` MCP) whenever evaluating secondary vendor statistics, sample populations, or contested attributions to prevent secondary-source citation decay. For pre-DOI print/literary loci (e.g., newspaper supplements), pair **`perplexity_search`** with **Gemini `search_web`**.
3. **Phase 3 — Live Technical Frameworks, Vector Stores & Privacy SDKs:** Always run **`context7` MCP** (`resolve-library-id` → `query-docs`) for Books 2–5 technical chapters (RAG, vector databases, differential privacy, unlearning libraries) rather than relying on LLM-generated pseudocode.
4. **Mandatory Bibliographic Lock & `sources.bib` Persistence:** Pass every cited academic paper or preprint through **`academic-bib` MCP** (`crossref_lookup`, `arxiv_search`, `openalex_work`) to verify exact DOIs, volume/issue/page numbers, and retraction flags (`is_retracted`), then persist the entry to `book-0X-*/research/sources.bib` via **`add_bibtex_entry`**. Never paste raw `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs into notes or chapters.
5. **Pre-PR Manuscript Gate:** Run `python scripts/audit_manuscript.py book-0X-*` (`make audit BOOK=book-0X-*`) before opening any chapter PR to enforce zero metaphor collisions, valid footnote definitions, and character continuity.

## Project automation

- Antigravity **rules, skills & hooks** live in `.agents/` (`rules/`, `skills/`, `hooks.json`).
- Cursor **rules, skills & hooks** live in `.cursor/` (`rules/`, `skills/`, `hooks.json`).
- **Academic & Bibliographic MCP:** `scripts/mcp_academic_bib.py` (exposed as `academic-bib` MCP server and CLI via `--cli`).
- **Manuscript & Continuity Auditor:** `python scripts/audit_manuscript.py book-NN-…` (`make audit BOOK=book-NN-…`).
- **Audiobook TTS Generator:** `python scripts/generate_audiobook_tts.py book-NN-… --dry-run` (`make audiobook-dry-run` / `make audiobook-tts`).
- **Merged manuscripts:** from repo root, `python scripts/merge_book_chapters.py book-NN-…` (add `--audiobook` for TTS; optional `--prefix NAME`). Or `make merge BOOK=book-NN-…` / `make merge-audiobook BOOK=book-NN-…` (optional `PREFIX=…`). VS Code: tasks in `.vscode/tasks.json`.
