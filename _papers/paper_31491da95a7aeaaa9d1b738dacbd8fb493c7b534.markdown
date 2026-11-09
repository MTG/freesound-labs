---
layout: paper
id: "31491da95a7aeaaa9d1b738dacbd8fb493c7b534"
title: "Multiple Neural Networks With Ensemble Method For Audio Tagging With Noisy Labels And Minimal Supervision"
publication: ""
year: 2019
external_url: https://www.semanticscholar.org/paper/31491da95a7aeaaa9d1b738dacbd8fb493c7b534
authors: "K. He, Yu-Han Shen, W. Zhang"
---

In this paper, we describe our system for the Task 2 of Detection and Classiﬁcation of Acoustic Scenes and Events (DCASE) 2019 Challenge: Audio tagging with noisy labels and minimal supervision . This task provides a small amount of veriﬁed data (curated data) and a larger quantity of unveriﬁed data (noisy data) as training data. Each audio clip contains one or more sound events, so it can be considered as a multi-label audio classiﬁcation task. To tackle this problem, we mainly use four strategies. The ﬁrst is a sigmoid-softmax activation to deal with so-called sparse multi-label classiﬁcation. The second is a staged training strategy to learn from noisy data. The third is a post-processing method that normalizes output scores for each sound class. The last is an ensemble method that averages models learned with multiple neural networks and various acoustic features. All of the above strategies contribute to our system signiﬁcantly. Our ﬁnal system achieved labelweighted label-ranking average precision (lwlrap) scores of 0.758 on the private test dataset and 0.742 on the public test dataset, winning the 2nd place in DCASE 2019 Challenge Task 2.
