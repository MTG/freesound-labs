---
layout: paper
id: "ed718df6317e09c06a66962e1cf4d4c9dd0e6bdc"
title: "The Npu-Aslp System For Music Restoration In The Ccf-Aatc 2026 Challenge"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/ed718df6317e09c06a66962e1cf4d4c9dd0e6bdc
authors: "Ze-Yu Zhu, Yi-Ke Zhu, Xing-Chen Li, Chao-Ren Yu, Jing-Yi Wang, Yu-Run Li, Jie-Rui Guo, Chun-Jiang He, Lei Xie"
---

This paper presents the NPU-ASLP music restoration system developed for Track 1 of the China Computer Federation (CCF) Advanced Audio Technology Competition (AATC) 2026 Challenge. The task aims to recover clean music from mobile-device-captured recordings affected by coupled degradations from playback devices, acoustic propagation, environmental noise and recording terminals. System development is further constrained by limited and imperfectly aligned real data pairs and a strict model-complexity budget. In our system, we adopt TF-MoE as the backbone for its dual-axis modeling of cross-band and temporal dependencies, whose Top-1 routing activates a single expert per token to bound computation under the strict budget. We extend it with two task-specific adaptations: a scale-aware encoder and a complex mapping decoder. The former encodes normalized complex spectra jointly with per-band log-RMS to preserve the band-energy cues discarded by band-wise normalization. The latter directly estimates the clean complex spectrum rather than masking the input, thereby repairing coupled degradations. To address the limited, imperfectly aligned real recordings, we further build a challenge-calibrated playback--propagation--recording simulator that generates 1,572.12 h of sample-aligned data across 202 acoustic conditions. The final system contains 2.951M parameters and requires 82.659 GMACs for a 10-s input. On the official blind test, it achieved -49.067 dB SI-SNR, 1.273 LSD, 2.540 FAD, and 3.495 ViSQOL. It ranked third in LSD, FAD, and ViSQOL and received the third prize in the challenge.
