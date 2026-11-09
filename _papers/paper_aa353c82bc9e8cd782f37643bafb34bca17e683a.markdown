---
layout: paper
id: "aa353c82bc9e8cd782f37643bafb34bca17e683a"
title: "Bridging Auditory Perception And Natural Language Processing With Semantically Informed Deep Neural Networks"
publication: "bioRxiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/aa353c82bc9e8cd782f37643bafb34bca17e683a
authors: "Michele Esposito, Giancarlo Valente, Yenisel Plasencia-Calaña, M. Dumontier, Bruno L. Giordano, Elia Formisano"
---

Sound recognition is effortless for humans but poses a significant chal-lenge for artificial hearing systems. Deep neural networks (DNNs), especially convolutional neural networks (CNNs), have recently sur-passed traditional machine learning in sound classification. However, current DNNs map sounds to labels using binary categorical variables, neglecting the semantic relations between labels. Cognitive neuroscience research suggests that human listeners exploit such semantic informa-tion besides acoustic cues. Hence, our hypothesis is that incorporating semantic information improves DNN’s sound recognition performance, emulating human behavior. In our approach, sound recognition is framed as a regression problem, with CNNs trained to map spec-trograms to continuous semantic representations from NLP models (Word2Vec, BERT, and CLAP text encoder). Two DNN types were trained: semDNN with continuous embeddings and catDNN with cat-egorical labels, both with a dataset extracted from a collection of 388,211 sounds enriched with semantic descriptions. Evaluations across four external datasets, confirmed the superiority of semantic labeling from semDNN compared to catDNN, preserving higher-level relations. Importantly, an analysis of human similarity ratings for natural sounds, showed that semDNN approximated human listener behavior better than catDNN, other DNNs, and NLP models. Our work contributes to understanding the role of semantics in sound recognition, bridging the gap between artificial systems and human auditory perception.
