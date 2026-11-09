---
layout: paper
id: "03c7f61b0c6bc4c480ed6da4e9d7dda104ddfec3"
title: "Cross-Modal Fine-Tuning: Align Then Refine"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/03c7f61b0c6bc4c480ed6da4e9d7dda104ddfec3
authors: "Junhong Shen, Liam Li, L. Dery, Corey Staten, M. Khodak, Graham Neubig, Ameet Talwalkar"
---

Fine-tuning large-scale pretrained models has led to tremendous progress in well-studied modalities such as vision and NLP. However, similar gains have not been observed in many other modalities due to a lack of relevant pretrained models. In this work, we propose ORCA, a general cross-modal fine-tuning framework that extends the applicability of a single large-scale pretrained model to diverse modalities. ORCA adapts to a target task via an align-then-refine workflow: given the target input, ORCA first learns an embedding network that aligns the embedded feature distribution with the pretraining modality. The pretrained model is then fine-tuned on the embedded data to exploit the knowledge shared across modalities. Through extensive experiments, we show that ORCA obtains state-of-the-art results on 3 benchmarks containing over 60 datasets from 12 modalities, outperforming a wide range of hand-designed, AutoML, general-purpose, and task-specific methods. We highlight the importance of data alignment via a series of ablation studies and demonstrate ORCA's utility in data-limited regimes.
