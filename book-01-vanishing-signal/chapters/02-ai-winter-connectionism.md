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

Historians such as Mikel Olazaran have argued that the book’s framing—“parallelism of *local* information”—shaped what reviewers and funders took neural nets to be **about**, sometimes over-tightening the collar.[^olazaran] Later writers, including figures in the PDP revival, claimed the critique was read as a blanket condemnation. Minsky and Papert themselves addressed that 1980s backlash in the **1988 expanded edition** of *Perceptrons*—a retrospective preface, not a retraction.[^perceptrons1988] The honest story is contested. What is not contested is that **symbolic AI** offered, in the 1970s, a competing story that was easier to audit: rules you could print, traces you could step through, demos that looked like intelligence to a committee.

---

## Organizational lens — Lighthill and the combinatorial explosion

In **early 1973**, Sir James Lighthill—Cambridge’s Lucasian Professor—delivered a general survey of artificial intelligence to the British Science Research Council.[^lighthill] The report’s memorable move was tripartite: **Category A** (automation and robotics), **Category B** (“central” AI: pattern recognition, problem solving), **Category C** (nervous-system simulation). Lighthill’s skepticism concentrated on Category B, where ambitious claims had met the **combinatorial explosion**—search spaces that grow faster than hardware and wit.

The SRC **cut** AI funding sharply; British labs closed or shrank; researchers emigrated. The report did not single-handedly invent doubt—American funders were already tightening—but it **amplified** a narrative of overreach. The **Mansfield Amendments** (1969; reaffirmed 1973) required DARPA-funded work—including projects under **IPTO**, the Information Processing Techniques Office—to demonstrate direct military relevance. Open-ended “basic” AI lost room to maneuver. IPTO budgets fell in **constant dollars** from **1970** through **1976**; historians often shorthand the squeeze around **1974**, but the mechanism was legislative and cumulative, not a single cancellation memo.[^mansfield]

From the standpoint of **institutional memory**, the Lighthill moment is almost too neat: one commissioned document, a funding shock, a transatlantic echo. Real institutions are messier. Still, the pattern is familiar: when evaluation horizons shorten, **long-horizon** methods—those that need years of tinkering before they “work”—lose share of voice. Connectionism, lacking backprop in practice, looked like Category B’s risky cousin.

The **ALPAC** report (*Languages and Machines: Computers in Translation and Linguistics*, National Academy of Sciences / National Research Council, **November 1966**) framed its recommendations as **redirecting** resources toward basic computational linguistics; in practice, substantial US machine-translation funding **ended** for roughly twenty years—an operational freeze historians describe as the near-total suspension of the field.[^alpac] By the time Lighthill wrote, “AI winter” was not a metaphor waiting to happen. It was a **mood** with receipts.

---

## Philosophical lens — What counts as refutation?

A theorem refutes a **claim**. It does not, by itself, refute a **research programme**—unless the community **decides** the programme is defined narrowly enough that the theorem is fatal. The sociology of the 1970s made that decision, at least temporarily, against connectionism in many funding rooms.

This raises a philosophical question the series will revisit: **who bears the burden of persistence?** If an idea is correct-but-premature—multilayer learning before backprop—does the field owe it continuity, or is it acceptable for institutional attention to wander? There is no innocent answer. Letting attention wander **erases** tacit skill; keeping every thread alive **dissipates** resources. Winter is not only cruelty. It is also a **budget**.

---

## The underground stream

Connectionism did not vanish. In Britain, the deep cut lasted roughly **1973–1983**—until the **Alvey** programme, partly a response to Japan’s Fifth Generation initiative, put government money back into AI at scale; **Edinburgh, Essex, and Sussex** were among the universities where work survived the worst of the contraction. James Anderson’s brain-state-in-a-box work (**1977**), Teuvo Kohonen’s self-organizing maps, Shun-Ichi Amari in Tokyo—small groups kept the lamps lit.[^note-underground] The chapter’s organizational mirror is straightforward: **resilience without budget** is heroic and fragile. Knowledge survived in people and in marginal venues, not in the center of the symbolic-AI parade.

That matters for Book 1’s arc. The “spring” of the 1980s did not spring from nowhere. It sprang from a **latent state** maintained at the periphery—the same structural situation, in kind, as an RNN holding a hidden vector while the output looks idle.

---

## Notes

[^perceptrons]: M. Minsky and S. Papert, *Perceptrons: An Introduction to Computational Geometry* (Cambridge, MA: MIT Press, 1969). Summary and XOR/locality nuance: research note § 1.

[^olazaran]: M. Olazaran’s sociological reading cited in research note § 1; interpretive debate with Minsky noted there.

[^lighthill]: J. Lighthill, *Artificial Intelligence: A General Survey*, Science Research Council, early 1973. SRC impact: research note § 2; research/fact-checks/ch02.md (ARC-19).

[^mansfield]: Mansfield Amendments (1969; 1973); DARPA **IPTO** budget trajectory 1970–1976; no single cancellation document—see research/fact-checks/ch02.md (ARC-19).

[^alpac]: Automatic Language Processing Advisory Committee (ALPAC), *Languages and Machines: Computers in Translation and Linguistics* (Washington, D.C.: National Academy of Sciences / National Research Council, November 1966). Operational outcome on US MT funding: W. J. Hutchins, “ALPAC: The (in)famous report,” in *Machine Translation* (1996), via ACL Anthology—summarized in research/fact-checks/ch02.md (ARC-19).

[^perceptrons1988]: M. Minsky and S. Papert, *Perceptrons: An Introduction to Computational Geometry*, expanded ed. (Cambridge, MA: MIT Press, 1988)—authors’ response to 1980s criticism in the new preface; no formal retraction.

[^note-underground]: Underground stream: Anderson, Kohonen, Amari; UK survival universities and Alvey revival: research/fact-checks/ch02.md (ARC-19); research note § 3.
