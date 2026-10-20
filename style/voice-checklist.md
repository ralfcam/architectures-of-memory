# Voice Checklist (Pre-Commit & Pre-PR Review)

Before committing any chapter draft across *Architectures of Memory* or *Parenthood: The Atlas*, verify:

## 1. Calm & Non-Sensational
- [ ] No urgency or hype markers (*"revolutionary breakthrough"*, *"critical window closing"*, *"changes everything"*).
- [ ] No alarmism (*"ruins"*, *"destroys"*, *"irreversibly harms"*).
- [ ] No optimization-culture or self-help prescriptions (*"you should"*, *"maximize your child's potential"*).

## 2. Curious & Anomaly-Driven
- [ ] Chapter opens with a concrete historical scene, engineering failure mode, or developmental anomaly—never a textbook definition.
- [ ] Language is investigative (*"we examine"*, *"this raises a structural question"*) rather than instructional.

## 3. Empirically & Mathematically Disciplined
- [ ] Every empirical or benchmark claim is backed by a verified citation in `sources.bib` / `SOURCES.md` and an OKF v0.2 card in `evidence-cards/`.
- [ ] Claim verbs match the OKF v0.2 certainty grade (*High* $\to$ **shows**; *Moderate* $\to$ **suggests**; *Low* $\to$ **is associated with**).
- [ ] No raw `vertexaisearch.cloud.google.com/grounding-api-redirect/` URLs appear anywhere in notes or prose.

## 4. Three-Lens Integrity
- [ ] **Lens 1 (Technical / Science):** Exposes the exact mechanism (mathematical derivation, system architecture, or biological/behavioral cascade).
- [ ] **Lens 2 (Organizational / Interpretation):** Connects the mechanism to interacting feedback loops (team handoffs, institutional incentives, or caregiver-child systems).
- [ ] **Lens 3 (Philosophical / Art):** Clarifies the conceptual or normative boundary without substituting philosophy for empirical evidence.

## 5. Boundary & Anti-Determinism
- [ ] Explicitly states what the evidence or theorem **does not mean** (matching the Evidence Card's `## What This Does Not Mean` section).
- [ ] Zero cross-chapter metaphor collisions (verified via `make audit`).
