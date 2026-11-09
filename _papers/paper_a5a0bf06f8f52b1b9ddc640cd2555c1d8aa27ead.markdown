---
layout: paper
id: "a5a0bf06f8f52b1b9ddc640cd2555c1d8aa27ead"
title: "Improving Sound Event Classification By Increasing Shift Invariance In Convolutional Neural Networks"
publication: "ArXiv"
year: 2021
external_url: https://www.semanticscholar.org/paper/a5a0bf06f8f52b1b9ddc640cd2555c1d8aa27ead
authors: "Eduardo Fonseca, Andrés Ferraro, Xavier Serra"
---

Recent studies have put into question the commonly assumed shift invariance property of convolutional networks, showing that small shifts in the input can affect the output predictions substantially. In this paper, we analyze the benefits of addressing lack of shift invariance in CNN-based sound event classification. Specifically, we evaluate two pooling methods to improve shift invariance in CNNs, based on low-pass filtering and adaptive sampling of incoming feature maps. These methods are implemented via small architectural modifications inserted into the pooling layers of CNNs. We evaluate the effect of these architectural changes on the FSD50K dataset using models of different capacity and in presence of strong regularization. We show that these modifications consistently improve sound event classification in all cases considered. We also demonstrate empirically that the proposed pooling methods increase shift invariance in the network, making it more robust against time/frequency shifts in input spectrograms. This is achieved by adding a negligible amount of trainable parameters, which makes these methods an appealing alternative to conventional pooling layers. The outcome is a new state-of-the-art mAP of 0.541 on the FSD50K classification benchmark.
