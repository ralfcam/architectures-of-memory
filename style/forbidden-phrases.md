# Forbidden Phrases (Multi-Series Living List)

These phrases violate the compositional grammar of both series (*Architectures of Memory* and *Parenthood: The Atlas*). [`scripts/audit_manuscript.py`](../scripts/audit_manuscript.py) checks chapter drafts against this list.

## Universal Epistemic & Instructional Violations
- `"you should"` / `"you must"` (instructional/self-help tone; exempted only inside direct historical quotations)
- `"science says"` / `"studies prove that"` (conflates empirical findings with unconditional interpretation)
- `"irreversibly harms"` / `"ruins"` / `"destroys"` (alarmism, determinism)

## Series 1 (*Architectures of Memory*) — Anti-Anthropomorphism & Anti-Hype
- `"the network thinks"` / `"the model believes"` / `"the AI wants"` (anthropomorphic projection onto matrix operations)
- `"just like the human brain"` / `"mirrors human neurons"` (ungrounded biological conflation)
- `"solved memory forever"` / `"infinite memory"` (breathless technical hype)
- `"hallucinates"` without mechanistic qualification (use distribution/retrieval failure terminology when describing mechanism)

## Series 2 (*Parenthood: The Atlas*) — Anti-Determinism & Anti-Optimization
- `"optimal"` / `"optimize"` (when applied to parenting or child development; allowed only in mathematical optimization contexts in Series 1)
- `"perfect child"` / `"ideal child"` (manufacturing narrative)
- `"brain-based proof that"` (neuroscience sensationalism)
- `"evolutionarily designed to"` (evolutionary storytelling detached from evidence)
- `"critical window"` (unless evidence grade is High and persistence is demonstrated)
- `"parental fate"` / `"developmental destiny"` (determinism)

## Revision Protocol
If a forbidden phrase appears, revise to:
1. Calibrate claim strength to the underlying OKF v0.2 Evidence Card grade (*shows* / *suggests* / *is associated with*).
2. Replace anthropomorphic or deterministic labels with concrete mechanisms (gradients, state transitions, dyadic feedback loops).
3. Return to the concrete human or engineering case.
