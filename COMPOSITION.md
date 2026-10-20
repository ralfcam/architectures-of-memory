# Unified Compositional Grammar & Three-Lens Crosswalk

This monorepo houses two flagship nonfiction series governed by a shared epistemic contract, grade-calibrated prose grammar, and Open Knowledge Format (**OKF v0.2**) evidence layer:

1. **Series 1 — *Architectures of Memory*** ([`series/architectures-of-memory/`](series/architectures-of-memory/)): A five-book investigation of memory, persistence, and forgetting across machine learning, human institutions, and philosophy.
2. **Series 2 — *Parenthood: The Atlas*** ([`series/parenthood-atlas/`](series/parenthood-atlas/)): A developmental science field guide mapping human emergence from preconception through early childhood and beyond.

---

## I. The Three-Lens Epistemic Crosswalk

Both series reject breathless hype, pop-science determinism, and ungrounded abstraction by triangulating every phenomenon through **three distinct epistemic lenses**:

| Lens Tier | Series 1: *Architectures of Memory* | Series 2: *Parenthood: The Atlas* | Shared Epistemic Function |
| :--- | :--- | :--- | :--- |
| **Lens 1: Mechanism & Empirical Ground** | **Technical** — Mathematical derivations, neural architectures, retrieval benchmarks, differential privacy bounds, and systems failure modes. | **Science** — What can be observed, measured, tested, replicated across cohorts/RCTs/genetically informed designs, and graded. | **What the mechanism actually does** under controlled measurement, stripped of metaphor. |
| **Lens 2: Interacting Systems & Context** | **Organizational** — How institutions, engineering teams, regulatory regimes, and documentation handoffs mirror or amplify technical memory bottlenecks. | **Interpretation** — The explanatory and systems frameworks (attachment, dyadic regulation, developmental cascades) that connect findings across domains. | **How the mechanism behaves inside a living feedback loop** where incentives, environment, and selection confound simple linear causes. |
| **Lens 3: Normative & Existential Meaning** | **Philosophical** — What persistence, identity, testimony, and oblivion mean (Heraclitus, Plato, Locke, Bergson, Borges, Stiegler, Ricoeur). | **Art** — Where empirical certainty ends and parental judgment, values, autonomy, and lived human meaning begin. | **What the boundary of knowledge demands of human judgment** without mistaking philosophy for empirical proof. |

---

## II. Narrative Engine: The Anomaly & The Concrete Case

Across both series, chapters never open with textbook definitions or abstract conclusions. They open with **an anomaly, a concrete failure mode, or an empirical puzzle**:

- **In *Architectures of Memory*:** A 1958 Navy press conference promising a walking, talking perceptron; an aviation safety manual whose warnings were overwritten across three corporate reorganizations; a recurrent network whose gradient norm decays below $10^{-12}$ across fifty time steps.
- **In *Parenthood: The Atlas*:** A newborn orienting toward a maternal voice heard in utero; a toddler knowingly violating a rule while watching the adult's face; an infant crying more intensely when the parent returns than when the parent left.

### Default Chapter Trajectory
$$\text{Phenomenon / Concrete Scene} \longrightarrow \text{Apparent Contradiction (Puzzle)} \longrightarrow \text{Competing Explanations} \longrightarrow \text{Mechanism (Lens 1)} \longrightarrow \text{Calibrated Evidence & Confounding} \longrightarrow \text{Systems / Organizational Cascade (Lens 2)} \longrightarrow \text{Boundary ("What This Does Not Mean")} \longrightarrow \text{Philosophical / Human Return (Lens 3)}$$

---

## III. Evidence-to-Prose Calibration (Mandatory Across All Books)

Prose verbs must strictly reflect the **Certainty Grade** recorded in the underlying OKF v0.2 Evidence Card (`evidence-cards/*.md`):

| Certainty Grade | Permitted Claim Strength | Required / Permitted Verbs | Prohibited Overreach |
| :--- | :--- | :--- | :--- |
| **High** (`high`) | Established causal effect, formal mathematical theorem, or independently replicated benchmark bound. | *"shows"*, *"demonstrates"*, *"proves"* (formal theorems only), *"causally increases/reduces"* | Extrapolating a bounded proof or lab RCT to untested organizational or lifelong outcomes without qualification. |
| **Moderate** (`moderate`) | Multiple studies, ablations, or cohorts with partial replication and known boundary conditions. | *"suggests"*, *"indicates"*, *"likely contributes to"*, *"under benchmark conditions"* | Using unconditional *"proves"* or *"always causes"*. |
| **Low** (`low`) | Observational correlation, single-case postmortem, or un-replicated preprint/cohort finding. | *"is associated with"*, *"correlates with"*, *"may"*, *"appears in observational data"* | Active causal verbs (*"drives"*, *"shapes"*, *"determines"*, *"rewires"*). |
| **Very Low** (`very-low`) | Conflicting, imprecise, high-bias evidence, or effects eliminated in stronger causal/ablation designs. | *"remains unclear"*, *"evidence is conflicting"*, *"no reliable effect persists after controlling for..."* | Citing the finding as positive support for any mechanism or recommendation. |

---

## IV. Voice & Forbidden Phrasing

All chapters across both series are audited by [`scripts/audit_manuscript.py`](scripts/audit_manuscript.py) and `.agents/hooks/post_edit_guard.py` against:
- [`style/forbidden-phrases.md`](style/forbidden-phrases.md): Bans deterministic clichés (*"hardwired"*, *"toxic stress ruins"*, *"AI remembers/hallucinates like a human"*), vague intensifiers, and uncalibrated certainty.
- [`style/voice-checklist.md`](style/voice-checklist.md): Enforces calm, investigative, anti-deterministic prose.
- Series-specific bibles:
  - [`series/architectures-of-memory/series-bible.md`](series/architectures-of-memory/series-bible.md) & [`series/architectures-of-memory/characters.md`](series/architectures-of-memory/characters.md)
  - [`series/parenthood-atlas/COMPOSITION.md`](series/parenthood-atlas/COMPOSITION.md) & [`series/parenthood-atlas/style/anomaly-bank.md`](series/parenthood-atlas/style/anomaly-bank.md)
