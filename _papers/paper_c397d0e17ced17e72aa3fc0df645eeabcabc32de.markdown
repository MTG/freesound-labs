---
layout: paper
id: "c397d0e17ced17e72aa3fc0df645eeabcabc32de"
title: "Efficient Training Of Audio Transformers With Patchout"
publication: "INTERSPEECH"
year: 2021
external_url: https://www.semanticscholar.org/paper/c397d0e17ced17e72aa3fc0df645eeabcabc32de
authors: "Khaled Koutini, Jan Schlüter, Hamid Eghbal-zadeh, G. Widmer"
---

The great success of transformer-based models in natural language processing (NLP) has led to various attempts at adapting these architectures to other domains such as vision and audio. Recent work has shown that transformers can outperform Convolutional Neural Networks (CNNs) on vision and audio tasks. However, one of the main shortcomings of transformer models, compared to the well-established CNNs, is the computational complexity. In transformers, the compute and memory complexity is known to grow quadratically with the input length. Therefore, there has been extensive work on optimizing transformers, but often at the cost of degrading predictive performance. In this work, we propose a novel method to optimize and regularize transformers on audio spectrograms. Our proposed models achieve a new state-of-the-art performance on Audioset and can be trained on a single consumer-grade GPU. Furthermore, we propose a transformer model that outperforms CNNs in terms of both performance and training speed. Source code: https://github.com/kkoutini/PaSST
