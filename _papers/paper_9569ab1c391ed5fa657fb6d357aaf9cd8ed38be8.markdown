---
layout: paper
id: "9569ab1c391ed5fa657fb6d357aaf9cd8ed38be8"
title: "Diffatr: Diffusion-Based Generative Modeling For Audio-Text Retrieval"
publication: "INTERSPEECH"
year: 2024
external_url: https://www.semanticscholar.org/paper/9569ab1c391ed5fa657fb6d357aaf9cd8ed38be8
authors: "Yifei Xin, Xuxin Cheng, Zhihong Zhu, Xusheng Yang, Yuexian Zou"
publication_date: "2024-09-01"
---

Existing audio-text retrieval (ATR) methods are essentially discriminative models that aim to maximize the conditional likelihood, represented as p(candidates|query). Nevertheless, this methodology fails to consider the intrinsic data distribution p(query), leading to difficulties in discerning out-of-distribution data. In this work, we attempt to tackle this constraint through a generative perspective and model the relationship between audio and text as their joint probability p(candidates,query). To this end, we present a diffusion-based ATR framework (DiffATR), which models ATR as an iterative procedure that progressively generates joint distribution from noise. Throughout its training phase, DiffATR is optimized from both generative and discriminative viewpoints: the generator is refined through a generation loss, while the feature extractor benefits from a contrastive loss, thus combining the merits of both methodologies. Experiments on the AudioCaps and Clotho datasets with superior performances, verify the effectiveness of our approach. Notably, without any alterations, our DiffATR consistently exhibits strong performance in out-of-domain retrieval settings.
