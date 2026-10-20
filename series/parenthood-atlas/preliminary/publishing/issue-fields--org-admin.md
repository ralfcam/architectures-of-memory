# GitHub Issue Fields — blocked on owner type

Date: 2026-09-17. Sequenced step 3 of the post-PR-#17 harness plan.

## What was requested

Organization-level fields: Priority, Effort, Domain, Card Status, Chapter, Target Date.

## What this repository can do

GitHub Issue Fields are created with `POST /orgs/{org}/issue-fields` and require an **organization administrator** (`admin:org`). This repository’s owner is a **User** (`ralfcam`), not an Organization. `GET /orgs/ralfcam/issue-fields` returns 404.

Until the project lives under an organization (or GitHub ships user-owned issue fields), **do not treat missing fields as a failed template**. The same metadata is encoded as required dropdowns on:

- `.github/ISSUE_TEMPLATE/extraction.yml` (defaults: P2, S, draft)
- `.github/ISSUE_TEMPLATE/stable-candidate.yml` (defaults: P1, M, stable-candidate)

Issue Fields also cannot be pre-filled from issue templates; values would still be set in the sidebar, Projects, the API, or Actions after an org exists.

## What an org admin should create later

| Field | Type | Options |
|---|---|---|
| Priority | single-select | `P0-critical`, `P1-high`, `P2-medium`, `P3-low` |
| Effort | single-select | `XS`, `S`, `M`, `L`, `XL` |
| Domain | single-select | `prenatal`, `birth`, `regulation`, `cognition`, `language`, `social`, `executive`, `ecology`, `waypoint` |
| Card Status | single-select | `draft`, `stable-candidate`, `stable`, `held` |
| Chapter | single-select | `Ch. 1`–`Ch. 15` |
| Target Date | date | — |

API version header used in this check: `X-GitHub-Api-Version: 2026-03-10`.
