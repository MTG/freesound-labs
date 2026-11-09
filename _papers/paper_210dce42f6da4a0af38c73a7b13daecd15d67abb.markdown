---
layout: paper
id: "210dce42f6da4a0af38c73a7b13daecd15d67abb"
title: "From Birdsong To Rumbles: Classifying Elephant Calls With Out-Of-Species Embeddings"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/210dce42f6da4a0af38c73a7b13daecd15d67abb
authors: "Christiaan M. Geldenhuys, T. Niesler"
---

We show that pretrained acoustic embeddings classify elephant vocalisations at a level approaching that of end-to-end supervised neural networks, without any fine-tuning of the embedding model. This result is of practical importance because annotated bioacoustic data are scarce and costly to obtain, leaving conventional supervised approaches prone to overfitting and to poor generalisation under domain shift. A broad range of embedding models drawn from general audio, speech, and bioacoustic domains is evaluated, all of which are either out-of-domain (containing no bioacoustic data) or out-of-species (containing no elephant call data). The embedding networks themselves remain fixed; only the lightweight downstream classifiers, which include a linear model and several small neural networks, are trained. Among the models considered, Perch 2.0 achieves the best cross-validated classification performance, attaining AUCs of 0.849 on African bush elephant (Loxodonta africana) calls and 0.936 on Asian elephant (Elephas maximus) calls, with Perch 1.0 close behind. The best-performing system is within 2.2 % of an end-to-end supervised elephant call classification system. A layerwise analysis of pretrained transformer encoders, considered as embedding models, shows that intermediate representations outperform final-layer outputs. The second layer of both wav2vec2.0 and HuBERT encodes sufficient information for effective elephant call classification; truncation at this layer therefore preserves classification performance whilst retaining only approximately 10 % of the parameters of the full network. Such compact embedding networks are well suited to on-device processing where computational resources are limited.
