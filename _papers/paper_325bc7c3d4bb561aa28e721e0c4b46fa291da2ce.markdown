---
layout: paper
id: "325bc7c3d4bb561aa28e721e0c4b46fa291da2ce"
title: "Deep Learning-Based Speech Specific Source Localization By Using Binaural And Monaural Microphone Arrays In Hearing Aids"
publication: "IEEE/ACM Transactions on Audio, Speech, and Language Processing"
year: 2023
external_url: https://www.semanticscholar.org/paper/325bc7c3d4bb561aa28e721e0c4b46fa291da2ce
authors: "Peyman Goli, S. van de Par"
---

A deep learning-based method is proposed for jointly detecting and localizing speech sources in a complex acoustic scene by using microphones of a hearing aid. Motivated by the human auditory system, peripheral preprocessing is applied on the microphone signals to obtain auditory subband signals that serve as input to the proposed deep neural network for detecting and localizing speech sources. In the proposed neural network, a combination of residual and dense aggregation learning is utilized rather than the conventional residual learning to preserve and reuse the spatial representations at the output layers. This process is performed to improve the gradient flow in deeper layers, in the training stage. The learning curves show that the proposed residual-dense aggregation mapping do improve the speed and accuracy of the convergence. The proposed model shows good performance in joint speech source detection and localization using a binaural microphone array (i.e., three channels at each side) but also using a monaural microphone array (i.e., four channels at the right side) despite of the short distances between the microphones. The proposed methods also outperform neural networks that are directly using STFT components of the binaural or monaural microphone arrays. In addition, the proposed models extended with learnable peripheral processing show slightly improved in detection and localization scores compared to the proposed models using the plain auditory subband signals, in both the binaural and monaural microphone arrays but only so, when the learnable peripheral processing is initialized with parameters stemming from human peripheral processing.
