# Ch.14 — The Ship of Theseus as a Memory Architecture Problem

**Issue:** ARC-14  
**Status:** Research complete — open questions logged  
**Branch:** `research/ch14-ship-of-theseus`

***

## Query set executed

1. "Plutarch Life of Theseus ship passage original Greek English"
2. "Ship of Theseus Hobbes Locke variation history"
3. "Ship of Theseus four-dimensionalism endurantism perdurantism philosophy"
4. "personal identity over time philosophy Lowe Wiggins"

***

## Findings

### 1. Plutarch's source text: *Life of Theseus* 23.1 and the philosophical problem as originally posed

The Ship of Theseus problem originates in a single passage of Plutarch's *Life of Theseus*, chapter 23, section 1. The text, preserved in the Bernadotte Perrin translation for the Loeb Classical Library (Penelope/UChicago; Lexundria), reads:

> "The ship on which Theseus sailed with the youths and returned in safety, the thirty-oared galley, was preserved by the Athenians down to the time of Demetrius Phalereus. They took away the old timbers from time to time, and put new and sound ones in their places, so that the vessel became a standing illustration for the philosophers in the mooted question of growth, some declaring that it remained the same, others that it was not the same vessel."

Demetrius Phalereus governed Athens from 317 to 307 BCE, placing this tradition in a verifiable historical context: the ship was preserved, with active plank replacement, for at least 150 years after the legendary voyage. The passage does not itself adjudicate between the two positions; it presents the ship as a *standing illustration* (*paradeigma*) for philosophers, noting the dispute without resolution. The key phrase in the Greek is *auxēseōs aporia* — "the puzzle of growth" — which frames the problem as metaphysical, not merely practical: what must be conserved for growth or change to constitute the *same* thing?

The Wikipedia article on the Ship of Theseus (en.wikipedia.org) adds that Hobbes in his later version refers to the ship as the *Argo* rather than Theseus's galley, which may indicate he was working from a different source or from memory. This conflation is worth flagging for the chapter: the Plutarch passage at 23.1 is the authoritative source; Hobbes's version diverges on the ship's identity even at the mythological level.

For the ML mirror thread: Plutarch's framing is precise and useful. The Athenians did not *debate* whether to preserve the ship; they *did* preserve it, actively maintaining its material coherence through continuous partial replacement. The question was philosophical: does the practice of continuous partial replacement constitute identity-preservation or identity-destruction? This is the exact question that faces any continual learning system that performs incremental weight updates. The ship-maintainers are the optimiser; the timbers are the weights; the question is whether the model after 10,000 gradient steps is the same model that was deployed, or a different model.

### 2. Hobbes's variation and the two-ship problem: matter vs. form as competing criteria

Thomas Hobbes introduced the most philosophically generative variation on the Plutarch scenario in *De Corpore* ("On Body"), Part II, Chapter 11, "Of Identity and Difference" (1655). The Wikipedia article on Locke's socks (which covers the Ship of Theseus) reproduces Hobbes's move:

> Hobbes considers the two resulting ships as illustrating two definitions of "Identity" or sameness that are being compared to the original ship: (1) the ship that maintains the same "Form" as the original, that which persists through complete replacement of material; and (2) the ship made of the same "Matter", that which stops being 100 per cent the same ship when the first part is replaced.

Hobbes then adds the generating counterexample: suppose that as each plank is removed from Theseus's ship, it is stored and eventually reassembled into a second ship. Now there are two ships: the gradually renewed ship that has maintained continuous functional operation in Athens harbour (form-identity), and the reassembled ship built from the original planks (matter-identity). Which is the Ship of Theseus? Hobbes's answer (Boston University WCP analysis, bu.edu) is that this is a counterexample to the claim that form alone determines identity: form-identity and matter-identity each pick out a different object, yet both candidates satisfy the criteria for identity under their respective definitions. This is not a paradox but a *bifurcation*: the concept of identity itself has two logically independent components, and Plutarch's scenario drives them apart.

For the organisational mirror thread: the Hobbes bifurcation maps directly onto the distinction between two competing criteria for organisational identity. **Form-identity** ≈ continuity of function, mission, and brand: the organisation is the same organisation if it continues to perform the same function, even if all its people have turned over. **Matter-identity** ≈ continuity of personnel and tacit knowledge: the organisation is the same organisation only if it retains the people whose tacit memories constitute its actual institutional knowledge. Most organisations assert form-identity in their public communications ("We are the same company with the same values") while experiencing matter-identity destruction through turnover, restructuring, and reorganisation. The Hobbes two-ship problem names the precise failure mode: the organisation that asserts form-identity while its matter has been replaced has produced a *replica* of itself, not a continuation.

For the ML mirror thread: the Hobbes bifurcation maps onto the distinction between a model's *architecture* (form) and its *weights* (matter). A model retrained from scratch on the same data with the same architecture is form-identical but not matter-identical. A model whose weights have been fine-tuned is matter-identical in ancestry but may be form-identical in function to a completely different model. The two-ship problem asks: when we say "the same model," which criterion are we applying? The answer determines what it means to say that continual learning has preserved identity.

### 3. Four-dimensionalism, endurantism, and perdurantism: the contemporary metaphysical framework

The contemporary philosophical debate over identity through time is structured by the contrast between **endurantism** (three-dimensionalism) and **perdurantism** (four-dimensionalism). The authoritative academic treatments are Ted Sider's *Four-Dimensionalism: An Ontology of Persistence and Time* (Oxford University Press, 2001) and Katherine Hawley's *How Things Persist* (Oxford University Press, 2001). The Academia.edu summary of Sider (acad. 3074691) provides the key definitions:

- **Endurantism**: objects are extended in three spatial dimensions and persist through time by being *wholly present* at any moment at which they exist. The Ship of Theseus is wholly present at each moment; its identity conditions are specified by criteria that must be satisfied at each moment.
- **Perdurantism**: objects are extended both in space and *time*, and persist by having "temporal parts," no part being present at more than one time. The Ship of Theseus is a four-dimensional "worm" stretched across spacetime; each temporal slice of the worm is a distinct object; the whole worm is the Ship of Theseus.

Katherine Hawley (*How Things Persist*, 2001) defines the perdurantist account of change as "the possession of different properties by different temporal parts of an object" (Wikipedia, Perdurantism article). David Lewis (*On the Plurality of Worlds*, 1986) articulates the same point: change is "the possession of different properties by different temporal parts of an object" (PhilArchive, Persistence as a Four-Dimensionalist). On the perdurantist account, the Ship of Theseus problem dissolves: there is no paradox about which ship is the "real" one because each temporal slice of each candidate ship is a distinct object, and the four-dimensional worm that is "the Ship of Theseus" is simply whichever worm we decide to name. The apparent paradox is generated by endurantist intuitions (the ship must be wholly present at each moment) applied to a scenario that exposes the limits of those intuitions.

For the ML mirror thread: the endurantism/perdurantism distinction maps onto two ways of thinking about a model's identity across training. **Endurantist model identity**: the model is wholly present at each checkpoint; the question of whether checkpoint-N and checkpoint-N+10,000 are "the same model" is a question about whether the criteria for model-identity (same architecture, same name, same deployed endpoint) are satisfied at each checkpoint. **Perdurantist model identity**: the trained model is a four-dimensional object; its history of weight updates is the temporal extension of the model; each checkpoint is a temporal slice; the "same model" just is the complete temporal worm from initialisation to retirement. On the perdurantist account, catastrophic forgetting is not identity-destruction but a discontinuity in the temporal worm — a gap in the history. The chapter should use this framework to argue that the perdurantist account, while philosophically consistent, is practically useless for continual learning: what practitioners need is not a metaphysical account of model-identity but a *functional* account of which learned representations must be preserved for the model to remain *useful*.

### 4. Personal identity over time: Wiggins and Lowe — the *sortal* solution and its organisational applications

David Wiggins's *Sameness and Substance* (Harvard University Press, 1980; revised as *Sameness and Substance Renewed*, Cambridge University Press, 2001) is the most rigorous contemporary analytic treatment of identity through time. Wiggins's central claim is that identity is always *sortal-relative*: to say that x at time t1 is identical to y at time t2, you must specify the *kind* of thing they are (the sortal concept — ship, person, organisation, model). Different sortals license different persistence conditions. A ship and a heap of planks have different persistence conditions; what counts as "the same" ship over time is not the same criterion as what counts as "the same" heap (Wiggins 2001, Scribd; Cambridge University Press review, static.cambridge.org).

For personal identity specifically, Wiggins argues against both pure psychological-continuity theories (neo-Lockean: same person = continuity of memories and psychological states) and pure bodily-continuity theories (same person = continuity of biological substrate). His position is that personal identity is the continuity of a living organism of the kind *human being*, where the persistence conditions for human beings are fixed by biology and psychology jointly. The Cambridge review (static.cambridge.org) notes: "Personal identity is not a matter of the continuity of either mind or body, but of the enduring existence of a kind of creature whose identity conditions are fixed by the nature of that kind." Wiggins explicitly targets Locke's memory theory of personal identity — the claim that personal identity consists in continuity of consciousness mediated by experiential memory — and sides with Bishop Butler's objection that experiential memory presupposes personal identity and cannot explain it.

E. J. Lowe's contribution (principally *Kinds of Being: A Study of Individuation, Identity and the Logic of Sortal Terms*, Blackwell, 1989, and *The Possibility of Metaphysics*, Clarendon Press, 1998) reinforces the sortal framework with a modal argument: the persistence conditions of an object are determined by its *essential* properties, which in turn are fixed by the natural kind to which it belongs. A ship essentially has the property of being a continuous functional artifact of a certain design; it can survive plank replacement but not, for example, being deliberately redesigned into a house. The persistence conditions are not arbitrary conventions but follow from the nature of the sortal.

For the organisational mirror thread: Wiggins's sortal framework is the chapter's most powerful conceptual tool. An organisation's identity conditions are fixed by its sortal — by the *kind* of thing it is. A hospital has different persistence conditions from a consulting firm: a hospital that ceases to provide medical care has ceased to exist as a hospital, regardless of whether its buildings remain. The sortal also fixes what *must* be remembered for the organisation to persist: a hospital must preserve its clinical knowledge and protocols; a consulting firm must preserve its client relationships and methodological frameworks. The mistake of treating all knowledge as equally worth preserving (the "more documentation is better" view of Chs.10–11) is the mistake of applying the wrong persistence conditions — of not knowing which sortal governs the organisation's identity.

For the ML mirror thread: the sortal framework maps onto the distinction between a model's *task-essential* representations and its *incidental* representations. Not all weights are equal; some are constitutive of the model's identity as a model-for-task-X, others are artifacts of training data distribution. Continual learning must identify the sortal of the model — what kind of model it is, what task defines its identity — and use that to specify which representations must be preserved. Elastic Weight Consolidation (EWC, Kirkpatrick et al. 2017) is an implicit sortal theory: the Fisher information matrix identifies which weights are most important for the model's current task (its identity-as-sortal), and regularises against their modification. The chapter can name EWC as the computational implementation of Wiggins's sortal persistence conditions.

***

## Narrative threads for Ch.14

1. **Plutarch's precise formulation** — open with the full passage at 23.1 as the chapter's epigraph. The Athenians did not debate whether to maintain the ship; the philosophical question arose *because* they maintained it so carefully. The paradox is a product of successful preservation, not neglect. This is the chapter's governing irony: the more faithfully you maintain the record, the more acute the identity question becomes.
2. **The Hobbes two-ship bifurcation** — use Hobbes's *De Corpore* split to frame the organisational mirror: form-identity (continuity of function and mission) vs. matter-identity (continuity of personnel and tacit knowledge). Most organisations claim form-identity while suffering matter-identity destruction. The two-ship problem is the story of every post-merger integration, every radical restructuring, every organisation that "transforms" itself while insisting it remains "the same company."
3. **Endurantism vs. perdurantism as models for checkpointing** — use the Sider/Hawley framework to distinguish two approaches to model identity: the checkpoint-as-whole-model (endurantist) vs. the training-history-as-4D-worm (perdurantist). Argue that perdurantism, while philosophically consistent, is operationally vacuous: practitioners need *functional* identity criteria, not metaphysical ones.
4. **Wiggins's sortal as the design requirement** — the chapter's constructive move: specify the *sortal* of your organisation (or model), derive its persistence conditions from the nature of that sortal, and use those conditions to identify what *must* be preserved. This is the design principle that Chs.9–11 lacked: not "preserve everything" but "preserve what is essential to being this kind of thing."
5. **EWC as applied Wiggins** — close the ML mirror thread with Elastic Weight Consolidation as the computational implementation of sortal-relative persistence: the Fisher information matrix identifies the weights that are task-essential (the organisational sortal's persistence conditions), and EWC regularises against their destruction. Book 2 will need to examine whether EWC actually works — i.e., whether Fisher information is a reliable proxy for task-essentiality.

***

## Open questions
> ⚠️ Flag for ARC fact-check issue (create separately):

1. **[Hobbes *De Corpore* 1655 — chapter and section reference for the Ship of Theseus passage]** — Hobbes's version of the Ship of Theseus problem is cited to *De Corpore*, Part II, Chapter 11, "Of Identity and Difference" (1655). Multiple secondary sources confirm this attribution but without a verified page or section number from a standard edition. The Wikipedia article notes Hobbes refers to the ship as the *Argo* rather than Theseus's galley. Both the precise locus and the *Argo* vs. Theseus confusion require verification against a primary edition of *De Corpore*.  
   Suggested query: `"Hobbes De Corpore 1655 Part II Chapter 11 Of Identity Difference Ship Theseus Argo passage section page standard edition English translation Molesworth"`

2. **[Sider *Four-Dimensionalism* 2001 — Oxford University Press, full bibliographic details]** — Ted Sider's *Four-Dimensionalism: An Ontology of Persistence and Time* is cited as Oxford University Press, 2001. The Academia.edu entry confirms this. However, the full subtitle, ISBN, and whether a paperback edition with different pagination was issued should be confirmed before use as a primary citation.  
   Suggested query: `"Ted Sider Four-Dimensionalism Ontology Persistence Time Oxford University Press 2001 ISBN full title bibliographic details edition paperback"`

3. **[Wiggins *Sameness and Substance Renewed* 2001 — relationship to the 1980 first edition]** — The research cites both the 1980 Harvard edition (*Sameness and Substance*) and the 2001 Cambridge revised edition (*Sameness and Substance Renewed*). The Cambridge review (static.cambridge.org) confirms the 2001 edition exists and discusses Locke. The chapter must specify which edition's argument it is using at each point: the 1980 and 2001 editions differ substantially in their treatment of personal identity. The Scribd excerpt appears to be from the 2001 edition.  
   Suggested query: `"David Wiggins Sameness and Substance 1980 Harvard vs Sameness and Substance Renewed 2001 Cambridge differences revisions personal identity chapter changes"`

4. **[EWC / Kirkpatrick et al. 2017 — correct citation for Elastic Weight Consolidation]** — Elastic Weight Consolidation is attributed to Kirkpatrick et al. 2017. The full citation ("Overcoming catastrophic forgetting in neural networks," *Proceedings of the National Academy of Sciences*, 2017) should be confirmed with volume, issue, pages, and DOI before the chapter uses it as a primary ML source. This is the bridge citation linking the philosophical framework of the chapter to Book 2's technical argument.  
   Suggested query: `"Kirkpatrick Overcoming catastrophic forgetting neural networks PNAS 2017 volume issue pages DOI Elastic Weight Consolidation full citation"`

***

## Definition of done (ARC-14 checklist)
- [x] Notes committed with citations
- [x] Open questions logged
- [ ] PR linked
