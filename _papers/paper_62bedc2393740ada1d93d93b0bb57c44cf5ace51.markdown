---
layout: paper
id: "62bedc2393740ada1d93d93b0bb57c44cf5ace51"
title: "Spatial Annotation-Free Sound Event Localization And Detection Via Spatial Instance Classification"
publication: "IEEE Access"
year: 2025
external_url: https://www.semanticscholar.org/paper/62bedc2393740ada1d93d93b0bb57c44cf5ace51
authors: "Masahiro Yasuda, Noboru Harada, Shoichiro Saito, Nobutaka Ono"
---

Sound Event Localization and Detection (SELD) typically relies on strongly labeled data that specify when, where, and which sounds occur, resulting in high annotation costs. To address this challenge, we present a framework that enables SELD training without spatial labels, termed spatial annotation-free SELD. The core idea is to reinterpret source localization—traditionally handled as a regression problem—as a classification task called spatial instance classification (SIC). SIC first partitions the observation region into sub-regions. For each sub-region, the acoustic signal capturing its sound events is extracted as a spatial instance. Classifying these instances reveals the sub-regions that contain sound events, thereby providing SELD functionality. By solving SIC under weak supervision, we realize spatial annotation-free SELD. SIC does not depend on a specific microphone configuration, and it is expected to be generally applicable as long as the sound in each divided region can be extracted as an instance. We validate the generality of SIC through two contrasting experiments: (i) application to SELD using first-order Ambisonics (FOA), and (ii) application to a newly introduced distributed SELD task, where events are localized on a 2D plane using widely spaced microphones. In both settings, SIC effectively trains SELD systems capable of localizing sound events without spatial annotations. The proposed approach, therefore, facilitates the development of practical, spatial-annotation-free SELD across diverse microphone setups.
