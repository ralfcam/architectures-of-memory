# Contributing / Research Standards

This repository follows a strict evidence-evaluation methodology. Any new or revised evidence card must adhere to the following.

## Evidence Card Format

Every major claim gets a card in `evidence-cards/` with these sections:

1. **What We Know** — the strongest supported conclusion, 1–2 sentences.
2. **How Confident We Are** — High / Moderate / Low / Very Low, with justification.
3. **Evidence and Causal Assessment** — key studies/syntheses, design types, replication, causal limitations.
4. **Effect Size and Persistence** — absolute/standardized effects, CIs where available, practical magnitude, time horizon.
5. **Bias, Heterogeneity, and Confounding** — alternative explanations, subgroup variation, attenuation in genetically informed designs.
6. **What Remains Uncertain** — decision-relevant unresolved questions.
7. **What This Does Not Mean** — explicitly prohibited overreach or deterministic interpretation.
8. **What Action Is Reasonably Justified** — proportionate guidance, or a statement that no action follows.

Keep cards to 200–400 words unless deeper analysis is explicitly warranted.

## Identification Strength

Prioritize causal triangulation using, where relevant:

- Randomized trials and intervention studies
- Natural experiments and instrumental variables
- Mendelian randomization
- Adoption, IVF cross-fostering, sibling, and children-of-twins designs
- Longitudinal cohorts
- Cross-sectional studies
- Mechanistic evidence

No design automatically establishes truth. Assess each design's assumptions, precision, replication, and fit to the claim.

## Certainty Grades

- **High** — independent experimental or genetically informed replication; consistent, precise, low-bias evidence.
- **Moderate** — multiple studies and partial replication, but meaningful limitations.
- **Low** — primarily observational or limited evidence; substantial uncertainty.
- **Very Low** — conflicting, imprecise, high-bias evidence, or effects eliminated in stronger causal designs.

## Causal and Bias Rules

- When adoption, IVF, sibling, or related genetically informed designs substantially attenuate an observational association, treat confounding as the default explanation unless competing evidence is compelling.
- Report attenuation from observational to controlled estimates when possible: largely confounded (>50%), partially confounded (20–50%), robust (<20%).
- Audit genetic confounding, selection/attrition, publication bias, measurement bias, and translation bias.
- Treat causal conflicts between observational and genetically informed evidence as findings to explain, not discrepancies to hide.
- Report variation by socioeconomic conditions, family structure, cultural context, baseline risk, and child characteristics where evidence permits.
- Assess child-to-parent, parent-to-child, and transactional effects. Parents are not static exposures.

## Topic-Specific Rules

**Screens**: Do not treat "screen time" as a unitary exposure. Decompose duration, content, context, co-use, purpose, timing, and displacement. Classify measurement as parent report, device logs, ecological momentary assessment, or content coding. Parent-reported total duration alone is weak causal evidence.

**Interventions**: Separate efficacy, real-world effectiveness, scalability, and institutional dependence. Identify plausible active ingredients. Do not attribute effects to "parenting" when material support, service quality, implementation fidelity, or broader systems may explain them.

## Versioning

Every substantive addition or revision to an evidence card must be logged in `CHANGELOG.md` under `[Unreleased]`, categorized as Added / Revised / Retracted / Structure. Periodically these are rolled into a dated or tagged release (see `preliminary/releases/v0.1-slice.md`).

## Compositional Grammar

This KB feeds a book, `Parenthood: The Atlas`, governed by a compositional grammar in `COMPOSITION.md`. When adding or revising evidence cards:

- If a card is intended to anchor a chapter, include `atlas_domains` (e.g., `[attachment, regulation]`) and `chapter_hooks` (e.g., `[anomaly, boundary, mechanism]`) in its OKF frontmatter.
- Chapter drafts must pass the `style/voice-checklist.md` review before being considered for inclusion in a release.
- See `COMPOSITION.md` Appendix A for how to translate certainty grades into prose strength.
