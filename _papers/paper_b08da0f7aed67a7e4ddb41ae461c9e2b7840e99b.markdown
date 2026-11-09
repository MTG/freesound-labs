---
layout: paper
id: "b08da0f7aed67a7e4ddb41ae461c9e2b7840e99b"
title: "Dual-Res: A Phase-Aware Lightweight Framework For Real-Time Denoising And Emergency-Caller Detection"
publication: "IEEE Access"
year: 2025
external_url: https://www.semanticscholar.org/paper/b08da0f7aed67a7e4ddb41ae461c9e2b7840e99b
authors: "Joonhwi Kim, Jungyu Choi, Sungbin Im"
---

Reliable acoustic instrumentation and measurement in disaster environments is challenging because structure-borne signals from survivors are often masked by highly nonstationary noise from machinery, sirens, and impacts. In particular, phase distortion severely degrades the accuracy of time-difference-of-arrival (TDOA) measurements used for source localization. To enhance measurement robustness, this paper introduces Dual-objective Ultra-lightweight Audio Low-power—Rescue-recognition & Enhancement System (DUAL–RES), a lightweight, phase-aware framework for real-time acoustic denoising and event detection. The system operates in the complex short-time Fourier transform (STFT) domain, estimating gain masks for both magnitude and phase components and applying waveform-domain refinement, while an integrated convolutional classifier enables simultaneous detection and characterization of structurally relevant acoustic events. Comprehensive evaluation across three datasets shows that DUAL–RES improves measurement reliability under noise: 1) on VoiceBank + DEMAND, it achieves competitive perceptual metrics with a compact 0.81M-parameter profile; 2) in controlled simulations, it increases classification accuracy at low signal-to-noise ratios (SNRs) and reduces phase distortion relative to representative baselines; and 3) on real microphone-array recordings, it preserves localization accuracy close to the unprocessed mixture, avoiding the degradation commonly observed with other denoisers. With real-time inference on embedded platforms such as the Jetson Nano, DUAL–RES provides a practical instrumentation framework for deployable acoustic measurement, monitoring, and event-based detection in disaster scenarios.
