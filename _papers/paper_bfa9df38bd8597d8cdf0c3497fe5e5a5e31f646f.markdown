---
layout: paper
id: "bfa9df38bd8597d8cdf0c3497fe5e5a5e31f646f"
title: "One-Peace: Exploring One General Representation Model Toward Unlimited Modalities"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/bfa9df38bd8597d8cdf0c3497fe5e5a5e31f646f
authors: "Peng Wang, Shijie Wang, Junyang Lin, Shuai Bai, Xiaohuan Zhou, Jingren Zhou, Xinggang Wang, Chang Zhou"
---

In this work, we explore a scalable way for building a general representation model toward unlimited modalities. We release ONE-PEACE, a highly extensible model with 4B parameters that can seamlessly align and integrate representations across vision, audio, and language modalities. The architecture of ONE-PEACE comprises modality adapters, shared self-attention layers, and modality FFNs. This design allows for the easy extension of new modalities by adding adapters and FFNs, while also enabling multi-modal fusion through self-attention layers. To pretrain ONE-PEACE, we develop two modality-agnostic pretraining tasks, cross-modal aligning contrast and intra-modal denoising contrast, which align the semantic space of different modalities and capture fine-grained details within modalities concurrently. With the scaling-friendly architecture and pretraining tasks, ONE-PEACE has the potential to expand to unlimited modalities. Without using any vision or language pretrained model for initialization, ONE-PEACE achieves leading results on a wide range of uni-modal and multi-modal tasks, including image classification (ImageNet), semantic segmentation (ADE20K), audio-text retrieval (AudioCaps, Clotho), audio classification (ESC-50, FSD50K, VGGSound), audio question answering (AVQA), image-text retrieval (MSCOCO, Flickr30K), and visual grounding (RefCOCO/+/g). Code is available at https://github.com/OFA-Sys/ONE-PEACE.
