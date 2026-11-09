---
layout: paper
id: "d112bbb1d5c89a2b7f989718ee5193eabed5ce7b"
title: "Cross-Modal Audio-Text Retrieval Via Sequential Feature Augmentation"
publication: "CACML"
year: 2023
external_url: https://www.semanticscholar.org/paper/d112bbb1d5c89a2b7f989718ee5193eabed5ce7b
authors: "Fuhu Song, Jifeng Hu, Che Wang, Jiao Huang, Haowen Zhang, Yi Wang"
publication_date: "2023-03-17"
---

The goal of cross-modal audio-text retrieval is to retrieve the target audio clips (textual descriptions), which should be relevant to a given textual (audial) query. It is a challenging task because it necessitates learning comprehensive feature representations for two different modalities and unifying them into a common embedding space. However, most existing cross-modal audio-text retrieval approaches do not explicitly learn the sequential representation in audio features. Moreover, their method of directly employing a fully connected neural network to transform the different modalities into a common space is detrimental to sequential features. In this paper, we introduce a sequential feature augmentation framework based on reinforcement learning and feature fusion to enhance the sequential feature for cross-modal features. First, we adopt reinforcement learning to explore effective sequential features in audial and textual features. Then, a recurrent fusion module is applied as a feature enhancement component to project heterogeneous features into a common space. Extensive experiments are conducted on two prevalent datasets: the AudioCaps and the Clotho. The results demonstrate that our method gains a significant improvement over previous state-of-the-art methods.
