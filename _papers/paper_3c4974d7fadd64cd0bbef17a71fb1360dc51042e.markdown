---
layout: paper
id: "3c4974d7fadd64cd0bbef17a71fb1360dc51042e"
title: "Cross-Talk Speech Reduction, By Separation, For Separation"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/3c4974d7fadd64cd0bbef17a71fb1360dc51042e
authors: "Zhong-Qiu Wang, Samuele Cornell"
---

In conversational speech separation and recognition tasks, close-talk microphones are typically attached to each speaker during training data collection to capture near-field, close-talk mixture signals, in addition to using far-field microphones to record far-field mixture signals. Each such close-talk mixture exhibits a reasonably high energy level for the wearer and could intuitively serve as weak supervision for training far-field speech separation models directly on real-recorded far-field signals. However, they are not sufficiently clean for this purpose, as they often contain strong cross-talk speech from other speakers in addition to background noise. To address this, we propose cross-talk reduction (CTR), a task aiming to isolate the wearer's speech from each close-talk mixture, and a novel method called CTRnet, which can be trained directly on real-recorded pairs of close-talk and far-field mixtures to accomplish CTR. Building on CTRnet, we further propose pseudo-label based far-field speech separation (PuLSS), which uses CTRnet's estimated clean speech as pseudo-labels to train models for separating far-field mixtures. A key advantage of the proposed framework is that both CTRnet and PuLSS can be trained on real-recorded data from the target domain, addressing the generalization gap commonly observed when models are trained exclusively on simulated data. On the CHiME-6 dataset, our framework achieves state-of-the-art ASR performance under both oracle and estimated speaker diarization, surpassing all CHiME-{7,8} challenge submissions. To our knowledge, it is the first neural speech separation method that substantially outperforms guided source separation on real conversational"speech-in-the-wild"data.
