# Ch.02 — The First AI Winter: Why Connectionism Failed

**Issue:** ARC-2
**Status:** Research complete — open questions logged
**Branch:** `research/ch02-ai-winter-connectionism`
**Output file:** `book-01-vanishing-signal/research/notes/ch02-ai-winter-connectionism.md`

---

## Query set executed

1. "Minsky Papert Perceptrons 1969 XOR limitation book summary"
2. "first AI winter 1970s funding cuts neural networks history Lighthill report 1973"
3. "connectionism decline 1970s symbolic AI dominance GOFAI"

---

## Findings

### 1. Minsky & Papert, *Perceptrons* (1969)

- **Full title:** *Perceptrons: An Introduction to Computational Geometry* — Marvin Minsky and Seymour Papert, MIT Press, 1969.
- **Core argument:** A single-layer perceptron with *restricted connectivity* (the "order" constraint — each hidden unit receives input from only a small local region) cannot compute functions like XOR or determine whether an image is topologically connected (the "connectivity predicate").
- **The XOR proof:** XOR returns 1 when inputs differ (0,1 or 1,0) and 0 when they match. No single linear decision boundary can separate the four input combinations; therefore a single-layer perceptron cannot learn it. The authors formalised this as a theorem, not a conjecture.
- **The localness constraint — critical nuance:** Minsky and Papert's proof applies to *order-restricted* perceptrons with "conjunctive localness" — not to multilayer networks in general. The book explicitly acknowledged that an unrestricted elementary perceptron (unlimited hidden units) *can* solve any classification problem (Existence Theorem), and that multilayer perceptrons could compute XOR. However, no effective training algorithm for multilayer networks was known in 1969, making the point practically moot at the time.
- **Sociological reading (Olazaran):** Historian of science Mikel Olazaran documented that Minsky and Papert's framing — "the interest of neural computing comes from parallelism of *local* information" — set the terms under which connectionism was judged, even when that framing did not strictly follow from their proofs.
- **Retrospective debate:** Later accounts (including Rumelhart & McClelland 1986) argued that Minsky and Papert overstated the generality of their negative results, contributing to an unwarranted abandonment of neural network research. Minsky disputed this reading. The book's reception is itself a historiographical problem worth addressing in the chapter.

### 2. The Lighthill Report (1973)

- **Author:** Sir James Lighthill, Lucasian Professor of Applied Mathematics at Cambridge; commissioned by the British Science Research Council (SRC).
- **Published:** 1973. Full title: *Artificial Intelligence: A General Survey*.
- **Central critique:** Lighthill identified three categories of AI work — (A) automation and robotics, (B) central AI (problem-solving, pattern recognition), (C) simulation of the nervous system. He argued that Category B — the domain connecting A and C and where most ambitious AI claims lived — had failed to produce useful results, largely because of the "combinatorial explosion": as problems scale, the search space grows exponentially and available compute cannot keep pace.
- **Immediate impact:** The SRC drastically cut AI funding to British universities. Several prominent AI laboratories closed or pivoted. Researchers emigrated to the US.
- **Transatlantic effect:** The report did not directly govern US funding but amplified existing skepticism at DARPA. By 1974, DARPA redirected AI funding toward specific goal-driven projects (autonomous vehicles, battle management) and away from open-ended basic research. AI research proposals were held to an unusually high standard of demonstrable near-term utility.

### 3. Connectionism's Decline and GOFAI's Ascendancy (mid-1970s)

- **GOFAI ("Good Old-Fashioned AI"):** The term, coined by philosopher John Haugeland, describes the symbolic paradigm dominant from the early 1960s through the late 1980s — intelligence as formal symbol manipulation, implemented in languages like LISP and Prolog.
- **Why GOFAI thrived while connectionism froze:** Symbolic systems produced visible, legible results (Logic Theorist, General Problem Solver, early expert systems), which were easier to explain to funding bodies and to publish. Neural network research, by contrast, lacked a training algorithm for multilayer architectures, lacked hardware to run them at meaningful scale, and carried the stigma of Minsky & Papert's critique.
- **Not a clean break:** Some connectionist research continued through the 1970s — notably James Anderson (brain-state-in-a-box, 1977) and Teuvo Kohonen's associative memory work — but it was marginal and underfunded.
- **The machine translation failure (context):** The 1966 ALPAC report had already concluded that machine translation by computer was slower, less accurate, and twice as expensive as human translation — cutting MT funding and contributing to a pre-Lighthill chill. By 1973, the pattern of over-promise and under-delivery was well established in the minds of funding agencies.
- **First winter vs. second winter:** The first AI winter (mid-1970s) was primarily a *funding and credibility* crisis. The second, more severe winter (late 1980s–early 1990s) followed the commercial failure of expert systems and the collapse of the Lisp machine market. Connectionism had already revived by then (Rumelhart & McClelland 1986, Hopfield 1982), making the second winter's impact on neural networks far less severe than the first.

---

## Narrative threads for Ch.02

1. **The paradox of the proof:** Minsky and Papert's result was mathematically correct but narratively over-read. A chapter can dramatise the gap between what the proof actually showed (limitations of *locally-connected* single-layer nets) and how it was received (neural networks are a dead end).
2. **The sociology of winter:** The Lighthill Report is a rare case where a single commissioned document reshaped an entire research landscape. The political economy of science funding is part of the story — not just the ideas.
3. **The underground stream:** Connectionism did not die; it went underground. The chapter can track the small, persistent communities (Kohonen in Helsinki, Anderson at Brown, Amari in Tokyo) who kept working through the winter. This sets up the "spring" of the 1980s.
4. **GOFAI's hubris:** The ascendancy of symbolic AI was not irrational — it had genuine early successes. The chapter should be fair to this before showing how its assumptions (brittleness of rule-based systems, the frame problem, the scaling wall) created the conditions for connectionism's return.

---

## Open questions

> **⚠️ Flag for ARC fact-check issue (create separately):**

1. **Lighthill Report exact date of publication and SRC response timeline** — The report is dated 1973 but the specific month of the SRC decision to cut funding is unclear. Needed for precise narrative sequencing relative to DARPA's 1974 cuts.
   - Suggested query: `"Lighthill report 1973 SRC funding cuts exact date British AI laboratories closed"`

2. **ALPAC report 1966 scope** — Confirm whether the ALPAC report explicitly recommended *suspending* or merely *redirecting* MT funding. The distinction matters for the narrative of escalating disillusionment.
   - Suggested query: `"ALPAC report 1966 machine translation recommendations funding suspension redirect"`

3. **Minsky's retrospective position** — Did Minsky ever formally respond to the claim (from Rumelhart, Hinton, and others) that *Perceptrons* caused an unwarranted abandonment of connectionism? Locate a specific published statement or interview.
   - Suggested query: `"Marvin Minsky response criticism Perceptrons book overstated neural network limitations interview"`

4. **Exact DARPA cut timeline** — Wikipedia and CMU lecture notes cite "1974" for DARPA cuts but do not name the specific programme or decision document. Identify the programme name and approximate date.
   - Suggested query: `"DARPA 1974 AI funding cuts programme name decision neural networks connectionism"`

---

## Definition of done (ARC-2 checklist)

- [x] Notes committed with citations
- [x] Open questions logged
- [ ] PR linked
