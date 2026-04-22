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
