---
layout: paper
id: "95da345cadb9d1b86010e590e78be6c64ce9eff2"
title: "Robust Audio Tagging Under Class-Wise Supervision Unreliability"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/95da345cadb9d1b86010e590e78be6c64ce9eff2
authors: "Yuan-Bo Hou, Zhaoyi Liu, T. Ye, Q. Ren, Jian Guan, Wen-Wu Wang, Stephen Roberts"
publication_date: "2026-05-17"
---

Weakly labeled datasets such as AudioSet have driven recent progress in audio tagging. However, annotation quality varies across sound classes. Labels may be incomplete, ambiguous, or unreliable, which introduces class-dependent supervision bias during optimisation. The issue becomes harder as real and generated audio are increasingly mixed in training, and generated samples do not always match their intended semantic labels. Prior work mainly addressed unreliable supervision from missing-positive labels, while this paper targets three other sources of unreliable supervision: spurious additions, misassignments between similar classes, and weakened label evidence. These effects introduce class-dependent optimisation bias that is not explicitly modeled by most existing methods. To bridge this gap, the paper proposes a Class-wise Supervision Unreliability (CSU) framework that controls supervision strength at the class level during training. CSU learns a separate unreliability parameter for each class and down-weights less reliable supervision without changing the model architecture or inference process. To support evaluations, this paper also introduces ESC-FreeGen50, a manually verified benchmark of 50 sound classes that combines real and generated audio. Experiments on controlled benchmarks and AudioSet show that CSU improves robustness across different architectures and different sources of supervision unreliability. The results indicate that explicit class-wise modeling of supervision unreliability is an effective and practical strategy for robust audio tagging under large-scale weakly labeled training. Code and data are available at: https://github.com/Yuanbo2020/CSU
