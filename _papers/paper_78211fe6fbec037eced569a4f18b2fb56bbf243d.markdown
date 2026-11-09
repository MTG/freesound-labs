---
layout: paper
id: "78211fe6fbec037eced569a4f18b2fb56bbf243d"
title: "Clap: Learning Audio Concepts From Natural Language Supervision"
publication: "ArXiv"
year: 2022
external_url: https://www.semanticscholar.org/paper/78211fe6fbec037eced569a4f18b2fb56bbf243d
authors: "Benjamin Elizalde, Soham Deshmukh, Mahmoud Al Ismail, Huaming Wang"
---

Mainstream machine listening models are trained to learn audio concepts under the paradigm of one class label to many recordings focusing on one task. Learning under such restricted supervision limits the flexibility of models because they require labeled audio for training and can only predict the predefined categories. Instead, we propose to learn audio concepts from natural language supervision. We call our approach Contrastive Language-Audio Pretraining (CLAP), which connects language and audio by using two encoders and a contrastive learning objective, bringing audio and text descriptions into a joint multimodal space. We trained CLAP with 128k audio and text pairs and evaluated it on 16 downstream tasks across 7 domains, such as classification of sound events, scenes, music, and speech. CLAP establishes state-of-the-art (SoTA) in Zero-Shot performance. Also, we evaluated CLAP’s audio encoder in a supervised learning setup and achieved SoTA in 5 tasks. The Zero-Shot capability removes the need of training with class labeled audio, enables flexible class prediction at inference time, and generalizes well in multiple downstream tasks. Code is available at: https://github.com/microsoft/CLAP.
