---
type: Evidence Card
title: "Empirical Power-Law Scaling of Transformer Language Models (Kaplan et al. 2020)"
description: "Cross-entropy loss in autoregressive Transformer language models scales as a power law with model parameter count, dataset size, and compute budget across more than seven orders of magnitude."
tags: [scaling-laws, compute-optimal, power-law, transformers]
status: stable
confidence: high
generated: { by: agent:antigravity, at: 2026-10-21T21:25:00Z }
stale_after: 2028-01-01T00:00:00Z
series_domains: [technical, organizational, philosophical]
chapter_hooks: [anomaly, mechanism, boundary]
sources:
  - id: kaplan2020arxiv
    resource: https://arxiv.org/abs/2001.08361
    title: "Kaplan et al. (2020), Scaling Laws for Neural Language Models"
---

# Empirical Power-Law Scaling of Transformer Language Models

> Domain: attention / scaling-laws
> Last updated: 2026-10-21
> Status: Stable (replicated empirical law)

## What We Know

Transformer cross-entropy test loss follows power-law relationships with parameter count $N$, dataset token volume $D$, and compute budget $C$ ($L(N) \propto N^{-\alpha_N}$, $L(D) \propto D^{-\alpha_D}$, $L(C) \propto C^{-\alpha_C}$) across more than seven orders of magnitude, with architectural hyper-parameters (aspect ratio, depth vs width) exerting minimal influence.

## How Confident We Are

**Grade**: High

Empirically established by Kaplan et al. (2020) across models from $10^3$ to $10^9$ parameters and compute budgets spanning $10^{17}$ to $10^{23}$ FLOPs, with subsequent structural refinement by Hoffmann et al. (2022 / Chinchilla) confirming the universal validity of power-law frontiers.

## Evidence and Causal Assessment

Controlled parameter grids isolating token horizons, context lengths, and layer geometries demonstrate that model performance depends primarily on scale ($N, D, C$) rather than architectural shape or attention head configuration within standard ranges.

## Effect Size and Persistence

The scaling exponent for parameter scale was estimated at $\alpha_N \approx 0.076$, dataset scale at $\alpha_D \approx 0.057$, and compute at $\alpha_C \approx 0.050$. Optimal allocation dictates that as compute increases, parameter scale and training data should both grow predictably.

## Bias, Heterogeneity, and Confounding

Classified as `robust (<20%)`. Kaplan et al. originally overestimated the relative priority of parameter growth over data volume ($N \propto C^{0.73}, D \propto C^{0.27}$) due to fixed learning rate schedules, an artifact corrected by Hoffmann et al. ($N \propto C^{0.5}, D \propto C^{0.5}$); however, the existence of smooth power-law frontiers remains invariant.

## What Remains Uncertain

The post-scaling ceiling of next-token pre-training loss and whether power-law loss decreases continue to yield proportional gains on complex deductive reasoning benchmarks without test-time compute scaling.

## What This Does Not Mean

Power-law reduction in perplexity does not prevent catastrophic out-of-distribution reasoning failures, nor does it guarantee that continuous pre-training on low-entropy synthetic data avoids model collapse.

## What Action Is Reasonably Justified

Use empirical power-law scaling curves to plan compute allocation, predict target loss, and size model architectures prior to executing multi-million-dollar training runs.

## Sources

- Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). Scaling Laws for Neural Language Models. *arXiv preprint arXiv:2001.08361*. https://arxiv.org/abs/2001.08361
