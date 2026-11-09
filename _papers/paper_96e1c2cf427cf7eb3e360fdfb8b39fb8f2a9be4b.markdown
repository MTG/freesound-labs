---
layout: paper
id: "96e1c2cf427cf7eb3e360fdfb8b39fb8f2a9be4b"
title: "Blat: Bootstrapping Language-Audio Pre-Training Based On Audioset Tag-Guided Synthetic Data"
publication: "ACM Multimedia"
year: 2023
external_url: https://www.semanticscholar.org/paper/96e1c2cf427cf7eb3e360fdfb8b39fb8f2a9be4b
authors: "Xuenan Xu, Zhiling Zhang, Zelin Zhou, Pingyue Zhang, Zeyu Xie, Mengyue Wu, Ke Zhu"
publication_date: "2023-03-14"
---

Compared with ample visual-text pre-training research, few works explore audio-text pre-training, mostly due to the lack of sufficient parallel audio-text data. Most existing methods incorporate the visual modality as a pivot for audio-text pre-training, which inevitably induces data noise. In this paper, we propose to utilize audio captioning to generate text directly from audio, without the aid of the visual modality so that potential noise from modality mismatch is eliminated. Furthermore, we propose caption generation under the guidance of AudioSet tags, leading to more accurate captions. With the above two improvements, we curate high-quality, large-scale parallel audio-text data, based on which we perform audio-text pre-training. We comprehensively demonstrate the performance of the pre-trained model on a series of downstream audio-related tasks, including single-modality tasks like audio classification and tagging, as well as cross-modal tasks consisting of audio-text retrieval and audio-based text generation. Experimental results indicate that our approach achieves state-of-the-art zero-shot classification performance on most datasets, suggesting the effectiveness of our synthetic data. The audio encoder also serves as an efficient pattern recognition model by fine-tuning it on audio-related tasks. Synthetic data and pre-trained models are available online1 The code, checkpoints and data are available at https://github.com/wsntxxn/BLAT and https://zenodo.org/record/8218696/.
