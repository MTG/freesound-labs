---
layout: paper
id: "1b2a496ba61dddf18e7aeee40a009ba7617a0a23"
title: "Conditional Sound Generation Using Neural Discrete Time-Frequency Representation Learning"
publication: "2021 IEEE 31st International Workshop on Machine Learning for Signal Processing (MLSP)"
year: 2021
external_url: https://www.semanticscholar.org/paper/1b2a496ba61dddf18e7aeee40a009ba7617a0a23
authors: "Xubo Liu, Turab Iqbal, Jinzheng Zhao, Qiushi Huang, Mark D. Plumbley, Wenwu Wang"
publication_date: "2021-07-21"
---

Deep generative models have recently achieved impressive performance in speech and music synthesis. However, compared to the generation of those domain-specific sounds, generating general sounds (such as siren, gunshots) has received less attention, despite their wide applications. In previous work, the SampleRNN method was considered for sound generation in the time domain. However, SampleRNN is potentially limited in capturing long-range dependencies within sounds as it only back-propagates through a limited number of samples. In this work, we propose a method for generating sounds via neural discrete time-frequency representation learning, conditioned on sound classes. This offers an advantage in efficiently modelling long-range dependencies and retaining local fine-grained structures within sound clips. We evaluate our approach on the UrbanSound8K dataset, compared to SampleRNN, with the performance metrics measuring the quality and diversity of generated sounds. Experimental results show that our method offers comparable performance in quality and significantly better performance in diversity.
