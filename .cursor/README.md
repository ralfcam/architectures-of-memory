# Cursor harness

Project rules, MCP, and agent permissions for *Parenthood: The Atlas*. These files are version-controlled. They do not replace `CONTRIBUTING.md`.

## Rules (`.cursor/rules/`)

| File | When it loads |
|---|---|
| `00-always-apply.mdc` | Every session. Keep it short. |
| `01-evidence-cards.mdc` | `evidence-cards/**/*.md` |
| `02-chapters.mdc` | `chapters/**/*.md` |
| `03-research-extraction.mdc` | `preliminary/research/extraction/**/*.md` |

Always-apply is identity and hard guardrails only. Path-scoped files carry templates and checklists.

## MCP (`.cursor/mcp.json`)

Cursor’s schema is `mcpServers` (command or URL), not a custom `scope` / `autoApprove` object. Read-only posture is enforced in `permissions.json`:

| Server | Package / URL | Intended use |
|---|---|---|
| `github` | GitHub official remote MCP | Issues, PRs, file contents (read tools allowlisted) |
| `crossref` | `@cyanheads/crossref-mcp-server` | DOI resolve, metadata, `update-to` / retraction signals |
| `pubmed` | `@cyanheads/pubmed-mcp-server` | PMID metadata, publication types |

Set `GITHUB_TOKEN`, `CROSSREF_MAILTO` (polite pool), and optionally `NCBI_API_KEY` in the local or Cloud Agent environment. Do **not** write MCP servers in this repo. Do **not** auto-approve merge, push, or `status: stable` writes.

Research-only scoping (Crossref/PubMed not loaded for every agent) is a team-dashboard allowlist, not a field this JSON can express. Until that dashboard is set, the committed files are the default for every workspace clone.

## Issue fields

GitHub Issue Fields are **organization-level** and require `admin:org`. This repository is owned by a **User** (`ralfcam`), so fields cannot be created here. Issue templates encode the same metadata as dropdowns. See `preliminary/publishing/issue-fields--org-admin.md`.
