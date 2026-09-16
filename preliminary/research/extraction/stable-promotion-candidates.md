# Stable-promotion candidates

Date: 2026-09-16. **No card is moved to `status: stable` in this pass.**

A card may move to `stable` only after all five rules in `catalog-wide-replication-attenuation.md`:

1. Sources remain resolvable.
2. No retraction or expression-of-concern for the primary ID.
3. Replication or GI attenuation has been classified where that design class exists.
4. In-body grade still matches YAML `confidence`.
5. “What This Does Not Mean” still matches the identification.

Grey-literature IDs without a journal DOI (`nichd-seccyd-2006`, `who-anc-2016`, `who-nurturing-care-2018`, `kramer-1987-lbw`) now have persistent URLs or PMID (`SOURCES.md`). They should not be load-bearing primary IDs for a first `stable` card. `hiscock-2016` remains retired.

The realistic path to first `stable` cards runs through **physiology / laboratory** claims where GI attenuation is `n/a`, independent replication of the *narrow* claim is classifiable, and those five IDs are not the primary source.

| Candidate | Rules already in better shape | Still pending | Work needed before any `stable` flip |
|---|---|---|---|
| `neonatal-cardiopulmonary-transition.md` | (1) Morton 2016 PMC resolvable; (2) no retraction flag; (3) GI `n/a`; sequence independently described | (4) YAML/in-body already compound; (5) WTDM matches identification but card is first-pass prose | Independent neonatology replication note on the *narrow* shunt/gas-exchange claim; confirm no grey-lit primary |
| `prenatal-folate-ntd.md` | (1) Cochrane + MRC DOIs; (2) none; (3) MRC independently followed by later RCTs; GI `n/a` for NTD | (4) compound grade; WHO ANC is adjacent not primary | Drop `who-anc-2016` from any stability-critical path or treat as framework not identification; cognition/other-anomaly Low stays |
| `infant-statistical-speech-segmentation.md` | (1) Saffran 1996 DOI; (2) none; (3) lab transitional-probability conceptually replicated; GI `n/a` | (4)–(5) first-pass; transfer remains Low | Short replication note (Saffran-line follow-ups); keep household-transfer Low |
| `prenatal-developmental-timing.md` | (1) Ujházy DOI; (2) none; (3) Wilson principles as clinical consensus; GI `n/a` | Identification is review-level, not a timed human experiment | Keep Moderate for the human principle; do not inflate to High epidemiology |
| `prenatal-neural-construction.md` | (1) Bystron DOI; (2) none; (3) independent neuroanatomy descriptions; GI `n/a` | Structure ≠ personality is interpretive High on a first-pass card | Confirm WTDM still blocks IQ/personality forecast |
| `infant-contingency-learning.md` | (1) Rovee DOI; (2) none; (3) mobile paradigm replicated across decades; GI `n/a` | Transfer / adult-like cause Low must stay | Do not promote a stimulation-mandate reading |
| `looking-time-as-measurement.md` | (1) Aslin DOI; (2) none; (3) looking-as-discrimination is standard | Rich-interpretation debate is the live replication issue | Promote only the *measurement* claim, never the rich-concept reading |
| `infant-perceptual-narrowing.md` | (1) Werker & Tees DOI; (2) none; (3) attunement conceptually replicated | Timetable not universal; sealed-deadline Low | Keep Low on permanence |

## Explicit non-promotions

- Zero cards set to `status: stable` in this note.
- Observational / GI-attenuated cards (`prenatal-maternal-stress-anxiety`, `breastfeeding-cognitive-development`, `self-regulation-delay-of-gratification`) are **not** first-wave `stable` candidates.
- Childcare, screens, sleep, and attachment-intervention cards wait; they are not physiology/lab cards and some still carry grey-lit or repaired IDs.
- New cards from the Chapter 1 / 6 / 7 / 8 package are first-pass drafts and are not on this list.

## Next concrete work

1. Write a one-page replication note for the three strongest lab/physiology candidates (transition, folate NTD, Saffran segmentation).
2. Confirm each candidate’s primary ID is a journal DOI, not WHO/NIH/Kramer grey literature.
3. Only then consider flipping YAML `status` — and only for the *narrow* claim already graded High.
