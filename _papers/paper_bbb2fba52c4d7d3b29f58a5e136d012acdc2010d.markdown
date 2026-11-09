---
layout: paper
id: "bbb2fba52c4d7d3b29f58a5e136d012acdc2010d"
title: "Mjepa: A Simple And Scalable Joint-Embedding Predictive Architecture For Audio-Visual Learning"
publication: "European Conference on Computer Vision"
year: 2026
external_url: https://www.semanticscholar.org/paper/bbb2fba52c4d7d3b29f58a5e136d012acdc2010d
authors: "Revant Teotia, Adrien Bardes, Michael G. Rabbat, S. Chopra, Matthew J. Muckley, Nicolas Ballas"
publication_date: "2026-06-23"
---

Self-supervised learning from large-scale video data has emerged as a dominant paradigm for visual representation learning. Since audio and visual streams naturally co-occur in video data, extending this success to jointly learn from both modalities is a natural next step, yet it remains challenging. Existing audio-visual self-supervised methods rely on modality-specific encoders and complex combinations of contrastive or reconstruction objectives, limiting cross-modal synergy and scalability. Joint Embedding Predictive Architectures (JEPAs) offer a simple, modality-agnostic alternative, but have to date been applied primarily to individual modalities. We introduce MJEPA, a joint-embedding predictive architecture for audio-visual learning that uses a single, unified encoder for both modalities. Our approach uses only a single predictive objective, applied both within and across modalities. We show that cross-modal prediction is critical: without it, a shared encoder degrades below unimodal baselines; with it, each modality's representation benefits from the other. Our frozen ViT-g model outperforms the best prior frozen baseline by over 6.8 mAP on AudioSet-20K, surpasses fully finetuned models on ESC-50 and FSD50K, and is competitive on video benchmarks despite using 10x less video data.
