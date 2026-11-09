---
layout: paper
id: "1b3eec9f95a2ac87179df4a5373facc54d3a0f54"
title: "Decorrelating Feature Spaces For Learning General-Purpose Audio Representations"
publication: "IEEE Journal of Selected Topics in Signal Processing"
year: 2021
external_url: https://www.semanticscholar.org/paper/1b3eec9f95a2ac87179df4a5373facc54d3a0f54
authors: "Sreyan Ghosh, Sandesh V Katta, Ashish Seth, S. Umesh"
publication_date: "2021-10-17"
---

Inspired by the recent progress in self-supervised learning for computer vision, in this paper, through the DeLoRes (Decorrelating latent spaces for Low Resource audio representation learning) framework, we introduce two new general-purpose audio representation learning approaches, the DeLoRes-S and DeLoRes-M. Our main objective is to make our network learn representations in a resource-constrained setting (both data and compute) that can generalize well across a diverse set of downstream tasks. Inspired by the Barlow Twins objective function, we propose learning embeddings invariant to distortions of an input audio sample while ensuring that they contain non-redundant information about the sample. We call this the DeLoRes learning framework, which we employ in different fashions with the DeLoRes-S and DeLoRes-M. In our experiments, we learn audio representations with less than half the number of model parameters and 10% audio samples compared to state-of-the-art algorithms to achieve state-of-the-art results on 7 out of 11 tasks on linear evaluation and 4 out of 11 tasks in the finetuning setup. In addition to being simple and intuitive, our pre-training procedure is amenable to compute through its inherent nature of construction. Furthermore, we conduct extensive ablation studies on our training algorithm, model architecture, and results and make all our code and pre-trained models publicly available1.
