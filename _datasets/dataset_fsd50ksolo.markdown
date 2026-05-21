---
layout: post
title: "FSD50K-Solo"
date: 2026-05-21
project_url: https://arxiv.org/pdf/2605.13931
institutions:
- Bose Corporation
- Stony Brook University
authors: 
- Ningyuan Yang
- Sile Yin
- Li-Chia Yang
- Bryce Irvin
- Xiao Quan
- Marko Stamenovic
- Shuo Zhang
---

High-quality training datasets are essential for the performance of neural networks. However, the audio domain still lacks a large-scale, strongly-labeled, and single-source sound event dataset. The FSD50K dataset, despite being relatively large and open, contains a considerable fraction of multi-source samples where background interference or overlapping events could limit the usefulness of the data. To address this challenge, we introduce a data curation framework designed for large-scale open audio corpora. Our approach leverages a generative diffusion model to synthesize clean single-class events to construct controlled noisy mixtures for supervision. We subsequently employ a pre-trained audio encoder coupled with a discriminative classifier to automatically identify and filter out multi-source samples. Experiments show that our framework achieves strong performance on a human expert-curated test set. Finally, we release FSD50K-Solo, a model-curated subset of FSD50K containing single-source audio samples identified by our method. Beyond FSD50K, our method establishes a scalable paradigm for curating open source audio corpora.



 


