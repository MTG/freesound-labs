---
layout: paper
id: "5adaaa4f7b91c78c27bda39306bf2dd03dfc1894"
title: "Collaborative Transformer Prototype Network With Pretrained Contrastive Language-Audio Encoder For Open Set Audio Recognition"
publication: "IEEE Transactions on Signal Processing"
year: 2025
external_url: https://www.semanticscholar.org/paper/5adaaa4f7b91c78c27bda39306bf2dd03dfc1894
authors: "Haiyan Yang, Jun Wang, Sheng Li, Di Zhou, Xingwei Chen, Juncheng Li, Yufeng Hua, Jun Shi"
---

Transformer models have achieved remarkable success in audio recognition, with the Swin Transformer standing out due to its ability to capture long-range dependencies in audio signals. However, existing Swin Transformer models are typically designed for closed-set environments, not able to deal with unknown classes in the test data. Additionally, the limited number of audio samples in each class exacerbates the training challenges. To address these limitations, we propose a novel framework called Collaborative Transformer Prototype Network with Pretrained Contrastive Language-Audio Encoder (PCLAE-CTPN). Specifically, CTPN extends the capabilities of Swin Transformer to open-set environments by employing it as the feature extractor and integrating a prototype classifier as the classification head. It is trained using a novel collaborative prototype learning mechanism, which enhances compactness within known classes while effectively separating unknown classes from known ones. This enables the network to accurately classify known classes and robustly identify unknown ones. To mitigate the challenge of limited audio samples in each class, we further devise a pretrained contrastive language-audio encoder (PCLAE), which incorporates prior knowledge into the model. Furthermore, we present two implementations of PCLAE-CTPN, differing in their class radius assignment strategies in collaborative prototype learning. Extensive experimental results on multiple benchmark datasets indicate that the proposed framework outperforms existing approaches, achieving state-of-the-art performance.
