---
layout: paper
id: "c2dd8c0db3e7b548a31a9d871d9b829f11b8dedf"
title: "Finelap: Taming Heterogeneous Supervision For Fine-Grained Language-Audio Pretraining"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/c2dd8c0db3e7b548a31a9d871d9b829f11b8dedf
authors: "Xiquan Li, Xuenan Xu, Ziyang Ma, Wenxi Chen, Haolin He, Qiuqiang Kong, Xie Chen"
---

Contrastively pretrained audio-language models (e.g., CLAP) excel at clip-level understanding but struggle with frame-level tasks. Existing extensions fail to exploit the varying granularity of real-world audio-text data, where massive clip-level textual descriptions coexist with limited frame-level annotations. This paper proposes Fine-grained Language-Audio Pretraining (FineLAP), a novel training paradigm that advances both clip- and frame-level alignment in CLAP with heterogeneous data. FineLAP introduces a dual-stream sigmoid loss with a cluster-based sampling strategy to jointly learn from clip- and frame-level supervision. To capture both global semantics and local details, FineLAP uses a decoupled audio projector on top of a self-supervised encoder. To alleviate the scarcity of temporally annotated data, we present FineLAP-100k, a large-scale synthetic SED dataset constructed through a scalable curation pipeline. Extensive experiments demonstrate that FineLAP achieves SOTA performance across multiple audio understanding tasks, including retrieval, classification, sound event detection, and text-to-audio grounding. Ablation studies further show that coarse- and fine-grained alignment are mutually beneficial, providing insights for building better audio-language models (ALMs).
