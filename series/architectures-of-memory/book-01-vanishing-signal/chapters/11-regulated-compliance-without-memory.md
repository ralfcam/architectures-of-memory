# Chapter 11 — The Regulated Industry as an Extreme Case: Compliance Without Memory

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
