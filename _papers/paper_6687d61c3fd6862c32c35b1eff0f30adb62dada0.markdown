---
layout: paper
id: "6687d61c3fd6862c32c35b1eff0f30adb62dada0"
title: "Audio Captioning Using Semantic Alignment Enhancer"
publication: "2023 8th IEEE International Conference on Network Intelligence and Digital Content (IC-NIDC)"
year: 2023
external_url: https://www.semanticscholar.org/paper/6687d61c3fd6862c32c35b1eff0f30adb62dada0
authors: "Yoon-Ah Park, Joon-Hyuk Chang"
publication_date: "2023-11-03"
---

Automated audio captioning (AAC) relies on the meaningful transfer of information from the encoder to the decoder. We propose a module called the semantic alignment enhancer to improve this process. This module converts the keywords extracted by the keyword extractor from audio features into captions. It then minimizes the distance between the text embeddings, output of the decoder, and the keyword caption embeddings, enhancing semantic similarity of alignment between audio features and text features. Additionally, to address the issue of data scarcity in audio captioning, we employ transfer learning. Specifically, we pre-train an audio encoder using the recently released large-scale audio-text paired WavCaps dataset. We use this pre-trained encoder to enhance the model's performance during the fine-tuning process. As a result, this approach enhances the alignment between audio features and textual information, which leads to improved performance in AAC tasks on the Clotho dataset compared to the baseline.
