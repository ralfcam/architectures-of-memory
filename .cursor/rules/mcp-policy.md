# MCP and Tool Routing Policy (Definitive Protocol for Books 2–5)

All research, fact-checking, and drafting tasks MUST follow this routing protocol:

1. **Broad Historical & Multi-Paper Synthesis (Phase 1):**
   - Use **`perplexity_research`** (`perplexity` MCP) for chapter-level literature surveys, historical timelines, technical report numbers, and conference proceedings.
   - Use **`perplexity_ask`** (`perplexity` MCP) for targeted 2–3 paper comparisons.
2. **Contested Claims, Vendor Statistics & Methodological Audits (Phase 2):**
   - Run **`perplexity_reason`** (`perplexity` MCP) to audit sample scopes, debunk secondary-source citation decay, and separate vendor-secondary claims from peer-reviewed literature.
   - For pre-DOI literary/newspaper print sources, pair **`perplexity_search`** with **Gemini `search_web`**.
3. **Live Frameworks, Vector Stores, RAG & Privacy SDKs (Phase 3 / Books 2–5 Technical):**
   - Always run **`context7` MCP** (`resolve-library-id` → `query-docs`) to pull authoritative repository documentation and SDK signatures instead of writing generic pseudocode.
4. **Mandatory Bibliographic Lock & `sources.bib` Persistence:**
   - Pass every academic paper or preprint through **`academic-bib` MCP** (`crossref_lookup`, `arxiv_search`, `openalex_work`) to verify exact DOIs, volume/issue/pagination, and retraction status (`is_retracted`).
   - Persist every verified citation into `book-0X-*/research/sources.bib` using **`add_bibtex_entry`**.
   - **Never** commit raw `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs into `research/notes/`, `research/fact-checks/`, or `chapters/`; resolve permanent DOIs or canonical URLs first.
5. **Pre-PR Manuscript Gate:**
   - Run `python scripts/audit_manuscript.py book-0X-*` (`make audit BOOK=book-0X-*`) before opening any chapter PR to verify zero metaphor collisions, valid footnote definitions, and character continuity.
6. **Linear & GitHub Tracking:**
   - Track all issues on Linear team **ARC** (`b507edbe-bdaa-4c47-8bdd-63af48774ebf`), project **Architectures of Memory — Series** (`3cae0985-8124-4f85-a959-6216cb041c81`), with book milestone and taxonomy labels (`research`, `draft`, `edit`, `fact-check`, `structure`, `book-01`…`book-05`).
   - Use branches (`research/...`, `draft/...`, `edit/...`) and open PRs via `gh pr create`.
