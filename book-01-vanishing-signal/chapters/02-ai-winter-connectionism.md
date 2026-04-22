# Chapter 2 — The First AI Winter: Why Connectionism Failed and What Was Lost

*Sources: research note `research/notes/ch02-ai-winter-connectionism.md`; Minsky & Papert (1969); Lighthill (1973); characters — Minsky, Papert.*

---

## The winter that was not only weather

Histories of artificial intelligence like tidy seasons: a spring of ideas, a winter of funding, another spring. The metaphor is imperfect—work continued in rooms the headlines never visited—but the **first** AI winter of the mid-1970s did freeze whole laboratories. It did so for reasons that were at once **mathematical**, **political**, and **narrative**. This chapter keeps all three in frame, because connectionism’s decline was never a single cause.

If Chapter 1 introduced optimism’s megaphone, this chapter introduces the institutions that decide which promises count as **actionable**. The vanishing signal here is not yet the gradient across depth; it is the **credibility signal**—the confidence that a line of research will repay its keep. When that signal drops, money moves, careers pivot, and the field’s memory of what “counted” is rewritten.

---

## Technical lens — What *Perceptrons* proved—and what it did not

Marvin Minsky and Seymour Papert’s *Perceptrons: An Introduction to Computational Geometry* appeared from MIT Press in **1969**.[^perceptrons] Its central technical result is easy to state and easy to misread: a single-layer linear threshold network with **restricted locality** cannot compute certain predicates—**XOR** is the classroom example—because no single linear boundary separates the inputs. The authors formalized the limitation as a theorem, not a hunch.

The critical nuance—too often lost in reception—is that the book’s famous impossibility results target **particular architectures**, not “all possible neural networks.” Minsky and Papert acknowledged that multilayer networks could, in principle, compute what a single layer cannot; what was missing in 1969 was a **reliable training procedure** for those hidden layers. In other words: the proof bit, but the **engineering bridge** had not been built.

Historians such as Mikel Olazaran have argued that the book’s framing—“parallelism of *local* information”—shaped what reviewers and funders took neural nets to be **about**, sometimes over-tightening the collar.[^olazaran] Later writers, including figures in the PDP revival, claimed the critique was read as a blanket condemnation. Minsky disputed that reading. The honest story is contested. What is not contested is that **symbolic AI** offered, in the 1970s, a competing story that was easier to audit: rules you could print, traces you could step through, demos that looked like intelligence to a committee.

---

## Organizational lens — Lighthill and the combinatorial explosion

In **1973**, Sir James Lighthill—Cambridge’s Lucasian Professor—delivered a general survey of artificial intelligence to the British Science Research Council.[^lighthill] The report’s memorable move was tripartite: **Category A** (automation and robotics), **Category B** (“central” AI: pattern recognition, problem solving), **Category C** (nervous-system simulation). Lighthill’s skepticism concentrated on Category B, where ambitious claims had met the **combinatorial explosion**—search spaces that grow faster than hardware and wit.

The SRC **cut** AI funding sharply; British labs closed or shrank; researchers emigrated. The report did not single-handedly invent doubt—American agencies were already wary—but it **amplified** a narrative of overreach. By **1974**, DARPA’s posture toward open-ended AI had chilled; money flowed toward projects that could show near-term utility.[^darpa-open]

From the standpoint of **institutional memory**, the Lighthill moment is almost too neat: one commissioned document, a funding shock, a transatlantic echo. Real institutions are messier. Still, the pattern is familiar: when evaluation horizons shorten, **long-horizon** methods—those that need years of tinkering before they “work”—lose share of voice. Connectionism, lacking backprop in practice, looked like Category B’s risky cousin.

The **ALPAC** report on machine translation (**1966**) had already bruised confidence in language automation; MT was slower, pricier, and less accurate than human translators for many tasks.[^alpac-open] By the time Lighthill wrote, “AI winter” was not a metaphor waiting to happen. It was a **mood** with receipts.

---

## Philosophical lens — What counts as refutation?

A theorem refutes a **claim**. It does not, by itself, refute a **research programme**—unless the community **decides** the programme is defined narrowly enough that the theorem is fatal. The sociology of the 1970s made that decision, at least temporarily, against connectionism in many funding rooms.

This raises a philosophical question the series will revisit: **who bears the burden of persistence?** If an idea is correct-but-premature—multilayer learning before backprop—does the field owe it continuity, or is it acceptable for institutional attention to wander? There is no innocent answer. Letting attention wander **erases** tacit skill; keeping every thread alive **dissipates** resources. Winter is not only cruelty. It is also a **budget**.

---

## The underground stream

Connectionism did not vanish. James Anderson’s brain-state-in-a-box work (**1977**), Teuvo Kohonen’s self-organizing maps, Shun-Ichi Amari in Tokyo—small groups kept the lamps lit.[^note-underground] The chapter’s organizational mirror is straightforward: **resilience without budget** is heroic and fragile. Knowledge survived in people and in marginal venues, not in the center of the symbolic-AI parade.

That matters for Book 1’s arc. The “spring” of the 1980s did not spring from nowhere. It sprang from a **latent state** maintained at the periphery—the same structural situation, in kind, as an RNN holding a hidden vector while the output looks idle.

---

## Notes

[^perceptrons]: M. Minsky and S. Papert, *Perceptrons: An Introduction to Computational Geometry* (Cambridge, MA: MIT Press, 1969). Summary and XOR/locality nuance: research note § 1.

[^olazaran]: M. Olazaran’s sociological reading cited in research note § 1; interpretive debate with Minsky noted there.

[^lighthill]: J. Lighthill, *Artificial Intelligence: A General Survey* (1973). SRC impact: research note § 2.

[^darpa-open]: DARPA **1974** redirection—program name and primary document **open** per research note open questions.

[^alpac-open]: ALPAC (**1966**) recommendation nuance (suspend vs. redirect) **open** per research note.

[^note-underground]: Underground stream: Anderson, Kohonen, Amari; research note § 3.
