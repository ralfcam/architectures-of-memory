# Chapter 4 — Sequence as the Unsolved Problem: Language, Time, and Order

*Sources: research note `research/notes/ch04-sequence-time-order.md`; Jordan (1986 tech report); Elman (1990); Rumelhart, Hinton & Williams (1986) on BPTT; Hochreiter (1991 thesis); characters — Hochreiter (preview).*

---

## Why order is not “just more inputs”

After backpropagation made hidden layers trainable, the obvious next move was **time**. Speech, motor plans, sentences, and sensor streams are not bags of features—they are **ordered trajectories** where the same symbol means something different depending on what preceded it. The connectionist programme of the late 1980s attacked that problem with recurrent networks: machines that carry a **state** forward step by step, updating it as new input arrives.

This chapter tracks two architectures—**Jordan**’s and **Elman**’s—and the training procedure that made recurrence learnable in principle: **backpropagation through time** (BPTT), which unrolls a recurrent network across ticks into a deep feedforward structure and applies the same chain rule that Chapter 3 celebrated.[^bptt]

The triumph is real. So is the trap. By **1991**, Sepp Hochreiter’s diploma thesis at TU Munich would show that gradients across many time steps **vanish or explode**—not because programmers were careless, but because of multiplicative structure along unrolled depth.[^hochreiter1991] That proof is Book 1’s technical heart; here we meet the **problem statement** the proof will close.

If Chapter 3 introduced **gradient as debt** across layers, this chapter introduces the same metaphor **across time**: each timestep is another link in the chain of obligation. Past inputs lay claim on present error; the chain grows long; the bill must travel backward through every link. Some debts are paid in full; others dissipate before they reach the borrower who incurred them.

---

## Technical lens — From Jordan’s echo to Elman’s hidden memory

Michael I. Jordan’s **1986** UC San Diego technical report proposed a recurrent network for serial order in which **output** units feed **context** units, which are reinjected into the hidden layer at the next step.[^jordan1986] A crucial detail for our narrative: the context weights were **fixed**—the machine remembered its past outputs through a hard-coded fading window, not through learned credit assignment along the memory path.

Picture an organization that circulates **minutes** of last quarter’s decisions but never revises how those minutes are weighted. The past is present, but **frozen**—an echo, not a living interpretation.

Jeffrey Elman’s **1990** *Cognitive Science* paper, “Finding Structure in Time,” changed the attachment point: context units copy the **hidden** activations, not the outputs.[^elman1990] Hidden states are richer; they are already shaped by the task. Feeding them back makes memory **constitutive** of ongoing computation rather than a transcript of outward behavior. Elman showed—on long sequences and on miniature languages—that error patterns track temporal structure and that grammatical categories can emerge in hidden geometry without explicit symbol tables.

The move from Jordan to Elman is small on a wiring diagram and large in **theory of mind**: it is the difference between archiving outcomes and archiving **the internal deliberation that produced them**.

Open technical detail: textbooks disagree on whether Elman’s earliest specification trained every recurrence weight; the distinction matters for how we narrate “learned vs. hard-coded” memory.[^elman-weights-open]

---

## Organizational lens — BPTT and the decay chain

BPTT is the workhorse that trains recurrent nets: unroll, differentiate, step backward. It aligns beautifully with organizational fantasies of **after-action review**: outcomes generate error signals; the signals propagate to earlier decisions; policies update.

Hochreiter’s thesis interrupted the fantasy. When the unrolled network is long, Jacobian products along the trajectory either shrink toward zero (**vanishing**) or grow without bound (**exploding**). In the vanishing case, early timesteps learn almost nothing about the loss—exactly the organizational failure mode where a frontline decision from last year cannot be **charged** to this quarter’s outcome because too many layers of reporting attenuated the signal.

This isomorphism is not decorative. Institutions call it “accountability drift”; networks call it “gradient decay.” The mathematics gives the phenomenon a **scale**: dependencies beyond roughly ten to fifteen timesteps become effectively invisible to standard training—an order-of-magnitude handle historians rarely get.

---

## Philosophical lens — Syntax, statistics, and two cultures

The late-1980s **past-tense debate**—Rumelhart and McClelland’s feedforward model of English inflection versus Pinker and Prince’s symbolic critique—was partly about verbs and partly about **what linguistic knowledge is**.[^past-tense] Elman’s recurrent models escalated the stakes: if sequential structure lives in hidden dynamics, then grammar begins to look like **geometry in time**, not like a detachable rule engine.

Meanwhile mainstream NLP began to pivot toward **n-gram** statistical models that scaled without depth-in-time—at the cost of abandoning explicit structure. The field **forked**: cognitive modellers ran SRNs on theory-friendly corpora; industry pipelines chased perplexity with Markov assumptions. Two communities, two memories of what “worked,” two publication venues—a recipe for the kind of partial forgetting institutions specialize in.

---

## The cliff

By the early 1990s, the sequence problem had a name and a **theorem-shaped** obstacle. The field knew recurrent networks could represent rich temporal patterns; it also knew standard training could not reliably **reach** long-range dependencies. The resolution—gated memory, constant error carousel—belongs to Book 2’s engineering story. Book 1 ends this movement on a question, not a gadget: **what does it mean to live in time** when your learning signal cannot survive the journey backward?

---

## Notes

[^bptt]: BPTT described with Rumelhart, Hinton & Williams (1986); research note § 3.

[^hochreiter1991]: S. Hochreiter, *Untersuchungen zu dynamischen neuronalen Netzen* (Diplom thesis, TU Munich, 1991); summary via Schmidhuber secondary discussions in research note.

[^jordan1986]: M. I. Jordan, *Serial Order: A Parallel, Distributed Processing Approach*, ICS Report 8604 (UC San Diego, 1986). Canonical title/archival detail **open** per research note.

[^elman1990]: J. L. Elman, “Finding Structure in Time,” *Cognitive Science* 14 (1990): 179–211.

[^elman-weights-open]: Trainability of context-to-hidden weights in original SRN—**open** per research note.

[^past-tense]: Past-tense debate: Rumelhart & McClelland in PDP vol. 2; Pinker & Prince (1988); research note § 4.
