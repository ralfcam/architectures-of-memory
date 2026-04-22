# Series Bible — The Architectures of Memory

Living reference for voice, spine, metaphors, and shared vocabulary. Load this (or excerpts) as system context for drafting, research synthesis, and edits.

---

## Voice

- **Analytic and narrative:** Explain mechanisms clearly; anchor claims in named people, papers, and dates. Prefer concrete scenes (a thesis unread in Munich; a winter after an optimistic headline) over abstract slogans.
- **Historically grounded:** Treat AI history as contested interpretation, not folklore. Distinguish what the field *believed* from what *held* under later mathematics.
- **Three lenses, one argument:** Each book rotates **technical**, **organizational**, and **philosophical** angles. Technical chapters set the mechanism; org chapters show structural analogues; philosophy chapters name what is at stake for persons and institutions.
- **No triumphalism:** Progress is real but costly. Solutions create new memory architectures — and new ways to forget, obscure, or harm.
- **Reader:** Educated non-specialist willing to follow equations *described* in prose; specialists should still find fidelity and surprise.

---

## Argument spine (five books)

1. **Book 1 — The Vanishing Signal:** Before the fix, a *proof of failure*: learning across depth and time hits structural limits (vanishing gradients). Organizations and philosophy supply parallel “signals that don’t survive.”
2. **Book 2 — The Forget Gate:** **Selective forgetting** as design — the LSTM family encodes judgment about what to retain. Institutions face the same tradeoff; ethics and law enter.
3. **Book 3 — The Weight of Attention:** **Attention** dissolves the recurrent bottleneck; memory becomes **weighted access**. Retrieval supplants compression — and *retrieval ≠ memory*.
4. **Book 4 — The Context Window:** **Scale** distributes memory into parameters and a finite **window**. Opaque parametric memory and governance gaps matter for regulated domains.
5. **Book 5 — The Architecture of Forgetting:** **Forgetting** as policy, math, and morality — unlearning, privacy, cost, asymmetry. The series closes where Book 1 began: Hochreiter’s thesis as unread proof — now read against systems that “remember everything.”

**Central claim:** Memory architecture is **moral** architecture: every design chooses what persists, what decays, and who bears the cost.

---

## Recurring metaphors (use sparingly, consistently)

| Metaphor | Where it applies |
|----------|------------------|
| **Gradient as debt** | Backprop / depth — errors compound or vanish like obligations rolling up a chain. |
| **Gate as judgment** | LSTM / org policy — what to admit, hold, release. |
| **Attention as valuation** | Weights reveal what the system (or org) treats as relevant. |
| **Window as horizon** | Context limits — what lies outside was never “present” to the model. |
| **Forgetting as design** | Not absence of memory but a necessary, ethical, and technical choice. |

---

## Cross-book callbacks

- **Hochreiter’s 1991 thesis:** Book 1 climax and Book 5 coda — proof before the audience; circle closing.
- **Perceptrons winter → backprop spring → sequence deadlock:** Book 1 timeline seeds Book 2’s engineering response.
- **“Funes” and perfect memory:** Book 2–3 bridge — total retention as pathology.
- **Meno / extended mind:** Book 3 — retrieval, external stores, where “knowing” lives.
- **Chinese Room at scale:** Book 4 — pattern, comprehension, and institutional trust.
- **Right to be forgotten / Ricoeur:** Book 2 introduces; Book 5 deepens.

---

## Epigraph index (working)

- **Book 1:** Signal diminishing backward; nothing remains of what came before.
- **Book 2:** Memory that never forgets vs. one that forgets everything; *what is worth keeping*.
- **Book 3:** To attend is to choose; every weight a value judgment at scale.
- **Book 4:** Read everything / remembers nothing / knows everything you ask.
- **Book 5:** Machines that remember everything; forgot to ask whether they should.

---

## Glossary (series-level)

- **Vanishing / exploding gradient:** During backprop through many layers or time steps, gradients shrink or blow up, making learning unstable or ineffective — not merely a “bad hyperparameter” story in deep time.
- **Recurrent neural network (RNN):** Sequence model with hidden state carried across time; “memory” is distributed in activations, limited by depth-in-time training dynamics.
- **LSTM / GRU:** Gated architectures mitigating vanishing gradients via additive paths and learned gates.
- **Constant Error Carousel (CEC):** Informal name for the LSTM’s stable error-flow idea — *addition* as the benign alternative to repeated multiplicative shrinkage.
- **Attention:** Mechanism mapping queries to keys/values; soft selection over positions or tokens.
- **Transformer:** Parallel sequence model built on self-attention and position information.
- **Context window:** Maximum tokens the model can attend to in one forward pass — working memory bound.
- **Parametric memory:** Knowledge encoded in weights (implicit, hard to audit) vs. **activation** or **external** memory.
- **RAG (Retrieval-Augmented Generation):** External documents retrieved into the window to ground generation.
- **Hallucination (operational):** Confident outputs unsupported by source or world — treated as a **memory / grounding** failure, not only a stylistic bug.
- **Machine unlearning:** Attempts to remove influence of specific data from a trained model — incomplete and contested.
- **Differential privacy:** Mathematical constraint limiting what a procedure leaks about individuals — a form of enforced forgetting.
- **Right to be forgotten:** Legal and normative demand that some data decay — clashes with model retention and logs.
- **Institutional memory:** Not “more docs” but **what survives** reorgs, turnover, and incentives — analogues to gates and gradients.

---

## Style constraints for drafts

- Prefer **one controlling metaphor per section**; avoid mixing gate/window/debt in the same paragraph without purpose.
- When citing, **primary + one good secondary** beats citation sprawl.
- Flag **uncertainty** explicitly where history is murky (priority disputes, “first” claims).

---

## Revision hygiene

- Large moves: `structure` label + outline PR.
- Line edits: `edit` + small PR.
- New claims: `fact-check` before polishing prose.
