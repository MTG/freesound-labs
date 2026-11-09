---
layout: paper
id: "fe11f7b7f5b0bae01d5af5e03f4a2c99e72c5ff0"
title: "Sound Event Detection Based On Large Receptive Field Dynamic Convolution"
publication: "2026 6th International Conference on Advanced Algorithms and Neural Networks (AANN)"
year: 2026
external_url: https://www.semanticscholar.org/paper/fe11f7b7f5b0bae01d5af5e03f4a2c99e72c5ff0
authors: "Jun-Hai Liu, Lian-Jun Zhang, Xiao-Dong Wang, Zhi-Hua Lu"
---

Sound event detection (SED) aims to identify event categories in audio signals and estimate their temporal boundaries. Most existing methods rely on two-dimensional convolutions for feature extraction; however, the inherent time-frequency translation equivariance assumption of conventional convolutions limits their ability to model inter-frequency dependencies and complex non-stationary acoustic events. To address this issue, this paper proposes a novel SED framework based on large-receptive-field dynamic convolution. First, a large-kernel separable attention mechanism is designed for spectrogram feature extraction. Specifically, a large receptive field is introduced along the temporal axis to capture long-duration acoustic events, while a smaller receptive field is adopted along the frequency axis to preserve fine-grained frequency-band characteristics, thereby significantly enhancing long-range dependency modeling. Second, during the dynamic convolution generation stage, an independent dual-branch spatial perception attention mechanism and a multi-dimensional statistical pooling channel attention mechanism are introduced, enabling the model to achieve high sensitivity to both stationary background sounds and transient acoustic events. Experimental results demonstrate that the proposed architecture realizes deep joint optimization from feature extraction to dynamic weight generation, significantly improving the detection performance of overlapping sound events in complex acoustic environments.
