---
layout: paper
id: "6ae0dee9bca532778ab3e80aef6da1bc4d9124d2"
title: "Soundcollage: Automated Discovery Of New Classes In Audio Datasets"
publication: "ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"
year: 2024
external_url: https://www.semanticscholar.org/paper/6ae0dee9bca532778ab3e80aef6da1bc4d9124d2
authors: "Ryuhaerang Choi, Soumyajit Chatterjee, Dimitris Spathis, Sung-Ju Lee, F. Kawsar, Mohammad Malekzadeh"
publication_date: "2024-10-30"
---

Developing new machine learning applications often requires the collection of new datasets. However, existing datasets may already contain relevant information to train models for new purposes. We propose SoundCollage: a framework to discover new classes within audio datasets by incorporating (1) an audio pre-processing pipeline to decompose different sounds in audio samples, and (2) an automated model-based annotation mechanism to identify the discovered classes. Furthermore, we introduce the clarity measure to assess the coherence of the discovered classes for better training new downstream applications. Our evaluations show that the accuracy of downstream audio classifiers within discovered class samples and a held-out dataset improves over the baseline by up to 34.7% and 4.5%, respectively. These results highlight the potential of SoundCollage in making datasets reusable by labeling with newly discovered classes. To encourage further research in this area, we open-source our code at github.com/nokia-bell-labs/audio-class-discovery.
