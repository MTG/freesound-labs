---
layout: paper
id: "bcf266f2afeadf6b67652143cfae45dbfc184e4d"
title: "Dolph2Vec: Self-Supervised Representations Of Dolphin Vocalizations"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/bcf266f2afeadf6b67652143cfae45dbfc184e4d
authors: "Chiara Semenzin, Faadil Mustun, Roberto Dessì, P. Orhan, Alexis Emanuelli, Yair Lakretz, G. D. de Polavieja, Germán Sumbre"
---

Self-supervised learning (SSL) has opened new opportunities in bioacoustics by enabling scalable modeling of animal vocalizations without the need for expensive manual annotation. However, current SSL models in this domain prioritize broad generalization across species and are not optimized for uncovering the fine-grained structure of individual communication systems. In this work, we collect and release a novel dataset of over five years of longitudinal recordings, from five known dolphins in a semi-naturalistic marine environment, an unprecedented resource for studying dolphin communication. We adapt the Wav2Vec2.0 Baevski et al. (2020) architecture to this domain and introduce Dolph2Vec, the first large-scale, species-specific SSL model trained exclusively on this data. We benchmark our model on two biologically relevant tasks: signature whistle classification and whistle detection. Dolph2Vec significantly outperforms general-purpose baselines in both tasks. Beyond performance, we show that learned embeddings and codebook structure capture interpretable acoustic units aligned with dolphin whistle categories and possibly sub-whistle structure, enabling fine-grained analysis of communication patterns. Our findings demonstrate how SSL can serve as both a model and a scientific tool to explore hypotheses in animal communication research.
