# Publishing workbench

In-repo packets for controlled manuscript and audience work. **None is a live public deposit.**

| Track | Current artifact | Boundary |
|---|---|---|
| KB releases | `v0.1`–`v0.3` tagged on `main` | No `v0.4`; Reader Edition 0.1 is not a KB release |
| Private reader editions | `parenthood-atlas-reader-edition-01.pdf` + HTML proof + extraction report | Private working manuscript; physical proof-print and reader feedback remain human steps |
| Chapter preprints | Internal Chapter 1 packet | No PsyArXiv/OSF post or DOI |
| Evidence briefs | Internal Brief #1 | No public distribution; wait until 10–12 `stable` cards |

## Reader Edition 0.1

`reader-edition-01--manifest.md` freezes the 15 curated chapters at post-PR-#18 commit `9f3b151`. Reader note, evidence/uncertainty note, feedback guide, print checklist, and de-identified feedback templates sit beside it. The 84-page PDF is a US Letter reading proof with explicit chapter order, page-numbered contents, real tables, inline emphasis, chapter breaks, and an edition footer.

Generate and verify all publishing outputs:

```bash
python3 -m pip install -r requirements-publishing.txt
python3 scripts/render_publishing_pdfs.py
```

The renderer writes `reader-edition-01--extraction-report.txt`. The report checks all chapter starts, all 15 contents page numbers, 1,406 source fragments, nonblank pages, footer numbering, and HTML anchors. It does not replace the two-copy physical checklist in `reader-edition-01--print-checklist.md`.

Feedback intake uses `feedback/reader-edition-01--feedback-log.csv`; keep names and identifying details out of the repository. Complete the triage template only after the private reading window closes. Reader agreement is not evidence validation.

Issue Fields cannot be created on this User-owned repository; see `issue-fields--org-admin.md`.
