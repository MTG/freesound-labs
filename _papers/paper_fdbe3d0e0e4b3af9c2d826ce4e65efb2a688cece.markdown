---
layout: paper
id: "fdbe3d0e0e4b3af9c2d826ce4e65efb2a688cece"
title: "Subband Architecture Aided Selective Fixed-Filter Active Noise Control"
publication: ""
year: 2025
external_url: https://www.semanticscholar.org/paper/fdbe3d0e0e4b3af9c2d826ce4e65efb2a688cece
authors: "Hong Liang, Man-Wai Mak, K. Lee"
publication_date: "2025-08-01"
---

The feedforward selective fixed-filter method selects the most suitable pre-trained control filter based on the spectral features of the detected reference signal, effectively avoiding slow convergence in conventional adaptive algorithms. However, it can only handle limited types of noises, and the performance degrades when the input noise exhibits non-uniform power spectral density. To address these limitations, this paper devises a novel selective fixed-filter scheme based on a delayless subband structure. In the off-line training stage, subband control filters are pre-trained for different frequency ranges and stored in a dedicated sub-filter database. During the on-line control stage, the incoming noise is decomposed using a polyphase FFT filter bank, and a frequency-band-matching mechanism assigns each subband signal the most appropriate control filter. Subsequently, a weight stacking technique is employed to combine all subband weights into a fullband filter, enabling real-time noise suppression. Experimental results demonstrate that the proposed scheme provides fast convergence, effective noise reduction, and strong robustness in handling more complicated noisy environments.
