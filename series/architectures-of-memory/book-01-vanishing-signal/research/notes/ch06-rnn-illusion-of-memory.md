# Ch.06 — Recurrent Networks and the Illusion of Memory

**Issue:** ARC-6  
**Status:** Research complete — open questions logged  
**Branch:** `research/ch06-rnn-illusion-of-memory`

***

## Query set executed

1. "Elman network recurrent neural network 1990 Finding Structure in Time architecture"
2. "Jordan recurrent neural network 1986 1990 sequence"
3. "backpropagation through time BPTT Werbos Rumelhart history"
4. "early recurrent neural network long sequence failure vanishing gradient before LSTM"

***

## Findings

### 1. Elman's 1990 network and *Finding Structure in Time*

Jeffrey L. Elman published "Finding Structure in Time" in *Cognitive Science*, Vol. 14, pp. 179–211 (1990), introducing the architecture now known universally as the **Elman network**. The paper's central concern was the representation of *time* in connectionist models — a problem Elman regarded as inescapable for any account of language, music, or motor planning. His proposed solution: recurrent connections from hidden units back to a set of **context units**, which feed forward into the hidden layer at the next time step, giving the network a one-step memory of its own internal state (Elman, 1990, Cognitive Science; PDF via baulab.info; Semantic Scholar record).

Elman's innovation was explicitly twofold: (1) the context units are not fixed memory slots but are re-written at every time step, cloning the hidden-unit activation vector from the previous step $t-1$; and (2) the connections from context units to hidden units carry **trainable weights**, meaning the network learns what to do with its own history, not merely that it has one (Pablo Insente analysis, 2020). Simulations ranged from a temporal XOR task to discovering latent syntactic/semantic categories for words — the network could learn that nouns and verbs form natural classes purely from distributional sequence statistics, without any explicit labelling.

The chapter's title, "the illusion of memory," is already latent in Elman's design: the context units provide only a **single time-step lag** of the hidden state. The network has no mechanism to selectively retain information from two or five or twenty steps back; everything beyond the immediately preceding state is accessible only indirectly, through the compressed trace left in the current hidden representation. This is a structurally thin form of memory — behaviorally adequate for short dependencies, catastrophically inadequate for long ones.

For the organisational mirror thread: the Elman network's context units are structurally analogous to the **short-term institutional memory** embodied in weekly status updates, stand-up meetings, or sprint reviews. These mechanisms faithfully reflect the state one time-step ago; they carry nothing of the reasoning behind decisions made six months prior. An organisation running on Elman-style memory will exhibit the same failure mode as an Elman network on long sequences: coherent short-range behaviour collapsing into noise over long horizons.

### 2. Jordan's 1986 architecture and sequence production

Michael I. Jordan introduced his recurrent architecture in a 1986 technical report (later published as Jordan, 1997, in *Artificial Intelligence*), where context units received their input from the **output layer** rather than the hidden layer (Jordan, 1986; CMU lecture slides; Baeldung/Trendspider summaries). This distinction is architecturally significant: Jordan networks are designed for **sequence production** (e.g., planning a series of motor actions given an initial plan), whereas Elman networks are designed for **sequence prediction** (e.g., anticipating the next element of a sensory sequence). Jordan explicitly conceived of the recurrent connections as encoding a "Plan" associated with a serial "Action" sequence — the context units encode where the sequence is going, not where it has been.

The CMU lecture notes (2023) record that Jordan's original implementation did not use backpropagation, owing to his concern about biological implausibility — a decision that limited the network's learning capacity and contributed to Elman's approach becoming the dominant paradigm by the early 1990s (CMU slides, recurrentnet.html via jontalle). The *Critical Review of Recurrent Neural Networks* (arXiv:1506.00019) confirms Jordan networks' context units receive output-layer activations and are "context units" in Jordan's own terminology, not hidden-layer copies.

For the organisational mirror thread: the Jordan/Elman distinction maps cleanly onto two distinct organisational memory modes. Jordan-style memory is **goal-anchored** — the context carries the declared plan, and each action step is shaped by it. Elman-style memory is **state-anchored** — the context carries what just happened, with no privileged representation of the original goal. Organisations that rely exclusively on state-anchored memory ("what did we do last sprint?") lose track of the goal; organisations relying exclusively on goal-anchored memory ("what does the roadmap say?") lose track of current reality. Neither architecture alone is sufficient.

### 3. Backpropagation through time (BPTT): Werbos, Rumelhart, and the unfolding trick

Backpropagation through time is the algorithm that makes recurrent networks trainable: the recurrent network is **unfolded in time** into an equivalent feedforward network with one layer per time step, and standard backpropagation is then applied to the unfolded graph (Wikipedia, BPTT article; dlsi.ua.es pbook). Because every copy of the network shares the same parameters, the gradients from all time steps are summed before the weight update — the algorithm is computing the gradient of the loss over the entire sequence simultaneously.

Attribution is contested. The most commonly cited reference is Rumelhart, Hinton & Williams (1986), Chapter 8 of *Parallel Distributed Processing*, Vol. 1 (MIT Press), but the dlsi.ua.es pbook explicitly states that "an earlier description of BPTT may be found in Werbos (1974)'s PhD dissertation." Werbos published a fully worked treatment in a widely-read IEEE Proceedings paper: Paul J. Werbos, "Backpropagation through time: what it does and how to do it," *Proceedings of the IEEE*, Vol. 78, No. 10, pp. 1550–1560 (1990). Williams & Peng (1990) published a complementary gradient-based algorithm for on-line training in *Neural Computation* 2(4): 490–501 (GM-RKB record). The independent derivation by multiple groups over the 1974–1990 period is itself a narrative hook: BPTT, like backprop itself, was not invented once.

For the organisational mirror thread: BPTT's unfolding trick requires treating the entire past sequence as a single computational graph before computing credit. This is the algorithmic equivalent of a **retrospective review** or **post-mortem** — the sequence of decisions must be laid out in full, shared parameters (culture, strategy) must be identified, and gradient information (what went wrong) must flow backward through the entire history before any learning occurs. Organisations that run only prospective planning (forward pass only) without structured retrospectives are not performing BPTT.

### 4. Failure on long sequences: the vanishing gradient before LSTM

The fundamental failure mode of all pre-LSTM recurrent networks — Elman, Jordan, and BPTT-trained variants alike — was identified theoretically by Sepp Hochreiter in his 1991 TU Munich diploma thesis and empirically confirmed by Bengio, Simard & Frasconi (1994) in *IEEE Transactions on Neural Networks*, Vol. 5, No. 2, pp. 157–166. In BPTT, the gradient of the loss at the final time step with respect to hidden state at time $t$ requires multiplying the Jacobian of the hidden state transition function across all intermediate steps. If this Jacobian has spectral radius less than 1, the product decays exponentially; if greater than 1, it explodes (arXiv:1603.00423, vanishing gradient in RNNs; Baeldung, 2023).

In practice, this meant that Elman and Jordan networks trained on sequences longer than roughly 5–10 steps would exhibit essentially zero gradient signal at the earliest time steps — the network could not learn dependencies that spanned more than a short window. Several workarounds were attempted in the early 1990s: time-delay neural networks (Lang et al., 1990), simulated annealing (Bengio et al., 1994), and echo state approaches, but none solved the problem structurally (Insente, 2020). The structural solution arrived with Hochreiter & Schmidhuber's **Long Short-Term Memory** (LSTM), *Neural Computation*, Vol. 9, No. 8, pp. 1735–1780 (1997), which introduced the constant error carousel — a cell state with multiplicative gates that could maintain gradient magnitude across hundreds of time steps.

The "illusion of memory" is therefore not rhetorical. An Elman network trained on a 50-step sequence nominally has access to all 50 prior states through the recursive hidden-unit update — but the gradient signal informing its weights about events at step 1 has been multiplied by the Jacobian 49 times and is numerically zero. The network's apparent memory is an architectural promise that the mathematics cannot keep.

For the organisational mirror thread: this is the chapter's sharpest insight. An organisation with a 10-year strategy, annual reviews, quarterly OKRs, and weekly stand-ups has a **formal** memory spanning a decade. But if the information about decisions made in year one does not survive the repeated compressions and retellings that constitute organisational BPTT, the long-range memory is an illusion — structurally identical to an Elman network on a 50-step sequence. The LSTM analogy (gated cells that selectively preserve and discard) points directly at the design principles an organisation would need to implement real long-horizon memory.

***

## Narrative threads for Ch.06

1. **One step back, forever** — the Elman context unit as a metaphor for the corporate status update: it faithfully records last week's state but carries nothing of the reasoning behind decisions made last year.
2. **Jordan vs. Elman as two failure modes** — goal-anchored memory (Jordan) vs. state-anchored memory (Elman): organisations oscillate between "we forgot the plan" and "we forgot where we are" because they have no gated mechanism.
3. **BPTT as the retrospective that never happens** — organisations that cannot lay out their full decision history as an unfolded graph before computing credit are structurally incapable of learning from it.
4. **The 5-step cliff** — dramatise the empirical finding that BPTT-trained RNNs lose usable gradient signal beyond ~10 steps; map this to the practical horizon of institutional memory in most teams.
5. **From Elman to LSTM as organisational design** — end the chapter with the LSTM's constant error carousel as a design blueprint: what does it mean to implement a *forget gate*, an *input gate*, and an *output gate* in an organisational context?

***

## Open questions
> ⚠️ Flag for ARC fact-check issue (create separately):

1. **[Elman 1990 context unit trainability — 1988 vs. 1990 versions]** — Semantic Scholar records an Elman 1988 preprint ("A network architecture introduced by Elman (1988) for predicting successive elements") separate from the 1990 *Cognitive Science* paper. It is unclear whether the 1988 version already included trainable context-to-hidden weights or whether this was introduced in 1990. The chapter must not conflate the two. Suggested query: `"Elman 1988 technical report context units trainable weights vs 1990 Cognitive Science paper difference"`

2. **[Jordan 1986 original technical report availability]** — Jordan's 1986 work is cited as a technical report (Institute for Cognitive Science, UCSD, Report 8604) and later as Jordan (1997) in *Artificial Intelligence*. The 1997 publication is likely a revision. It is unclear whether the 1986 report and the 1997 paper differ substantively in architecture or learning rule. Suggested query: `"Jordan 1986 UCSD technical report 8604 recurrent network serial order 1997 Artificial Intelligence revision differences"`

3. **[BPTT first derivation — Werbos 1974 vs. Rumelhart 1985/1986]** — The dlsi.ua.es pbook cites Werbos (1974) for the first BPTT description, GM-RKB cites Rumelhart et al. (1985). The Wikipedia BPTT article states "independently derived by numerous researchers" without precise dates. A definitive timeline is needed, especially since Werbos (1990) is the widely-read IEEE paper but the claim is that the 1974 thesis already contained BPTT. Suggested query: `"Werbos 1974 Harvard PhD thesis backpropagation through time recurrent network Chapter 5 content primary source"`

4. **[Bengio 1994 empirical threshold — exactly how many steps before gradient vanishes?]** — The claim that RNNs lose gradient signal beyond "~5–10 steps" is widely repeated but the precise empirical result from Bengio et al. (1994) should be cited with exact sequence lengths and gradient magnitude measurements from the paper. Suggested query: `"Bengio Simard Frasconi 1994 learning long-term dependencies gradient signal decay exact sequence length results IEEE Transactions Neural Networks"`

***

## Definition of done (ARC-6 checklist)
- [x] Notes committed with citations
- [x] Open questions logged
- [ ] PR linked
