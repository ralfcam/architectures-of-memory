# Manuscript, Continuity & OKF Audit — `book-01-vanishing-signal`

## 1. Overview Metrics
- **Chapters audited:** 16
- **Total words:** 19,469
- **Unresolved `[citation needed]` markers in prose:** 0
- **BibTeX entries in `sources.bib`:** 21
- **OKF v0.2 Evidence Cards (`evidence-cards/`):** 2/2 passing mechanical 5-rule gate

| Chapter | Words | Footnotes | `[citation needed]` |
| :--- | ---: | ---: | ---: |
| `01-rosenblatt-perceptron.md` | 1,235 | 6 | 0 |
| `02-ai-winter-connectionism.md` | 1,147 | 7 | 0 |
| `03-backprop-1986.md` | 1,150 | 6 | 0 |
| `04-sequence-time-order.md` | 1,165 | 5 | 0 |
| `05-backprop-chain-rule.md` | 1,161 | 4 | 0 |
| `06-rnn-illusion-of-memory.md` | 1,136 | 4 | 0 |
| `07-hochreiter-1991-thesis.md` | 1,190 | 7 | 0 |
| `08-vanishing-gradient-theorem.md` | 1,055 | 4 | 0 |
| `09-reorg-as-gradient-vanishing.md` | 1,620 | 9 | 0 |
| `10-documentation-no-gating.md` | 1,192 | 8 | 0 |
| `11-regulated-compliance-without-memory.md` | 1,204 | 14 | 0 |
| `12-what-orgs-need-to-remember.md` | 1,121 | 8 | 0 |
| `13-heraclitus-river-identity.md` | 1,561 | 6 | 0 |
| `14-ship-of-theseus.md` | 1,240 | 6 | 0 |
| `15-bergson-duration.md` | 1,222 | 6 | 0 |
| `16-question-unanswered.md` | 1,070 | 7 | 0 |

## 2. Metaphor Collision Check (Rule: Max 1 Controlling Metaphor / Section)
- **Pass:** No multi-metaphor collisions detected within any single chapter section.

## 3. Footnote Integrity & Cross-Chapter Collisions
- **Pass:** Every chapter's inline `[^key]` matches its local `## Notes` definitions.
- **Notice (5 shared footnote keys across chapters):** `[^bengio1994]` (06-rnn-illusion-of-memory.md, 16-question-unanswered.md), `[^bptt]` (04-sequence-time-order.md, 06-rnn-illusion-of-memory.md), `[^elman1990]` (04-sequence-time-order.md, 06-rnn-illusion-of-memory.md), `[^independence]` (05-backprop-chain-rule.md, 07-hochreiter-1991-thesis.md), `[^jordan1986]` (04-sequence-time-order.md, 06-rnn-illusion-of-memory.md)

## 4. Forbidden-Phrase & Epistemic Hygiene Check (`style/forbidden-phrases.md`)
- **Pass:** Zero forbidden phrases or raw redirect URLs detected in unquoted chapter prose.

## 5. OKF v0.2 Five-Rule Evidence Card Gate (`evidence-cards/`)
- **Pass:** All 2 OKF v0.2 evidence card(s) pass mechanical Rules 1, 4, and 5.

## 6. Character Continuity Map (`characters.md`)
| Character | First Mention | Chapters Appearing |
| :--- | :--- | :--- |
| Frank Rosenblatt | Ch.01 | Ch.01 |
| Marvin Minsky | Ch.01 | Ch.01, Ch.02, Ch.03, Ch.05 |
| Seymour Papert | Ch.01 | Ch.01, Ch.02, Ch.03 |
| David E. Rumelhart | Ch.03 | Ch.03, Ch.04, Ch.05, Ch.06 |
| Geoffrey E. Hinton | Ch.03 | Ch.03, Ch.04, Ch.05, Ch.06, Ch.16 |
| Paul J. Werbos | Ch.03 | Ch.03, Ch.04, Ch.05, Ch.06 |
| Sepp Hochreiter | Ch.04 | Ch.04, Ch.05, Ch.07, Ch.08, Ch.15, Ch.16 |
| Jürgen Schmidhuber | Ch.07 | Ch.07, Ch.16 |
| Yoshua Bengio | Ch.05 | Ch.05, Ch.06, Ch.07, Ch.08, Ch.15, Ch.16 |
| Heraclitus | Ch.13 | Ch.13 |
| Plutarch | Ch.13 | Ch.13, Ch.14 |
| Plato | Ch.13 | Ch.13 |
| Henri Bergson | Ch.15 | Ch.15, Ch.16 |

## 7. Residual Fact-Check Action Items (`research/fact-checks/*.md`)
- `ch01.md:93`: - [ ] This issue closed with commit reference
- `ch02.md:104`: - [ ] PR linked
- `ch03.md:115`: - [ ] PR linked
- `ch04.md:131`: - [ ] PR linked
- `ch05.md:115`: - [ ] PR linked
- `ch06.md:117`: - [ ] PR linked
- `ch07.md:134`: - [ ] PR linked
- `ch08.md:130`: - [ ] PR linked
- `ch09.md:148`: - [ ] PR linked
- `ch11.md:94`: - [ ] Ch.11 draft: audit for "compliance theater" attribution to Schneier
- `ch11.md:95`: - [ ] Ch.11 draft: qualify any SOX 802 prosecution statistics or substitute Arthur Andersen + *Yates* illustration
- `ch12.md:122`: - [ ] Ch.12 draft: audit for ATP 5-19 citation in AAR context — replace with TC 7-0.1
- `ch12.md:123`: - [ ] TC 7-0.1 edition date: confirm from CAR for complete footnote
- `ch13.md:132`: - [ ] Kahn appendix: verify exact Kahn numbers for B49a and B91
- `ch13.md:133`: - [ ] Kahn hardback ISBN: confirm 0-521-21632-9 if hardback cited
- `ch14.md:124`: - [ ] Molesworth Vol. I page number for De Corpore II.11.§7 — requires physical edition verification
- `ch14.md:125`: - [ ] Sider hardback ISBN — requires OUP/Clarendon catalogue confirmation
- `ch15.md:140`: - [ ] *DS* reprint-refusal: primary archival source required before presenting as verified fact
- `ch15.md:141`: - [ ] Zone Books 1991 ISBN: confirm 0-942299-40-8 from WorldCat or physical copy
- `ch16.md:136`: - [ ] Waibel 1987 CMU TR: primary source required if 1987 cited in chapter
