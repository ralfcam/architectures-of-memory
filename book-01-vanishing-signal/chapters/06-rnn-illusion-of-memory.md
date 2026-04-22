# Chapter 6 — Recurrent Networks and the Illusion of Memory

*Sources: research note `research/notes/ch06-rnn-illusion-of-memory.md`; Jordan (1986, ICS 8604); Elman (1989 report, 1990 *Cognitive Science*); Werbos (1974, 1990); Rumelhart, Hinton, and Williams (1985/1986); Bengio, Simard, and Frasconi (1994); research/fact-checks/ch04.md, ch06.md (ARC-20, ARC-26).*

---

## One step back, forever

A recurrent network is supposed to *remember* something about what just happened. In Jeffrey Elman’s “simple recurrent” design—presented in a UC San Diego Center for Research in Language report in **1989** and, more famously, in *Cognitive Science* in **1990**—a vector of **context** units receives a *copy* of the previous time step’s **hidden** activations (fixed copy weights of 1.0) while the **context-to-hidden** weights are *learned* by gradient descent (Elman’s figure marks copy links as non-trainable and the rest as learnable).[^elman1990] The machine therefore carries, at each tick, a compressed trace of the step before.

That is a faithful mirror of many institutions: a standing meeting, a stand-up, a “last week in review.” They retain **yesterday’s state**; they are not, by that mechanism alone, a durable archive of *why* a decision in the prior fiscal year was made. The architecture has **one step of explicit recurrence**; everything older must be folded into what that single lagged vector can still represent. When the *gradient* to early time steps is driven toward zero, that limitation stops being a metaphor and starts being **algebra**.

---

## Technical lens — Jordan, Elman, and backprop through time

**Michael I. Jordan**’s **May 1986** technical report, *Serial Order* (ICS Report 8604), gave recurrent nets a “plan and action” feel: part of the state loop runs through **output** units into **context** units, reinjecting a trace of the *product* of the system—what the network just *said* or *did*—on the next step.[^jordan1986] For our purposes the pivot is the *function* of the loop, not a prize fight between authors: Jordan’s emphasis fits **serial production** (plan-shaped memory); Elman’s shift to *hidden* feedback fits **perception and prediction** (state-shaped memory), as the field later narrated it. Both still train with the same time-unfolded object.

**Backpropagation through time (BPTT)** is how those loops learn. The recurrent system is **unrolled** for *T* steps into a feedforward graph with *T* *temporal* layers that **share** weights. The error at the end is pushed backward through *all* *T* slices; gradients from all times are summed into one update for each shared weight. The algorithm’s intellectual spread matches backprop’s own scatter plot: **Paul J. Werbos** described BPTT in his 1974 Harvard thesis (Chapter 5) and in a 1990 *Proceedings of the IEEE* tutorial; the PDP group’s 1985–**1986** account is the version a generation of cognitive scientists *read* first, even when the *priority* of the idea belonged to Werbos.[^bptt]

**The illusion:** An Elman network *running* on a long sequence is not the same object as the same network *learning* a dependency that must survive fifty steps. **Yoshua Bengio**, **Patrice Simard**, and **Paolo Frasconi** (1994) do not give a single magic number of steps as “the” failure point; their analysis shows that, when a recurrent net must *hold* information across a long span *T* while the loss is computed late in the run, the **magnitude of the gradient** with respect to an early time step is driven by a **product** of local Jacobians along the unrolled path—*and that product can shrink exponentially* as *T* grows, making the credit signal to the earliest part of the sequence vanish in effect. The practical horizon people quote from *secondary* sources (rough order-of-magnitude “short windows”) is not a substitute for the paper’s **formal** claim.[^bengio1994]

**Sound bite for the next chapter:** The network’s activations *look* like history; the gradient, under standard training, *may not* reach that history. Memory as **observed behavior** and memory as **trainable by local descent** are two different propositions. That gap is what Chapter 7 names as a **proof**.

---

## Organizational lens — The retrospective you never unroll

BPTT is, procedurally, the closest thing in optimization to a **serious** after-action: you cannot assign blame at day *T* to an event at day 1 without laying the **whole** timeline flat and *differentiating* *through* it. Firms that run only a forward pass—KPIs up, KRs green—*feel* as if they are learning; the backward pass, when it is missing, is not a mood problem. It is a *missing algorithm*.

Two stylised failure modes echo the **Jordan/Elman** split in a mild form: **plan-anchored** institutions forget the *ground truth* in front of them; **state-anchored** ones forget the *objective* they once declared. Either half alone is an honest human mistake; the point is that **gated**, selective retention—the topic of a later book—is not yet in the design.

---

## Philosophical lens — When “history” is not legible to learning

A historian might say: we have the documents; the memory is *there*. A trainer of an RNN must answer a harder sub-question: is the *process that updates* the system sensitive to the far past, or not? A century of narrative theory would call that the difference between the **continuity of a story** and the **sensitivity of a dynamics**. Elman’s nets wrote beautiful stories; Bengio, Simard, and Frasconi showed how stiff the *dynamics* could be.

---

## The cliff

We have, at last, a machine that *carries* a state, and a training rule that, in principle, **flows credit backward in time**—**and** a growing body of analysis that those flows need not *arrive* at the beginning of a long run. The next move is not to blame engineers for bad luck; it is to read a **diagnostic document** that made the “vanishing or exploding” reading *inescapable* for anyone who would look at the Jacobian straight on.

---

## Notes

[^jordan1986]: M. I. Jordan, *Serial Order: A Parallel, Distributed Processing Approach*, ICS Report 8604, Institute for Cognitive Science, University of California, San Diego, May 1986. research/fact-checks/ch04.md (ARC-20); ch06.md (ARC-26) — rely on 1986; do **not** cite an unverified “Jordan 1997 *Artificial Intelligence*” paper.

[^elman1990]: J. L. Elman, “Representation and structure in connectionist models,” CRL Technical Report 8903, Center for Research in Language, UC San Diego, 1989; J. L. Elman, “Finding Structure in Time,” *Cognitive Science* 14, no. 2 (1990): 179–211. Same architecture, journal article definitive (ARC-26).

[^bptt]: P. J. Werbos, *Beyond Regression* (Ph.D. diss., Harvard, 1974), Ch. 5; P. J. Werbos, “Backpropagation through time: what it does and how to do it,” *Proceedings of the IEEE* 78, no. 10 (1990); D. E. Rumelhart, G. E. Hinton, R. J. Williams, 1985–86 as in ch04. See research/fact-checks/ch06.md.

[^bengio1994]: Y. Bengio, P. Simard, P. Frasconi, “Learning Long-Term Dependencies with Gradient Descent Is Difficult,” *IEEE Transactions on Neural Networks* 5, no. 2 (1994): 157–166, DOI 10.1109/72.279181. The paper **proves** difficulty growing with dependency span and the **latch** construction varies *T* relative to a fixed *L*—it does **not** state a single universal “5–10 step” constant as the *paper’s* main finding (ch06, ch08 fact-checks). PDF mirrors linked in ch08.
