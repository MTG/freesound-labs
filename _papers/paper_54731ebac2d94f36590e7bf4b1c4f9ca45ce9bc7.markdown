---
layout: paper
id: "54731ebac2d94f36590e7bf4b1c4f9ca45ce9bc7"
title: "An Ensemble Of Convolutional Neural Networks For Sound Event Detection"
publication: "Mathematics"
year: 2025
external_url: https://www.semanticscholar.org/paper/54731ebac2d94f36590e7bf4b1c4f9ca45ce9bc7
authors: "Abdinabi Mukhamadiyev, Ilyos Khujayarov, Dilorom Nabieva, Jinsoo Cho"
publication_date: "2025-05-01"
---

Sound event detection tasks are rapidly advancing in the field of pattern recognition, and deep learning methods are particularly well suited for such tasks. One of the important directions in this field is to detect the sounds of emotional events around residential buildings in smart cities and quickly assess the situation for security purposes. This research presents a comprehensive study of an ensemble convolutional recurrent neural network (CRNN) model designed for sound event detection (SED) in residential and public safety contexts. The work focuses on extracting meaningful features from audio signals using image-based representation, such as Discrete Cosine Transform (DCT) spectrograms, Cocheagrams, and Mel spectrograms, to enhance robustness against noise and improve feature extraction. In collaboration with police officers, a two-hour dataset consisting of 112 clips related to four classes of emotional sounds, such as harassment, quarrels, screams, and breaking sounds, was prepared. In addition to the crowdsourced dataset, publicly available datasets were used to broaden the study’s applicability. Our dataset contains 5055 audio files of different lengths totaling 14.14 h and strongly labeled data. The dataset consists of 13 separate sound categories. The proposed CRNN model integrates spatial and temporal feature extraction by processing these spectrograms through convolution and bi-directional gated recurrent unit (GRU) layers. An ensemble approach combines predictions from three models, achieving F1 scores of 71.5% for segment-based metrics and 46% for event-based metrics. The results demonstrate the model’s effectiveness in detecting sound events under noisy conditions, even with a small, unbalanced dataset. This research highlights the potential of the model for real-time audio surveillance systems using mini-computers, offering cost-effective and accurate solutions for maintaining public order.
