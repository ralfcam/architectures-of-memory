# Research Note: Ch.01 — Rosenblatt's Perceptron and the Dream of Learning Machines

**Date:** 2026-04-22  
**Linear Issue:** ARC-1  
**Queries:**
1. "Frank Rosenblatt 1957 1958 perceptron paper history Psychological Review"
2. "Cornell Mark I Perceptron hardware parallel perceptron history"
3. "New York Times 1958 perceptron thinking machine headline"
4. "Frank Rosenblatt biography Cornell connectionism"

---

## Findings

### Query 1 — The 1957–1958 Paper

Frank Rosenblatt, a research psychologist at the Cornell Aeronautical Laboratory in Buffalo, New York, first described the perceptron in 1957. The canonical publication is:

> **Rosenblatt, F.** "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain." *Psychological Review*, Vol. 65, No. 6 (November 1958), pp. 386–408.

The paper took an explicit **connectionist / empiricist** position: storage is distributed across connection weights, not in localized coded images — a direct counter to the symbolic AI programme dominant at the time. The first simulation ran on an **IBM 704** at the Cornell Aeronautical Laboratory.

The 1957 funding proposal for the "Cornell Photoperceptron" already stated:
> *"Devices of this sort are expected ultimately to be capable of concept formation, language translation, collation of military intelligence, and the solution of problems through inductive logic."*

This gap between what the mathematics *guaranteed* and what the *publicity* promised is the structural starting point for Book 1.

---

### Query 2 — Cornell Mark I Perceptron Hardware

The Mark I Perceptron was built at the Cornell Aeronautical Laboratory, funded jointly by the **Office of Naval Research (ONR)** and the **Rome Air Development Center**. It was first publicly demonstrated on **23 June 1960**.

Hardware architecture (three layers):

| Layer | Units | Description |
|-------|-------|-------------|
| S-units (sensory) | 400 photocells | 20×20 grid — the input "retina" |
| A-units (association) | 512 perceptrons | Each S-unit connects to up to 40 A-units |
| R-units (response) | 8 perceptrons | Output layer |

Rosenblatt insisted on **random** S→A connections, modelling his belief that the biological retina connects randomly to the visual cortex. He called this three-layer variant the *alpha-perceptron*.

A subsequent classified application of the Mark I ran from 1963–1966 at the **National Photographic Interpretation Center (NPIC)**.

The machine is currently housed at the **Smithsonian National Museum of American History** (Washington, D.C.).

---

### Query 3 — The NYT Headline and the Hype Ceiling

At a **1958 Navy press conference**, Rosenblatt made expansive claims about the perceptron's potential. *The New York Times* reported it as:

> *"the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence."*

Rosenblatt himself called it:

> *"the first machine which is capable of having an original idea."*

**Authorial note:** These quotes establish the hype ceiling the chapter requires before the *Perceptrons* (1969) critique lands. The NYT quote is contemporary and attributable to the 1958 Navy press conference. The claim is *structural*: the gap between mathematical guarantee and public promise is the vanishing signal Book 1 tracks.

---

### Query 4 — Rosenblatt Biography

- **Born:** 1928, New York City
- **Died:** 1971 (age 43) — cause: boating accident on the Chesapeake Bay
- **Education:** Cornell B.A. 1950, Ph.D. (Psychology) 1956
- **Position at time of Perceptron work:** Research Psychologist and Project Engineer, Cornell Aeronautical Laboratory, Buffalo, NY (1957–c.1962)
- **Later position:** Associate Professor of Neurobiology and Behavior, Cornell University Division of Biological Sciences

His death in 1971 predated backprop's revival, the LSTM, and the Transformer — leaving permanently open the question of how Rosenblatt would have read the vindication of connectionism. The interaction between the hype he generated and the structural critique of Minsky & Papert (1969) is the core narrative spine of Book 1, Chapter 1.

---

## Verified Claims

- [x] Rosenblatt born 1928, died 1971
- [x] First paper: *Psychological Review* Vol. 65, No. 6, November 1958, pp. 386–408
- [x] First simulation: IBM 704, Cornell Aeronautical Laboratory
- [x] Mark I hardware: 400 photocells (S), 512 A-units, 8 R-units
- [x] First public demo of Mark I: 23 June 1960
- [x] Funding: ONR + Rome Air Development Center
- [x] Mark I now at Smithsonian NMAH
- [x] NYT "walk, talk, see, write, reproduce" quote — 1958 Navy press conference
- [x] "First machine capable of having an original idea" — Rosenblatt's own words at the press conference

---

## Open Questions `[citation needed]`

- [ ] Exact archival URL / document title for the **1957 "Cornell Photoperceptron" proposal** (partial evidence in Mark I Wikipedia sourcing, no direct archival link)
- [ ] Was there a **prior internal report** before the *Psychological Review* paper? (Rosenblatt 1957 is cited in media archaeology sources as distinct from the 1958 paper — confirm)
- [ ] Did Rosenblatt attend the **1958 Mechanisation of Thought Processes** NPL symposium in person, or did he only submit? (Wikipedia says "presented" — confirm via symposium proceedings)
- [ ] **Exact date and page of the NYT article** — the quoted text is confirmed but the specific issue date is not yet pinned

→ Capture as Linear `fact-check` issue: *"Verify: Rosenblatt 1957 proposal document and NYT article exact date"*
