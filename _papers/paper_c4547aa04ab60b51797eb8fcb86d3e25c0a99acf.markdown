---
layout: paper
id: "c4547aa04ab60b51797eb8fcb86d3e25c0a99acf"
title: "Wavebyol: Self-Supervised Learning For Audio Representation From Raw Waveforms"
publication: "IEEE Access"
year: 2023
external_url: https://www.semanticscholar.org/paper/c4547aa04ab60b51797eb8fcb86d3e25c0a99acf
authors: "Sunghyun Kim, Yong-Hoon Choi"
---

In this paper, we propose the WaveBYOL model, which can learn general-purpose audio representations directly from raw waveforms based on the bootstrap your own latent (BYOL) approach, a Siamese neural network architecture. WaveBYOL does not extract features in a handcrafted manner, and the model learns general-purpose audio representations from raw waveforms by itself. Thus, the model can be easily applied to various downstream tasks. The augmentation layer in the WaveBYOL model is designed to create various views from the time domain of the raw audio waveforms; the encoding layer is designed to learn representations by extracting features from the views, which are augmented audio waveforms. We assess the representations learned by WaveBYOL by conducting experiments with seven audio downstream tasks under both frozen-model evaluation and fine-tuning settings. The accuracy, precision, recall, and F1-score are observed as performance evaluation metrics of the proposed model, and the accuracy score is compared with those of the existing models. In most downstream tasks, WaveBYOL achieves competitive performance compared to that of the recently developed state-of-the-art models such as contrastive learning for audio (COLA), BYOL for audio (BYOL-A), self-supervised audio spectrogram transformer (SSAST), audio representation learning with teacher-student transformer (ATST), and DeLoRes. Our implementation and pretrained models are located on GitHub.
