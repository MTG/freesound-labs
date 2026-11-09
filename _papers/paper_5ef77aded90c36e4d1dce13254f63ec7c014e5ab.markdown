---
layout: paper
id: "5ef77aded90c36e4d1dce13254f63ec7c014e5ab"
title: "Back To Ear: Perceptually Driven High Fidelity Music Reconstruction"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/5ef77aded90c36e4d1dce13254f63ec7c014e5ab
authors: "Kangdi Wang, Zhiyue Wu, Dinghao Zhou, Rui Lin, Junyu Dai, Tao Jiang"
publication_date: "2025-09-18"
---

Variational Autoencoders (VAEs) are essential for large-scale audio tasks like diffusion-based generation. However, existing open-source models often neglect auditory perceptual aspects during training, leading to weaknesses in phase accuracy and stereophonic spatial representation. To address these challenges, we propose {\epsilon}ar-VAE, an open-source music signal reconstruction model that rethinks and optimizes the VAE training paradigm. Our contributions are threefold: (i) A K-weighting perceptual filter applied prior to loss calculation to align the objective with auditory perception. (ii) Two novel phase losses: a Correlation Loss for stereo coherence, and a Phase Loss using its derivatives--Instantaneous Frequency and Group Delay--for precision. (iii) A new spectral supervision paradigm where magnitude is supervised by all four Mid/Side/Left/Right components, while phase is supervised only by the LR components. Experiments show {\epsilon}ar-VAE at 44.1kHz substantially outperforms leading open-source models across diverse metrics, showing particular strength in reconstructing high-frequency harmonics and the spatial characteristics.
