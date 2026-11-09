---
layout: paper
id: "a143a662d2c1f3bdaad3f5fe9b1ed03c617e4394"
title: "Df-Palm: Dynamic Fusion Prompt Learning For Audio--Language Models"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/a143a662d2c1f3bdaad3f5fe9b1ed03c617e4394
authors: "Yu-Lin Sun, Sheng-Hua Li, Yong Dou, Xin-Wang Liu, Cheng Yang, Ke-Le Xu"
publication_date: "2026-10-18"
---

Few-shot audio classification requires audio--language models to distinguish variable acoustic events from limited labeled data. PALM's main formulation adapts encoded class representations without changing pretrained encoders, but its class representations remain input-independent and classification uses audio features without class-conditioned refinement. We introduce DF-PALM, a dynamic feature-space prompting framework that combines audio-conditioned class representations with asymmetric cross-attention for audio refinement. Class representations are conditioned after text encoding, held fixed across fusion layers for each input, and reused for final scoring. Both pretrained encoders remain frozen, avoiding audio-conditioned text-encoder passes. With PENGI as the frozen backbone, the main 16-shot evaluation covered 11 benchmarks and six baselines. DF-PALM achieved 80.69% mean accuracy and 80.32% macro-averaged F1, exceeding PALM by 4.11 and 4.30 percentage points, respectively. Paired benchmark-level tests supported both gains after Holm correction. Across four shot settings, DF-PALM achieved the highest mean accuracy and macro-averaged F1 among the four evaluated prompt-learning methods. The gains extended to LAION-CLAP and OpenFLAM, with significant improvements over PALM in both metrics. At 50 candidate classes, operator-counted inference floating-point operations increased by 0.39% relative to PALM. These results support instance-conditioned feature-space adaptation as an effective approach to few-shot audio classification. Our code is publicly available at GitHub https://github.com/sunyulin0421/DF-PALM.
