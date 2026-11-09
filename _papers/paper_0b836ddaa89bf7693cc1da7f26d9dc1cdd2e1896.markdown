---
layout: paper
id: "0b836ddaa89bf7693cc1da7f26d9dc1cdd2e1896"
title: "Improving Noise Robustness Of An End-To-End Neural Model For Automatic Speech Recognition"
publication: ""
year: 2020
external_url: https://www.semanticscholar.org/paper/0b836ddaa89bf7693cc1da7f26d9dc1cdd2e1896
authors: "J. Balam, Jocelyn Huang, V. Lavrukhin, Slyne Deng, Somshubra Majumdar, B. Ginsburg"
---

We present our experiments in training robust to noise an end-to-end automatic speech recognition (ASR) model using intensive data augmentation. We explore the efficacy of fine-tuning a pre-trained model to improve noise robustness, and we find it to be a very efficient way to train for various noisy conditions, especially when the conditions in which the model will be used, are unknown. Starting with a model trained on clean data helps establish baseline performance on clean speech. We carefully fine-tune this model to both maintain the performance on clean speech, and improve the model accuracy in noisy conditions. With this schema, we trained robust to noise English and Mandarin ASR models on large public corpora. All described models and training recipes are open sourced in NeMo, a toolkit for conversational AI.
