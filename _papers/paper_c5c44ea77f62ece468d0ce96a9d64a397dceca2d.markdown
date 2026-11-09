---
layout: paper
id: "c5c44ea77f62ece468d0ce96a9d64a397dceca2d"
title: "Omni-Embed-Audio: Leveraging Multimodal Llms For Robust Audio-Text Retrieval"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/c5c44ea77f62ece468d0ce96a9d64a397dceca2d
authors: "Haejun Yoo, Yong-Joo Shin, Insung Lee, M. Koo, Du-Seong Chang"
publication_date: "2026-04-20"
---

Audio-text retrieval systems based on Contrastive Language-Audio Pretraining (CLAP) achieve strong performance on traditional benchmarks; however, these benchmarks rely on caption-style queries that differ substantially from real-world search behavior, limiting their assessment of practical retrieval robustness. We present Omni-Embed-Audio (OEA), a retrieval-oriented encoder leveraging multimodal LLMs with native audio understanding. To systematically evaluate robustness beyond caption-style queries, we introduce User-Intent Queries (UIQs) - five formulations reflecting natural search behaviors: questions, commands, keyword tags, paraphrases, and exclusion-based negative queries. For negative queries, we develop a hard negative mining pipeline and propose discrimination metrics (HNSR, TFR) assessing models'ability to suppress acoustically similar distractors. Experiments on AudioCaps, Clotho, and MECAT show that OEA achieves comparable text-to-audio retrieval performance to state-of-the-art M2D-CLAP, while demonstrating clear advantages in two critical areas: (1) dominant text-to-text retrieval (+22% relative improvement), and (2) substantially superior hard negative discrimination (+4.3%p HNSR@10, +34.7% relative TFR@10), revealing that LLM backbones provide superior semantic understanding of complex queries.
