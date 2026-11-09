---
layout: paper
id: "b9bfccdcf4c0102cb4fc63d297ee94df3b913d4e"
title: "Universr: Unified And Versatile Audio Super-Resolution Via Vocoder-Free Flow Matching"
publication: "IEEE International Conference on Acoustics, Speech, and Signal Processing"
year: 2025
external_url: https://www.semanticscholar.org/paper/b9bfccdcf4c0102cb4fc63d297ee94df3b913d4e
authors: "Woongjib Choi, Sangmin Lee, Hyungseob Lim, Hong-Goo Kang"
publication_date: "2025-10-01"
---

In this paper, we present a vocoder-free framework for audio super-resolution that employs a flow matching generative model to capture the conditional distribution of complex-valued spectral coefficients. Unlike conventional two-stage diffusion-based approaches that predict a mel-spectrogram and then rely on a pre-trained neural vocoder to synthesize waveforms, our method directly reconstructs waveforms via the inverse Short-Time Fourier Transform (iSTFT), thereby eliminating the dependence on a separate vocoder. This design not only simplifies end-to-end optimization but also overcomes a critical bottleneck of two-stage pipelines, where the final audio quality is fundamentally constrained by vocoder performance. Experiments show that our model consistently produces high-fidelity 48 kHz audio across diverse upsampling factors, achieving state-of-the-art performance on both speech and general audio datasets.
