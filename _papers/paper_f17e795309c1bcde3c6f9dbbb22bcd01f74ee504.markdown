---
layout: paper
id: "f17e795309c1bcde3c6f9dbbb22bcd01f74ee504"
title: "Matching Text And Audio Embeddings: Exploring Transfer-Learning Strategies For Language-Based Audio Retrieval"
publication: "DCASE"
year: 2022
external_url: https://www.semanticscholar.org/paper/f17e795309c1bcde3c6f9dbbb22bcd01f74ee504
authors: "B. Weck, Miguel P'erez Fern'andez, Holger Kirchhoff, Xavier Serra"
---

We present an analysis of large-scale pretrained deep learning models used for cross-modal (text-to-audio) retrieval. We use embeddings extracted by these models in a metric learning framework to connect matching pairs of audio and text. Shallow neural networks map the embeddings to a common dimensionality. Our system, which is an extension of our submission to the Language-based Audio Retrieval Task of the DCASE Challenge 2022, employs the RoBERTa foundation model as the text embedding extractor. A pretrained PANNs model extracts the audio embeddings. To improve the generalisation of our model, we investigate how pretraining with audio and associated noisy text collected from the online platform Freesound improves the performance of our method. Furthermore, our ablation study reveals that the proper choice of the loss function and fine-tuning the pretrained models are essential in training a competitive retrieval system.
