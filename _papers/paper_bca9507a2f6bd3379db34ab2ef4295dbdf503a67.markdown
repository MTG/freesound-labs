---
layout: paper
id: "bca9507a2f6bd3379db34ab2ef4295dbdf503a67"
title: "From Discrete Tokens To High-Fidelity Audio Using Multi-Band Diffusion"
publication: "NeurIPS"
year: 2023
external_url: https://www.semanticscholar.org/paper/bca9507a2f6bd3379db34ab2ef4295dbdf503a67
authors: "Robin San Roman, Yossi Adi, Antoine Deleforge, R. Serizel, Gabriel Synnaeve, Alexandre D'efossez"
publication_date: "2023-08-02"
---

Deep generative models can generate high-fidelity audio conditioned on various types of representations (e.g., mel-spectrograms, Mel-frequency Cepstral Coefficients (MFCC)). Recently, such models have been used to synthesize audio waveforms conditioned on highly compressed representations. Although such methods produce impressive results, they are prone to generate audible artifacts when the conditioning is flawed or imperfect. An alternative modeling approach is to use diffusion models. However, these have mainly been used as speech vocoders (i.e., conditioned on mel-spectrograms) or generating relatively low sampling rate signals. In this work, we propose a high-fidelity multi-band diffusion-based framework that generates any type of audio modality (e.g., speech, music, environmental sounds) from low-bitrate discrete representations. At equal bit rate, the proposed approach outperforms state-of-the-art generative techniques in terms of perceptual quality. Training and, evaluation code, along with audio samples, are available on the facebookresearch/audiocraft Github page.
