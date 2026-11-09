---
layout: paper
id: "8d88ce897cb34441e94bab8f8adedff0d3e269bf"
title: "Auto-Aeg: Scalable Data Construction For Open-Vocabulary Audio Event Grounding"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/8d88ce897cb34441e94bab8f8adedff0d3e269bf
authors: "Zi-Han Zhang, Xi-Ze Cheng, Wenhao Yan, Tongchen Zhang, Dong-Jie Fu, Wen-Xu Jia, Boyun Zhang, Yongbo He, Qi-Fei Zhang, Lin-Jun Li, Wen-Shi Chen, Tao Jin"
publication_date: "2026-07-05"
---

Large Audio-Language Models (LALMs) reason fluently about sound yet struggle to localize precisely when events occur, while classical Sound Event Detection (SED) attains frame-level precision only over a closed label set. At the intersection of these paradigms lies the task of Open-Vocabulary Audio Event Grounding: predicting all time intervals of a target sound event described by an arbitrary natural language query. Progress is bottlenecked by data scarcity: no large-scale resource provides open-vocabulary onset/offset supervision, and manual temporal annotation is prohibitively expensive. To address this, we introduce Auto-AEG, a scalable pipeline that constructs such supervision by automatic data construction and model fine-tuning. It pairs programmatically synthesized clips, which carry placement-exact ground-truth intervals for supervised cold-start, with multi-model pseudo-labels on real-world audio that supply the reward signal for reinforcement learning. Training with this pipeline yields large temporal-localization gains on AEGBench, an independent difficulty-stratified benchmark whose annotations we release, and these gains generalize to various held-out SED and audio grounding benchmarks. Our results show that automatically constructed data, coupled with interval-aware reward design, provides an effective data-side route to expanding the temporal localization capability of LALMs.
