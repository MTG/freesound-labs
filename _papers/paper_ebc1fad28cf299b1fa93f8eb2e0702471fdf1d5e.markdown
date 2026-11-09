---
layout: paper
id: "ebc1fad28cf299b1fa93f8eb2e0702471fdf1d5e"
title: "Addressing Missing Labels In Large-Scale Sound Event Recognition Using A Teacher-Student Framework With Loss Masking"
publication: "IEEE Signal Processing Letters"
year: 2020
external_url: https://www.semanticscholar.org/paper/ebc1fad28cf299b1fa93f8eb2e0702471fdf1d5e
authors: "E. Fonseca, Shawn Hershey, M. Plakal, D. Ellis, A. Jansen, R. C. Moore"
publication_date: "2020-05-02"
---

The study of label noise in sound event recognition has recently gained attention with the advent of larger and noisier datasets. This work addresses the problem of missing labels, one of the big weaknesses of large audio datasets, and one of the most conspicuous issues for AudioSet. We propose a simple and model-agnostic method based on a teacher-student framework with loss masking to first identify the most critical missing label candidates, and then ignore their contribution during the learning process. We find that a simple optimisation of the training label set improves recognition performance without additional computation. We discover that most of the improvement comes from ignoring a critical tiny portion of the missing labels. We also show that the damage done by missing labels is larger as the training set gets smaller, yet it can still be observed even when training with massive amounts of audio. We believe these insights can generalize to other large-scale datasets.
