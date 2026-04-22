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
