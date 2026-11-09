---
layout: paper
id: "ef0bc67a0e8266b6ec9782db9d793efd95496aaf"
title: "End-To-End Multi-Task Learning For Adjustable Joint Noise Reduction And Hearing Loss Compensation"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/ef0bc67a0e8266b6ec9782db9d793efd95496aaf
authors: "Philippe Gonzalez, Vera Frederiksen, Torsten Dau, Tobias May"
---

A multi-task learning framework is proposed for optimizing a single deep neural network (DNN) for joint noise reduction (NR) and hearing loss compensation (HLC). A distinct training objective is defined for each task, and the DNN predicts two time-frequency masks. During inference, the amounts of NR and HLC can be adjusted independently by exponentiating each mask before combining them. In contrast to recent approaches that rely on training an auditory-model emulator to define a differentiable training objective, we propose an auditory model that is inherently differentiable, thus allowing end-to-end optimization. The audiogram is provided as an input to the DNN, thereby enabling listener-specific personalization without the need for retraining. Results show that the proposed approach not only allows adjusting the amounts of NR and HLC individually, but also improves objective metrics compared to optimizing a single training objective. It also outperforms a cascade of two DNNs that were separately trained for NR and HLC, and shows competitive HLC performance compared to a traditional hearing-aid prescription. To the best of our knowledge, this is the first study that uses an auditory model to train a single DNN for both NR and HLC across a wide range of listener profiles.
