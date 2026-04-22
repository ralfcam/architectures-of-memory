# Architectures Of Memory
## Design Principles

The system treats the book series as a **software project**: versioned content, tracked issues, automated research, and a clear separation between drafts (GitHub), tasks (Linear), and research (Perplexity). Every layer is queryable by AI agents.

***

## GitHub — Content Repository

### Repository Structure

**Monorepo:** one repository for the series; each book is a top-level folder.

```
github.com/ralfcam/architectures-of-memory/
├── README.md                         ← This file: series workflow & principles
├── series-bible.md                   ← Voice, spine, metaphors, glossary
├── characters.md                     ← Key figures across the series
├── baseline outlines.md              ← Combined outline snapshot (per-book lives in book-*/outline.md)
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── research-gap.md           ← Missing citation / fact
│       ├── chapter-draft.md          ← New chapter submission
│       └── revision-note.md          ← Edit request
├── book-01-vanishing-signal/
│   ├── README.md
│   ├── outline.md                    ← Living chapter-level outline
│   ├── chapters/
│   ├── research/
│   │   ├── sources.bib
│   │   ├── notes/                    ← Perplexity / research dumps
│   │   └── fact-checks/
│   └── drafts/
├── book-02-forget-gate/              ← Same structure
├── book-03-weight-of-attention/
├── book-04-context-window/
└── book-05-architecture-of-forgetting/
```


### Branching Strategy

```
main          ← Published / approved content only
├── outline   ← Living outline changes
├── draft/ch-01-dreaming-perceptron
├── draft/ch-02-minsky-proof
├── research/hochreiter-sources
└── edit/ch-01-line-edits
```

Each chapter gets its own branch. PRs are the review mechanism — AI agent (Copilot or Claude) reviews before human merge.

### Key Files for AI Optimization

- `series-bible.md` — loaded as system context for every writing session; defines voice, recurring metaphors, and argument spine
- `research/notes/` — raw Perplexity output stored as `.md` with query, date, and source URLs; fully searchable
- `fact-checks/` — one file per chapter, structured as `[claim] → [source] → [verified: yes/no]`

***

## Linear — Task and Editorial Management

**Team: ArchitecturesOfMemory** (`ARC`) is the right home — this is authorship/IP work distinct from Realized's RegTech operations .

### Project Structure

```
Linear / ArchitecturesOfMemory /
├── Project: "Architectures of Memory — Series"
│   ├── Milestone: Book 1 — The Vanishing Signal
│   ├── Milestone: Book 2 — The Forget Gate
│   └── ...
```


### Label Taxonomy

```
Type:
  research        ← Perplexity queries to run
  draft           ← New chapter / section to write
  edit            ← Revision of existing content
  fact-check      ← Claim requiring verification
  structure       ← Outline or architecture change

Status:
  Backlog → In Research → In Draft → In Review → Done

Priority:
  Urgent = blocking another chapter
  High   = current milestone
  Medium = next milestone
  Low    = series-level / future books
```


### Workflow per Chapter

```
1. [research]   Linear issue: "Research Ch.5 — Backprop history"
                → Perplexity query set defined in issue body
                → Results stored in GitHub: research/notes/ch05-backprop.md
                → Issue closed, linked to commit

2. [draft]      Linear issue: "Draft Ch.5 — Chain rule as debt"
                → Branch: draft/ch-05-chain-rule
                → Draft committed as chapters/05-chain-rule.md
                → PR opened, linked to Linear issue

3. [edit]       Linear issue: "Edit Ch.5 — tighten opening para"
                → Branch: edit/ch-05-opening
                → PR reviewed (Copilot + human)
                → Merged to main, issue closed

4. [fact-check] Linear issue: "Verify: Rumelhart 1986 paper date"
                → Perplexity query run
                → Result added to fact-checks/ch05.md
                → Issue closed with source link
```


***

## Perplexity — AI Research Engine

Perplexity's role is **structured research on demand**, always outputting to the GitHub `research/notes/` layer. Every query is traceable.

### Query Templates per Phase

**Phase 1 — Chapter Research (before drafting)**

```
Query set for Ch.7 — Hochreiter's 1991 Thesis:
1. "Hochreiter 1991 diploma thesis vanishing gradient Munich"
2. "Schmidhuber Hochreiter LSTM history 1991 to 1997"
3. "sepp hochreiter biography early career neural networks"
4. "vanishing gradient problem history 1990s connectionism"
```

**Phase 2 — Fact Verification (during editing)**

```
1. "Rumelhart Hinton Williams backpropagation 1986 Nature paper"
2. "Minsky Papert Perceptrons book publication date 1969"
3. "first AI winter dates funding cuts neural networks"
```

**Phase 3 — Cross-domain Bridging (philosophy / business chapters)**

```
1. "Bergson duration time philosophy lived experience"
2. "Ship of Theseus paradox original source Plutarch"
3. "institutional amnesia organizational knowledge loss research"
4. "Borges Funes the Memorious memory philosophy analysis"
```


### Output Format (stored in GitHub)

Each research session is saved as:

```markdown
# Research Note: Ch.07 — Hochreiter's Thesis
**Date:** 2026-04-22
**Linear Issue:** SG-42
**Queries:** [list]

## Findings
[Perplexity output with inline citations]

## Verified Claims
- [ ] Thesis written in German → source needed
- [x] Submitted 1991, Munich TU → [source]

## Open Questions
- Exact title of the thesis?
- Did Schmidhuber supervise or co-supervise?
```


***

## The Integrated Loop

```
┌─────────────────────────────────────────────────┐
│                   LINEAR                         │
│  Issue created → labels: [research] [Ch.07]      │
└──────────────────┬──────────────────────────────┘
                   │ triggers
┌──────────────────▼──────────────────────────────┐
│                 PERPLEXITY                        │
│  Structured query set → research note output     │
└──────────────────┬──────────────────────────────┘
                   │ committed to
┌──────────────────▼──────────────────────────────┐
│                  GITHUB                           │
│  research/notes/ch07-hochreiter.md               │
│  → PR → Copilot review → merged                  │
│  → Linear issue auto-closed via commit message   │
└─────────────────────────────────────────────────┘
```

Every artifact is versioned, every claim is traceable to a query, every query is traceable to a Linear issue. An AI agent entering this system at any point can reconstruct the full reasoning chain behind any sentence in any chapter.

***

## Immediate Next Steps

| Priority | Action | Tool |
| :-- | :-- | :-- |
| 1 | Create repo `architectures-of-memory` + `book-01-vanishing-signal` | GitHub |
| 2 | Create Linear project "Architectures of Memory" under ArchitecturesOfMemory | Linear |
| 3 | Commit the five baseline outlines as `outline.md` in each book repo | GitHub |
| 4 | Create label taxonomy in Linear ARC team | Linear |
| 5 | Open first research issues: Ch.1–4 of Book 1 | Linear |
| 6 | Draft `series-bible.md` — voice, recurring metaphors, glossary | GitHub |

