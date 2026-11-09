---
layout: paper
id: "507ccff63c410fdcbea02399ae830dab461f0d3f"
title: "Skillformer: Skill-Decomposed Adaptation For Audio Language Models"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/507ccff63c410fdcbea02399ae830dab461f0d3f
authors: "Seung-woo Lee, Bo-Wen Qi, Min-jun Kim, Won Jang"
publication_date: "2026-10-06"
---

Audio language models must handle dozens of distinct skills, from pitch comparison and speaker counting to musical tempo estimation and emotion recognition. Joint training on all skills at once causes interference: gains on one skill often come at the cost of another. We propose \textbf{SkillFormer}, which decomposes audio understanding into skill-specific low-rank adapters and composes them at inference time through a learned router. The router examines the question to decide which adapters to activate and how much weight each should carry, so that a pitch query engages different parameters than a genre classification query. An alternating training schedule updates each adapter on its own skill cluster before jointly calibrating the router, preventing the gradient conflicts that arise in standard multi-task optimization. SkillFormer adds fewer than 4\% of the base model's parameters and requires no changes to the audio encoder or language backbone. Evaluated on three architecturally distinct models across MMSU, MMAU-Pro, and MMAR, it raises the average accuracy by 2.5 to 4.1 points, with balanced gains across perception, reasoning, and semantic subcategories.
