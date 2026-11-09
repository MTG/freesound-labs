---
layout: paper
id: "9e14045c0229a182fea2dc6e9c5bedc52fdfe41c"
title: "Nest: Self-Supervised Fast Conformer As All-Purpose Seasoning To Speech Processing Tasks"
publication: "ArXiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/9e14045c0229a182fea2dc6e9c5bedc52fdfe41c
authors: "He Huang, T. Park, Kunal Dhawan, I. Medennikov, Krishna C. Puvvada, N. Koluguri, Weiqing Wang, Jagadeesh Balam, Boris Ginsburg"
publication_date: "2024-08-23"
---

Self-supervised learning (SSL) has been proved to benefit a wide range of speech processing tasks, such as speech recognition/translation, speaker verification and diarization, etc. However, most of current speech SSL approaches are computationally expensive. In this paper, we introduce a simplified and more efficient SSL framework, termed as NeMo Encoder for Speech Tasks (NEST). Specifically, we adopt the FastConformer architecture with 8x sub-sampling rate, which is faster than Transformer or Conformer architectures. Instead of clusteringbased quantization, we use fixed random projection for its simplicity and effectiveness. We also implement a generalized noisy speech augmentation that teaches the model to disentangle the main speaker from noise or other speakers. Experiments show that NEST improves over existing self-supervised models and achieves new state-of-the-art performance on a variety of speech processing tasks, such as speech recognition/translation, speaker diarization, spoken language understanding, etc. Code and checkpoints are publicly available via NVIDIA NeMo framework123.
