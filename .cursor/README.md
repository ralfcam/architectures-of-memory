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

Cursor’s schema is `mcpServers` (command or URL), not a custom `scope` / `autoApprove` object. Specifically reviewed versions are pinned:

| Server | Immutable version / source | Reviewed | Intended capabilities |
|---|---|---|---|
| `github` | GitHub official remote MCP (`https://api.githubcopilot.com/mcp/`) | 2026-09-18 | Issues, PRs, commits, file contents |
| `crossref` | `@cyanheads/crossref-mcp-server@0.3.12` · [source](https://github.com/cyanheads/crossref-mcp-server/tree/v0.3.12) · npm SHA-512 `VUtLNGhj0fCr+XeHMQz65GrhzK823JSZZvG7T868F4MdupPHQmw+5wxqK7WLacH5omu9tCLImCh4MwzLScskOQ==` | 2026-09-18 | Seven read-only DOI/work/reference/journal/funder/member/prefix tools |
| `pubmed` | `@cyanheads/pubmed-mcp-server@2.10.13` · [source](https://github.com/cyanheads/pubmed-mcp-server/tree/v2.10.13) · npm SHA-512 `s5sVazX3z+92mfabwLzxs3wYeEmXklcyKRSaxNeCjqj2qwuuIJ7e94U0v2pw9iaw1YLjHij4l6FesVo3jRaXSA==` | 2026-09-18 | Eleven read-only PubMed/Europe PMC metadata, full-text, citation, related, spelling, MeSH, and ID tools |

The package tarballs, manifests, changelogs, and emitted tool IDs were inspected. Both pinned packages smoke-started over stdio and exposed only the enumerated tools. Their manifests require Node 24 or Bun 1.4; they also smoke-start under this image’s Node 22 with an engine warning. Upgrade the environment before relying on unsupported Node 22 behavior.

`permissions.json` allowlists the exact read-only tools for **unattended use**. It is not an absolute deny policy: depending on Cursor run mode and team policy, a non-allowlisted tool may still be offered for explicit approval.

Set `GITHUB_TOKEN`, `CROSSREF_MAILTO` (polite pool), and optionally `NCBI_API_KEY` in the local or Cloud Agent environment. Do **not** write MCP servers in this repo. Do **not** auto-approve merge, push, or `status: stable` writes.

Research-only scoping (Crossref/PubMed not loaded for every agent) is a team-dashboard allowlist, not a field this JSON can express. Until that dashboard is set, the committed files are the default for every workspace clone.

### MCP dependency upgrade process

1. Replace one exact version in `mcp.json`; never use a range, tag, or `@latest`.
2. Inspect the tagged source, release/changelog, package manifest, and npm integrity hash.
3. Download the tarball without credentials and inspect every registered tool ID and its read/write behavior.
4. Smoke-start it without credentials; verify the emitted tool list exactly matches `permissions.json`.
5. Update the audit row above and exact allowlist if justified.
6. Open a dedicated PR and require review before merge.

## Issue fields

GitHub Issue Fields are **organization-level** and require `admin:org`. This repository is owned by a **User** (`ralfcam`), so fields cannot be created here. Issue templates encode the same metadata as dropdowns. See `preliminary/publishing/issue-fields--org-admin.md`.
