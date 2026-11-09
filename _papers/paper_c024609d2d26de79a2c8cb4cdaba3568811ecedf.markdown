---
layout: paper
id: "c024609d2d26de79a2c8cb4cdaba3568811ecedf"
title: "Efficient Audio-Visual Speech Separation With Discrete Lip Semantics And Multi-Scale Global-Local Attention"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/c024609d2d26de79a2c8cb4cdaba3568811ecedf
authors: "Kai Li, Kejun Gao, Xiaolin Hu"
---

Audio-visual speech separation (AVSS) methods leverage visual cues to extract target speech and have demonstrated strong separation quality in noisy acoustic environments. However, these methods usually involve a large number of parameters and require high computational cost, which is unacceptable in many applications where speech separation serves as only a preprocessing step for further speech processing. To address this issue, we propose an efficient AVSS method, named Dolphin. For visual feature extraction, we develop DP-LipCoder, a dual-path lightweight video encoder that transforms lip-motion into discrete audio-aligned semantic tokens. For audio separation, we construct a lightweight encoder-decoder separator, in which each layer incorporates a global-local attention (GLA) block to efficiently capture multi-scale dependencies. Experiments on three benchmark datasets showed that Dolphin not only surpassed the current state-of-the-art (SOTA) model in separation quality but also achieved remarkable improvements in efficiency: over 50% fewer parameters, more than 2.4x reduction in MACs, and over 6x faster GPU inference speed. These results indicate that Dolphin offers a practical and deployable solution for high-performance AVSS in real-world scenarios. Our code and demo page are publicly available at http://cslikai.cn/Dolphin/.
