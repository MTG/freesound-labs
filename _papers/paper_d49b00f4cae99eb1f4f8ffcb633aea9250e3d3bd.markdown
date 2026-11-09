---
layout: paper
id: "d49b00f4cae99eb1f4f8ffcb633aea9250e3d3bd"
title: "Focus Then Listen: An Empirical Study Of Plug-And-Play Audio Enhancer For Noise-Robust Large Audio Language Models"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/d49b00f4cae99eb1f4f8ffcb633aea9250e3d3bd
authors: "Han Yin, Yang Xiao, Younghoo Kwon, Ting Dang, Jung-Woo Choi"
---

Large audio language models (LALMs) are a class of foundation models for audio understanding. Existing LALMs tend to degrade significantly in real-world noisy acoustic conditions where speech and non-speech sounds interfere. While noise-aware fine-tuning can improve robustness, it requires task-specific noisy data and expensive retraining, limiting scalability. To address this issue, we propose Focus-Then-Listen (FTL), a plug-and-play audio enhancer that improves LALMs'noise robustness. Specifically, FTL first separates the input waveform into speech and non-speech, and a modality router is applied to predict the target audio modality (e.g., speech) based on the user's instruction. Finally, a modality-aware fusion block generates a task-adaptive enhanced signal for improved downstream perception and reasoning. Experiments across multiple LALMs and tasks show that FTL improves performance across different noise levels without fine-tuning on LALMs.
