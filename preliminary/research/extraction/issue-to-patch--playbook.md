# Issue-to-patch playbook (read-only first)

Date: 2026-09-17. After PR #17 (7 narrowly `stable` cards). This is the Cloud Agent / GitHub Actions workflow for issues labeled `extraction` or `stable-candidate`. **No auto-merge. No `status: stable` flip from automation.**

Related: [replication note](stable-candidates--replication-note.md) · [five-rule script](../../scripts/five_rule_check.py)

## Trigger

1. A new GitHub issue uses `.github/ISSUE_TEMPLATE/extraction.yml` or `stable-candidate.yml`.
2. Labels `extraction` or `stable-candidate` are present.
3. GitHub Actions posts a structured comment (`/.github/workflows/stable-candidate-checklist.yml`).
4. A Cloud Agent may be pointed at the same issue. It **reads**; it does not merge.

## Read-only pass (this stage)

On the card named in the issue body (`### Card filename`):

1. Run `python3 scripts/five_rule_check.py evidence-cards/<file>` for mechanical rules (4) and (5) and source-URL presence.
2. Resolve primary DOIs (Crossref MCP or `https://api.crossref.org/works/{doi}`). Check `update-to` / `updated-by` for retraction or expression-of-concern.
3. PubMed publication types if a PMID is the persistent ID.
4. Post a comment with pass/fail per rule. Rule 3 (replication of the *narrow* claim) is **human-judged**; the script only notes whether a second source ID exists.

If any rule fails, the comment states what evidence would be needed. Stop. Do not open a promotion PR.

## Write path (not this automation)

Only after a human (or a later explicitly enabled agent run) confirms all five rows are green:

1. Create `cursor/<card-slug>-stable-7d96` from current `main`.
2. Set `status: stable` for the *narrow* High claim only.
3. Update `evidence-cards/index.md`, `preliminary/MANIFEST.md`, `REPO_DIGEST.md`, CHANGELOG, and the replication note.
4. Open a **draft** PR. Do not merge it from the agent.

Sleep, attachment-intervention, and screen-time theory cards are out of scope unless the issue says otherwise. Archival `preliminary/drafts-chapters/` stays untouched.

## Defaults (until org-level Issue Fields exist)

| Template | Priority | Effort | Card Status |
|---|---|---|---|
| Extraction | P2-medium | S | draft |
| Stable candidate | P1-high | M | stable-candidate |

See `preliminary/publishing/issue-fields--org-admin.md`.
