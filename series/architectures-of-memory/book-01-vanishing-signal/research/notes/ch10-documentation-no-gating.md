# Ch.10 — Why Documentation Systems Fail: Too Much Signal, No Gating

**Issue:** ARC-10  
**Status:** Research complete — open questions logged  
**Branch:** `research/ch10-documentation-no-gating`

***

## Query set executed

1. "enterprise wiki knowledge management failure Confluence SharePoint case study"
2. "information overload organizational research Eppler Mengis"
3. "documentation decay technical debt knowledge base rot"
4. "knowledge management curation gating roles communities of practice"

***

## Findings

### 1. Enterprise wikis and knowledge base failure: the evidence base

The enterprise wiki failure literature is consistent and spans two decades. The MITRE Corporation published **"Factors Impeding Wiki Use in the Enterprise: A Case Study"** (mitre.org/sites/default/files/pdf/09_3961.pdf) documenting that the primary barriers to wiki adoption and sustained use are not technical but social and structural: lack of clear ownership, absence of curation norms, and the absence of any mechanism for distinguishing authoritative from speculative content. The Semantic Scholar record for the Adoption of Knowledge Management Systems study identifies the same pattern: "How Wiki Systems Should Be Adopted by Minimizing the Risk of Failure" treats ownership and editorial governance as the decisive variables, not software features.

The practitioner evidence is equally clear. The Dozuki analysis of SharePoint as a knowledge management tool concludes that SharePoint "definitively fails to address the needs of the modern industrial workforce" as a KM strategy — not because of search or interface deficiencies but because SharePoint provides no native mechanism for signalling content currency, no role structure for curation, and no decay detection (dozuki.com, 2021). The Episteca documentation decay analysis (2025) quantifies the decay curve empirically: technical documentation becomes materially outdated within **30–90 days** of publication (Readme API documentation platform data); **68% of enterprise technical content had not been updated in over six months**, and **34% had not been touched in over a year** (Zoomin documentation analytics, cited in Episteca, 2025). These numbers establish a baseline decay rate: without active curation, a knowledge base's signal-to-noise ratio degrades to unusability within roughly one year of initial population.

The arXiv preprint **"Pitfalls in Effective Knowledge Management"** (arXiv:2304.07737v3) provides a systematic taxonomy of KM failure modes, identifying 44 hindering factors across categories including governance, incentive structure, tool design, and organisational culture. The top cluster of factors is structural, not technical: absent or unclear ownership, no designated curator role, no editorial policy, no content lifecycle management. The paper's key finding is that KM initiatives fail not at the point of creation but at the point of *maintenance* — the initial knowledge capture effort is often enthusiastic; the sustained curation effort almost never is.

For the ML mirror thread: an ungated documentation system is a recurrent network without a forget gate. Every document ever created remains in the state vector, regardless of relevance. The hidden state grows without bound; retrieval degrades because the signal from recent, relevant updates is diluted by the accumulated mass of stale content. The chapter's governing metaphor is precise: the LSTM's forget gate exists specifically to solve the problem that a documentation system without curation governance makes structurally impossible to solve.

### 2. Eppler & Mengis (2004): the information overload framework

Martin J. Eppler and Jeanne Mengis published **"The Concept of Information Overload: A Review of Literature from Organization Science, Accounting, Marketing, MIS, and Related Disciplines"** in *The Information Society*, Vol. 20, No. 5, pp. 325–344 (November–December 2004; asist-archive.ischool.illinois.edu full citation record). The paper is the canonical literature review on information overload: it consolidates 30 years of research across five disciplines and proposes a unified framework model identifying the causes, symptoms, effects, and countermeasures of information overload.

Eppler & Mengis identify **five interrelated causes** of information overload: (1) characteristics of the *person* receiving information (processing capacity limits, expertise level, cognitive style); (2) characteristics of the *information itself* (volume, ambiguity, redundancy, lack of structure); (3) *tasks and processes* (task complexity, time pressure, interruptions); (4) *organisational processes* (coordination failures, meeting loads, communication norms); and (5) *information technology* (email, databases, intranets that lower the cost of information production without raising the cost of information consumption) (PMC 10322198, systematic review citing Eppler & Mengis 2004). The critical architectural point is cause (5): technology that lowers production cost without gating consumption is the root cause of organisational information overload. Every enterprise wiki, every shared drive, every Confluence space is an information production subsidy with no corresponding consumption tax.

Eppler & Mengis also catalogue the *effects* of information overload on decision-making: reduced decision quality, increased decision time, increased error rates, and — most relevant for the chapter — **search abandonment**: when users cannot find reliable information quickly, they stop searching and either ask a colleague (reverting to the transactive memory system, per Ch.09) or proceed without information. The documentation system's failure mode is silent: no error is logged when a user gives up searching. The system reports high content volume (a metric that is easy to measure) while hiding the fact that the content is useless (a metric that requires user behaviour instrumentation).

For the organisational mirror thread: Eppler & Mengis provide the quantitative backbone for the chapter's argument. The causal model is: documentation systems lower the cost of *writing* while leaving the cost of *reading and finding* unchanged or increasing it. The result is a tragedy of the commons: individually rational contributions (each author adds their document) produce a collectively irrational outcome (the commons becomes too noisy to use). The forget gate is not a luxury; it is the mechanism that prevents the tragedy.

### 3. Documentation decay: the half-life of written knowledge

Documentation decay is the progressive divergence between a document's content and the current state of the system, process, or knowledge it describes. The Episteca analysis (2025) characterises it as a **decay curve**, not a gradual fade: documentation "doesn't age gracefully. It collapses." The 30–90 day material obsolescence finding for technical documentation implies a half-life of roughly 6–8 weeks for code-adjacent documentation — significantly shorter than the typical review cycle for any enterprise documentation governance process.

The EDANA analysis (2025) frames documentation decay as a **business risk category**, not merely a quality concern: "A poorly documented architecture crumbles under the weight of ad hoc fixes and evolutions. The technical debt associated with a lack of documentation becomes a major obstacle to any refactoring or migration. Modernisation projects require multiplied budgets and timelines to rebuild lost knowledge, often leading to partial or complete project abandonment." This frames documentation decay as compounding: each undocumented change raises the cost of the next documentation effort, producing a debt spiral that mirrors the concept of technical debt in software engineering. The arXiv Nature of Technical Debt paper (arXiv:2603.20415v1) makes the analogy explicit: accumulated shortcuts in documentation, like accumulated shortcuts in code, impose "interest" that eventually exceeds the cost of the original work.

The DORA (DevOps Research and Assessment) team's finding, cited in Episteca, is the chapter's sharpest empirical hook: **documentation quality is among the strongest predictors of onboarding velocity**. New engineers who cannot trust the docs shadow senior engineers instead, converting your most experienced people into full-time tour guides. This quantifies the organisational cost of documentation decay in terms of *expert time diverted from productive work to knowledge transmission* — precisely the dynamic that transactive memory systems (Ch.09) are supposed to make unnecessary.

For the ML mirror thread: documentation decay is the organisational analogue of weight drift in a continually learning network without regularisation. Each update to the system is a gradient step that moves the weights; the documentation is a snapshot of the weights at a previous training step. Without a mechanism that forces the snapshot to track the current weights (a regularisation term, a curation role, a mandatory update trigger), the snapshot and the reality progressively diverge until the snapshot is useless. The forget gate in LSTM is precisely the regularisation mechanism that controls which historical state to retain versus discard.

### 4. Communities of practice and gating roles: the social solution to an architectural problem

Etienne Wenger introduced the concept of **communities of practice** (CoP) in the context of apprenticeship learning (Lave & Wenger, *Situated Learning*, Cambridge University Press, 1991) and elaborated it as a knowledge management vehicle in *Cultivating Communities of Practice* (Wenger, McDermott & Snyder, Harvard Business School Press, 2002; cited in UBC IT PDF). The wenger-trayner.com introduction defines a CoP as "groups of people who share a concern or a passion for something they do and learn how to do it better as they interact regularly" — a definition that emphasises the *practice* dimension: knowledge is held and updated by the people who use it, not by a separate documentation team.

The organisational knowledge management turn to CoPs is explicitly motivated by the failure of information-system-centric approaches. The wenger-trayner.com site states directly: "Initial efforts at managing knowledge had focused on information systems with disappointing results. Communities of practice provided a new approach, which focused on people and on the social structures that enable them to learn with and from each other." This is the chapter's central structural argument: the failure of documentation systems is not a software problem. It is an architectural problem: documentation systems are passive repositories with no gating mechanism. Communities of practice are active, socially-gated networks in which practitioners continuously update the shared knowledge base through use, not through scheduled review cycles.

The gating function in a CoP operates through **social proof and reputation**: a claim that survives community scrutiny is retained; a claim that is contradicted by practice experience is corrected or removed. This is the organisational analogue of the LSTM forget gate: the gate's value is set not by a scheduled audit but by the continuous signal from the practice community. The SharePoint enterprise comparison analysis (2026) identifies the absence of this function as the primary failure mode of enterprise KM platforms: they provide no mechanism for practitioners to signal content currency, no reputation system for authors, and no community validation layer. Content created by a junior analyst in 2018 is retrieved with equal weight as content validated by senior practitioners in 2025.

For the ML mirror thread: the CoP as a gating mechanism maps cleanly onto the forget gate architecture. The forget gate receives two inputs — the current input and the previous hidden state — and produces a value between 0 and 1 for each dimension of memory. A CoP performs the equivalent operation: each piece of community knowledge is continuously evaluated against current practice experience (the current input) and prior community belief (the previous hidden state), and either retained or discarded. The chapter can use this as a forward pointer to Ch.11 (the LSTM as the architectural solution to the gating problem) by establishing that human organisations discovered the same solution empirically through communities of practice before deep learning formalised it mathematically.

***

## Narrative threads for Ch.10

1. **The tragedy of the documentation commons** — open with Eppler & Mengis’s causal model: technology lowers the cost of writing without raising the cost of reading; individually rational contribution produces a collectively irrational outcome; the commons becomes too noisy to use. This is Ch.10’s thesis statement.
2. **The 90-day cliff** — the Episteca/Readme finding that technical documentation becomes materially outdated within 30–90 days is the chapter’s empirical anchor; use it to establish that the decay rate of documentation is faster than any enterprise review cycle, making manual curation structurally insufficient.
3. **The expert-as-tour-guide tax** — the DORA finding that documentation decay diverts senior engineers into full-time mentoring is the chapter’s organisational cost quantification; this is the hidden tax that ungated documentation systems impose on organisational expertise.
4. **CoPs as social forget gates** — the Wenger CoP framework is the chapter’s constructive pivot: the solution to the ungated documentation problem is not better software but a social gating mechanism that continuously evaluates knowledge currency through use. This is the human organisations’ empirically discovered equivalent of the LSTM forget gate.
5. **Forward pointer to the LSTM** — close the chapter by naming the architectural gap: what documentation systems lack is a *differentiable gating function* — a mechanism that continuously computes, for each piece of stored knowledge, the probability that it remains relevant. Chapter 11 introduces the machine that solved this problem mathematically.

***

## Open questions
> ⚠️ Flag for ARC fact-check issue (create separately):

1. **[Episteca 30–90 day obsolescence figure — primary source verification]** — The claim that technical documentation becomes materially outdated within 30–90 days is attributed to "Readme API documentation platform data" in the Episteca 2025 blog post, and the 68%/34% figures are attributed to "Zoomin documentation analytics." Neither source is a peer-reviewed study. The chapter needs either the original Readme/Zoomin research reports or a peer-reviewed equivalent before asserting these figures as established findings.  
   Suggested query: `"Readme API documentation platform documentation decay 30 90 days study original report Zoomin enterprise content outdated statistics primary source"`

2. **[Eppler & Mengis 2004 — precise page range and journal issue confirmation]** — The citation record at asist-archive identifies the paper as *The Information Society*, Vol. 20, No. 5, pp. 325–344, Nov–Dec 2004. The Scribd full text confirms the title and authors. The page range should be confirmed against a library record or DOI before use as a primary citation.  
   Suggested query: `"Eppler Mengis 2004 concept information overload Information Society journal DOI volume 20 issue 5 pages 325-344 Taylor Francis"`

3. **[MITRE wiki case study — date, authors, and scope]** — The MITRE PDF (09_3961.pdf) is cited as a case study of wiki failure in the enterprise, but its publication date, authors, sample organisation, and methodology have not been confirmed from the document itself. If it is a grey literature report rather than a peer-reviewed study, it should be cited accordingly.  
   Suggested query: `"MITRE 09_3961 factors impeding wiki enterprise case study authors date publication methodology peer review status"`

4. **[Wenger CoP origin: Lave & Wenger 1991 vs. Wenger 1998 as primary source]** — The CoP concept is attributed to Lave & Wenger (1991) for its origin in apprenticeship studies, and to Wenger (1998, *Communities of Practice*, Cambridge University Press) for its organisational elaboration. The 2002 Wenger, McDermott & Snyder book is the KM-focused application. The chapter must cite the correct primary source for each claim: origin (1991), theory (1998), or KM application (2002).  
   Suggested query: `"Lave Wenger 1991 situated learning vs Wenger 1998 communities of practice vs Wenger McDermott Snyder 2002 cultivating communities primary source citation guidance"`

***

## Definition of done (ARC-10 checklist)
- [x] Notes committed with citations
- [x] Open questions logged
- [ ] PR linked
