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

### Added
- Populated evidence-cards/ with 8 preliminary evidence cards (prenatal maternal stress/anxiety, breastfeeding and cognitive development, early childcare quality, screen time and language development, responsive caregiving and attachment interventions, infant sleep training, self-regulation/delay of gratification, preschool early education RCTs) plus an index.


## [2026-09-14]

### Structure
- Retrofitted all 8 existing evidence cards with Open Knowledge Format (OKF) v0.2 frontmatter (`type`, `title`, `description`, `tags`, `status`, `generated`, `stale_after`, `sources`), making the bundle machine-readable and agent-traversable without changing card bodies.
- Replaced `evidence-cards/_INDEX.md` with OKF-reserved `evidence-cards/index.md` (no frontmatter, per OKF section 8).
- Added a bundle-root `index.md` declaring `okf_version: "0.2"` and linking to the evidence-cards directory and core documentation files, per OKF section 8/12.
- All cards remain `status: draft` pending confidence-grade assignment and deeper source audit; `stale_after` set to 2027-03-14 as a 6-month re-audit horizon.
