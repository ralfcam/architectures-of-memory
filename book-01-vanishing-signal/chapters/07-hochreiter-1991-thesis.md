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
