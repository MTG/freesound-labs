---
layout: paper
id: "5e0c020bc4adf1c6b698bef84e70513bd0c691bb"
title: "Tse-Pi: Target Sound Extraction Under Reverberant Environments With Pitch Information"
publication: "Interspeech 2024"
year: 2024
external_url: https://www.semanticscholar.org/paper/5e0c020bc4adf1c6b698bef84e70513bd0c691bb
authors: "Yiwen Wang, Xihong Wu"
---

Target sound extraction (TSE) separates the target sound from the mixture signals based on provided clues. However, the performance of existing models significantly degrades under reverberant conditions. Inspired by auditory scene analysis (ASA), this work proposes a TSE model provided with pitch information named TSE-PI. Conditional pitch extraction is achieved through the Feature-wise Linearly Modulated layer with the sound-class label. A modified Waveformer model combined with pitch information, employing a learnable Gammatone filterbank in place of the convolutional encoder, is used for target sound extraction. The inclusion of pitch information is aimed at improving the model's performance. The experimental results on the FSD50K dataset illustrate 2.4 dB improvements of target sound extraction under reverberant environments when incorporating pitch information and Gammatone filterbank.
