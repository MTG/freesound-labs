---
layout: paper
id: "acf8f48cb9a7741db508a5c80d6d0dcf0d5e2627"
title: "Harp: Harmonic-Aware Residual Partitioning For Neural Audio Codecs"
publication: "Interspeech"
year: 2026
external_url: https://www.semanticscholar.org/paper/acf8f48cb9a7741db508a5c80d6d0dcf0d5e2627
authors: "Qiao-Yu Yang, Li-Xing He, Binyue Deng, Wei-Feng Zhao"
publication_date: "2026-07-18"
---

Neural audio codecs with residual vector quantization (RVQ) normally treat all frequencies uniformly, so their codebooks become spectrally entangled. Truncating stages then removes an unpredictable mix of frequencies. Parallel band decomposition addresses this by splitting audio into independent bands, but fragments the latent space and loses cross-frequency coherence. We introduce HARP (Harmonic-Aware Residual Partitioning), a training strategy that partitions RVQ stages into frequency-ordered groups where each group refines its target band while the decoder retains access to all lower frequencies. Overtones are reconstructed in the context of their fundamentals, preserving coherence that parallel methods lose. HARP requires no architectural changes; it only modifies the training loss, leaving inference identical to standard RVQ. On speech, music, and general audio, HARP outperforms both standard RVQ and parallel decomposition. MUSHRA listening tests also show perceptual improvements.
