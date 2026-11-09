---
layout: paper
id: "5e604fe080cde6a535ebecfec5131a159be8ac0d"
title: "W2V-Seld: A Sound Event Localization And Detection Framework For Self-Supervised Spatial Audio Pre-Training"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/5e604fe080cde6a535ebecfec5131a159be8ac0d
authors: "Orlem Lima dos Santos, Karen Rosero, R. Lotufo"
---

Sound Event Localization and Detection (SELD) is a critical challenge in various industrial applications, such as autonomous systems, smart cities, and audio surveillance, which require accurate identification and localization of sound events in complex environments. Traditional supervised approaches heavily rely on large, annotated multichannel audio datasets, which are expensive and time-consuming to produce. This paper addresses this limitation by introducing the w2v-SELD architecture, a self-supervised model adapted from the wav2vec 2.0 framework to learn effective sound event representations directly from raw, unlabeled 3D audio data in ambisonics format. The proposed model follows a two-stage process: pre-training on large, unlabeled 3D audio datasets to capture high-level features, followed by fine-tuning with a smaller, labeled SELD dataset. Experimental results show that our w2v-SELD method outperforms baseline models on Detection and Classification of Acoustic Scenes and Events (DCASE) challenges, achieving a 66% improvement for DCASE TAU-2019 and a 57% improvement on DCASE TAU-2020 with respect to baseline systems. The w2v-SELD model performs competitively with state-of-the-art supervised methods, highlighting its potential to significantly reduce the dependency on labeled data in industrial SELD applications. The code and pre-trained parameters of our w2v-SELD model are available online.
