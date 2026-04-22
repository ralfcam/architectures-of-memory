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
