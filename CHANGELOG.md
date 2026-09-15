# Changelog

All notable additions and revisions to the evidence atlas are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/), adapted for a research synthesis project rather than software.

Entry types:
- `Added` - new evidence cards or topics
- `Revised` - updated confidence grades, new studies incorporated, corrected attenuation estimates
- `Retracted` - claims withdrawn or downgraded due to failed replication or new genetically informed evidence
- `Structure` - changes to templates, methodology, or repository organization

## [Unreleased]

### Structure
- Initialized repository: README, CONTRIBUTING guide, evidence card template, and directory structure.
- Added `REPO_DIGEST.md`, a repository map covering the three-layer layout (preliminary workbench, OKF evidence cards, canonical manuscript), current inventories, the 8- vs 15-chapter numbering split, and known gaps. Linked from `index.md` and `README.md`.
- Renamed `preliminary/drafts-chapters/chapter 16` to `chapter 15` so the filename matches its Chapter 15 heading (*Three Years: What Has Been Built?*).
- Added the preliminary corpus governance layer: `preliminary/MANIFEST.md` (inventory of every uploaded file), naming convention for future curated copies (originals not renamed), `triage/` (Part I sequence plus Ch. 1–2 notes), `research/extraction/` (atomic-claim pipeline and Chapter 2 Evidence Map), and `drafts-chapters/reviews/` (voice review kept separate from draft text).
- Adopted the 15-chapter draft sequence as the working TOC in `chapters/_OUTLINE.md`; kept seed outlines as sketches for draft Ch. 2 and 4.
- Added `SPEC.md` as a pointer to the external OKF v0.2 specification.
- Synced `evidence-cards/_TEMPLATE.md` with live OKF frontmatter (`type`, `title`, `description`, `tags`, `status`, `confidence`, `generated`, `stale_after`, `sources`; optional `atlas_domains` / `chapter_hooks`).
- Added Chapter 3 and Chapter 4 triage notes (Part I). Archival drafts not overwritten.
- Promoted a curated, voice-checked Chapter 2 to `chapters/02-first-environment.md`. Relocated the regulatory seed sketch to `chapters/04-regulatory-relationship.md`. Archival `preliminary/drafts-chapters/chapter 2` unchanged.

### Added
- Populated evidence-cards/ with 8 preliminary evidence cards (prenatal maternal stress/anxiety, breastfeeding and cognitive development, early childcare quality, screen time and language development, responsive caregiving and attachment interventions, infant sleep training, self-regulation/delay of gratification, preschool early education RCTs) plus an index.
- Source-audited Chapter 2 claims C05 and C07: added `prenatal-auditory-learning.md` and `prenatal-folate-ntd.md`.
- Source-audited remaining Chapter 2 claims C01–C04 and C08–C12: added timing, placenta, neural-construction, fetal-autonomic, iodine, FASD, tobacco-growth, mixtures, and fetal-growth cards. C13 held as interpretive continuity on the growth card.

### Revised
- Aligned YAML `confidence` on all eight first-pass cards with in-body grades (cards remain `status: draft`).
- Resolved the 12 previously unresolved `SOURCES.md` citations (two were already verified; two titles were corrected to the matching papers).


## [2026-09-14]

### Structure
- Retrofitted all 8 existing evidence cards with Open Knowledge Format (OKF) v0.2 frontmatter (`type`, `title`, `description`, `tags`, `status`, `generated`, `stale_after`, `sources`), making the bundle machine-readable and agent-traversable without changing card bodies.
- Replaced `evidence-cards/_INDEX.md` with OKF-reserved `evidence-cards/index.md` (no frontmatter, per OKF section 8).
- Added a bundle-root `index.md` declaring `okf_version: "0.2"` and linking to the evidence-cards directory and core documentation files, per OKF section 8/12.
- All cards remain `status: draft` pending confidence-grade assignment and deeper source audit; `stale_after` set to 2027-03-14 as a 6-month re-audit horizon.

## [2026-09-14b]

### Structure
- Added `SOURCES.md`, a bundle-root Master Source Catalog cataloging every reference cited across the 8 evidence cards: 19 sources with verified, resolvable resource links (mirrored in the file's OKF frontmatter `sources` array) and 12 sources named in card bibliographies during the initial pass but not yet matched to a stable verified link ("Unresolved Citations"). Those 12 were resolved on 2026-09-15; see `[Unreleased]`.
- Updated `index.md` and `evidence-cards/index.md` to reference `SOURCES.md`.
- Established a maintenance rule: all future evidence-card additions/revisions must update `SOURCES.md` in the same commit.
