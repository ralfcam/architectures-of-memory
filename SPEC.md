# Open Knowledge Format (OKF) v0.2

This bundle conforms to **Open Knowledge Format v0.2**. The normative specification is external; this file is a pointer, not a copy of the spec.

- Canonical spec: [GoogleCloudPlatform/open-knowledge-format `SPEC.md`](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
- Version declaration: bundle-root [`index.md`](index.md) declares `okf_version: "0.2"`.
- Index files (`index.md`, `evidence-cards/index.md`) have no frontmatter, per OKF §8.

## How this repository uses OKF

Evidence cards and `SOURCES.md` are concept documents with YAML frontmatter. Typical fields:

| Field | Role here |
|---|---|
| `type` | `Evidence Card` or `Source Catalog` |
| `title`, `description`, `tags` | Human/agent routing |
| `status` | `draft` until a card is source-audited and graded; `stable` is not used yet |
| `confidence` | Certainty grade from `CONTRIBUTING.md` (may be compound, e.g. `low-to-moderate`) |
| `generated` | `{ by, at }` provenance |
| `stale_after` | Re-audit horizon |
| `sources` | `{ id, resource, title }` entries mirrored in `SOURCES.md` |

Card bodies follow `CONTRIBUTING.md` (What We Know, certainty grade, causal assessment, effect size, confounding, uncertainty, prohibited inferences, justified action).

If this stub and the upstream spec disagree, the [upstream spec](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) wins.
