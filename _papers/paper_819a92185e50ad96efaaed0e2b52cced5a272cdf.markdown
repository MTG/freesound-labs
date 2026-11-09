---
layout: paper
id: "819a92185e50ad96efaaed0e2b52cced5a272cdf"
title: "Multi-Modal Continual Pre-Training For Audio Encoders"
publication: "ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"
year: 2024
external_url: https://www.semanticscholar.org/paper/819a92185e50ad96efaaed0e2b52cced5a272cdf
authors: "Gyuhak Kim, Ho-Hsiang Wu, Luca Bondi, Bing Liu"
---

Several approaches have been proposed to pre-train an audio encoder to learn fundamental audio knowledge. These training frameworks range from supervised learning to self-supervised learning with a contrastive objective under multi-modal supervision. However, these approaches are constrained to a single pretext task, preventing their adaptability to multi-modal interactions beyond the modalities provided in training data. Continual learning (CL), in the meantime, allows machine learning systems to incrementally learn a new task while preserving the previously acquired knowledge, making the system more knowledgeable over time. The existing CL approaches are limited to learning downstream tasks such as classification. In this work, we propose to combine CL methods with several audio encoder pre-training methods. The audio encoders, when pre-trained continually over a sequence of multi-modal tasks, namely audiovisual and audio-text, exhibit improved performance across various downstream tasks compared to their non-continual learning counterparts, due to knowledge accumulation. The audio encoders are also capable of performing cross-modal tasks of all learned modalities.
