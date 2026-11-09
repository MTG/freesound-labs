---
layout: paper
id: "ca46dcaf25bd7970b3e9ca976c08ff990d1a42ee"
title: "A Gated Multi-Head Network With Semantic–Spatial Features For Sound Event Localization And Detection"
publication: "Electronics"
year: 2026
external_url: https://www.semanticscholar.org/paper/ca46dcaf25bd7970b3e9ca976c08ff990d1a42ee
authors: "Min-Jin Kim, Seok-Pil Lee"
publication_date: "2026-08-11"
---

Sound event localization and detection (SELD) aims to identify active sound event classes and estimate their spatial locations from audio signals. Stereo SELD remains challenging because two-channel recordings provide limited directional and distance information for jointly estimating sound event detection (SED), direction of arrival (DOA), source distance, and source coordinates. This paper proposes a Gated Multi-Head Network (GMHN) for DCASE 2025 Task 3 stereo SELD. The proposed model is built on a ResNet-Conformer backbone and uses an 8-channel semantic–spatial feature representation as the encoder input. In addition, task-specific auxiliary cues are incorporated into different prediction branches: energy cues are used to improve source distance estimation (SDE), phase cues are used to refine DOA estimation, and BEATs features are used to enhance SELD. For source coordinate estimation (SCE), the model combines a raw coordinate branch and a geometry-based coordinate branch derived from DOA and distance predictions through a learnable gate. This design encourages geometric consistency among direction, distance, and coordinate estimates while preserving the flexibility of direct coordinate regression. Experimental results show that the proposed model improves SELD performance by achieving more accurate distance and localization estimation.
