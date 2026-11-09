---
layout: paper
id: "beb88574c7c630cb2cc4bd65ebcc7f1a0e10566e"
title: "From Objectives To Applications: Aligning Architectural Biases In Audio Self-Supervised Learning"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/beb88574c7c630cb2cc4bd65ebcc7f1a0e10566e
authors: "Ke-Le Xu, Yu Fang, Bo-Da Zhou, Yu-Lin Sun, Qi-Sheng Xu, Qi-Ya Song, Jin Zhang, Cheng Yang, Huai-Min Wang"
publication_date: "2026-07-01"
---

This paper examines audio self-supervised learning (SSL) through the alignment between pretraining objectives, architectural inductive biases, and downstream applications. Rather than treating SSL methods as a chronological sequence of pretext tasks or model families, we ask how different supervisory signals shape the representations that models are expected to learn. The discussion is organized around five paradigms: auxiliary tasks, contrastive learning, generative reconstruction, discrete token prediction, and multimodal alignment. These objectives place different demands on the model, from local structural sensitivity and contrastive invariance to contextual inference, discrete semantic abstraction, and multimodal grounding. We relate these demands to the biases of CNNs, recurrent and State Space Models, Transformers, and hybrid architectures, showing how local acoustic compression, sequential state propagation, content-dependent global routing, and local--global integration support different forms of audio SSL. The same view is then used to interpret downstream applications in speech processing, environmental sound analysis, music information retrieval, medical and bioacoustic analysis, and multimodal audio understanding as practical tests of whether learned representations and architectural choices generalize across domains. We also review benchmark protocols and open challenges, including tokenization bottlenecks, long-context efficiency, robustness, and secure multimodal deployment, and discuss how codec-based tokenization and audio-language modeling extend this objective--architecture--application pipeline. The accompanying repository is released at https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning.
