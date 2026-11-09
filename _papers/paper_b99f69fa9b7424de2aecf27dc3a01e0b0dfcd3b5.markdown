---
layout: paper
id: "b99f69fa9b7424de2aecf27dc3a01e0b0dfcd3b5"
title: "On The Language Encoder Of Contrastive Cross-Modal Models"
publication: "ACL"
year: 2023
external_url: https://www.semanticscholar.org/paper/b99f69fa9b7424de2aecf27dc3a01e0b0dfcd3b5
authors: "Mengjie Zhao, Junya Ono, Zhi-Wei Zhong, Chieh-Hsin Lai, Yuhta Takida, Naoki Murata, Wei-Hsiang Liao, Takashi Shibuya, Hiromi Wakaki, Yuki Mitsufuji"
publication_date: "2023-10-20"
---

Contrastive cross-modal models such as CLIP and CLAP aid various vision-language (VL) and audio-language (AL) tasks. However, there has been limited investigation of and improvement in their language encoder, which is the central component of encoding natural language descriptions of image/audio into vector representations. We extensively evaluate how unsupervised and supervised sentence embedding training affect language encoder quality and cross-modal task performance. In VL pretraining, we found that sentence embedding training language encoder quality and aids in cross-modal tasks, improving contrastive VL models such as CyCLIP. In contrast, AL pretraining benefits less from sentence embedding training, which may result from the limited amount of pretraining data. We analyze the representation spaces to understand the strengths of sentence embedding training, and find that it improves text-space uniformity, at the cost of decreased cross-modal alignment.
