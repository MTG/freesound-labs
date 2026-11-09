---
layout: paper
id: "c0efb9f8e87a8a57d883c87a317ca06c4fdfebca"
title: "Unfused: Unsupervised Finetuning Using Self Supervised Distillation"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/c0efb9f8e87a8a57d883c87a317ca06c4fdfebca
authors: "Ashish Seth, Sreyan Ghosh, S. Umesh, Dinesh Manocha"
publication_date: "2023-03-10"
---

In this paper, we introduce UnFuSeD, a novel approach to leverage self-supervised learning and reduce the need for large amounts of labeled data for audio classification. Unlike prior works, which directly fine-tune a self-supervised pre-trained encoder on a target dataset, we use the encoder to generate pseudo-labels for unsupervised fine-tuning before the actual fine-tuning step. We first train an encoder using a novel self-supervised learning algorithm (SSL) on an unlabeled audio dataset. Then, we use that encoder to generate pseudo-labels on our target task dataset via clustering the extracted representations. These pseudo-labels are then used to guide self-distillation on a randomly initialized model, which we call unsupervised fine-tuning. Finally, the resultant encoder is fine-tuned on our target task dataset. Through UnFuSeD, we propose the first system that moves away from generic SSL paradigms in literature, which pretrain and fine-tune the same encoder, and presents a novel self-distillation-based system to leverage SSL pre-training for low-resource audio classification. In practice, UnFuSeD achieves state-of-the-art results on the LAPE Benchmark, significantly outperforming all our baselines. Additionally, UnFuSeD allows us to achieve this at a $\approx 40$% reduction in the number of parameters over the previous state-of-the-art system. We make all our codes publicly available 1. 1https://github.com/Sreyan88/LAPE
