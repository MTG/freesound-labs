---
layout: paper
id: "0ab6ed460757b238fc7aeede432c2deae8203c38"
title: "Psla: Improving Audio Tagging With Pretraining, Sampling, Labeling, And Aggregation"
publication: "IEEE/ACM Transactions on Audio, Speech, and Language Processing"
year: 2021
external_url: https://www.semanticscholar.org/paper/0ab6ed460757b238fc7aeede432c2deae8203c38
authors: "Yuan Gong, Yu-An Chung, James R. Glass"
---

Audio tagging is an active research area and has a wide range of applications. Since the release of AudioSet, great progress has been made in advancing model performance, which mostly comes from the development of novel model architectures and attention modules. However, we find that appropriate training techniques are equally important for building audio tagging models with AudioSet, but have not received the attention they deserve. To fill the gap, in this work, we present PSLA, a collection of model agnostic training techniques that can noticeably boost the model accuracy including ImageNet pretraining, balanced sampling, data augmentation, label enhancement, model aggregation. While many of these techniques have been previously explored, we conduct a thorough investigation on their design choices and combine them together. By training an EfficientNet with pretraining, balanced sampling, data augmentation, and model aggregation, we obtain a single model (with 13.6 M parameters) and an ensemble model that achieve mean average precision (mAP) scores of 0.444 and 0.474 on AudioSet, respectively, outperforming the previous best system of 0.439 with 81 M parameters. In addition, our model also achieves a new state-of-the-art mAP of 0.567 on FSD50K. We also investigate the impact of label enhancement on the model performance.
