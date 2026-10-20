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
