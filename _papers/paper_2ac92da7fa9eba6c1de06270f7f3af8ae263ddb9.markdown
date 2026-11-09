---
layout: paper
id: "2ac92da7fa9eba6c1de06270f7f3af8ae263ddb9"
title: "Hierarchical Label Propagation: A Model-Size-Dependent Performance Booster For Audioset Tagging"
publication: "ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"
year: 2025
external_url: https://www.semanticscholar.org/paper/2ac92da7fa9eba6c1de06270f7f3af8ae263ddb9
authors: "Ludovic Tuncay, Étienne Labbé, Thomas Pellegrini"
---

AudioSet is one of the most used and largest datasets in audio tagging, containing about 2 million audio samples that are manually labeled with 527 event categories organized into an ontology. However, the annotations contain inconsistencies, particularly where categories that should be labeled as positive according to the ontology are frequently mislabeled as negative. To address this issue, we apply Hierarchical Label Propagation (HLP), which propagates labels up the ontology hierarchy, resulting in a mean increase in positive labels per audio clip from 1.98 to 2.39 and affecting 109 out of the 527 classes. Our results demonstrate that HLP provides performance benefits across various model architectures, including convolutional neural networks (PANN’s CNN6 and ConvNeXT) and transformers (PaSST), with smaller models showing more improvements. Finally, on FSD50K, another widely used dataset, models trained on AudioSet with HLP consistently outperformed those trained without HLP. Our source code will be made available on GitHub.
