---
layout: paper
id: "1448dae778f161b41bfad95afd74c7c82edff40e"
title: "Foa Tokenizer: Low-Bitrate Neural Codec For First Order Ambisonics With Spatial Consistency Loss"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/1448dae778f161b41bfad95afd74c7c82edff40e
authors: "Parthasaarathy Sudarsanam, Sebastian Braun, Hannes Gamper"
publication_date: "2025-10-25"
---

Neural audio codecs have been widely studied for mono and stereo signals, but spatial audio remains largely unexplored. We present the first discrete neural spatial audio codec for first-order ambisonics (FOA). Building on the WavTokenizer architecture, we extend it to support four-channel FOA signals and introduce a novel spatial consistency loss to preserve directional cues in the reconstructed signals under a highly compressed representation. Our codec compresses 4-channel FOA audio at 24 kHz into 75 discrete tokens per second, corresponding to a bit rate of 0.9 kbps. Evaluations on simulated reverberant mixtures, non-reverberant clean speech, and FOA mixtures with real room impulse responses show accurate reconstruction, with mean angular errors of 13.76{\deg}, 3.96{\deg}, and 25.83{\deg}, respectively, across the three conditions. In addition, discrete latent representations derived from our codec provide useful features for downstream spatial audio tasks, as demonstrated on sound event localization and detection with STARSS23 real recordings.
