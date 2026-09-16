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
- Classified replication/genetically informed attenuation for every live card (`preliminary/research/extraction/catalog-wide-replication-attenuation.md`). **No card moved to `status: stable`.**
- Citation-repaired `screen-time-language-development.md`: `madigan-2020` now points at Madigan et al. 2020 *JAMA Pediatrics* (DOI 10.1001/jamapediatrics.2020.0327). Jing, Ye, Kirkorian & Mares 2023 *Child Development* is a separate vocabulary meta-analysis (`jing-2023-cdev`). Grade unchanged.
- Repaired the five remaining no-DOI listings and ran a catalog-wide Retraction Watch dump (`preliminary/research/extraction/five-listings-and-retraction-watch-dump.md`). `hiscock-2016` retired and replaced by Mindell 2006, Gradisar 2016, and Bilgin & Wolke 2020. WHO/NIH/Kramer 1987 now have IRIS or NIH identifiers. **No card moved to `status: stable`.**
- Promoted a curated, voice-checked Chapter 5 (`chapters/05-becoming-a-mind.md`) in the Appendix B range. Archival draft untouched. Looking-time, attention, object-permanence, and joint-attention cards added; narrowing, statistical-segmentation, and contingency cards reconciled, not rewritten.
- Recovered DOIs for 15 of 20 previously Crossref-unchecked catalog IDs and queried Crossref/PubMed/Retraction Watch (`preliminary/research/extraction/doi-recovery-retraction-watch.md`). Five IDs remain without a journal DOI (WHO, NICHD report, 1987 bulletin, mismatched sleep listing). **No card moved to `status: stable`.**
- Promoted curated, voice-checked Chapter 3 (`chapters/03-the-great-transition.md`) and Chapter 4 (`chapters/04-regulatory-relationship.md`, replacing the 10-step seed). Archival drafts untouched.
- Source-audited Chapter 4 feeding-as-regulation (Black & Aboud 2011). Sleep and attachment cards still not rewritten in that pass. `hiscock-2016` was later retired.
- Source-audited Chapter 7 language claims into draft cards (perceptual narrowing, statistical segmentation, conversational turns, dual-language). Existing `screen-time-language-development.md` and `prenatal-auditory-learning.md` reconciled, not rewritten. C07-P1 vs C07-S1 hash-compared (not identical).
- Promoted a curated, voice-checked Chapter 7 to `chapters/07-the-birth-of-language.md` (Appendix B range). Archival `preliminary/drafts-chapters/chapter 7` unchanged.
- Ran a catalog-wide Crossref/PubMed retraction lookup (`preliminary/research/extraction/catalog-wide-retraction-search.md`). No retraction or expression-of-concern titles among DOI-resolved records. Cochrane updates are new review versions. **No card moved to `status: stable`.**
- Source-audited remaining Chapter 3 C04/C05/C07 (crying, feeding coordination, preterm group risk). Mode of delivery still held.
- Source-audited Chapter 3 transition physiology and Chapter 4 co-regulation/deprivation claims into draft cards; C03-P1 vs C03-S1 hash-compared (not identical). Sleep and attachment cards reconciled, not rewritten. Mode of delivery still held.
- Began a selected-card replication/bias re-audit (`preliminary/research/extraction/selected-cards--replication-bias-reaudit.md`). No card moved to `status: stable`.
- Finished a curated, voice-checked Chapter 6 expansion at `chapters/06-the-mind-in-motion.md` (Appendix B range). Archival `preliminary/drafts-chapters/chapter 6` unchanged.
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
- Source-audited Chapter 3 C02/C06 and Chapter 4 C01/C02: added neonatal-transition, skin-to-skin, co-regulation, and severe-deprivation cards. Added a Chapter 6 contingency-learning card to support the curated expansion.
- Source-audited Chapter 7 C02/C03/C07–C09: added perceptual-narrowing, statistical-segmentation, conversational-turns, and dual-language cards. Screen-time card reconciled, not rewritten.
- Source-audited remaining Chapter 3 C04/C05/C07: added crying-as-signal, suck–swallow–breathe, and preterm group-risk cards.
- Source-audited Chapter 4 C04: added `responsive-feeding-as-regulation.md`.
- Source-audited Chapter 5 C01/C03/C06/C07: added looking-time, attention, object-permanence, and joint-attention cards. Narrowing, statistical-segmentation, and contingency cards reconciled, not rewritten.
- Source-audited remaining Chapter 7 C05/C06: added pointing and babbling cards. Parent-implemented interventions still open. Screen-time card IDs repaired, not re-theorized.

### Revised
- Aligned YAML `confidence` on all eight first-pass cards with in-body grades (cards remain `status: draft`).
- Resolved the 12 previously unresolved `SOURCES.md` citations (two were already verified; two titles were corrected to the matching papers).
- Citation-repaired `infant-sleep-training.md`: retired `hiscock-2016`; identified Mindell 2006, Gradisar 2016, and Bilgin & Wolke 2020. Harm claim and Low-to-Moderate grade unchanged.
- Citation-repaired `screen-time-language-development.md`: separated Madigan 2020 *JAMA Pediatrics* from Jing et al. 2023 *Child Development*. Low-to-Moderate grade unchanged.


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
