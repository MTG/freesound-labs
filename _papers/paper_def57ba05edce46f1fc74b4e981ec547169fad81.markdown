---
layout: paper
id: "def57ba05edce46f1fc74b4e981ec547169fad81"
title: "Evoaudio: Recursive Self-Improvement For Audio Understanding"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/def57ba05edce46f1fc74b4e981ec547169fad81
authors: "Yu-Xiang Wang, Sheng-Bo Cai, Ying Shen, Ming-Hao Hsu, Qin-Ke Ni, Li-Qiang Zhang, T.-K. Sun, Steve Yevs, Zhi-Zheng Wu"
publication_date: "2026-09-23"
---

Audio language models understand what is said far better than how it sounds. Closing this gap takes more than data. Detailed acoustic annotation is costly, labels from stronger models inherit their errors and limits, and fixed data cannot adapt as the learner improves. We therefore propose EvoAudio, a recursive self-improvement system for audio understanding. To our knowledge, it is the first to evolve the model, waveforms, questions, and difficulty in one closed loop. EvoAudio uses the current model's performance to set the focus and difficulty of the next training data. A library of audio tools then constructs questions whose answers follow from how the audio was made, providing verifiable supervision without new human annotation. Reinforcement learning updates the model, and validation decides whether it enters the next evolution round. Across 13 rounds, EvoAudio improves five models with different audio encoders and language backbones on MMSU, MMAU-Pro, and MMAR. It achieves the highest average for every backbone, raising overall performance by up to 6.3 points. The improvement unfolds over successive rounds, with each stronger model starting the next round.
