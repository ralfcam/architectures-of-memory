# book-01-vanishing-signal — Full manuscript

Compiled from `book-01-vanishing-signal/chapters/*.md` in sorted filename order (2026-04-22).

**Footnotes:** Each chapter defines reference-style footnotes locally. Some labels repeat across chapters; in one file, renderers may attach one definition to every use of a label.

---

# Chapter 1 — Rosenblatt's Perceptron and the Dream of Learning Machines

*Sources: research note `research/notes/ch01-rosenblatt-perceptron.md`; Rosenblatt (1958); characters — Rosenblatt.*

---

## A machine that learns to see

In January 1957, Cornell Aeronautical Laboratory circulated *The Perceptron: A Perceiving and Recognizing Automaton (Project PARA)*—Technical Report 85-460-1—Frank Rosenblatt’s first formal write-up of the architecture, predating the canonical journal article by nearly two years.[^tr1957] In November 1958, the *Psychological Review* published a paper that sounds, to modern ears, almost modest. Rosenblatt, a research psychologist at the same laboratory in Buffalo, described a **probabilistic model** for how information might be stored—not as discrete symbols in fixed addresses, but as strengths on connections between simple units.[^rosenblatt1958] The perceptron was not yet a cultural icon. It was an argument about **where knowledge lives**.

Rosenblatt took an explicitly connectionist position: storage is **distributed** across weights, not localized into coded images. That stance placed him athwart the symbolic programme that dominated much of mid-century artificial intelligence. The first simulations ran on an **IBM 704** at the same laboratory—slow, expensive, and enough to prove that the idea could move from speculation to running code.

Two years later, on **23 June 1960**, the laboratory demonstrated something no journal page could fully convey: the **Mark I Perceptron**, a physical machine funded by the Office of Naval Research and the Rome Air Development Center. Four hundred photocells in a **20×20** grid stood in for a retina; 512 association units and eight response units completed a three-layer stack. Rosenblatt insisted on **random** wiring from sensory to association layers, modelling his belief that biology does not hand you a neat grid.[^mark1] The device now sits in the Smithsonian—a relic of the moment when “learning machine” meant hardware you could photograph.

This chapter begins with that optimism because the rest of Book 1 is built on what optimism **cannot** guarantee. The perceptron really learned—within the limits its mathematics allowed. The public story often outran those limits. The gap between the two is the first taste of a pattern that will recur: **the signal that fails to arrive** where it is needed, whether in a network, an organization, or a life cut short.

---

## Technical lens — What the perceptron was

Without turning this into a textbook derivation: a perceptron computes a weighted sum of inputs, thresholds it, and updates weights when it is wrong. The learning rule is local—each weight changes in proportion to its contribution to the error. That locality was philosophically important to Rosenblatt: it suggested a path from biology to mechanism without importing a homunculus “executive” that already knows the answer.

The 1958 paper is the canonical citation; it is also the place where Rosenblatt framed the perceptron as a theory of **information storage and organization in the brain**, not merely a curve-fitting trick.[^rosenblatt1958] Historians can disagree about how close the model is to real neurons; what matters for our arc is that the field **treated** it as a serious hypothesis about representation. If knowledge is in the weights, then training is a form of memory formation—plasticity made executable.

The Mark I made the same point in steel and light. The architecture—S-units, A-units, R-units—was an **alpha-perceptron**: enough structure to be impressive, enough constraint that the mathematics could speak clearly. A later classified deployment at the National Photographic Interpretation Center (1963–1966) reminds us that these dreams were never purely academic. The military imagination and the psychologist’s model travelled together.

---

## Organizational lens — Promises that travel faster than proofs

Research funding proposals are rarely shy. The 1957 “Cornell Photoperceptron” proposal already envisioned devices that might one day tackle concept formation, translation, and inductive logic.[^proposal-open] Whether those sentences were sober forecasts or fundraising rhetoric, they **set a horizon** against which later disappointments would be measured.

At a **1958 Navy press conference**, the story widened. *The New York Times* reported an “embryo” machine the Navy expected would someday “walk, talk, see, write, reproduce itself and be conscious of its existence.”[^nyt1958] Rosenblatt himself called it “the first machine which is capable of having an original idea.” The quotes are famous; what matters structurally is that they **compress** decades of uncertainty into a headline. Institutions—newspapers, funding agencies, rival labs—do not wait for page proofs. They act on the version of the idea that fits their timetable.

Think of **attention as valuation**: a funding line, a newsroom, a committee cannot weigh everything at infinite depth. They allocate scarce notice to a few salient claims. Once the perceptron became salient, the **valuation** stuck faster than the mathematical caveats. That is not unique to AI. It is how organizational memory forms around **narratives** before it forms around **derivations**—and how later corrections must fight the earlier story for bandwidth.

---

## Philosophical lens — Original ideas and their debts

What would it mean for a machine to have an “original idea”? Rosenblatt’s phrase was a provocation, not a definition. Philosophers of mind might ask whether novelty requires intentionality, whether a statistical update counts as thought, whether “original” implies accountability. This book will not settle those questions. It **inherits** them—as unresolved pressure on every later architecture that claims to learn.

There is a quieter philosophical fact under the hype: **distributed storage** challenges a picture of memory as a vault of discrete records. If knowledge is smeared across weights, then forgetting, bias, and drift are not accidents—they are properties of the medium. The perceptron era did not yet have the vocabulary of vanishing gradients and gates; it already had the experience of **memory as transformation**. Each update rewrote the machine’s past in small ways. Sound familiar?

---

## Coda — Death before the spring

Rosenblatt was born in New York in **1928**, earned his Cornell Ph.D. in **1956**, and died in **1971** in a boating accident on the Chesapeake—before backpropagation’s revival, before the LSTM, before the Transformer.[^bio] The historiographical question is not whether connectionism “won” later; it is what voice he would have brought to the argument had he lived to see it.

The interaction between the publicity he helped generate and the structural critique that **Minsky and Papert** would publish in *Perceptrons* (1969) is the hinge to Chapter 2. The proof there is about **linear separability** and restricted architectures—not about “all neural networks forever.” The reception, as we will see, often treated it as a broader verdict. That mismatch—between what a theorem **secures** and what a field **remembers**—is itself a vanishing signal. The mathematics arrived; the nuance did not always survive the journey.

---

## Notes

[^rosenblatt1958]: F. Rosenblatt, “The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain,” *Psychological Review* 65, no. 6 (November 1958): 386–408. See research note § Query 1.

[^tr1957]: F. Rosenblatt, *The Perceptron: A Perceiving and Recognizing Automaton (Project PARA)*, Technical Report 85-460-1, Cornell Aeronautical Laboratory, January 1957. See research/fact-checks/ch01.md (ARC-17).

[^mark1]: Mark I architecture and 23 June 1960 demonstration: research note § Query 2; funding ONR + Rome Air Development Center; Smithsonian NMAH.

[^proposal-open]: Scope quotation transmitted via the Mark I Perceptron Wikipedia article; OAPEN secondary literature confirms ONR funding from July 1957; Smithsonian NMAH object record confirms dual ONR and Rome Air Development Center funding on the hardware. **Primary** proposal document not located in open archives—see research/fact-checks/ch01.md (ARC-17).

[^nyt1958]: “New Navy Device Learns by Doing,” *The New York Times*, July 8, 1958, p. 25 (Navy press conference; Rosenblatt quoted). See research/fact-checks/ch01.md (ARC-17).

[^bio]: Biographical dates and Cornell positions: research note § Query 4.

---

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

---

# Chapter 3 — The Return: Rumelhart, Hinton, and Backpropagation (1986)

*Sources: research note `research/notes/ch03-backprop-1986.md`; Rumelhart, Hinton & Williams (1986); PDP volumes (1986); Werbos (1974); characters — Rumelhart, Hinton, Werbos.*

---

## Four pages in *Nature*

On **9 October 1986**, *Nature* published a four-page paper titled “Learning representations by back-propagating errors.”[^nature1986] David Rumelhart, Geoffrey Hinton, and Ronald Williams showed how to adjust the weights in a network with **hidden layers** so that internal units could develop task-relevant features—not because a programmer placed them there, but because error signals **flowed backward** through the architecture, allocating credit.

The algorithm’s mechanics are now textbook: compare the network’s output to a target, compute a loss, take derivatives with the chain rule, propagate gradients layer by layer. What was not textbook in 1986 was the **social fact** that multilayer training had been, for many funders and skeptics, the very thing Minsky and Papert had implied was **stuck**.

This chapter’s technical story is therefore also a story about **publication ecologies**. The result did not arrive only as mathematics. It arrived as a short, legible article in a general-science journal, adjacent to the two-volume *Parallel Distributed Processing* manifesto from MIT Press—the PDP books that made connectionism a **movement** with a bibliography you could assign to a graduate seminar.[^pdp]

---

## Technical lens — Hidden layers as memory in motion

Backpropagation is often taught as calculus. For this book, it is also **memory architecture**: the hidden layer is where the network stashes intermediate structure it cannot yet name. When gradients reach those units, the system learns which internal configurations reduce error. Without that backward pass, hidden weights are inert ornament—they cannot learn from outcomes they indirectly caused.

Rumelhart, Hinton, and Williams were explicit that their demonstration reopened questions that *Perceptrons* had framed harshly: networks with hidden units could represent **non-linearly separable** functions.[^nature1986] The engineering consequence was immediate: you could build deeper stacks in principle—**in principle** being the operative phrase Book 1 will stress again when depth and time make gradients misbehave.

For now, notice the metaphor the series calls **gradient as debt**: each layer is a station in a chain of obligation. Error at the output is a bill. Backpropagation asks every upstream weight how much it contributed to the bill. Some weights pay a large share; some pay nearly nothing. The accounting is meticulous—until, later, distance makes the accounts **vanish**.

---

## Organizational lens — Werbos and the decade-long latency

Paul Werbos’s Harvard dissertation (**August 1974**) already contained the core of backpropagation applied to neural networks—work he struggled to publish in a field that preferred different stories about neurons and objectives.[^werbos] By the time the *Nature* paper appeared, many practitioners treated Rumelhart, Hinton, and Williams as **originators**; historians now routinely credit Werbos with **priority** on the neural-network formulation, Rumelhart et al. with **institutionalization**.

This is more than a priority squabble. It is an organizational parable: **a correct error-correction signal existed**; what was missing was the routing infrastructure that could carry it to the nodes prepared to act on it. Werbos’s “latency” mirrors every organization where insight lives in a peripheral lab notebook while the center standardizes on an older paradigm.

The lineage is three genuinely **independent** derivations, not one story with photocopies: Seppo Linnainmaa’s **1970** master’s thesis gave **reverse-mode automatic differentiation** in discrete networks—priority on the chain rule, but not yet framed as learning in neural nets. Werbos (**1974**) was the first explicit **backpropagation for multi-layer nets**. Rumelhart arrived at the procedure around **1982** without, at first, knowing those antecedents; the *Nature* paper **popularized** and empirically anchored the method for the connectionist coalition. David Parker’s MIT report *Learning-Logic*, Technical Report **TR-47** (**February 1985**), pursued a parallel track.[^precursors] The honest historiography—this series will keep insisting—tracks **independent reinvention** and **differential uptake**. The version that wins is often the one embedded in a **working coalition** (PDP at UC San Diego, *Nature*’s reach, cognitive science’s appetite).

The PDP volumes themselves are organizational artefacts: **collective authorship** credited to the PDP Research Group—core contributors included, among others, Rumelhart, McClelland, Hinton, Williams, Jordan, Sejnowski, and Zipser (full roster on volume 1 preface, p. xi)—an ensemble portrait of distributed work.[^pdp] If the brain is parallel and distributed, the research group mirrored its subject—a nice symmetry and a real management challenge for credit assignment in science.

---

## Philosophical lens — Representation without homunculus

Hidden layers force a philosophical upgrade. If internal units encode features without hand-labeling, then **representation** becomes a statistical achievement, not a gift from a designer. That reopens ancient questions—Meno’s recollection, the status of rules—but in a new key: are the emergent features **concepts**, or merely correlational compressions?

The second-wave connectionist debate with symbolic AI was partly epistemological: minds as rule engines versus minds as **high-dimensional activation landscapes**.[^debate] Fairness demands acknowledging symbolic AI’s genuine successes in the 1980s—expert systems that paid salaries—while still tracing why brittle rule bases and scaling walls would later tilt the field again.

---

## Nobel shadows and structural irony

John Hopfield’s recurrent networks (**1982**) and Hinton’s Boltzmann line gave the 1980s theoretical guardrails—stability and stochastic learning—that made “neural” feel less like alchemy.[^hopfield-hinton] Four decades later, Hopfield and Hinton shared the **2024 Nobel Prize in Physics** for those foundations—retroactive validation that also poses a question: why physics claimed the story is as interesting as the award itself (a thread for another chapter).

The deeper irony—Book 1’s spine—is already visible in 1986: backpropagation **is** the backward signal that makes depth plausible, yet depth-in-time and depth-in-layer will make that same signal **attenuate**. The algorithm that fixes hidden layers seeds the mathematics that will expose **vanishing** across time. Optimism and diagnosis share a parentage.

---

## Notes

[^nature1986]: D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning representations by back-propagating errors,” *Nature* 323, no. 6088 (9 October 1986): 533–536.

[^pdp]: *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, 2 vols. (Cambridge, MA: MIT Press, 1986), eds. Rumelhart, McClelland, and the PDP Research Group. Member list: vol. 1 preface, p. xi; research/fact-checks/ch03.md (ARC-18).

[^werbos]: P. J. Werbos, *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences*, Ph.D. dissertation, Committee on Applied Mathematics, Harvard University, **August 1974** (scanned PDF often cited at gwern.net/doc/ai/nn/1974-werbos.pdf; full text republished P. J. Werbos, *The Roots of Backpropagation: From Ordered Derivatives to Neural Networks and Political Forecasting*, Wiley-IEEE Press, 1994). Reception history: research note § 3; research/fact-checks/ch03.md (ARC-18).

[^precursors]: **Linnainmaa (1970):** reverse-mode AD, not framed for neural networks—J. Schmidhuber, “Who invented backpropagation?” (2014), IDSIA. **Werbos (1974)** and **Rumelhart c. 1982** (unaware of prior work): Wikipedia *Backpropagation*; Yuxi Liu, “The backstory of backpropagation” (2023). **Parker:** D. B. Parker, *Learning-Logic: Casting the Cortex of the Human Brain in Silicon*, Technical Report TR-47, Center for Computational Research in Economics and Management Science, MIT, **February 1985**. See research/fact-checks/ch03.md (ARC-18).

[^debate]: Symbolic vs. connectionist framing: research note § 4.

[^hopfield-hinton]: Hopfield (1982), Boltzmann line—research note § 4; Nobel 2024 noted as retrospective frame, not contemporary to 1986 drafting.

---

# Chapter 4 — Sequence as the Unsolved Problem: Language, Time, and Order

*Sources: research note `research/notes/ch04-sequence-time-order.md`; Jordan (1986 tech report); Elman (1990); Werbos (1974, 1990) and Rumelhart, Hinton & Williams (1986) on BPTT; Hochreiter (1991 thesis); characters — Hochreiter (preview).*

---

## Why order is not “just more inputs”

After backpropagation made hidden layers trainable, the obvious next move was **time**. Speech, motor plans, sentences, and sensor streams are not bags of features—they are **ordered trajectories** where the same symbol means something different depending on what preceded it. The connectionist programme of the late 1980s attacked that problem with recurrent networks: machines that carry a **state** forward step by step, updating it as new input arrives.

This chapter tracks two architectures—**Jordan**’s and **Elman**’s—and the training procedure that made recurrence learnable in principle: **backpropagation through time** (BPTT), which unrolls a recurrent network across ticks into a deep feedforward structure and applies the chain rule backward along that unfolded depth. Paul Werbos had already formulated BPTT in his **1974** dissertation and gave it a definitive tutorial in **1990**; Rumelhart, Hinton, and Williams (**1986**) supplied the vivid, widely circulated version that the PDP revival treated as canonical—same mathematics, different **routing** of attention in the field.[^bptt]

The triumph is real. So is the trap. By **1991**, Sepp Hochreiter’s diploma thesis at TU Munich would show that gradients across many time steps **vanish or explode**—not because programmers were careless, but because of multiplicative structure along unrolled depth.[^hochreiter1991] That proof is Book 1’s technical heart; here we meet the **problem statement** the proof will close.

If Chapter 3 introduced **gradient as debt** across layers, this chapter introduces the same metaphor **across time**: each timestep is another link in the chain of obligation. Past inputs lay claim on present error; the chain grows long; the bill must travel backward through every link. Some debts are paid in full; others dissipate before they reach the borrower who incurred them.

---

## Technical lens — From Jordan’s echo to Elman’s hidden memory

Michael I. Jordan’s **May 1986** UC San Diego technical report proposed a recurrent network for serial order in which **output** units feed **context** units, which are reinjected into the hidden layer at the next step.[^jordan1986] A crucial detail for our narrative: the context weights were **fixed**—the machine remembered its past outputs through a hard-coded fading window, not through learned credit assignment along the memory path.

Picture an organization that circulates **minutes** of last quarter’s decisions but never revises how those minutes are weighted. The past is present, but **frozen**—an echo, not a living interpretation.

Jeffrey Elman’s **1990** *Cognitive Science* paper, “Finding Structure in Time,” changed the attachment point: **context** units receive a one-to-one **copy** of the **hidden** activations from the previous step—not of the outputs—with **fixed** copy weights of **1.0**; the **context-to-hidden** weights, by contrast, are **trained** by gradient descent (Elman’s figure marks the copy links as non-trainable and the rest as dotted, learnable lines).[^elman1990] Hidden states are richer; they are already shaped by the task. Feeding them back makes memory **constitutive** of ongoing computation rather than a transcript of outward behavior. Elman showed—on long sequences and on miniature languages—that error patterns track temporal structure and that grammatical categories can emerge in hidden geometry without explicit symbol tables.

Picture an institution that **snapshots** yesterday’s working deliberation into the record **verbatim** (the hardcoded copy) yet still **learns**, through feedback, how heavily today’s meeting should lean on that snapshot (the trainable context-to-hidden weights). The *mechanism* of carryover is fixed; the *use* of what is carried is not.

The move from Jordan to Elman is small on a wiring diagram and large in **theory of mind**: it is the difference between archiving outcomes and archiving **the internal deliberation that produced them**.

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

[^bptt]: **Origin:** P. J. Werbos, *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences*, Ph.D. dissertation, Harvard University, August 1974; **formalization:** P. J. Werbos, “Backpropagation through time: what it does and how to do it,” *Proceedings of the IEEE* 78, no. 10 (October 1990): 1550–1560. **Popularization in the PDP revival:** D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning representations by back-propagating errors,” *Nature* 323 (9 October 1986): 533–536. Research note § 3; research/fact-checks/ch04.md (ARC-20).

[^hochreiter1991]: S. Hochreiter, *Untersuchungen zu dynamischen neuronalen Netzen* [Investigations into Dynamic Neural Networks], Diploma thesis, Institut für Informatik, Technische Universität München, 1991 (supervisor: Jürgen Schmidhuber). **No authoritative English translation;** English-language commentary: J. Schmidhuber (IDSIA). Research/fact-checks/ch04.md (ARC-20).

[^jordan1986]: M. I. Jordan, *Serial Order: A Parallel, Distributed Processing Approach*, ICS Report 8604, Institute for Cognitive Science, University of California, San Diego, **May 1986** (unpublished technical report; widely circulated). research/fact-checks/ch04.md (ARC-20).

[^elman1990]: J. L. Elman, “Finding Structure in Time,” *Cognitive Science* 14, no. 2 (1990): 179–211 (copy connections fixed at 1.0; context-to-hidden weights trained—fig. 2). research/fact-checks/ch04.md (ARC-20).

[^past-tense]: Past-tense debate: Rumelhart & McClelland in PDP vol. 2; Pinker & Prince (1988); research note § 4.

---

# Chapter 5 — How Backpropagation Works: The Chain Rule as Accumulating Debt

*Sources: research note `research/notes/ch05-backprop-chain-rule.md`; Minsky (1961); Werbos (1974, 1990); Parker (1982, 1985); Rumelhart, Hinton and Williams (1985, 1986); Richards and Lillicrap (2019); research/fact-checks/ch05.md (ARC-25).*

---

## The question

Before it was a training recipe, it was a **puzzle of blame**. In 1961 Marvin Minsky, writing in the *Proceedings of the IRE*, gave the credit-assignment problem its canonical phrasing: in a long chain of decisions where only the *final* outcome is visible, *which* intermediate move deserves credit, and which should accept blame?[^minsky1961]  

> “If the outcome is poor, one must discover which decisions were at fault and correct them. This is the problem of *credit assignment*: given a sequence of decisions leading to some terminal outcome, assign credit (or blame) for the outcome to each decision in the sequence.”

That sentence is not about neural networks; it is about any layered process. Yet it describes exactly what backpropagation would later **compute**: a backward pass that apportions responsibility to every weight, layer by layer, according to how much that weight moved the final error. The mechanism is the **chain rule of calculus**—and in deep nets, the chain is long.

---

## Technical lens — Three passes, one chain

**Forward pass.** Input flows through the network: each layer takes activations, applies a weighted sum and a nonlinearity, and hands the result forward. A loss at the end measures how far the answer was from what you wanted.  

**Backward pass.** The derivative of the loss with respect to each weight is *not* computed in isolation. Because each layer is a function of the previous one, the partial derivative of the loss with respect to a weight deep in the net decomposes into a **product** of local derivatives through every layer that sits *between* that weight and the output. The algorithm that computes those products efficiently is backpropagation; its mathematical heart is the chain rule.  

**Update pass.** Weights move a little in the direction that would have reduced the loss—steepest descent in parameter space, one step at a time.

**Gradient as debt.** You can read that backward product as a bill traveling upstream: the error at the output is the invoice; every layer the signal crosses applies its own “exchange rate” to what the previous layer is owed. For a **sigmoid** nonlinearity, the derivative of the squashing function is *never* more than 0.25, and often much smaller. Multiply a string of such factors and you are multiplying by numbers that sit below one—**multiplicative discounting** at every hop. The algebra does not *feel* like metaphor; the metaphor is a translation of the math.

**Who invented it?** The standard story and the *priority* story diverge. **Paul J. Werbos** derived backpropagation for neural networks in his 1974 Harvard Ph.D. thesis, *Beyond Regression*—**first** in print for this use. **David E. Rumelhart**, **Geoffrey E. Hinton**, and **Ronald J. Williams** re-derived and popularized the same idea (UCSD report 1985; *Nature* 1986) without, at the time, knowing Werbos. **David Parker** arrived independently (Stanford, 1982; MIT, 1985). The 1986 *Nature* paper is the one that *trained a generation*; Werbos and Parker are the ones who *were there first*. History rewards the last re-inventor; mathematics does not care.[^backprop-attr]

**Shadow of what comes next.** The backward pass through a **deep** stack is, algebraically, a product of **Jacobians**—matrices of partial derivatives. When those products shrink consistently, early layers receive a gradient near zero. That is not an accident of the next chapter; it is the same chain rule, continued across **depth** before we repeat the story across **time**. Hints of it appeared in parallel: **Sepp Hochreiter** (as the 1991 thesis would later be cited) and **Yoshua Bengio** and colleagues in the 1990s would analyze the *same* multiplicative structure from different angles, without yet sharing a common bibliography—**convergent rediscovery** of a structural fact, not a single lab’s hunch.[^independence] Chapters 6–8 will name that fact on its own terms.

---

## Organizational lens — Forward pass only

Many organizations run a **forward pass** nearly all the time: targets roll up, revenue is scored, a headline metric moves. A **backward pass**—tracing which mid-level choice actually caused a strategic outcome—requires time, data, and political will. Without it, the firm observes the *loss* (missed target) but not the **deltas** that would tell you which team or policy to nudge. That is Minsky’s credit problem with a P&L attached.

Hierarchies add another layer: each time a signal is *summarised* rather than transmitted, something like a **bounded derivative** can appear—the detail that would have changed a decision is smoothed out. The chart still looks like learning (everyone is “aligned” to the number); the **gradient** to the true cause has already faded.

---

## Philosophical lens — Credit in the head

Do brains do backpropagation? **Blake A. Richards** and **Timothy P. Lillicrap** (2019) have suggested that *dendritic* computation in pyramidal neurons might **approximate** something like credit assignment along apical and basal branches—but they frame it as a **live hypothesis** with *limited* direct evidence, not as settled fact.[^richards2019] The chapter does not need the brain to validate the machine; it needs honesty about what is still *argued*.

What *is* established is a distinction of kind: there is a difference between **feeling** that an action mattered and **computing** how much it mattered to a distant outcome. Backprop, for all its biologically awkward details, is a *procedure* for the second. The first without the second is the ordinary human condition; the second without the first is a spreadsheet with no one left to read it.

---

## Hand-off

Chapter 3 set **debt** across **layers** in a feedforward network. This chapter has named the same debt’s **source**: the chain rule, multiplied out. The same formalism, unfolded along **time** instead of only depth, governs what recurrent networks *think* they remember—and what the gradient can *actually* touch. The next three chapters take that unrolled object seriously.

---

## Notes

[^minsky1961]: M. Minsky, “Steps Toward Artificial Intelligence,” *Proceedings of the IRE* 49, no. 1 (1961), Section III-D, “The Credit-Assignment Problem for Learning Systems,” 8–30, at 8. Quotation checked against incompleteideas.net scan; for commercial republishing, confirm **IEEE** permissions—see research/fact-checks/ch05.md (ARC-25).

[^backprop-attr]: Timeline attested in research/fact-checks/ch05.md (ARC-25): Linnainmaa (1970) reverse-mode AD; **P. J. Werbos**, *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences* (Ph.D. diss., Harvard University, 1974); D. C. Parker, Stanford (1982) and MIT (1985); **D. E. Rumelhart, G. E. Hinton, R. J. Williams**, UCSD and *Nature* (1985/1986). **Werbos** has priority in NNs; **Rumelhart et al.** drove the visible wave.

[^independence]: **S. Hochreiter** (1991 thesis) and **Y. Bengio, P. Simard, P. Frasconi** (1994) analyzed the same family of long-range gradient difficulties **independently**; Bengio et al. do not cite the 1991 German thesis. Cross-awareness and synthesis come later—**Hochreiter and Schmidhuber** (LSTM, 1997) cites Bengio et al.; see research/fact-checks/ch05.md and ch07.md.

[^richards2019]: B. A. Richards and T. P. Lillicrap, “Dendritic solutions to the credit assignment problem,” *Current Opinion in Neurobiology* 54 (2019): 28–36—**hypothesis**, not proof of backprop in cortex.

---

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

---

# Chapter 7 — Hochreiter’s 1991 Thesis: A Student Proves the Paradigm Is Broken

*Sources: research note `research/notes/ch07-hochreiter-1991-thesis.md`; Hochreiter, “Untersuchungen zu dynamischen neuronalen Netzen” (Diplomarbeit, TU München, 1991); J. Schmidhuber (IDSIA; arXiv:2509.24732, 2025); Y. Bengio, P. Simard, P. Frasconi (1994); S. Hochreiter and J. Schmidhuber (1997); research/fact-checks/ch07.md (ARC-27).*

---

## The document

On **15 June 1991**, **Sepp Hochreiter** submitted a diploma thesis—*Diplomarbeit* in the German system—to the Institute of Computer Science at the **Technische Universität München**. The formal examiner was **Walter Brauer**; the *Betreuer* (direct supervisor) was **Jürgen Schmidhuber**. The title: ***Untersuchungen zu dynamischen neuronalen Netzen*** (Investigations into **dynamic**—here, recurrent / time-unfolded—**neural networks**).[^thesis] It is a **book-length** thesis, with main text running on the order of **seventy** pages before the bibliography, not a pamphlet. The internet occasionally floats a “twenty-something page” mis-memory; the primary PDF does not.[^thesis-pages]

**What it showed.** Hochreiter analyzed how **error flows backward** through **unrolled** recurrent networks and deep **feedforward** structures when you train with ordinary backprop. The **gradient** with respect to early layers—or early *time steps*—takes the form of a **product of Jacobians** along the path from output to the place you care about. For broad classes of **weights, nonlinearities, and initializations** that were standard at the time, that product is **not** a neutral average: it tends **toward vanishing** (factors persistently < 1) or **exploding** (factors persistently > 1). A student had turned *empirical fragility* into **structural** diagnosis. The work’s most cited English-language bridge would later be the **Hochreiter and Schmidhuber** (1997) *Neural Computation* paper, which **opens** with a précis of the 1991 analysis.[^lstm1997]

**A precursor inside the same thesis to what became LSTM’s core trick.** In Chapter 4, Hochreiter explored **constant error flow** (German *Konstanter Fehlerrückfluß*) and “memory” units designed so a **self-connection** of weight **1.0** on a linear *Konstanter-Fehlerrückfluß*-Knoten carries a signal without multiplicative *decay* through that *particular* path. This is the intellectual ancestor of the **constant error carousel** the field now associates with **long short-term memory (LSTM)**.[^ceflow]

**Schmidhuber’s “residual” retelling.** Jürgen Schmidhuber, in 2025, has argued in an arXiv essay that a **self-loop of weight 1.0** in the 1991 work anticipates a family of *recurrent residual* ideas that later reappear in deep feedforward work (Highway Networks, ResNets). The claim is *historical*, contested in the online conversation, and **not** a substitute for the field’s *usual* attribution of **skip-style** depth to **Kaiming He** et al. (ResNet, 2015) and **Rupesh K. Srivastava** et al. (Highway Networks, 2015), both for feedforward stacks. A careful sentence is: **Hochreiter** wrote the mathematics; **Schmidhuber** now reads part of it through the vocabulary of “residuals.” Judge the packaging separately from the **PDF**.[^residual-claim]

---

## Technical lens — Where the vanishing is proven

**Chapter 2** of the thesis, especially the material around **pp. 19–21** in the scan quoted by the 1997 LSTM paper, is where the **unfolding-in-time** analysis lives: you see the *same* layer copied across time, you write the *same* backprop *product* as in a deep *feedforward* net, and you *prove* a statement your eyes already suspected: **debt** can die on the *way* back. That is the **gradient vanishing (or explosion) problem** in *embryo* for recurrent nets trained by standard methods.

**Independence, not plagiarism.** The Montréal group’s journal paper of **Yoshua Bengio**, **Patrice Simard**, and **Paolo Frasconi (1994)** *does* **not** cite the 1991 German thesis. The results **converge**—two labs, two languages, one obstacle—rather than a neat chain of footnotes. By **1997** the *LSTM* paper **does** **cite** **Bengio** et al., knitting the story together *after* the fact. The moral is *not* “someone was scooped” but “the phenomenon was *real* enough to *find* *twice* before Twitter could remind you to read a Diplom.”[^independence]

---

## Organizational lens — The advisor as the carrier frequency

A thesis is an institution with one reader. **Hochreiter** had **Schmidhuber**, and **Schmidhuber** *kept* the file—within **IDSIA**’s working memory, in talks, in the later **LSTM** line. A finding that is **true** but **unpublished in English** in 1991 is also a finding that the **broad** community, absent a conference camera-ready PDF in the Anglosphere, may simply **not** *route* to. That is a **transmission** problem, not a **truth** problem.

**What “available” meant.** A PDF *today* on an advisor’s or author’s page is *not* the same fact as a PDF in **1991** on arXiv—there *was* no arXiv. The safe statement is: the thesis *circulated* in its *lineage*; **broad, English, widely indexed** expository access came later, notably through the **1997** LSTM paper and a **2001** book chapter in S. C. Kremer and J. F. Kolen, eds., *A Field Guide to Dynamical Recurrent Networks* (IEEE Press)—the closest thing to a *formal* English walk-through of the 1991 analysis for many readers. **Do not** claim a *first* day the thesis *hit the public web* without a **Wayback** receipt; the fact-check file records the **IDSIA** upload date as **unverified**.[^availability]

**Retro-citations.** After **1997**, the thesis and the **Hochreiter** name become **legible** to a global *citation* graph *through* the LSTM *paper*. Citation is not a *morality* play; it is a *graph* of *retrieval*.

---

## Philosophical lens — The proof you did not review

Philosophy often asks whether an idea is *valid*. The episode asks whether a *valid* idea can **fail to become common knowledge**. **Hochreiter** did not lack rigor; the **infrastructure of attention** for a German *Diplom* thesis in 1991 lacked the **bandwidth** a *Neural Computation* cover line would get in 1997. The lesson for this book is sharp: a **vanishing signal** is not *only* a vector of small partial derivatives; it is also a **finding** that *never* reached *enough* desks in time to redirect the default practice.

---

## The cliff

A student *proved* that the dominant training recipe of his moment could misfire **in principle** on **long** unrolled computations—before the community had a shared English name for the disease. The next chapter is not a bug list; it is the **theorem-shaped** claim the field would live with for years—and a mirror for non-mathematical forgetting, too.

---

## Notes

[^thesis]: S. Hochreiter, *Untersuchungen zu dynamischen neuronalen Netzen*, Diplomarbeit, Institut für Informatik, Technische Universität München, 15 June 1991; supervisor: J. Schmidhuber; examiner: W. Brauer. Primary scan (example): JKU Linz `bioinf.jku.at/publications/older/3804.pdf` (see ch07 fact-check). German title: “**zu dynamischen**,” not *der*; English gloss “Investigations of” / “into” dynamic NNs is conventional.

[^thesis-pages]: **~70+** main-text pages in the bioinf.jku scan; **not** a “24-page” thesis. Ch.2 (vanishing / error backflow), pp. 19–21 in the scan the 1997 LSTM paper points to; Ch.4 **Konstanter Fehlerrückfluß** (constant error flow). research/fact-checks/ch07.md (ARC-27).

[^lstm1997]: S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” *Neural Computation* 9, no. 8 (1997): 1735–1780. Cites Bengio *et al.* 1994; reviews 1991 thesis (introductory pages).

[^ceflow]: Ch.4 **Konstanter Fehlerrückfluß**; linear KFR node; self-loop weight 1.0. LSTM’s constant error *carousel*—Book 2.

[^residual-claim]: J. Schmidhuber, *Who Invented Deep Residual Learning?* arXiv:2509.24732 (2025)—**interpretive** priority; contrast community attribution: K. He *et al.*, ResNets, 2015; R. K. Srivastava *et al.*, Highway Networks, 2015. research/fact-checks/ch07.md.

[^independence]: Y. Bengio, P. Simard, and P. Frasconi (1994) does not cite Hochreiter (1991). S. Hochreiter and J. Schmidhuber (1997) does cite Bengio *et al.* (1994). research/fact-checks/ch07.md.

[^availability]: On **pre-1997** “**public** web” availability, no confirmed first-upload date; **IDSIA** PDF date unverified. English synthesis: 2001 Field Guide chapter (see research notes ch07, fact-check ch07).

---

# Chapter 8 — The Vanishing Gradient as a Theorem, Not a Bug

*Sources: research note `research/notes/ch08-vanishing-gradient-theorem.md`; Y. Bengio, P. Frasconi, and P. Simard, ICNN 1993; Y. Bengio, P. Simard, and P. Frasconi (1994); S. Hochreiter (1991 thesis); T. Mikolov *et al.*, Interspeech 2010; R. Pascanu, T. Mikolov, Y. Bengio, ICML 2013; L. Johnston *et al.*, *Neural Networks* 2025; research/fact-checks/ch08.md (ARC-28).*

---

## Read the title as a claim

In 1994 **Yoshua Bengio**, **Patrice Simard**, and **Paolo Frasconi** published “Learning Long-Term Dependencies with Gradient Descent Is Difficult” in the *IEEE Transactions on Neural Networks*. The title is an argument, not a mood. The paper shows that standard gradient-based training of recurrent systems—viewed through the unrolled graph that backpropagation walks—faces a structural obstacle that worsens as the span of the dependency to be learned grows. The point is not that engineers are careless; it is that **partial derivatives compose** along long unrolled paths in a way that can **shrink** (or, in other regimes, **blow up**) the signal that early time steps need for credit assignment.

A conference sketch appeared the year before at **ICNN 1993** (authors listed as Bengio, Frasconi, and Simard). The 1994 journal version is the standard reference for the full formal development and the latch experiment everyone teaches. Cite 1993 for the first public framing; cite 1994 for the journal proof.[^bengio1993_1994]

**Section III: what the latch is.** The authors train a parametric system to classify two kinds of **sequences of length T** in which the **class** depends only on the **first L** values of the external input. *L* is fixed; *T* may grow. The paper does *not* reduce its contribution to a single magic integer of steps (“*n* is where it breaks”) copied from a blog. The formal claim is the **trend** with span and the **shape** of the failure. Informal “five to ten step” talk belongs to lore and teaching slides—treat it as such, not as a Bengio-1994 theorem.[^latch]

**The attractor reading.** A strand of the 1994 paper (and a staple of how teachers retell it) links **latching** to **dynamical systems**—stable fixed points and attracting behavior that are what you want for **reliable storage**, yet can align with **tiny long-range gradients** when you train only with backprop through time. The abstract’s “trade-off between efficient learning by gradient descent and latching on information for long periods” is the line worth engraving: **efficient** first-order learning and **durable** memory under naive training are not both yours to max out for free in the same breath.

---

## Technical lens — Products, radii, and an asymmetric pair of repairs

Unroll a recurrent map for *T* steps and you have a feedforward network *T* layers deep, reusing the same weights. The sensitivity of a late loss to an early hidden state is a **product** of local Jacobians along the chain—the same multiplicative shape **Sepp Hochreiter** analyzed in his **1991** Munich *Diplomarbeit* (Chapter 7) and that **Bengio**, **Simard**, and **Frasconi** make the workhorse of their **1994** *Transactions* paper: a single journal volume a broad English-speaking audience could actually find in a university library.

**Exploding** gradients are *loud*—the loss may diverge, weights may scream; **vanishing** ones are *quiet*—the loss curve can look well behaved while the model learns a *shorter* horizon than the one you *thought* you specified.

**Clipping, twice.** In RNN **language** modeling, **Tomas** **Mikolov** and coauthors (Interspeech **2010**) kept training from blowing up by scaling down updates when **gradient** **norms** passed a ceiling—heuristic but effective. **Razvan** **Pascanu**, **Mikolov**, and **Bengio** (ICML **2013**; arXiv **1211.5063** from 2012) gave **gradient**-**norm** **clipping** a **formal** analysis in dialogue with the Bengio-1994 vanish-versus-explode duality. Asymmetry in one line: **clipping** tames **wild** gradients; it does not manufacture **distant** **credit** where the chain **rule** already **zeroed** the path out.[^clip]

---

## Organizational lens — Sirens and slow rot

**Crises** are loud. **Drift** is quiet. The analogy to the Bengio story is not decorative: a firm in acute failure is forced to run something like a backward pass, however crude; a firm in “everything looks fine” mode can *lose* the thread of *why* a policy exists while the headline metrics still *move* the right way on this quarter’s slide.

---

## Philosophical lens — 2025 as revision, not burial

**L. Johnston**, **Y. Cui**, **V. Patel**, and **P. Balaprakash** (2025), in a peer-reviewed *Neural Networks* paper (vol. 183, article 106887), re-examined whether simple vanish/explode labels predict long-range learning failure in very large RNN training sweeps. The outcome, they find, is more sensitive to **training** conditions—including **learning rate**—than older heuristics had suggested. That is **science** revising its map, not burning the 1994 *composition* story: a theorem about Jacobian products is not the last word on every optimizer choice in 2025, but the unrolled path does not stop being *multiplicative* because a new paper says so. Read the 2025 result as **nuance**, not as a license to forget **Bengio** (1994).[^ornl2025]

---

## Coda to Part II

Part I set **order** in **time** on the table. Part II names the **signal** that **fails** to **arrive** after **enough** **unrolling**—a **structural** point about **chained** **sensitivities**, not a bug report for bad **seeds** alone. Part III carries the **metaphor** to **bureaucracies** and **firms** where nobody **multiplies** **Jacobians** in code before **lunch**—**same** **shape**, different **room**.

---

## Notes

[^bengio1993_1994]: Y. Bengio, P. Frasconi, and P. Simard, “The problem of learning long-term dependencies in recurrent networks,” in *Proc. IEEE International Conference on Neural Networks* (ICNN), 1993, DOI 10.1109/ICNN.1993.298725. Y. Bengio, P. Simard, and P. Frasconi, “Learning Long-Term Dependencies with Gradient Descent Is Difficult,” *IEEE Trans. Neural Networks* 5, no. 2 (1994): 157–166, DOI 10.1109/72.279181. research/fact-checks/ch08.md (ARC-28). PDF: `https://www.comp.hkbu.edu.hk/~markus/teaching/comp7650/tnn-94-gradient.pdf`

[^latch]: Section III, Bengio, Simard, and Frasconi (1994): *C*(*u*₁,…,*u*ₜ) ∈ {0,1} depends only on the first *L* values; *T* > *L* allowed. No single universal *T* is the paper’s only numerical headline—see *fact-check* (ARC-28) for the verbatim structure.

[^clip]: T. Mikolov, M. Karaňát, L. Burget, J. Černocký, and S. Khudanpur, “Recurrent neural network based language model,” *Interspeech* (2010): 1045–1048 (heuristic). R. Pascanu, T. Mikolov, and Y. Bengio, “On the difficulty of training recurrent networks,” in *Proc. 30th ICML* (PMLR 28(3), 2013), arXiv:1211.5063 (formal *norm* clipping with analysis). research/fact-checks/ch08.md (ARC-28).

[^ornl2025]: L. Johnston, Y. Cui, V. Patel, and P. Balaprakash, “Revisiting the problem of learning long-term dependencies in recurrent networks,” *Neural Networks* 183 (2025): 106887, PubMed 39637825. Peer-reviewed; nuance, not a wholesale dismissal of 1990s Jacobian-product analysis.

---

# Chapter 9 — The Reorg as Gradient Vanishing: Knowledge That Cannot Survive Change

*Sources: research note `research/notes/ch09-reorg-as-gradient-vanishing.md`; L. Argote and P. Ingram (2000); D. Epple, L. Argote, and K. Murphy (1996); J. P. Walsh and G. R. Ungson (1991); D. M. Wegner (1987); M. Polanyi (1966); I. Nonaka (1994); I. Nonaka and H. Takeuchi (1995); E. W. Stein and V. Zwass (1995); research/fact-checks/ch09.md (ARC-29).*

---

## A reset in the middle of training

Picture a recurrent network that has been learning: weights encode dependencies the loss has not yet fully satisfied, but something is *there*—a path error could still refine. Now imagine **zeroing the recurrent weight matrix** midstream. The past is not “forgotten” in the colloquial sense; it is **detached** from the mechanism that would have carried instruction backward. Whatever signal might have traveled along that matrix **vanishes**—not because the world stopped making sense, but because the **substrate** for carrying sense was removed.

A corporate **reorganization** is often sold as a neutral rearrangement: boxes on a chart, a cleaner span of control, a “strategic realignment.” In the language of **organizational memory**, it is frequently something harsher: a deliberate disruption of the **interaction networks** in which work actually lives. **Linda Argote** (Carnegie Mellon) and **Paul Ingram** (Columbia), in a canonical *Organizational Behavior and Human Decision Processes* paper, argue that a firm’s advantage can rest on knowledge **embedded in interactions** among people, tasks, and tools—precisely the substructures a reorg rewrites when it shuffles people, reassigns tasks, and replaces tooling in one stroke. The firm does not set out to destroy knowledge. It **dissolves the reservoir** the knowledge was sitting in.[^argote2000]

When both people and task–tool sequences change together, the negative case in their framing is at its starkest. **David Epple**, **Linda Argote**, and **Kenneth Murphy** showed—at a plant that added a second shift long after the first was mature—that the second shift, staffed largely with new members, could reach in weeks a productivity level the first shift had required many months to build. The difference was that **task sequences and tools** on the line **preserved** what the first shift had embedded in the plant. Where restructuring breaks all three—people, tasks, and tools—there is no such subsidy. The empirical point belongs to Epple, Argote, and Murphy (1996); the reservoir *framework* that organizes the story in Argote and Ingram’s review draws on subsequent work by **J. E. McGrath** and **Argote** in edited social-psychology handbooks, not on that shift study itself.[^epple1996][^mcgrath2001]

The parallel to depth-in-time **gradient flow** (Chapter 8) is not decorative. A reorg does to interaction networks what a pathological reset can do to an unrolled recurrent path: the signal of “what we learned and why” can no longer **route** to the people who would have to act on it. **Vanishing** in the network was quiet. So is this.

---

## Technical lens — Transactive memory as a routing table

**Daniel M. Wegner** (social psychologist) proposed in 1987 that groups often hold knowledge as a **transactive memory system** (TMS): each member specializes; the team also maintains **metamemory**—who is likely to know what, and how to locate it. The published locus of the full theoretical statement is a chapter in *Theories of Group Behavior* (Wegner’s pages 185–208 in that volume); an in-text pointer to a 1985 working line exists inside that chapter, but the citable primary is **Wegner (1987)**.[^wegner1987]

A TMS is a **distributed index** at least as much as a distributed database. A reporting change that shuffles experts to new teams does not erase each person’s *private* know-how, but it can erase the team’s **map of who to ask**—the index the old group had tuned through practice. A fresh team *exists*; it has not yet relearned the **addressing** layer. The productivity dip that follows reorgs is, in this reading, partly the clock time required to **rebuild metamemory**—not a mysterious drop in *individual* IQ, but a wipe of the router.

That is a precise organizational analogue to what later architectures would solve with **learned attention** over positions (Book 2’s bridge): before any new knowledge can be integrated, a system with **broken routing** cannot bring error to the right place. Gradient-based training does not *care* that you “used to know the answer in the old org”; it only sees whether the backward signal can still move through the wiring you have *now*.

---

## Organizational lens — The bins and what reorgs attack

**James P. Walsh** and **Gerardo R. Ungson** gave organizational memory a durable spatial metaphor: retention in “bins”—**individuals**, **culture**, **transformations** (encoded routines), **structure** (roles and reporting relationships), and **ecology** (the physical and spatial layout of work). Their *Academy of Management Review* paper appeared in January 1991; it is a touchstone, not a footnote, in later reviews of the field.[^walsh1991]

**Structure** is both frequently an explicit target of reorgs and, in the Walsh–Ungson picture, a conduit of memory about who knows what and which escalation paths *work*—memory that is **tethered to relationships** rather than to files. **Culture** is slow to form and, for good or ill, durable; reorgs that leave slogans in place can still **cut the muscle** that executed yesterday’s work. The irony is a familiar one: the organization “still believes in *quality*” (culture) while not remembering *how* it once shipped on time (transformations) after structure is redrawn.

Wikis, document-management systems, and intranets are where modern firms often **hope** the bins will compress into one repository. **Eric W. Stein** and **Vladimir Zwass** analyze information systems as an essential **mediator** of organizational memory and outline acquisition, retention, maintenance, search, and retrieval as **mnemonic functions** an organizational memory information system (OMIS) must serve. Their *Information Systems Research* paper is not “Walsh plus one bin,” but it sharpens the separate question of what IT can and cannot anchor when *practice* moves.[^stein1995] Walsh and Ungson’s own logic already predicts a painful gap: the system can hold what is **codified**; the tacit and relational loads in other bins are **not** duplicated by a documentation sprint *before* the **interaction network** dissolves.

---

## Philosophical lens — Tacit knowledge and the broken spiral

**Michael Polanyi**’s *The Tacit Dimension* (1966) gave the field a slogan that doubles as a warning: *we can know more than we can tell.* Skill, judgment, and context travel through apprenticeship and **shared work**, not only through text. In organizations, a large slice of what “the firm knows” is resistant in principle to **exhaustive** externalization.[^polanyi1966]

**Ikujiro Nonaka**’s *Organization Science* paper (1994) formalizes knowledge creation as a **spiral** through four modes—**Socialization** (tacit to tacit), **Externalization** (tacit to explicit), **Combination** (explicit to explicit), **Internalization** (explicit back into skilled practice). The **SECI** picture, including the figures and **spiral** language, belongs to *that* article. The widely read *The Knowledge-Creating Company*, with **Hirotaka Takeuchi** (1995), extends the story with case material—Honda, Canon, and others.[^nonaka1994][^nonaka1995]

A reorg is often, in these terms, a **Combination** event on paper—new org charts, new role templates—while the **Socialization** infrastructure (stable teams, repeated contact, time) is the very thing being **broken**. The standard palliative is a pre-reorg **documentation** spurt: **Externalize** everything before the people scatter. Nonaka’s own spiral says why that is **necessarily lossy**—Externalization is *one* mode, not a stand-in for the others. What restructuring does to Polanyi-style **tacit** stock is the organizational twin of a **clipped** gradient update: you address a symptom (write it down) while the mechanism you needed—continuous **tacit** transfer in place—stops **existing**.

---

## The silent handoff

**Exploding** gradients are *loud*; **vanishing** ones are *quiet* (Chapter 8). So is the knowledge drop that follows a reorg that **erases routing** while leaving the *appearance* of continuity: spreadsheets still close; customers are still served—until the team that knew *why* a guardrail existed cannot be **reached** as a team any longer.

The next chapter is not a kinder case. It is a **wider** one: what happens when the firm does **not** zero a network in one day but **drowns** it in stored text with no gate—too much **signal** and no mechanism that says **what to forget**.

---

## Notes

[^argote2000]: L. Argote and P. Ingram, “Knowledge Transfer: A Basis for Competitive Advantage in Firms,” *Organizational Behavior and Human Decision Processes* 82, no. 1 (2000): 150–169. research/fact-checks/ch09.md (ARC-29).

[^epple1996]: D. Epple, L. Argote, and K. Murphy, “An Empirical Investigation of the Microstructure of Knowledge Acquisition and Transfer Through Learning by Doing,” *Operations Research* 44, no. 1 (1996): 77–86 (second shift vs. first shift, tools and task sequences preserved). research/fact-checks/ch09.md (ARC-29).

[^mcgrath2001]: J. E. McGrath and L. Argote, “Group Processes in Organizational Contexts,” in *Blackwell Handbook of Social Psychology: Group Processes*, ed. M. A. Hogg and R. S. Tindale (Oxford: Blackwell, 2001), 603–627—published form of the “knowledge reservoirs” framing cited *in* Argote and Ingram (2000) as in press.

[^wegner1987]: D. M. Wegner, “Transactive Memory: A Contemporary Analysis of the Group Mind,” in *Theories of Group Behavior*, ed. B. Mullen and G. R. Goethals (New York: Springer-Verlag, 1987), 185–208. Do *not* cite a standalone “Wegner 1985” as primary. research/fact-checks/ch09.md (ARC-29).

[^walsh1991]: J. P. Walsh and G. R. Ungson, “Organizational Memory,” *Academy of Management Review* 16, no. 1 (1991): 57–91. Venue is *AMR*—**not** *Administrative Science Quarterly*. research/fact-checks/ch09.md (ARC-29).

[^stein1995]: E. W. Stein and V. Zwass, “Actualizing Organizational Memory with Information Systems,” *Information Systems Research* 6, no. 2 (1995): 85–117, https://doi.org/10.1287/isre.6.2.85 (OMIS, mnemonic functions; IT and organizational memory).

[^polanyi1966]: M. Polanyi, *The Tacit Dimension* (Garden City, NY: Doubleday, 1966) — tacit vs. articulable knowledge (secondary summaries standard in management literature).

[^nonaka1994]: I. Nonaka, “A Dynamic Theory of Organizational Knowledge Creation,” *Organization Science* 5, no. 1 (1994): 14–37 (SECI matrix and spiral; primary theoretical source for the four modes).

[^nonaka1995]: I. Nonaka and H. Takeuchi, *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation* (New York: Oxford University Press, 1995) — case material and popularization; four modes *introduced* in Nonaka 1994.

---

# Chapter 10 — Why Documentation Systems Fail: Too Much Signal, No Gating

*Sources: research note `research/notes/ch10-documentation-no-gating.md`; M. J. Eppler and J. Mengis (2004); L. J. Holtzblatt, L. E. Damianos, and D. Weiss (2010); J. Mimouni *et al.* (2022, arXiv:2212.01479); Episteca (2025); J. Lave and E. Wenger (1991); E. Wenger (1998); E. Wenger, R. McDermott, and W. M. Snyder (2002); research/fact-checks/ch10.md (ARC-30); research/fact-checks/ch10-residual.md (ARC-49).*

---

## The tragedy of the documentation commons

**Martin J. Eppler** and **Jeanne Mengis**, in an *Information Society* review that has become a standard reference, catalogue **causes of information overload** that cross disciplines—characteristics of the person, of the information itself, of tasks, of organizational process, and of **information technology** that *lower the cost of production* without a matching tax on *consumption*. The architectural point for institutions is (5): email, wikis, and intranets that make writing cheap can make *finding* *true* and *useful* **expensive**. Each author’s rational add becomes the commons’ irrational noise.[^eppler2004]

A firm’s **knowledge base** is not “failed” the day it launches. It is failed the day nobody has **permission to forget**—or to govern what stays *valid*. The contrast with the last chapter is instructive. A reorg is a *sudden* substrate **loss**; a runaway wiki is a *slow* dilution of *relevance*—a recurrent state in which *everything* the firm ever said remains in the **corpus** unless someone **removes** it, while nothing in the system *automatically* downweights the stale.

---

## Technical lens — A recurrent state without a forget gate

A plain recurrent network *without* a gating path keeps one hidden **trajectory** through time: old activations and new input add in fixed roles; stale **context** and current **signal** can fight in the same **vector**. The LSTM family, which *Book* *2* takes up as *engineering* (*The* *Forget* *Gate*), was built to **choose** what to carry and what to **discard** (forget gate, input gate) because unbounded **accumulation** in time is not *neutral* for learning—it is a **structural** hazard.[^bridge]

An “open” enterprise wiki that **treats** every new page as *equally* authoritative in retrieval is, in the analogy, a state in which the text base only *grows*; the reader is left to guess what still **matters**. The mechanism the LSTM line discovered—a **trainable** choice about *how* much of the past to attenuate in each **dimension**—is what a curation-poor **knowledge management** platform does **not** implement in software, governance, or roles.

Gating is not a decoration. It is how you **bound** a memory when **inflow** is unpriced.

---

## Organizational lens — Decay, vendor numbers, and the tax on experts

What reads as “helpful” on launch can rot on a faster clock than most governance cycles touch. A 2025 industry blog (Episteca) attributes dramatic figures to Readme- and Zoomin-sourced data—**API**-**class** technical documentation *materially* stale on the order of **tens of days**, and large fractions of enterprise technical content not updated for half-year or year scales. As of 2026 the **original** vendor **reports** for those exact numbers are not independently **archived** in **forms** this book can **verify** (see research/fact-checks/ch10-residual). Treat the Episteca figures as *vendor-routed* **order of magnitude**, not a peer-reviewed experiment. A **citable** independent result in the same **direction** is **Mimouni** *et al.* (2022) on **outdated** code-element references in popular GitHub **project** **documentation** (arXiv preprint).[^episteca2025][^mimouni2022]

**Lester J. Holtzblatt**, **Laurie E. Damianos**, and **Daniel Weiss** (MITRE) used **Contextual Inquiry** with 26 **participants** in an **extended** **abstract** at **CHI 2010** to map impediments to **internal** wiki use—a **qualitative** portrait of one large not-for-profit R&D **employer**, not a **statistical** law of all firms. The tension is as much **social** as **technical**: **reluctance** to **share** unfinished or **sensitive** work on open pages; **reliance** on familiar **non-wiki** channels—**governance** **deficits** (ownership, curation) more than a universal “people hate wikis” mood.[^holtzblatt2010]

Practitioner research in the DORA/Accelerate tradition—cited, in the Episteca-mediated chain this chapter uses for the documentation–onboarding link—gives a plausible **mechanism** for cost: if juniors cannot **trust** the **knowledge** **base**, they **revert** to **shadowing** seniors, **converting** expert time into **tour-guide** time and **bypassing** the transactive-memory routing **efficiency** Chapter 9 **described** (ask a sage **instead** of a search **box**).

---

## Philosophical lens — Communities of practice as *social* forget gates

The cure managers want to *buy* from a vendor may need to *grow* in **communities of practice (CoP)**. **Jean Lave** and **Etienne** **Wenger** (1991) are the **primary** source for the ethnographic **origin** of **situated** **learning** and “legitimate peripheral **participation**.” **E.** **Wenger**’s 1998 monograph is the primary for the *sociology-level* **framework** of communities of practice—mutual **engagement**, joint **enterprise**, shared **repertoire**; **E.** Wenger, **R.** **McDermott**, and **W.** **M.** **Snyder** (2002) is the primary for *cultivating* **communities** as an **organizational** **knowledge** **intervention**.[^lavewenger1991][^wenger1998][^wenger2002]

The three texts answer different questions; do not collapse them. A mature **CoP** **governs** its knowledge a little like a well-trained **forget** **gate**: people in daily **contact** with the **work** may **falsify** a **stale** page; **reputation** and **repeated** **use** supply **pressure** to **revise** or **remove**—a **selective** **editing** of the **corpus** that a read-only **repository** **cannot** do by metadata **alone**.

---

## The architectural gap to Book 2

What the **gated** RNN **family** did in **code** (*Book* *2*), vendors of “wiki as filing **cabinet**” **rarely** did in **product** **design** for **human** **curation** **incentives** and **roles**. A **knowledge** **base** is not a **theory** of **relevance**; an LSTM is a **theory** of **relevance** **under** a **loss** **function**. The **compliance** **extreme**—**“remember** **everything** in **the** **log**” without **assimilation**—waits in the **next** **chapter**: a **pathology** of a **different** **sign** than **vanishing** **gradients** **alone**.

---

## Notes

[^eppler2004]: M. J. Eppler and J. Mengis, “The Concept of Information Overload: A Review of Literature from Organization Science, Accounting, Marketing, MIS, and Related Disciplines,” *The Information Society* 20, no. 5 (2004): 325–344, https://doi.org/10.1080/01972240490507974. research/fact-checks/ch10.md (ARC-30).

[^bridge]: Long short-term memory: *Book 2 — The Forget Gate* (series bible); S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” *Neural Computation* 9, no. 8 (1997): 1735–1780.

[^episteca2025]: Episteca, *The Documentation Decay Problem: Why Your Technical Docs Are Outdated*, Episteca.ai, 19 January 2025, https://episteca.ai/blog/documentation-decay/ — **vendor-secondary**; attributes numeric claims to Readme- and Zoomin-sourced data without publicly archived primary reports (research/fact-checks/ch10-residual.md, ARC-49).

[^mimouni2022]: J. Mimouni *et al.*, “Detecting Outdated Code Element References in Software Repository Documentation,” arXiv:2212.01479 (2022) (peer-reviewed-adjacent; 28.9% of popular GitHub projects with outdated code references in documentation per abstract/finding—cited as *independently* *verifiable* *decay* *shape* in ch10 fact-check, ARC-49).

[^holtzblatt2010]: L. J. Holtzblatt, L. E. Damianos, and D. Weiss, “Factors Impeding Wiki Use in the Enterprise: A Case Study,” in *CHI 2010 Extended Abstracts* (New York: ACM, 2010), 4661–4676, https://doi.org/10.1145/1753846.1754202 (n=26; qualitative, MITRE; non-generalizing claim). research/fact-checks/ch10.md (ARC-30).

[^lavewenger1991]: J. Lave and E. Wenger, *Situated Learning: Legitimate Peripheral Participation* (Cambridge: Cambridge University Press, 1991) — origin of the situated-learning/CoP line per fact-check mapping. research/fact-checks/ch10.md (ARC-30).

[^wenger1998]: E. Wenger, *Communities of Practice: Learning, Meaning, and Identity* (Cambridge: Cambridge University Press, 1998) — three-dimension model; theoretical elaboration. research/fact-checks/ch10.md (ARC-30).

[^wenger2002]: E. Wenger, R. McDermott, and W. M. Snyder, *Cultivating Communities of Practice* (Boston: Harvard Business School Press, 2002) — applied organizational cultivation of CoPs. research/fact-checks/ch10.md (ARC-30).

---

﻿# Chapter 11 — The Regulated Industry as an Extreme Case: Compliance Without Memory

*Sources: research note `research/notes/ch11-regulated-compliance-without-memory.md`; Sarbanes–Oxley Act of 2002 (Pub. L. 107-204); 17 C.F.R. §210.2-06 (Regulation S-X, Rule 2-06); HIPAA (45 C.F.R.); Regulation (EU) 2016/679 (GDPR); UK ICO guidance on the right to erasure; Financial Stability Board, *Recommendations to Achieve Greater Convergence in Cyber Incident Reporting* (12 April 2023); Regulation (EU) 2022/2554 (DORA); Swiss Federal Act on Information Security (ISG) Art. 74a seq.; SEC rules on material cybersecurity incident disclosure (Form 8-K, 2023); B. Schneier, *Beyond Fear* (2003); *Arthur Andersen LLP v. United States*, 544 U.S. 696 (2005); *Yates v. United States*, 576 U.S. 186 (2015); research/fact-checks/ch11.md (ARC-31).*

---

## The write-only archive

The **Sarbanes–Oxley Act** of 2002 (Pub. L. 107-204) arrived after U.S. corporate accounting scandals with a new weight on **records** in **federal** matters. Section 802 and related provisions connect to **federal** criminal law—notably 18 U.S.C. § 1519 (falsification or destruction of records in **federal** investigations)—and to **civil** obligations on **auditors** and **issuers** (use the current **U.S. Code** for precise elements and penalties). **SEC** Rule 2-06 of Regulation S-X (17 C.F.R. § 210.2-06) requires retention of **audit** workpapers and certain related material for a long horizon—commonly summarized as on the order of **seven** years from **conclusion** of the relevant process (confirm current **eCFR** for applicability).[^sox][^sec2-06]

In practice, many artifacts are stored in **append-only**, **tamper-evident** form—rational for regulators who need **chains of custody** (*what* existed *when*). That choice serves evidence; it is less friendly to the **iterative** narrative that **operational** learning often needs (revising a past failure note with deeper context after a later near-miss). The pathology of this chapter is the **complement** of **vanishing** gradients (Chapters 7–8): not exponential shrinkage of a **backward** signal through a long path, but **indefinite** retention without **reweighting**—a log that grows like a **write-only** layer that rarely updates the weights of habit and procedure (*how* we work *now*).

---

## Technical lens — Trace, proxies, and "security theater"

Audit trails and retention satisfy a regulator: *can you prove what happened?* They do not, by themselves, answer the practitioner: *should we operate differently next time?* Storing events is a necessary condition for **compliance**; it is not sufficient for **assimilation** (the step in which a finding becomes revised procedure and retrained habit—a rough organizational analog of applying a weight update after a gradient step).

**Bruce Schneier** popularized the phrase "security theater"—the performance of risk reduction that may outrun the reduction itself—in *Beyond Fear: Thinking Sensibly about Security in an Uncertain World* (Copernicus Books, 2003, ISBN 0-387-02620-7). The later industry coinage "compliance theater" (checklist rituals with little effect on actual risk) is derivative; it is not Schneier's own term in that book, and it should not be footnoted as if he had written it there.[^schneier2003][^theater-caveat]

Goodhart's Law (when a measure becomes a target, it ceases to be a good measure) names the incentive problem when post-incident reports are written first for a supervisor and only second for the line. The **Financial** **Stability** **Board** (April 2023) published *Recommendations* *to* *Achieve* *Greater* *Convergence* *in* *Cyber* *Incident* *Reporting*—**explicitly** **non**-**binding** G20 guidance, not a universal statute.[^fsb2023] Domestic law then hardened pieces of that pattern: the **EU** **DORA** (Regulation (EU) 2022/2554) in full application for key incident-reporting and ICT elements on 17 **January** **2025**; Swiss **ISG** (e.g. Art. 74a *seq.*) serious cyber-attack notification for in-scope operators (1 **January** **2025** in the policy roundups the ch11 fact-check used—verify current federal law); U.S. **SEC** material cybersecurity **Form** **8**-**K** disclosure (effective **December** **2023** per the adopted rule); the UK FCA/PRA operational-resilience **regime** remains a separate evolution from DORA.[^dora][^swiss][^sec8k][^ukcaveat] **Mandated** reporting and a **usable** line-of-business lesson are not the same deliverable.

---

## Organizational lens — HIPAA, Article 17, and legal obligation

U.S. **HIPAA**-covered entities must retain **policies, procedures, and documentation** (often described in guidance as about **six** years from creation or last effective date; see 45 C.F.R. and HHS materials). In the **EU/EEA**, the "right to erasure" in **GDPR** Article 17 can appear to clash with long retention; the treaty text resolves the tension in **Article** **17(3)**: erasure does not apply where processing is necessary to comply with a **legal** **obligation** ((b)) or for **legal** **claims** ((e))—a delete request can fail when a **higher**-**order** duty to keep **records** governs. The **UK** **ICO** states in right-to-erasure **guidance** that controllers can refuse where erasure would prevent compliance with a **legal** **obligation** (worked **examples** include tax and **regulator** **filings**). Where a regulatory **purpose** can be met with **anonymised** or **aggregated** data, **anonymisation** is a **frequent** **supplement**; it does not replace the **statutory** **carve**-**out** when **identifiable** **personal** **data** must **lawfully** **remain**.[^gdpr][^ico]

The tension is real in politics and product; at the level of **black**-**letter** law (GDPR/UK GDPR structure), the exemptions are the **relief** **valve** (per ARC-31). The narrow claim of this chapter is: **compliance**-tuned memory optimises for **trace** (what happened), not necessarily for **reusable** learning (what we should do differently on Monday).

---

## Philosophical lens — Illustrations, not a prosecution count

A civil society wants **evidence** in **court**; a learning organization also wants a **loop** in which the record **changes** default **behavior**. *United* *States* *v.* *Arthur* *Andersen* *LLP* (conviction **reversed**, *Arthur* *Andersen* *LLP* *v.* *United* *States*, 544 U.S. 696 (2005)) is the **landmark** Enron-era narrative about record destruction, not a published aggregate tally of § 1519 prosecutions. *Yates* *v.* *United* *States*, 576 U.S. 186 (2015), is a different opinion about the reach of the same **section** (tangible object)—**breadth** of statutory **reach** without a published **federal** census of **compliance** **cases** .[^andersen][^yates][^dojcaveat]

Where the narrative is **trained** on a **proxy** (legibility to **power**), the backward signal is not necessarily aligned with the true loss (prevent the next **recurrence**). That is a governance-shaped "poisoned **gradient**" in **discourse** (Chapter 10 **named** a **gating** **failure** in **documentation**; this chapter names a **loss**-**landscape** **warp** in **incentives**).

---

## The handoff to Chapter 12

We have mapped **vanishing** (Chapters 7–8), reorg **substrate** **loss** (Chapter 9), ungated **corpus** **dilution** (Chapter 10), and **append**-**only** **compliance** **retention** (this chapter). The next chapter—the **Part** **III** closer—poses a **positive** question: *what* would an institution need to **actually** **remember** in the **training**-**loop** sense?

---

## Notes

[^sox]: Sarbanes–Oxley Act of 2002, Pub. L. 107-204, 116 Stat. 745; 18 U.S.C. (e.g. §1519). research/fact-checks/ch11.md (ARC-31).
[^sec2-06]: 17 C.F.R. §210.2-06. research/fact-checks/ch11.md (ARC-31).
[^schneier2003]: B. Schneier, *Beyond Fear: Thinking Sensibly* *about* *Security* *in* *an* *Uncertain* *World* (New York: Copernicus Books, 2003), ISBN 0-387-02620-7. research/fact-checks/ch11.md (ARC-31).
[^theater-caveat]: "Compliance theater" is derivative industry usage, not Schneier coinage in *Beyond Fear*. research/fact-checks/ch11.md (ARC-31).
[^fsb2023]: FSB, *Recommendations* *to* *Achieve* *Greater* *Convergence* *in* *Cyber* *Incident* *Reporting* (12 April 2023), FSB/2023/8—non-binding guidance. research/fact-checks/ch11.md (ARC-31).
[^dora]: Regulation (EU) 2022/2554 (DORA), full application 17 Jan 2025. research/fact-checks/ch11.md (ARC-31).
[^swiss]: Swiss ISG Art. 74a *seq.*; in-force dates in ch11 fact-check; verify *SR*. research/fact-checks/ch11.md (ARC-31).
[^sec8k]: SEC Form 8-K material cybersecurity incident disclosure (2023 rule). research/fact-checks/ch11.md (ARC-31).
[^ukcaveat]: UK FCA/PRA regime evolving; not DORA copy. research/fact-checks/ch11.md (ARC-31).
[^gdpr]: Regulation (EU) 2016/679, Art. 17(3)(b), (3)(e). research/fact-checks/ch11.md (ARC-31).
[^ico]: UK ICO, right to erasure guidance. ico.org.uk. research/fact-checks/ch11.md (ARC-31).
[^andersen]: *Arthur* *Andersen* *LLP* *v.* *United* *States*, 544 U.S. 696 (2005). research/fact-checks/ch11.md (ARC-31).
[^yates]: *Yates* *v.* *United* *States*, 576 U.S. 186 (2015). research/fact-checks/ch11.md (ARC-31).
[^dojcaveat]: No published aggregate DOJ/SEC count for corporate §1519-only cases in ch11 fact-check. research/fact-checks/ch11.md (ARC-31).

---

# Chapter 12 — What Would an Organization Need to Actually Remember?

*Sources: research note `research/notes/ch12-what-orgs-need-to-remember.md`; P. Senge, *The Fifth Discipline* (1990); C. Argyris and D. A. Schön, *Organizational Learning* (1978); C. Argyris, *Strategy, Change, and Defensive Routines* (1985); C. Argyris, *Overcoming Organizational Defenses* (1990); D. A. Garvin, “Building a Learning Organization,” *Harvard Business Review* (July–August 1993); U.S. Army TC 7-0.1, *After Action Reviews*; U.S. Army FM 7-0, Appendix K; NASA APPEL Knowledge Services history; research/fact-checks/ch12.md (ARC-32).*

---

## A specification, not a product catalog

Chapters 9–11 traced how knowledge can **vanish** in reorgs, **dilute** in ungated documentation, and **accumulate** without assimilation in compliance-shaped archives. This chapter states—in **abstraction**—what a serious **learning loop** would need. You can read the list as analogs to **gradients**, **updates**, and **gates** from Part II; it is not a shopping list for software.

**Peter Senge**’s *The Fifth Discipline* (1990; revised 2006) remains the door most readers open first. A “learning organization,” in his framing, is one where people expand their capacity to create the results they want, where new patterns of thinking are nurtured, and where people learn how to learn together. The five disciplines—personal mastery, mental models, shared vision, team learning, systems thinking—are a **theory of coupling**: what must stay connected if an institution is to close the loop between **event**, **insight**, and **changed behavior**. This chapter returns to *mental models*—the implicit pictures of how the world works—because they are the closest organizational analog to a **weight matrix**: the pattern of associations that governs how new evidence is read before it becomes policy or habit.[^senge1990]

---

## Technical lens — Single-loop, double-loop, defensive routines

**Chris Argyris** and **Donald A. Schön**, in *Organizational Learning: A Theory of Action Perspective* (1978), distinguish **single-loop** learning (detect and correct error inside fixed goals and norms) from **double-loop** learning (scrutinize and potentially revise those goals and assumptions). A compliance apparatus that only asks *Did we follow the rule?* is a single-loop engine par excellence: it corrects deviation from procedure; it does not, by itself, ask whether the procedure fits the world you now inhabit.[^argyris1978]

For the **specific** claim that **defensive routines**—habits that shield embarrassment or threat and block inquiry—**short-circuit** double-loop learning, the fact-check (ARC-32) assigns primary weight to **Chris Argyris**, *Strategy, Change, and Defensive Routines* (1985, Pitman), where the construct is **titular**, and to *Overcoming Organizational Defenses* (1990, Allyn & Bacon) for the widely cited organizational definition and for the link to obstruction of double-loop change. Do **not** cite *Theory in Practice* (1974) or *Organizational Learning* (1978) as the **primary** homes for “defensive routines” as a **central** object; those volumes are primary for theories of action and for the single-/double-loop distinction, not for the named construct in the role Argyris later gives it.[^argyris1985][^argyris1990]

---

## Organizational lens — AAR, CALL, current doctrine, Garvin, NASA

The U.S. Army’s **After Action Review** (AAR) and the **Center for Army Lessons Learned** (CALL, established 1985) are this book’s chief **positive** exhibit: an event, a facilitated collective review (immediacy, broad participation), and an institution tasked with turning outputs into doctrine and training updates—not merely filing them.

For **current** AAR doctrine, cite **TC 7-0.1**, *After Action Reviews* (Training Circular; authoritative text via the Central Army Registry, rdl.train.army.mil), and **FM 7-0**, Appendix K, which also defines the AAR (see ARC-32 for wording). **Do not** substitute **ATP 5-19** as the successor to older AAR manuals: ATP 5-19 addresses **risk management** (superseding FM 5-19), not AAR procedure. Citing FM 25-20 (1993) alone would be historically incomplete; the fact-check names **TC 7-0.1** as the current primary for AAR process.[^tc701][^fm7k]

**David A. Garvin**’s *Harvard Business Review* article “Building a Learning Organization” (vol. 71, no. 4, July–August 1993, pp. **78–91**—**not** beginning at p. 80; archive at https://hbr.org/1993/07/building-a-learning-organization) compresses what a learning organization *does*: creating, acquiring, and transferring knowledge—and, in the italicized clause initiatives love to skip, *modifying its behavior to reflect new knowledge and insights*. Secondary pagination drift (reprint “p. 2” vs. journal pp. 78–91) is its own small lesson in **how organizational memory corrupts**.[^garvin1993]

NASA’s arc, in the APPEL Knowledge Services history and related synthesis, is a natural experiment: **Challenger** (1986) triggered the **Program and Project Management Initiative** (PPMI, from 1988)—a first-order emphasis on **individual** competence and formal training (single-loop at agency scale). After **Columbia** (2003), the **Columbia Accident Investigation Board** concluded NASA had not demonstrated the characteristics of a learning organization; practices associated with the Challenger era had **returned**. The second-order response embedded knowledge capture and sharing more deeply in APPEL and related infrastructure—double-loop at institutional scale. Do not conflate the two reform waves.[^nasa]

---

## Philosophical lens — Six requirements (a working spec)

Synthesising Senge, Argyris, the AAR/CALL pattern, Garvin, and the NASA sequence (with Senge’s *systems thinking* as the integrator for the other disciplines), a memorable—**not** unique—specification is:

1. **Immediacy** — capture while the signal is strong (AAR after the event, not only in the annual audit).
2. **Psychological safety** — room to name error and assumption (precondition for double-loop work).
3. **Structural assimilation** — a role or function (CALL, standards owners) authorized to **change** procedure, not only to file the memo.
4. **Behavioral testing** — evidence that practice moved, not only that a PDF exists.
5. **Forgetting discipline** — retire stale doctrine (parallel to a forget gate), not infinite append-only growth.
6. **Loss-function alignment** — measure the right thing (Garvin’s italic); optimize document count and you **overfit** the proxy.[^garvin1993]

---

## Handoff — Book 1 ends on a question Book 2 answers in metal

Book 1 began with a **proof** of what ordinary recurrent training could not do across long depth in time. Book 2—*The Forget Gate*—names the **gated** machines engineers built to address that failure. The question this chapter closes is not “store more,” but **which forgetting is permitted**—and at what cost—to make **memory** and **learning** the same sentence.

---

## Notes

[^senge1990]: P. Senge, *The Fifth Discipline: The Art and Practice of the Learning Organization* (New York: Doubleday, 1990; updated ed. 2006).

[^argyris1978]: C. Argyris and D. A. Schön, *Organizational Learning: A Theory of Action Perspective* (Reading, MA: Addison-Wesley, 1978). research/fact-checks/ch12.md (ARC-32).

[^argyris1985]: C. Argyris, *Strategy, Change, and Defensive Routines* (London: Pitman, 1985). research/fact-checks/ch12.md (ARC-32).

[^argyris1990]: C. Argyris, *Overcoming Organizational Defenses: Facilitating Organizational Learning* (Boston: Allyn and Bacon, 1990). research/fact-checks/ch12.md (ARC-32).

[^tc701]: U.S. Army, TC 7-0.1, *After Action Reviews*—current edition via CAR (rdl.train.army.mil); confirm edition date for final ms. **Do not** cite ATP 5-19 as primary AAR doctrine. research/fact-checks/ch12.md (ARC-32).

[^fm7k]: U.S. Army, FM 7-0, Appendix K—AAR definition and guidance (per ARC-32).

[^garvin1993]: D. A. Garvin, “Building a Learning Organization,” *Harvard Business Review* 71, no. 4 (July–August 1993): 78–91, https://hbr.org/1993/07/building-a-learning-organization. research/fact-checks/ch12.md (ARC-32).

[^nasa]: NASA APPEL Knowledge Services history; PMI white paper narrative; Challenger → PPMI (1988/89) vs. Columbia → CAIB → APPEL evolution. research/fact-checks/ch12.md (ARC-32).

---

# Chapter 13 — Heraclitus and the River: Identity Across Time

*Sources: research note `research/notes/ch13-heraclitus-river-identity.md`; Diels–Kranz, *Fragmente der Vorsokratiker* (22 B12, B49a, B91); C. H. Kahn, *The Art and Thought of Heraclitus* (Cambridge University Press, 1979, paperback ISBN 0-521-28645-X); Plato, *Cratylus* 402a8–10, trans. H. N. Fowler (Loeb Classical Library vol. 167, 1926); Simplicius, *In Aristotelis Physicorum Libros Commentaria* 1313.11; research/fact-checks/ch13.md (ARC-33).*

---

## The three rivers, one doctrine

**Heraclitus** of Ephesus (fl. c.500 BCE) left no running treatise. What survives is a lattice of some **130** fragments, mostly second-hand. In that lattice, a single cluster of “river” sayings (DK 22 B12, B49a, and B91) is not decorative local colour; for many readers it is the *control room* of his thought.[^kahn-dk] This chapter will use the cluster as a *map*—not a proof that Heraclitus “anticipated” backprop—because B12, B49a, and B91 are not three retellings of the same aphorism. They are three *different* answers to a question our book has been asking since Part II: **when everything changes, what, if anything, is still the same thing?**

- **B12** (Cleanthes, via a chain to Eusebius) says, in paraphrase: the rivers are *the same* rivers, and *other and other* waters are ever flowing. Identity is *through* change; sameness and flux are *jointly asserted*.  
- **B49a** doubles the first-person: *we* step and do *not* step, *are* and are *not*—a variant reading (some editors treat 49a as an alternate transmission of the same “river” thought) that adds a crucial twist: the observer, not only the world, is in motion.  
- **B91** (Plutarch) goes negative: *you cannot step into the same river twice*—a sentence many later readers took as the *whole* of Heraclitus, though B12 is the one that *also* affirms the river’s *sameness*. The scholarly tradition, following **Charles H. Kahn**’s 1979 edition and commentary, often reads B12 as the *positive* thesis: the **logos** of flow—patterned change—rather than mere chaos.[^kahn-river]

A modern shorthand, **πάντα ῥεῖ** (*panta rhei*, “all things flow”), is **not** a verbatim Heraclitean line. The compact formula is first attested in **Simplicius** (6th c. CE), *In Phys.* 1313.11; the *content* of universal flux is what **Plato** fastens to Heraclitus in the *Cratylus* (402a) — a crucial reception story, not a direct quotation.[^panta-simplicius] The authenticated textual anchors for this chapter are B12, B49a, and B91, cited in the **Diels–Kranz (DK) numbers** that anglophone scholarship standardises.[^dk-concordance]

**Three fragments, three stances (metaphor: the river as channel).** Read as a *taxonomy of memory* rather than a biography of Ephesus, the cluster asks which kind of constancy a learning system is trying to preserve: an address and pattern (B12), the co-moving learner (B49a), or only the fact of unrepeatable replacement (B91).

---

## Technical lens — Logos, weights, and the moving observer

Kahn’s central interpretive move is to shift attention from *flux* as a slogan to **logos** as **structure in motion**—the rule-like pattern that makes a river a river, not a bucket. For this book, that pattern has an uncomfortable neighbour: a trained neural network’s **weight matrix**—a fixed set of numbers that, together, impose a consistent mapping from new inputs to outputs even when every activation (the *waters*) differs from step to step. Catastrophic **fine-tuning** is, in that vocabulary, a failure of **logos**: the channel is re-cut so brutally that the *same* name (“the same checkpoint”) no longer governs a recognisable policy.

- **B12** (same rivers, ever-new waters) ≈ a hidden state *slot* that stays numerically the same *address* while its contents are overwritten. Successive time steps *replace* the vector even when you still call the variable `h`—identity as **patterned replacement**.  
- **B49a** (we step and we do *not* step) ≈ **online learning** under distribution shift: the model that ingests a minibatch is not, in a strict sense, the *same* object that will process the next one if your training rule has already moved its weights. The **observer** and the **river** are co-evolving.  
- **B91** (no second step into the *same* river) ≈ the limit where **no shared state** remains between tasks—*catastrophic forgetting* in its purest guise, when every update erases the trace you needed for yesterday’s loss.  

Plato, in the *Cratylus*, gives **Socrates** a Heraclitean-sounding line at **402a8–10**: “all things are in process and nothing stays still,” and “likening existing things to the stream of a river,” you could *not* step into the *same* river *twice*. The Greek is Plato’s, not a DK text; Fowler’s Loeb translation is a standard anglophone anchor. The structural point for us is *reception*: the tradition often imports **B91’s negation** while de-emphasising B12’s *joint* claim of *sameness* and change. A reader who *only* keeps B91 gets maximum flux.[^cratylus-fowler] That is not necessarily what the fragments, read together, *force* you to read—hence the decades-long fight over “flux vs. *logos*.”

**One metaphor, one line:** the river is the **channel**; the waters are **activations**; the **logos** is the **geometry of the channel** (including what your weights *mean* in practice after training).

---

## Organizational lens — Substrate, form, and the pattern of exchange

The pre-Socratic *family of answers* to identity-through-change (see research note) is not a museum display; it is a *menu* of ways institutions argue they are *still* the same *company* when every plank has been changed.

- **Milesian “substrate”** (conserved stuff) ≈ the durable **asset base** (servers, data centres, the balance sheet) or *parameter identity* in ML (“the same *weights* in the same *parameters* if you haven’t reinitialised the tensor id”). The institution can replace every *person* and still *claim* material continuity.  
- **Pythagorean *form* or proportion** ≈ the **org chart and mission statement** (pattern-level identity) or *functional identity* in models (“it still does the *task* with acceptable loss”). The ship is the same *shape* even when every timber is new.  
- **Heraclitean *logos*** ≈ the **tacit pattern of *how* decisions, blame, and credit actually run** (the topic of Chapters 9–12): what survives *reorg* and *documentation sprawl* is not “stuff” and not a slogan, but a **governed** pattern of exchange (who talks to whom, which gradient-like incentives decide what is recorded). A firm that rewrites every policy without preserving *why* the old pattern existed is not *preserving* *logos*; it is flooding the channel.  

**Diagnostic parallel:** a **reorg** that preserves headcount in each box but severs the **informal graph** of trust is *substrate* theatre with *logos* loss—the organisational analogue of fine-tuning that keeps tensor *names* but not their learned role.

---

## Philosophical lens — Plato’s paraphrase as motivated framing

The *Cratylus* uses a Heraclitus-like flux doctrine as *premise* in a wider argument about names and *stability* of reference; the *Theaetetus*’s *Flusslehre* polemic is, in the eyes of many historians, a **construction** of “Heraclitus the radical” fit for a Platonic *elenchus*—the opponent you need, not a neutral exegesis of every DK line. The ML mirror is *post-mortem* culture: the frame is chosen so the *conclusion* is easy (blame a vendor, bless a reorg) while evidence that *complexifies* the story is treated as noise. Colvin and related scholarship (Semantic Scholar) stress that the *magnitude* of “flux” in Plato can exceed what the **fragments** warrant.[^plato-citation] If we want intellectual honesty, we hold B12 and B91 **together**—**sameness** *and* **unrepeatable change**—even though slogans love to keep only one pole.

A late-antique *summary formula* (*panta rhei*) is not a fragment; it is a **shorthand** a thousand years younger than the Ephesian. The telephone game (B12 → *Cratylus* → Simplicius → digests) is the philosophical cousin of the organisational *wiki drift* Chapter 10 described: a crisp phrase survives; the **nuance** that tied it to evidence does not.[^kahn-dk]

---

## Handoff

**Identity-through-flux** in B12 is the *positive* thesis; **B91** is the *limit case*; **B49a** is the *recursive* one (the knower in motion). The next chapter moves from **rivers** to **ships**—a single civic object preserved and repaired until **philosophers** (not the shipwrights) cannot agree whether it is “the same” *vessel*. The question is *kind* before it is *cleverness*: the **Ship of Theseus** makes **persistence** *visible* as **replacement**.

---

## Notes

[^kahn-dk]: C. H. Kahn, *The Art and Thought of Heraclitus: An Edition of the Fragments with Translation and Commentary* (Cambridge: Cambridge University Press, 1979). ISBN 0-521-28645-X (paperback of record). No revised *edition*; later printings reissue the 1979 text. research/fact-checks/ch13.md (ARC-33).  

[^kahn-river]: The river fragments: DK 22 B12, B49a, B91; on reception and the B12 / B49a / B91 relation, Kahn 1979 and the SAGP “river fragments” analysis cited in the research note. research/fact-checks/ch13.md (ARC-33).  

[^panta-simplicius]: *Panta rhei* first attested Simplicius, *In Phys.* 1313.11 (6th c. CE). Plato, *Crat.* 402a, attributes a flux doctrine; see Fowler translation below. **Do not** quote *panta rhei* as Heraclitus’s own words. research/fact-checks/ch13.md (ARC-33).  

[^dk-concordance]: **Primary system: DK 22** (B12, B49a, B91). **Miroslav Marcovich** (*Heraclitus*, Merida 1967) numbers these *frg.* 40, 40c2, 40c3 and treats 49a/91 as secondary reminiscences of B12 (an editorial *stance*, not a neutral renumbering). **Kahn 1979** uses a **thematic** order; use his appendix *concordance* (DK–Kahn) for cross-reference—exact Kahn numbers for B49a/B91 should be double-checked in that appendix for your final bibliography. research/fact-checks/ch13.md (ARC-33).  

[^cratylus-fowler]: Plato, *Cratylus* 402a8–10, trans. H. N. Fowler, *Loeb Classical Library* vol. 167 (1926). Quotation/paraphrase is *Plato’s* reported view of Heraclitus, not a DK fragment. Greek at 402a8–10 in standard editions; *St.* pagination 402a. research/fact-checks/ch13.md (ARC-33).  

[^plato-citation]: On Plato’s *Flusslehre* vs. the fragments, e.g. S. A. Colvin, “Heraclitean Flux and Unity of Opposites in Plato’s *Theaetetus* and *Cratylus*” (Semantic Scholar); OpenEdition 2002 materials on *Cratylus* / *Theaetetus* reception—see `research/notes/ch13-heraclitus-river-identity.md` and ARC-33 for secondary list.

---

# Chapter 14 — The Ship of Theseus as a Memory Architecture Problem

*Sources: research note `research/notes/ch14-ship-of-theseus.md`; Plutarch, *Life of Theseus* 23.1, trans. B. Perrin (Loeb Classical Library); T. Hobbes, *De Corpore*, Part II, Ch. 11, §7, in *The English Works of Thomas Hobbes*, ed. W. Molesworth, vol. I (London, 1839); T. Sider, *Four-Dimensionalism: An Ontology of Persistence and Time* (Clarendon Press, 2001); K. Hawley, *How Things Persist* (Oxford University Press, 2001); D. Wiggins, *Sameness and Substance Renewed* (Cambridge University Press, 2001); E. J. Lowe, *Kinds of Being* (Blackwell, 1989); J. Kirkpatrick *et al.*, *Proc. Natl. Acad. Sci. U. S. A.* 114(13) (2017); research/fact-checks/ch14.md (ARC-34).*

---

## A puzzle born of *careful* maintenance

**Plutarch** records that the **Athenians** preserved the **thirty-oared ship** in which **Theseus** had sailed with the youths and back—down to the time of **Demetrius of Phalerum** (Athenian governance **317–307 BCE**). They *removed old timbers* and *replaced* them, “so that the ship became a standing illustration to philosophers of the mooted question of growth, some declaring that it remained the same, others that it was not the same vessel.”[^plutarch-theseus]

The paradox was not a failure to keep records. The puzzle arose *because* the polis maintained the ship. Plutarch’s *auxēseōs aporia* (the aporia of growth) is the ancestor of a hundred identity disputes in objects, persons, and—our topic—models and organisations.

---

## Technical lens — Form, matter, and the two ships

**Thomas Hobbes**, in *De Corpore* (1655), Part II, Chapter 11, “Of Identity and Difference,” **§7** (Molesworth *English Works* vol. I, 1839), does not *dissolve* the question in a mood. He *splits* it. Take continuous replacement in situ so the ship *remains in service* (Plutarch’s standing exhibit). *Then* take the old planks, stored and reassembled elsewhere, producing a second candidate with the original *matter* but a discontinuous *history*. *Which* is the Ship of Theseus? Form-continuity and matter-continuity, Hobbes’s readers saw, can pick out *different* candidates.[^hobbes-decorpore] The fact-check is explicit: in *this* locus Hobbes names **the Ship of Theseus**; some secondary digests conflate a different Hobbes *example* (the *De Mundo* material) with *Argo*—do not import that conflation when citing *De Corpore* alone.[^hobbes-argo-caveat]

**Neural analogue.** **Architecture** (form) and **weight tensors** (matter) support different notions of *sameness* for a *deployed* model. Reinitialise a net, retrain the *same* architecture on comparable data, and you may recover similar behaviour without *byte-for-byte* weight identity—**form**-match, **new** matter. Keep the same checkpoint *filename* and aggressively fine-tune, and you may *destroy* the behaviour that *made* the service trustworthy while the tensor *address* is unchanged—**matter**-lineage with **rupture** in function. Continual learning policy is the *choice* of which criterion is governing. Failing to say which is a ship with *two* logbooks and *one* name on the bow.

A practical bridge from sortal talk to code is **Elastic Weight Consolidation (EWC)**: **James Kirkpatrick** and colleagues (2017) regularise against large changes to weights estimated important for *previous* tasks (via a **Fisher**-style importance measure), in order to *preserve* a task-relevant “shape” of the network while learning the next.[^kirkpatrick2017] EWC is not a citation of Hobbes; it is an operational guess at *which* timbers must remain for a model of a *kind* to count as the *same* service in deployment.

**Metaphor (this section):** timber, joints, and rigging—persistence is joinery; “same ship” is a claim about which joints *must* hold.

---

## Organizational lens — “Same company” as two logbooks

**Form-identity** is brand, legal entity, mission, and the slide that says *we* *transformed* *together*. **Matter-identity** is the tacit knowledge of specific people and teams (who actually knows *why* the rule exists, who can still read the scar tissue of the last outage). A post-merger “integration” that retires the tacit *carriers* while insisting on a single *culture* often behaves like Hobbes’s *second* ship (reassembled planks) **plus** a press release *about* the *first* (continuous refit in harbour).

**Callback to Chapter 9:** a reorg can erase the mesh of trust and *credit paths* that made gradient-like blame travel to the *right* owners. Identity of *form* (OKRs on the slide) with loss of *matter* (the people who held the *why*) is a standing organisational failure mode. Hobbes’s fork names the uncanny feeling: we said we were the same *company*; the *knowledge* was not the same *heap*.

**Metaphor:** two logbooks—one for what the *brand* is allowed to *say*; one for who can still *sail*.

---

## Philosophical lens — Slices, worms, and sortals

**Ted Sider** and **Katherine Hawley** set out the *standard* contemporary oppositions: **endurantism** (an object is wholly present at each time) versus **perdurantism** (persistence as *temporal* *parts*; a four-dimensional “**worm**” through spacetime). Sider, *Four-Dimensionalism* (Clarendon Press, 2001), and Hawley, *How Things Persist* (OUP, 2001), are the shelf anchors. If you **cite Sider to a page number**, your edition *matters*: the 2001 hardback and the 2003 paperback (ISBN 0-19-924443-3) have **different** paginations.[^sider-editions]

A *perdurantist* read of the training *history* is *elegant*: each checkpoint is a *slice*; the “model” is the whole *world-line* in weight space. That metaphysics is cold comfort on Monday if the *endpoint* is unsafe. For **operations** you still need **sortal-relative** criteria: *what* *kind* of *sameness* you care about for *safety* and for *the* *task*.

**David Wiggins**, *Sameness and Substance Renewed* (Cambridge University Press, 2001), is the edition to cite for **sortal** persistence conditions—what counts as the same *F* for a kind *F*. Use the 1980 *Sameness and Substance* only when you mean a *historical* claim Wiggins later revised; on **personal identity**, the 2001 book *retracts* large parts of the 1980 chapter.[^wiggins-2001] **E. J. Lowe** (*Kinds of Being*, 1989) reinforces the modal link between kind and the **essential** shape of persistence.

Wiggins’s own preface quip—whether 1980 and 2001 are the “same book”—is a sortal joke about sortals; the footnote culture gets the humour.

**Metaphor (this section):** the *worm* in four dimensions versus the *object* in three at *t*—persistence as a *line* through time, not only a *knot* on the deck at each instant.

---

## Handoff

We have a *civic* object (the ship in Plutarch), an analytic *bifurcation* (Hobbes in *De Corpore*), a 4D *option* (Sider / Hawley), a sortal *framework* (Wiggins 2001), and a **DeepMind**-era regulariser (EWC) that encodes a *first* *cut* *at* *“task-essential* *joints*” *in* *weights*.

**Chapter 15** asks a **Bergsonian** question: the **clock** of training *steps* and the **lived* *thickness* *of* *what* *weights* *have* *become* are not obviously the *same* *time* at all.

---

## Notes

[^plutarch-theseus]: Plutarch, *Life of Theseus* 23.1, trans. B. Perrin, *Loeb Classical Library*; passage via research note (Perrin / Lexundria / UChicago). Demetrius of Phalereum **317–307** BCE. research/fact-checks/ch14.md (ARC-34).  

[^hobbes-decorpore]: T. Hobbes, *De Corpore* (1655), *Elements* *of* *Philosophy* *I*—*Concerning* *Body*; *Part* *II*, *ch.* *11* §7; *in* *The* *English* *Works* *of* *Thomas* *Hobbes*, ed. W. Molesworth, vol. I (London, 1839). Molesworth *page* for §7: confirm for final *print* (ARC-34).  

[^hobbes-argo-caveat]: ARC-34: in *De Corpore* II.11.§7 Hobbes uses the Ship of Theseus. The Argo and other ship examples live in other Hobbes texts (e.g. *De Mundo Examined*); do not conflate when citing *De Corpore* alone.

[^kirkpatrick2017]: J. Kirkpatrick *et al.*, “Overcoming catastrophic forgetting in neural networks,” *Proc. Natl. Acad. Sci. U. S. A.* **114**, no. **13** (2017): 3521–3526, DOI 10.1073/pnas.1611835114. Fourteen authors; use PNAS as primary, not the arXiv preprint alone. research/fact-checks/ch14.md (ARC-34).

[^sider-editions]: T. Sider, *Four-Dimensionalism* (Clarendon Press, 2001, xxiv+280; OUP paperback 2003, xxiv+255, ISBN 0-19-924443-3). Match *page* *refs* to *edition*.

[^wiggins-2001]: D. Wiggins, *Sameness and Substance Renewed* (Cambridge: Cambridge University Press, 2001), ISBN 0-521-45619-3; *sortals* and persistence. On personal identity, cite 2001 (revised) not 1980; see Weatherson and ARC-34.

---

# Chapter 15 — Bergson’s Duration: Time as Lived Versus Time as Measured

*Sources: research note `research/notes/ch15-bergson-duration.md`; H. Bergson, *Essai sur les données immédiates de la conscience* (Paris: Félix Alcan, 1889); *Time and Free Will: An Essay on the Immediate Data of Consciousness*, trans. F. L. Pogson (London: George Allen & Unwin, 1910); H. Bergson, *Matière et mémoire* (1896); *Matter and Memory*, trans. N. M. Paul and W. S. Palmer (London: George Allen & Unwin, 1911); J. Canales, *The Physicist and the Philosopher: Einstein, Bergson, and the Debate that Changed our Understanding of Time* (Princeton University Press, 2015); G. Deleuze, *Bergsonism*, trans. H. Tomlinson and B. Habberjam (New York: Zone Books, 1991; French *Le Bergsonisme*, PUF, 1966); K. Ansell-Pearson, *Philosophy and the Adventure of the Virtual* (Routledge, 2002); research/fact-checks/ch15.md (ARC-35).*

---

## The two times

**Henri Bergson** (1859–1941) is often introduced as a critic of the **spatialisation of time**—the habit, common to clock-driven science and to everyday speech, of treating *duration* as a **line of interchangeable instants** you could, in principle, shuffle like beads. His **durée réelle** (*real* duration) is not that. It is a succession in which *former* states *interpenetrate* the present; the “moments” are not the same in *quality* even when they are the same in *number* (Stanford Encyclopedia of Philosophy; research note; Bergson, *Essai* 1889; Pogson, *Time and Free Will* 1910).[^bergson-essai]

**Metaphor (this section):** two clocks—**wall** time and the **thickness** of an interval *lived* as learning (or as institutional history), not merely counted.

The training **step** index *N* and the *functional* rate at which a model’s *representations* still move are not forced to be proportional. Early in training, one step can reshape the landscape; late in training, the same *increment* in *N* can do almost nothing. That **heterogeneity** is what Bergson’s critique of a single homogeneous time is *gesturing toward* when imported—carefully—into ML vocabulary.

---

## Technical lens — Habit-memory and pure memory

Bergson’s *Matter and Memory* (1896; Paul and Palmer, *Matter and Memory* 1911) gives the philosophy-of-memory architecture this book has been circling. A two-pole summary (see the research note; secondary outlines on *Matter and Memory*):

- **Habit** memory (*mémoire-habitude*) — condensed, motor, procedural: the poem recited by rote, where the *schema* eclipses the *occasion* of its first learning.  
- **Pure** memory (*souvenir pur*): the episode as a *dated* past, available as *that* episode and not only as a compression into habit.

A **crude** map to systems **practice** (analogy, not identity): *habit* ≈ a **trained weight matrix**—the compressed residue of past gradients, with no built-in re-enactment of *which* batch nudged *which* weight for *which* reason unless you log that elsewhere. *Pure* memory ≈ the training corpus, **replay** buffers, **RAG** stores—*dated* particulars the system can re-**actualize**. Continual learning’s partial remedies are *engineering* nudges toward a second pole; they do not turn a matrix into a soul.

Catastrophic **forgetting** in its everyday ML sense is the pathology of a system that, for deployment as a single forward pass, *only* has *habit*: new habit overwrites the disposition the old task needed.

**Metaphor (this section):** the *hummed* tune (habit) versus the *afternoon* of the first lesson (pure recollection).

---

## Organizational lens — Calendar time and functional duration

The same two-pole scheme maps onto **offices** (see research note):

- **Habit**-like knowledge ≈ SOPs, approved templates, tickets closed the same way every week. It survives reorgs when the org still enforces the *form*.  
- **Episodic** knowledge ≈ the decision in 2008, the client who only makes sense if you knew 2008, the rejected architecture whose *reasons* never made it into Jira.

Chapters 10 and 11 already named failure modes where *habit* swells (ungated documentation) or where *traces* accumulate without *reweighting* habit (compliance-shaped archives). Bergson sharpens the vocabulary: you can file the *procedure* and still lose the *episode* the procedure was meant to carry.

**Metaphor (this section):** *calendar* age of the company versus the *thickness* of one good decision thread that never made it to a wiki.

---

## Philosophical lens — Einstein, Bergson, and the virtual

On **6 April 1922**, the *Société française de philosophie* hosted **Albert Einstein** in Paris; **Bergson**, then writing *Durée et Simultanéité* (1922), intervened. **Jimena Canales**, *The Physicist and the Philosopher* (2015, 429 pp.), is the authoritative secondary for the April meeting, the surrounding debate over simultaneity, and the Nobel-era politics of relativity and *lived* duration.[^canales2015] Einstein’s physics *won* the consensus of working physicists; Bergson’s phenomenology of *lived* duration still names a *constraint* on when “time” in the **counting** sense is interchangeable with “time” in the **transforming-learner** sense. This chapter *imports* that *only* as a **caution about metrics**, not as a re-litigation of 1920s physics in a book about gradients.

**Nobel** facts (Canales; ARC-35): the **1921** physics prize, conferred in **December 1922**, cited Einstein for the **law of the photoelectric effect**—not “relativity” in the way popular memory imagines. **Svante Arrhenius** mentioned **Bergson** in the ceremony; how much that mention *causally* shaped the *wording* of the prize is contested in scholarship, but the institutional record is on the books.[^nobel-arrhenius]

A **tradition** (not an archivally verified document in the ARC-35 materials) reports that **Bergson** asked that *Durée et Simultanéité* not be reprinted in his **lifetime**; on Canales’s account, present this as *reported* *wishes*, not a *BnF* certificate.[^ds-hedge]

**Gilles Deleuze**, *Bergsonism* (Zone Books, **1991**; French *Le Bergsonisme*, PUF, 1966)—bibliographic year of the **English** book is **1991**; do not substitute the ©1988 *translation* copyright *notice* for the *publication* year (ARC-35). Deleuze re-reads Bergson through *virtual* versus *actual*. **Keith Ansell-Pearson**, *Philosophy and the Adventure of the Virtual* (Routledge, 2002, ISBN 0-415-23728-9), is a common Anglophone bridge.[^deleuze1991][^ansell2002] A **careful** gloss for ML: a model’s *latent* space is *virtual* in Deleuze’s sense—**real** *as* *structure*—and not *identical* to any single forward pass. Continual learning is the problem of *differentiating* that reservoir *without* collapsing what older tasks need.

**Metaphor (this section):** *reservoir* (virtual multiplicity) and *faucet-line* (this token’s actual output).

---

## Handoff

Chapter 16 returns to the **technical** history: **Bengio**, **Simard**, and **Frasconi** (1994) as an impossibility result for naive recurrence; the **TDNN** and **NARX** evasions; **Hochreiter**’s 1991 *Untersuchungen* and the 1997 **LSTM** paper. The field had *Bergson’s* worry about homogeneous step time in its mouth; it did not yet have the *industrial* stack to *live inside* the answer.

---

## Notes

[^bergson-essai]: H. Bergson, *Essai sur les données immédiates de la conscience* (Paris: Félix Alcan, 1889); *Time and Free Will*, trans. F. L. Pogson (London: George Allen & Unwin, 1910). *Studylib* “1899” is a spurious date (ARC-35). research/fact-checks/ch15.md (ARC-35).

[^canales2015]: J. Canales, *The Physicist and the Philosopher: Einstein, Bergson, and the Debate that Changed our Understanding of Time* (Princeton, NJ: Princeton University Press, 2015), 429 pp. **6** **April** **1922** *Société* session per Canales; research note April 22 slip corrected. research/fact-checks/ch15.md (ARC-35).

[^nobel-arrhenius]: Nobel Prize in Physics 1921 (conferred Dec. 1922); photoelectric effect, not relativity, as the cited work. Arrhenius and Bergson: narrative in Canales (2015) and ARC-35.

[^ds-hedge]: *Durée et Simultanéité* reprint: attested biographical tradition, not primary archive in ARC-35; chapter hedges in prose as directed.

[^deleuze1991]: G. Deleuze, *Bergsonism*, trans. H. Tomlinson and B. Habberjam (New York: Zone Books, 1991); orig. *Le Bergsonisme* (PUF, 1966). **1991** = English publication; ©1988 = translation copyright, not the cite year. research/fact-checks/ch15.md (ARC-35).

[^ansell2002]: K. Ansell-Pearson, *Philosophy and the Adventure of the Virtual: Bergson and the Time of Life* (London: Routledge, 2002), 256 pp., ISBN 0-415-23728-9. Monograph. research/fact-checks/ch15.md (ARC-35).

---

# Chapter 16 — The Question the Field Couldn’t Yet Answer

*Sources: research note `research/notes/ch16-question-unanswered.md`; Y. Bengio, P. Simard, and P. Frasconi, *IEEE Trans. Neural Netw.* 5(2) (1994); A. Waibel *et al.*, *IEEE Trans. Acoust. Speech Signal Process.* 37(3) (1989); S. Chen, S. A. Billings, and P. M. Grant, *Int. J. Control* 51 (1990); K. S. Narendra and K. Parthasarathy, *IEEE Trans. Neural Netw.* 1(1) (1990); R. Pascanu, T. Mikolov, and Y. Bengio, ICML 2013 (arXiv:1211.5063); S. Hochreiter, *Untersuchungen zu dynamischen neuronalen Netzen* (Diplomarbeit, Technische Universität München, 1991); S. Hochreiter and J. Schmidhuber, *Neural Comput.* 9(8) (1997); M. Hammer and J. Champy, *Reengineering the Corporation* (1993); I. Nonaka and H. Takeuchi, *The Knowledge-Creating Company* (1995); T. A. Stewart, *Intellectual Capital* (1997); research/fact-checks/ch16.md (ARC-36).*

---

## A theorem dressed as a training failure

**Yoshua Bengio**, **Patrice Simard**, and **Paolo Frasconi** published “Learning Long-Term Dependencies with Gradient Descent is Difficult” in the *IEEE Transactions on Neural Networks*, March **1994**, **5**(2), **157**–**166** (DOI 10.1109/72.279181, PMID 18267787).[^bengio1994] The paper is *not* a story about bad luck with hyperparameters. It formalises a **structural** tension: with standard recurrent training, gradients through long *time* depth tend to **vanish** or **explode**; the conditions that help a recurrent dynamic *retain* information and the conditions that make gradient-based **credit assignment** across the same depth *tractable* stand in the *tension* the paper makes precise (read the theorem, not this gloss). The work circulated earlier as a Université de Montréal technical report; the **citable** anchor is the **1994** journal paper.[^tr-note]

**Metaphor (this section):** a **fence**—a *bounded* question: what naive BPTT could not honestly *promise* under the paper’s assumptions.

---

## Technical lens — Evasions, not miracles

**Time–delay neural networks (TDNN).** The peer-reviewed anchor is **Alexander Waibel**, **Toshiyuki Hanazawa**, **Geoffrey Hinton**, **Kiyohiro Shikano**, and **Kevin Lang**, “Phoneme Recognition Using Time-Delay Neural Networks,” *IEEE Transactions on Acoustics, Speech, and Signal Processing* **37**(3): 328–339 (1989).[^tdnn] Secondary histories often date the *idea* to **1987** CMU work; ARC-36 did not close a primary 1987 technical report number—**cite 1989** for the reviewed article. The design *trades* full recurrence for a *designed* temporal *window* and **weight sharing** across time; the limit is *architectural*: dependencies longer than the window are *out of scope* by construction. This is the **anti-recurrence** fork’s early *move* (later: temporal convolutions, **WaveNet**, then the **Transformer** in 2017—Book 3’s problem field).

**NARX** (nonlinear autoregressive with exogenous inputs). **Sheng Chen**, **Stephen A. Billings**, and **P. M. Grant**, “Non-linear system identification using neural networks,” *International Journal of Control* **51**: 1191–1214 (1990), is a foundational discrete-time identification paper; the **issue** number within vol. 51 is **TBC** against the journal record (ARC-36).[^narx] In parallel, **Kumpati Narendra** and **Kannan Parthasarathy**, “Identification and Control of Dynamical Systems Using Neural Networks,” *IEEE Transactions on Neural Networks* **1**(1): 4–27 (1990), is an independent 1990 pillar; the two strands are **parallel** foundations, not parent and child.[^narendra] **NARX** *recurrent* variants (e.g. Lin *et al.*, NeurIPS 1996, in the research note) exploit *shorter* gradient paths through explicit lags; the **maximum** lag is still **fixed** at design time.

**Clipping and geometry.** **Razvan Pascanu**, **Tomas Mikolov**, and **Yoshua Bengio**, “On the Difficulty of Training Recurrent Neural Networks,” *ICML* **2013** (arXiv 1211.5063), extends the **geometric** picture; **gradient norm clipping** addresses the *exploding* side. It does not, by itself, restore unbounded *vanishing-free* depth.[^pascanu]

**Six years.** **Sepp Hochreiter**’s 1991 Munich *Diplomarbeit*, *Untersuchungen zu dynamischen neuronalen Netzen* (supervisor **Jürgen Schmidhuber**), identified vanishing/exploding gradients in RNNs. The **LSTM** paper—**Hochreiter** and **Schmidhuber**, “Long Short-Term Memory,” *Neural Computation* **9**(8): 1735–1780 (1997), DOI 10.1162/neco.1997.9.8.1735—is the **journal** of record (not a Springer chapter reprint alone).[^lstm] Bengio *et al.* (1994) do **not** cite the 1991 thesis; *convergence* of the *story* is post-hoc *bibliography*, not simultaneous *discovery*.

---

## Organizational lens — Identified problems, lagging stacks

The same **decade** that could not *close* the long-dependency problem in **recurrent** nets also saw **Business Process Reengineering** (**Michael Hammer** and **James Champy**, 1993), early **knowledge management** movements, and **Nonaka** and **Takeuchi**’s *The Knowledge-Creating Company* (1995) alongside **Thomas Stewart**’s *Intellectual Capital* (1997). The *organizational* mirror is **not** the claim that “KM caused RNNs.” It is a **parallel pattern**: both discourses often **named** tacit knowledge *loss* and *transfer* *failure* *without* an *institutional* *architecture* that *reliably* *closed* the *loop* between *event* and *changed* *habit* *at* *decade* *scale*—*the* *same* *sort* *of* *infrastructural* *lag* *that* *later* *GPUs*, *data*, and *tooling* *would* *help* *neural* *sequence* *models* *outrun* *.*

**Metaphor (this section):** the 1990s *intranet* *folder*—*what* *a* *place* *knew* *before* *the* *link* *stayed* *stable* *long* *enough* *to* *trust* *.*

---

## Philosophical lens — Durée of uptake

Ideas have their own **duration**: a 1997 paper can *wait* while **GPUs**, **datasets**, and **automatic differentiation** *catch up*—*Bergson* *in* *metaphor* *only*; this book does *not* reopen 1920s *physics* . The *field* *knew* in *outline* what naive *BPTT* could *not* *guarantee*; *it* *lacked* the *machine* *room* to *make* *LSTM* the *default* *engineering* *move* *.* *Exact* *LSTM* *bibliometric* *tables* *belong* *in* *a* *methods* *note*;* *this* *chapter* *keeps* *the* *qualitative* *shape* *only* *.*

---

## Coda to Book 1 *main matter* — The fork, and Munich

**Anti-recurrence** (TDNN → convolutions in time → **Transformers** and **self-attention**) and **gated recurrence** (LSTM / GRU; later *state-space* **layers** for sequences) are the two design families **Book 2**—*The Forget Gate*—takes as **explicit** choices. **Hochreiter**’s **1991** Munich *Diplomarbeit* remains the *bookend* *proof*; the **1997** *LSTM* *paper* belongs on the *next* *spine*—*failure* *named* first, *gate* *second*, *industry* *still* *learning* to *read* *both* *.*

---

## Notes

[^bengio1994]: Y. Bengio, P. Simard, and P. Frasconi, “Learning Long-Term Dependencies with Gradient Descent is Difficult,” *IEEE Trans. Neural Netw.* **5** (2) (Mar. 1994): 157–166, DOI 10.1109/72.279181, PMID 18267787. research/fact-checks/ch16.md (ARC-36).

[^tr-note]: 1993 Montréal technical report predates the journal *publication*; canonical reference is 1994 *IEEE* *TNN*. ARC-36.

[^tdnn]: A. Waibel *et al.*, *IEEE Trans. Acoust. Speech Signal Process.* **37** (3) (1989): 328–339. 1987 CMU *origin* is attested in secondary sources without a closed primary TR in ARC-36. Hampshire and Waibel, NeurIPS 1989 (*Connectionist Architectures for Multi-Speaker Phoneme Recognition*), is a *different* *follow-on* *paper*—*not* the *first* *TDNN* *publication* *.

[^narx]: S. Chen, S. A. Billings, and P. M. Grant, “Non-linear system identification using neural networks,” *Int. J. Control* **51** (1990): 1191–1214. Issue no. TBC—ARC-36.

[^narendra]: K. S. Narendra and K. Parthasarathy, *IEEE Trans. Neural Netw.* **1** (1) (1990): 4–27. Parallel 1990 foundation, not a citation parent of Chen *et al.*

[^pascanu]: R. Pascanu, T. Mikolov, and Y. Bengio, *Proc. ICML* 2013; arXiv:1211.5063. See ARC-36.

[^lstm]: S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” *Neural Comput.* **9** (8) (1997): 1735–1780, DOI 10.1162/neco.1997.9.8.1735. *Springer* reprint: not primary. research/fact-checks/ch16.md (ARC-36).