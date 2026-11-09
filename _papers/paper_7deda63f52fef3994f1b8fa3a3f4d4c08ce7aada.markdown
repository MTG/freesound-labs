---
layout: paper
id: "7deda63f52fef3994f1b8fa3a3f4d4c08ce7aada"
title: "Biome: A Resource-Efficient Bioacoustic Foundational Model For Iot Applications"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/7deda63f52fef3994f1b8fa3a3f4d4c08ce7aada
authors: "Heitor R. Guimarães, Abhishek Tiwari, Mahsa Abdollahi, Anderson R. Avila, Tiago H. Falk"
publication_date: "2026-02-10"
---

Passive acoustic monitoring has become a key strategy in biodiversity assessment, conservation, and behavioral ecology, especially as Internet-of-Things (IoT) devices enable continuous in situ audio collection at scale. While recent self-supervised learning (SSL)-based audio encoders, such as BEATs and AVES, have shown strong performance in bioacoustic tasks, their computational cost and limited robustness to unseen environments hinder deployment on resource-constrained platforms. In this work, we introduce BioME, a resource-efficient audio encoder designed for bioacoustic applications. BioME is trained via layer-to-layer distillation from a high-capacity teacher model, enabling strong representational transfer while reducing the parameter count by 75%. To further improve ecological generalization, the model is pretrained on multi-domain data spanning speech, environmental sounds, and animal vocalizations. A key contribution is the integration of modulation-aware acoustic features via FiLM conditioning, injecting a DSP-inspired inductive bias that enhances feature disentanglement in low-capacity regimes. Across multiple bioacoustic tasks, BioME matches or surpasses the performance of larger models, including its teacher, while being suitable for resource-constrained IoT deployments. For reproducibility, code and pretrained checkpoints are publicly available.
