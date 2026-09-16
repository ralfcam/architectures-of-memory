# Preliminary Workbench

This directory is a staging area for materials that will later be integrated into the main knowledge base (`evidence-cards/`, `SOURCES.md`) and manuscript (`chapters/`, `COMPOSITION.md`).

Original uploads are **archival source artifacts**. Do not rename or move them. Create normalized derivatives only after a document has been reviewed.

## Subdirectories

- **`research/`** — Raw notes, literature summaries, and work-in-progress evidence syntheses that have not yet been formalized into OKF evidence cards.
- **`research/extraction/`** — Claim inventories, source-resolution notes, and evidence maps produced from dossiers.
- **`drafts-chapters/`** — Chapter drafts still in composition.
- **`drafts-chapters/reviews/`** — Structural and voice reviews kept separate from draft text.
- **`triage/`** — Chapter-level extraction plans. Not evidence cards.
- **`releases/`** — Tagged-snapshot definitions (v0.1 slice and later). Not a git tag.

## Source of truth

- [`MANIFEST.md`](MANIFEST.md) inventories every uploaded file, its chapter, artifact type, destination, and overlap.
- Numbering in this workbench follows the **15-chapter draft sequence** (Chapter 1 = framing; Chapter 2 = The First Environment). That is now the working TOC in `chapters/_OUTLINE.md`. Curated copies: `chapters/01-before-the-child-is-born.md` through `07-the-birth-of-language.md`. Staging: `chapters/14-what-actually-works.md`.

## Workflow

1. Inventory and triage against `MANIFEST.md` and `triage/`.
2. Extract atomic claims into `research/extraction/` (one claim per card candidate; never one card per dossier).
3. Audit sources into `SOURCES.md` in the same commit as any promoted card.
4. Review drafts with `style/voice-checklist.md`; save notes in `drafts-chapters/reviews/`.
5. Promote to `evidence-cards/` or `chapters/` only after the linked cards are audited and the voice review is complete.

Files in `preliminary/` are not expected to conform to OKF frontmatter or compositional-grammar rules until they are promoted.

## Canonical naming for future curated copies

Keep original filenames. When a reviewed derivative is created, use:

```text
chNN-kebab-title--artifact-type.ext
```

Examples:

```text
preliminary/research/ch01-before-the-child-is-born--dossier.docx
preliminary/research/ch02-first-environment--dossier.docx
preliminary/research/ch05-becoming-a-mind--research-plan.docx
preliminary/drafts-chapters/ch09-emotional-revolution--draft-01.md
preliminary/research/extraction/ch02-first-environment--evidence-map.md
preliminary/drafts-chapters/reviews/ch02-structural-and-voice-review.md
```

Rules:

- `chNN` is zero-padded and follows the 15-chapter draft sequence.
- Artifact suffixes: `research-plan`, `dossier`, `synthesis`, `draft-NN`, `evidence-map`, `claims`, `triage`.
- Use `.md` for new curated text. Do not overwrite the archival `.docx` / extensionless originals.
- Record the derivative path in `MANIFEST.md` and leave the original row in place.
