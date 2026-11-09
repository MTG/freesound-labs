---
layout: paper
id: "19b020eda40c1b54a7ccf27b6ceba43fe1af3524"
title: "Real Time Spectrogram Inversion On Mobile Phone"
publication: "ArXiv"
year: 2022
external_url: https://www.semanticscholar.org/paper/19b020eda40c1b54a7ccf27b6ceba43fe1af3524
authors: "Oleg Rybakov, M. Tagliasacchi, Yunpeng Li, Liyang Jiang, Xia Zhang, Fadi Biadsy"
publication_date: "2022-03-01"
---

We present two methods of real time magnitude spectrogram inversion: streaming Griffin Lim(GL) and streaming MelGAN. We demonstrate the impact of looking ahead on perceptual quality of MelGAN. As little as one hop size (12.5ms) of lookahead is able to significantly improve perceptual quality in comparison to its causal version. We compare streaming GL with the streaming MelGAN and show different trade-offs in terms of perceptual quality, on-device latency, algorithmic delay, memory footprint and noise sensitivity. For fair quality assessment of the GL approach, we use input log magnitude spectrogram without mel transformation. We evaluate presented real time spectrogram inversion approaches on clean, noisy and atypical speech. We specified conditions when streaming GL has comparable quality with MelGAN: noisy audio and no mel transformation. Streaming GL is 2.4x faster than real time on the ARM CPU of a Pixel4 and it uses 4.5x times less memory than MelGAN.
