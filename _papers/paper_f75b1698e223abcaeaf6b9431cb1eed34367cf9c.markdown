---
layout: paper
id: "f75b1698e223abcaeaf6b9431cb1eed34367cf9c"
title: "Dashengtokenizer: One Layer Is Enough For Unified Audio Understanding And Generation"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/f75b1698e223abcaeaf6b9431cb1eed34367cf9c
authors: "Heinrich Dinkel, Xing Sun, Gang Li, Jiahao Mei, Yadong Niu, Jizhong Liu, Xiyang Li, Yi-Hsiu Liao, Jiahao Zhou, Junbo Zhang, Jian Luan"
publication_date: "2026-02-27"
---

This paper introduces DashengTokenizer, a continuous audio tokenizer engineered for joint use in both understanding and generation tasks. Unlike conventional approaches, which train acoustic tokenizers and subsequently integrate frozen semantic knowledge, our method inverts this paradigm: we leverage frozen semantic features and inject acoustic information. In linear evaluation across 22 diverse tasks, our method outperforms previous audio codec and audio encoder baselines by a significant margin while maintaining competitive audio reconstruction quality. Notably, we demonstrate that this acoustic injection improves performance for tasks such as speech emotion recognition, music understanding, and acoustic scene classification. We further evaluate the tokenizer's generative performance on text-to-audio (TTA), text-to-music (TTM), and speech enhancement (SE). Our approach surpasses standard variational autoencoder (VAE)-based methods on TTA and TTM tasks, while its effectiveness on SE underscores its capabilities as a general-purpose audio encoder. Finally, our results challenge the prevailing assumption that VAE-based architectures are a prerequisite for audio synthesis. Checkpoints are available at https://huggingface.co/mispeech/dashengtokenizer.
