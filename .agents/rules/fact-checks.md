# Fact-check file format

Applies to: `book-*/research/fact-checks/**/*.md`

Use rows or bullets in this shape:

`| Claim | Source | Verified | Notes |`

- **verified:** `yes` | `no` | `partial`
- **partial:** must spawn a Linear **`fact-check`** issue + `book-0X` label until a primary or consensus source is found.
- Link to the relevant `research/notes/` file and section heading.
- Use `academic-bib` MCP (`crossref_lookup`, `openalex_work`, `arxiv_search`) to confirm exact DOIs, issue numbers, pagination, and retraction status.
- Do not mark `yes` from a single blog post or unattributed LLM summary.
