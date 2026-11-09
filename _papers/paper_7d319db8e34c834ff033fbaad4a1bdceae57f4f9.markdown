---
layout: paper
id: "7d319db8e34c834ff033fbaad4a1bdceae57f4f9"
title: "A General Unfolding Speech Enhancement Method Motivated By Taylor'S Theorem"
publication: ""
year: 2022
external_url: https://www.semanticscholar.org/paper/7d319db8e34c834ff033fbaad4a1bdceae57f4f9
authors: "Andong Li, Guochen Yu, C. Zheng, Wenzhe Liu, Xiaodong Li"
---

While deep neural networks have facilitated significant advancements in the field of speech enhancement, most existing methods are developed following either empirical or relatively blind criteria, lacking adequate guidelines in pipeline design. Inspired by Taylor's theorem, we propose a general unfolding framework for both single- and multi-channel speech enhancement tasks. Concretely, we formulate the complex spectrum recovery into the spectral magnitude mapping in the neighborhood space of the noisy mixture, in which an unknown sparse term is introduced and applied for phase modification in advance. Based on that, the mapping function is decomposed into the superimposition of the 0th-order and high-order polynomials in Taylor's series, where the former coarsely removes the interference in the magnitude domain and the latter progressively complements the remaining spectral detail in the complex spectrum domain. In addition, we study the relation between adjacent order terms and reveal that each high-order term can be recursively estimated with its lower-order term, and each high-order term is then proposed to evaluate using a surrogate function with trainable weights, so that the whole system can be trained in an end-to-end manner. Given that the proposed framework is devised with the motivation of Taylor's theorem, it possesses improved internal flexibility. Extensive experiments are conducted on WSJ0-SI84, DNS-Challenge, Voicebank+Demand, spatialized Librispeech, and L3DAS22 multi-channel speech enhancement challenge datasets. Quantitative results show that the proposed approach yields competitive performance over existing top-performing approaches in terms of multiple objective metrics.
