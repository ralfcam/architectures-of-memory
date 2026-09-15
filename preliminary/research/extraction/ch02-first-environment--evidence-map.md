# Chapter 2 Evidence Map — The First Environment

First full-system test of the extraction pipeline: raw dossier → atomic claims → likely cards → source/causal labels → manuscript links.

This file started as a map that did **not** create cards. C05 and C07 have since been source-audited into cards; C06 was reconciled. Original uploads stay where they are.

Related: [Ch. 2 triage](../../triage/ch02-first-environment--triage.md) · [draft](../../drafts-chapters/chapter%202) · [seed outline](../../../chapters/01-first-environment.md) · [existing stress card](../../../evidence-cards/prenatal-maternal-stress-anxiety.md) · [voice review](../../drafts-chapters/reviews/ch02-structural-and-voice-review.md)

---

## 1. Files and overlaps

| ID | Path | Role |
|---|---|---|
| C02-D1 | `preliminary/research/Chapter 2 Research Dossier — The First Environment.docx` | Canonical dossier. Already proposes 10 cards. Extract from here. |
| C02-S1 | `preliminary/research/The First Environment_ The Biological Architecture of Early Development.docx` | Alternate module synthesis (clock, placenta, circulation, cortex, stress, nutrition, mixtures, INTERGROWTH). |
| C02-P1 | `preliminary/research/Prenatal Biology Research Plan.docx` | Same byte size as C02-S1, different hash; opening title matches C02-S1. Treat as duplicate/alternate. |
| C02-D | `preliminary/drafts-chapters/chapter 2` | Long prose draft (~4,300 words). |
| Seed | `chapters/01-first-environment.md` | 10-step seed outline. **Numbering collision:** seed Chapter 1 = this Chapter 2. |
| Live cards | `prenatal-maternal-stress-anxiety.md` (C06), `prenatal-auditory-learning.md` (C05), `prenatal-folate-ntd.md` (C07) | C05/C07 source-audited; C06 frontmatter reconciled. All still `status: draft`. |

Do not extract C02-S1 as a second independent source of truth. Use it to recover named studies (DeCasper & Spence; INTERGROWTH-21st; SEPAGES; Bystron; Seckl/11β-HSD2) that C02-D1 cites more vaguely.

---

## 2. Candidate claims (13)

Each row is one claim. Labels: `promote` · `needs-source-audit` · `interpretive-only` · `exclude`.

### CH02-C01 — Developmental timing is process-specific

| Field | Content |
|---|---|
| Claim | The same exposure can have different structural or physiological effects depending on dose, route, and the developmental process underway; “prenatal exposure” is not a single window. |
| Outcome / window | Embryonic patterning vs fetal growth/maturation; not a later IQ endpoint. |
| Exposure | Any timed exposure (nutrient, teratogen, infection). |
| Designs | Developmental-biology sequence evidence; human embryo/gastrulation reviews; limited direct human observation. |
| Effect / persistence | No universal effect size. Unit is exposure × window × process × outcome. Persistence must be measured separately. |
| Threats | Model-system translation; sparse human observation; selection into ART cohorts; mis-timed exposure. |
| Sources (unverified) | C02-D1 refs on peri-implantation/gastrulation (snippet titles only). Need DOI/PMID. |
| Manuscript role | `mechanism` + `boundary` (sensitive ≠ inevitable-injury). |
| Label | `needs-source-audit` |
| Likely card | `prenatal-developmental-timing` |

### CH02-C02 — Placenta mediates fetal dose

| Field | Content |
|---|---|
| Claim | Maternal exposure is not equivalent to fetal dose. The placenta transports, metabolizes, restricts, or facilitates substances; 11β-HSD2 is one documented glucocorticoid buffer and is not absolute. |
| Outcome / window | Fetal circulating/tissue exposure, placental function, selected neonatal growth outcomes. |
| Exposure | Maternal glucocorticoids, nutrients, antibodies (IgG), selected xenobiotics. |
| Designs | Anatomical/physiological reviews; placental enzymology; delivery-sampled tissue (timing bias). |
| Effect / persistence | A placental biomarker is not evidence of lasting impairment. |
| Threats | Placenta sampled at birth; reverse causation; maternal–fetal genotype confounding. |
| Sources (unverified) | Burton 2015 placenta review (PMC, cited in C02-D1); 11β-HSD2 PubMed entries in C02-S1. |
| Manuscript role | `mechanism` |
| Label | `needs-source-audit` |
| Likely card | `placenta-as-mediator` (merge dossier cards 2 and 10) |

### CH02-C03 — Prenatal neural construction is unfinished at birth

| Field | Content |
|---|---|
| Claim | Prenatal neural development proceeds through overlapping proliferation, migration, differentiation, synaptogenesis, and early myelination; the brain remains immature at birth and continues under postnatal experience. |
| Outcome / window | Structure and contemporaneous physiology, not intelligence or personality. |
| Exposure | Construction process itself; severe disruption via IUGR, CMV, Zika as contrast cases. |
| Designs | Developmental neurobiology; human imaging; postmortem/clinical series; animal models for lamination. |
| Effect / persistence | Do not collapse structure, connectivity, cognition, and mental health. |
| Threats | Indirect fetal imaging; clinical-sample selection; postnatal confounding of later outcomes. |
| Sources (unverified) | Bystron et al. on human cortical development (named in C02-S1). |
| Manuscript role | `mechanism` |
| Label | `needs-source-audit` |
| Likely card | `prenatal-neural-construction` |

### CH02-C04 — Fetal autonomic behavior indexes present maturation, not future temperament

| Field | Content |
|---|---|
| Claim | Fetal heart-rate variability, movement, and state organization become more patterned in the second half of gestation; these measures support claims about present capacity, not reliable individual forecasts of later temperament or cognition. |
| Outcome / window | Contemporaneous fetal physiology (~mid-gestation to term). |
| Exposure | Gestational maturation; contrast: chronic hypoxemia/IUGR (depressed variability). |
| Designs | Longitudinal fetal neurobehavior cohorts; observational HRV studies. |
| Effect / persistence | Primary outcomes are now-measures. Later associations = prediction, not a persistent fetal trait. |
| Threats | Indirect measurement; fetal state and maternal movement; publication bias toward striking findings. |
| Sources (unverified) | C02-D1 “Studies in Fetal Behavior”; Pollatou 2024 mapping paper. |
| Manuscript role | `mechanism` + `boundary` |
| Label | `needs-source-audit` |
| Likely card | `fetal-autonomic-maturation` |

### CH02-C05 — Prenatal auditory discrimination is not “prenatal learning” as popularly sold

| Field | Content |
|---|---|
| Claim | Near-term fetuses and newborns can discriminate and prefer speech patterns heard before birth (classic: maternal-voice/story preference). This is sensory discrimination / short-horizon memory-like habituation, not evidence of complex prenatal cognition or lasting cognitive advantage. |
| Outcome / window | Late fetal / newborn preference and habituation. |
| Exposure | Repeated maternal speech / story reading. |
| Designs | Experimental newborn preference (DeCasper & Spence 1986); later habituation studies. Seed outline currently grades perceptual tuning **Moderate**, long-term learning **Low**. |
| Effect / persistence | Short-lived postnatal preference; long-term cognitive advantage **not** established. |
| Threats | Small classic samples; postnatal reinforcement (same parent continues the behavior); over-translation. |
| Sources | DeCasper & Spence 1986 DOI `10.1016/0163-6383(86)90025-1`; Partanen et al. 2013 PMC3847147. |
| Manuscript role | `anomaly` + `case` (seed opening: newborn turns toward a voice heard before birth) |
| Label | `promote` — card `evidence-cards/prenatal-auditory-learning.md` |
| Likely card | `prenatal-auditory-learning` |

### CH02-C06 — Population-range prenatal stress/anxiety associations largely attenuate under genetically informed designs

| Field | Content |
|---|---|
| Claim | Observational prenatal stress/anxiety associations with birthweight, gestational age, and offspring emotional/behavioral difficulties attenuate substantially — often toward the null — in sibling, children-of-twins, and related designs. Physiological pathways (HPA, placental 11β-HSD2) can exist without licensing a general lifelong forecast. |
| Outcome / window | Birth outcomes and early behavioral difficulties; not adult personality. |
| Exposure | Population-range maternal stress/anxiety/depressive symptoms (not disaster/trauma by default). |
| Designs | MoBa triangulation; UK Millennium sibling comparison; genetically informed meta-analysis; children-of-twins. |
| Effect / persistence | Observational small-to-moderate; genetically informed often indistinguishable from zero. Concurrent postnatal maternal symptoms retain a small nongenetic effect (existing card: r ≈ .13). **Largely confounded (>50%)** for prenatal-specific path. |
| Threats | Genetic transmission; shared family environment; residual severe-exposure heterogeneity. |
| Sources (verified in `SOURCES.md`) | `bmc-moba-2025`, `ije-millennium-2017`, `jaacap-meta-2021`, `lancet-psych-2018`. Dossier Card 5 agrees but does not use these IDs. |
| Manuscript role | `boundary` + `system` |
| Label | `promote` — frontmatter `confidence: low-to-moderate`; `status` still `draft`. |
| Likely card | existing `prenatal-maternal-stress-anxiety` |

### CH02-C07 — Periconceptional folic acid reduces neural-tube-defect risk

| Field | Content |
|---|---|
| Claim | Periconceptional folic acid supplementation reduces neural-tube-defect-affected pregnancy in randomized evidence (dossier-reported RR 0.31, 95% CI 0.17–0.58 across five trials). This does not generalize to all anomalies, intelligence, or “optimal development.” |
| Outcome / window | Neural-tube defects; periconception / early embryonic neurulation. |
| Exposure | Folic acid (and WHO antenatal iron + folic acid for anemia-related outcomes). |
| Designs | RCTs and systematic reviews; WHO antenatal guidelines. |
| Effect / persistence | Large relative-risk reduction for NTD; persistence is structural (present or absent), not fading IQ. |
| Threats | Baseline fortification; dose/timing/adherence; over-generalization to all nutrition. |
| Sources | De-Regil et al. 2015 Cochrane PMC8783750 (RR 0.31, 0.17–0.58, 5 RCTs); MRC 1991 *Lancet*; WHO ANC 2016. |
| Manuscript role | `evidence` / `mechanism` (iodine is a separate card) |
| Label | `promote` — card `evidence-cards/prenatal-folate-ntd.md` |
| Likely card | `prenatal-folate-ntd` |

### CH02-C08 — Severe early iodine deficiency can disrupt neurodevelopment; late correction does not rewind early corticogenesis

| Field | Content |
|---|---|
| Claim | Fetal brain thyroid hormone in the first half of pregnancy depends on maternal T4. Severe iodine deficiency causes endemic cretinism; milder early hypothyroxinemia is associated with altered cortical organization. This is a substrate-and-timing claim, not a brief for supplement maximalism in replete populations. |
| Outcome / window | Early–mid gestation neurogenesis/migration; later cognitive impairment in severe deficiency. |
| Exposure | Maternal iodine / thyroid hormone. |
| Designs | Physiological necessity; clinical/endemic-deficiency evidence; observational milder-deficiency studies. |
| Effect / persistence | Severe deficiency: large, lasting neurological injury. Mild deficiency: smaller, more contested. |
| Threats | Population iodine status; over-translation of endemic data to replete settings. |
| Sources (unverified) | C02-S1 iodine/neurodevelopment PMC links. |
| Manuscript role | `mechanism` + `anomaly` (timing) |
| Label | `needs-source-audit` |
| Likely card | `prenatal-iodine-thyroid` (keep separate from C07) |

### CH02-C09 — Prenatal alcohol can disrupt development across stages (FASD)

| Field | Content |
|---|---|
| Claim | Prenatal alcohol exposure is causally implicated in fetal alcohol spectrum disorders spanning growth, facial, and neurobehavioral outcomes. This is not a claim that any detected exposure equals FASD, nor that all neurobehavioral problems are alcohol-caused. |
| Outcome / window | Multiple gestational stages; neurobehavioral range. |
| Exposure | Maternal alcohol. |
| Designs | Clinical teratology; dose-range observational and clinical series. |
| Effect / persistence | Severity is dose- and timing-dependent; persistence is often substantial for FASD, not for unmeasured low-level exposure. |
| Threats | Exposure measurement; polysubstance confounding; stigma-driven underreport. |
| Sources (unverified) | C02-D1 FASD review snippets. |
| Manuscript role | `evidence` |
| Label | `needs-source-audit` |
| Likely card | `prenatal-alcohol-fasd` (teratogen family) |

### CH02-C10 — Maternal tobacco smoke is associated with reduced fetal growth, with dose-response evidence

| Field | Content |
|---|---|
| Claim | Active (and, in some syntheses, passive) maternal tobacco exposure is associated with lower birthweight and higher preterm risk, with reported dose-response. This is a birth-size/preterm claim, not a personality or IQ card. |
| Outcome / window | Fetal growth, LBW, preterm. |
| Exposure | Tobacco smoke. |
| Designs | Observational epidemiology with dose-response; not genetically informed in the dossier. |
| Effect / persistence | Birth-size effects better supported than long-run cognition. |
| Threats | SES, co-exposures, partner smoking, residual confounding. |
| Sources (unverified) | C02-D1 tobacco/stunting and active/passive smoking snippets. |
| Manuscript role | `evidence` |
| Label | `needs-source-audit` |
| Likely card | `prenatal-tobacco-birthweight` (same teratogen family as C09, separate claim) |

### CH02-C11 — Environmental mixtures (PM2.5, phthalates) are plausible but weakly identified for child outcomes

| Field | Content |
|---|---|
| Claim | Many pollutants can cross or alter the placenta. Mixture studies (e.g. SEPAGES) report associations with placental/hemodynamic markers. This does not establish that typical consumer-level detection causes permanent injury, nor that individual purification is the implied action. |
| Outcome / window | Placental biomarkers, fetal hemodynamics; child neurodevelopment mostly unproven here. |
| Exposure | Air pollution and chemical mixtures. |
| Designs | Environmental epidemiology; mixture models; mechanistic oxidative-stress work. |
| Effect / persistence | Uncertain fetal dose, thresholds, reversibility. |
| Threats | Multiple-exposure bias; SES; residential confounding; mechanism-to-outcome leap. |
| Sources (unverified) | SEPAGES / Philippat work named in C02-S1. |
| Manuscript role | `boundary` + `system` (institutional, not parental purity) |
| Label | `needs-source-audit` |
| Likely card | `prenatal-environmental-mixtures` |

### CH02-C12 — Fetal growth restriction is a clinical outcome, not a destiny

| Field | Content |
|---|---|
| Claim | Fetal growth reflects genes, placenta, maternal condition, and environment. Severe restriction is clinically meaningful. Birth size is not a proxy for intelligence, worth, or future personality. Many term infants show postnatal catch-up; catch-up does not erase every risk. |
| Outcome / window | Fetal measures → birth → infancy → age 3. |
| Exposure | Placental insufficiency and related constraints (not “smallness” as a trait). |
| Designs | Placental physiology; longitudinal growth follow-up; INTERGROWTH-21st standards vs regional references (measurement, not destiny). |
| Effect / persistence | Distinguish percentile difference, functional difference, and impairment. |
| Threats | Dating error; constitutional smallness; collider/selection; postnatal nutrition. |
| Sources (unverified) | INTERGROWTH-21st; catch-up growth follow-ups in C02-D1. |
| Manuscript role | `boundary` + `system` |
| Label | `needs-source-audit` |
| Likely card | `fetal-growth-not-destiny` |

### CH02-C13 — Prenatal differences can attenuate, persist, or change form after birth

| Field | Content |
|---|---|
| Claim | Prenatal development is plastic: early biological differences can attenuate, persist, or transform under postnatal environments. Plasticity is not unlimited reversibility; persistence is not inevitability. |
| Outcome / window | Fetal → neonatal → infancy → age 3. |
| Exposure | Any prenatal risk whose later meaning is in question. |
| Designs | Longitudinal follow-up; canalization literature (named in C02-S1). |
| Effect / persistence | Persistence must be measured, not assumed. |
| Threats | Attrition; regression to the mean; differential postnatal opportunity. |
| Sources (unverified) | C02-D1 catch-up papers; canalization review. |
| Manuscript role | `system` + `boundary` (prenatal-to-postnatal continuity) |
| Label | `needs-source-audit` |
| Likely card | `prenatal-postnatal-continuity` |

### Not extracted as standalone cards

| Candidate | Decision |
|---|---|
| Fetal circulation / shunts | `interpretive-only` — mechanism supporting C02/C12, not a claim with a child outcome. |
| Maternal immune activation / IL-6 | Hold. Human evidence is thinner than rodent lamination models; belongs with infection/teratogen family after source audit, not a first-wave card. |
| “Optimal prenatal environment” / supplement maximalism | `exclude` |
| Prenatal personality, fixed temperament, parental fate | `exclude` |

---

## 3. Likely evidence cards (10)

| Proposed card | Claims | Seed/draft hook | First action |
|---|---|---|---|
| `prenatal-developmental-timing` | C01 | Draft § “A Clock Before Memory”; seed competing explanations | Source-audit gastrulation/embryology reviews |
| `placenta-as-mediator` | C02 | Draft § “The Placenta” | Register Burton 2015 + 11β-HSD2 papers |
| `prenatal-neural-construction` | C03 | Draft § “Building a Brain” | Register Bystron; keep IUGR/Zika as contrast, not the claim |
| `fetal-autonomic-maturation` | C04 | Draft § “The Fetus Begins to Regulate Itself” | Fetal HRV primary sources |
| `prenatal-auditory-learning` | C05 | Seed phenomenon/case; draft does not yet open on the voice anomaly | DeCasper & Spence + replication search |
| `prenatal-maternal-stress-anxiety` | C06 | Draft § “Stress: The Biology and the Story” | **Reconcile existing card**; then assign frontmatter confidence |
| `prenatal-nutrition-micronutrients` | C07 | Draft § “Nutrition Is Construction Material” | WHO + folate RCT/Cochrane identifiers |
| `prenatal-iodine-thyroid` | C08 | Draft § “Iodine and the Problem of Timing” | Separate from C07 |
| `prenatal-alcohol-fasd` + `prenatal-tobacco-birthweight` | C09, C10 | Draft § “Beyond the Maternal Body” | Two cards, one teratogen family; mixtures = C11 |
| `fetal-growth-not-destiny` + `prenatal-postnatal-continuity` | C12, C13 | Draft §§ “Fetal Growth…”, “Plasticity”, “Birth Is a Change of Environment” | Continuity card also feeds Chapter 3 |

That is 11 filenames if alcohol and tobacco stay split, plus continuity. If grouping must stay near “8–15 claims / several cards,” the promotion set is **ten cards**, with C09/C10 as one teratogen card containing two claims if editorial economy requires it. Prefer the split: alcohol and tobacco have different identification strength.

---

## 4. Source-resolution queue (not yet in `SOURCES.md`)

Priority for the next extraction commit, not done here:

1. DeCasper & Spence 1986 — prenatal story/voice preference
2. Burton GJ 2015 — placenta as multifaceted organ (PMC)
3. Bystron, Blakemore, Rakic (or successor) — human cortical development
4. WHO antenatal care recommendations; folate NTD systematic review (need the five-trial paper behind RR 0.31)
5. INTERGROWTH-21st fetal growth standards
6. FASD neurobehavioral review named in C02-D1
7. Tobacco/low-birthweight dose-response paper named in C02-D1
8. SEPAGES mixture papers (Philippat)
9. Placental 11β-HSD2 / HSD11B2 epigenetic papers (mechanism for C02 and C06, not a substitute for genetically informed child-outcome evidence)

Existing verified sources already covering C06: `bmc-moba-2025`, `ije-millennium-2017`, `jaacap-meta-2021`, `lancet-psych-2018`.

The 12 first-pass unresolved citations in `SOURCES.md` have been resolved (other live cards, not this map). Remaining Chapter 2 work is C01–C04 and C08–C13.

---

## 5. Links into the manuscript

| Composition beat | Draft / outline location | Claims |
|---|---|---|
| Phenomenon / anomaly | Seed §§1–3 (voice/story). Draft currently opens on mediated systems, not the voice anomaly. | C05 |
| Puzzle / question | Seed §4; draft “A prenatal exposure is not automatically a fetal dose” | C02, C06 |
| Competing explanations | Seed §5 (learning vs tuning vs genetic confounding) | C05, C06 |
| Mechanism | Draft placenta, circulation, brain, iodine | C01–C04, C08 |
| Evidence | Nutrition, alcohol, tobacco, stress triangulation | C06–C10 |
| Boundary | Draft “What the First Environment Does Not Tell Us” | C04, C06, C12, C13 |
| System | Draft closing; seed §9 (language, attachment, regulation) | C13 → Ch. 3 and 4 |
| Return | Draft “Before the First Breath”; seed §10 | C13 |

Canonical seed still lists only the stress card plus “future cards on prenatal auditory exposure, birth, skin-to-skin.” Birth/skin-to-skin belong to **Chapter 3**, not this map.

---

## 6. What this map tested

| Pipeline step | Result |
|---|---|
| Inventory and overlaps | Three research files + draft + seed + one live card |
| Atomic claims | 13 claims; 2 interpretive/exclude holds |
| Card grouping | 10–11 likely cards; not one “prenatal development” card |
| Causal designs / confounds | Recorded per claim; genetically informed evidence only solid for C06 |
| Labels | 3 `promote` (C05, C06, C07); remaining C01–C04 and C08–C13 still `needs-source-audit`; several `interpretive-only`/`exclude` |
| Manuscript link | Seed outline is voice-anomaly-led; long draft is mechanism-led. Voice review captures the gap; draft is not overwritten. |

Next concrete extraction step: source-audit remaining Chapter 2 claims C01–C04 and C08–C13 (timing, placenta, neural construction, autonomic maturation, iodine, alcohol, tobacco, growth).
