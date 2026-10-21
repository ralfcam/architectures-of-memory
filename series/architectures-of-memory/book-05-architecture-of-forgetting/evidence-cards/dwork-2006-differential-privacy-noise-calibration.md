---
type: Evidence Card
title: "Calibrating Noise to Sensitivity for Differential Privacy (Dwork et al. 2006)"
description: "Calibrating additive noise to the global sensitivity of a query function establishes mathematically proven epsilon-differential privacy, bounding information leakage about any individual record regardless of auxiliary adversary knowledge."
tags: [differential-privacy, laplace-mechanism, global-sensitivity, privacy-guarantees]
status: stable
confidence: high
generated: { by: agent:antigravity, at: 2026-10-21T21:32:00Z }
stale_after: 2028-01-01T00:00:00Z
series_domains: [technical, organizational, philosophical]
chapter_hooks: [anomaly, mechanism, boundary]
sources:
  - id: Dwork_2006
    resource: https://doi.org/10.1007/11681878_14
    title: "Dwork et al. (2006), Calibrating Noise to Sensitivity in Private Data Analysis"
---

# Calibrating Noise to Sensitivity for Differential Privacy

> Domain: privacy / differential-privacy
> Last updated: 2026-10-21
> Status: Stable (mathematical foundation theorem)

## What We Know

Adding noise drawn from a Laplace distribution scaled to the global $L_1$ sensitivity $\Delta f$ divided by $\epsilon$ ($\text{Lap}(\Delta f / \epsilon)$) guarantees $\epsilon$-differential privacy, ensuring that the presence or absence of any single individual in a database alters query output distributions by at most a multiplicative factor of $e^\epsilon$.

## How Confident We Are

**Grade**: High

Proven as a mathematical theorem by Dwork, McSherry, Nissim, and Smith (2006), establishing the foundational theoretical framework for algorithmic privacy, composition theorems, and privacy accounting across computer science and statistical agencies.

## Evidence and Causal Assessment

Formal mathematical proof demonstrates that differential privacy provides a worst-case information-theoretic bound that holds independently of any computational constraints or external side-channel auxiliary information available to an attacker.

## Effect Size and Persistence

The guarantee is invariant under post-processing: any computation performed on an $\epsilon$-differentially private output remains $\epsilon$-differentially private without degradation. Privacy losses compose additively (or sub-additively via advanced composition) across sequential query executions.

## Bias, Heterogeneity, and Confounding

Classified as `n/a (formal theorem)`. The mathematical privacy bound is exact. Practical trade-offs center on utility loss: for queries with high global sensitivity, additive noise can overwhelm signal unless sample size $N$ is sufficiently large.

## What Remains Uncertain

Determining socially and operationally optimal values of the privacy budget $\epsilon$ across high-dimensional empirical analytics without destroying analytical utility for rare sub-populations.

## What This Does Not Mean

Differential privacy does not guarantee that true population-level facts about a cohort cannot be discovered; it guarantees that participating in the dataset exposes no additional individual risk relative to not participating.

## What Action Is Reasonably Justified

Require differential privacy formalisms and calibrated noise mechanisms for sensitive database queries, public data releases, and synthetic dataset generation.

## Sources

- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating Noise to Sensitivity in Private Data Analysis. In *Theory of Cryptography Conference* (pp. 265-284). Springer, Berlin, Heidelberg. https://doi.org/10.1007/11681878_14
