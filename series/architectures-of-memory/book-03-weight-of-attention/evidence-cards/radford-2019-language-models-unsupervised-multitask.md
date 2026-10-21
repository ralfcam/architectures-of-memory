---
type: Evidence Card
title: "Zero-Shot Multitask Learning via Autoregressive Language Modeling (Radford et al. 2019)"
description: "Training high-capacity autoregressive language models on diverse web corpora enables zero-shot task transfer across reading comprehension, translation, summarization, and question answering without explicit parameter supervision."
tags: [gpt-2, autoregressive, zero-shot, language-modeling]
status: stable
confidence: high
generated: { by: agent:antigravity, at: 2026-10-21T21:25:00Z }
stale_after: 2028-01-01T00:00:00Z
series_domains: [technical, organizational, philosophical]
chapter_hooks: [anomaly, mechanism, boundary]
sources:
  - id: radford2019gpt2
    resource: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
    title: "Radford et al. (2019), Language Models are Unsupervised Multitask Learners"
---

# Zero-Shot Multitask Learning via Autoregressive Language Modeling

> Domain: attention / autoregressive-lm
> Last updated: 2026-10-21
> Status: Stable (replicated benchmark finding)

## What We Know

Language models trained purely to predict next tokens on diverse large-scale text corpora (WebText) develop zero-shot competence across multiple distinct natural language processing tasks without explicit task-specific supervised training or fine-tuning.

## How Confident We Are

**Grade**: High

Demonstrated by Radford et al. (2019) across 8 language modeling benchmarks with state-of-the-art zero-shot perplexity, alongside competitive zero-shot performance on CoQA (55 F1), LAMBADA (63.2% accuracy), and Winograd Schema Challenge (70.3% accuracy).

## Evidence and Causal Assessment

Systematic model scaling from 117M to 1.5B parameters reveals that downstream zero-shot task error rates decrease log-linearly as a causal function of model parameter scale and pre-training log-loss reduction.

## Effect Size and Persistence

Zero-shot GPT-2 1.5B outperformed supervised domain-specific baselines on 7 out of 8 language modeling benchmarks. Cross-task transfer emerged without modifying the causal Transformer decoder architecture or adding specialized task heads.

## Bias, Heterogeneity, and Confounding

Classified as `robust (<20%)`. Web text corpora contain significant memorization risks and 8-gram benchmark test set overlap (memorization rate ~1.2% to 3.8%), although zero-shot performance improvements persisted when evaluated on deduplicated data splits.

## What Remains Uncertain

The degree to which zero-shot capabilities represent emergent generalized induction versus soft fuzzy retrieval from massive internet training sets.

## What This Does Not Mean

Predicting next tokens does not guarantee factual reliability or truthfulness; models generate fluent hallucinations when prompted on non-verifiable or conflicting premises.

## What Action Is Reasonably Justified

Treat next-token autoregressive prediction on diverse text as a universal pre-training engine for generative NLP, while acknowledging that zero-shot instruction following requires explicit demonstration prompting or post-training alignment.

## Sources

- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language Models are Unsupervised Multitask Learners. *OpenAI Technical Report*. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
