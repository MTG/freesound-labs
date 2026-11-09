---
layout: paper
id: "982bdaf9d19fd89d55ed88fcae35a5c4d7c5a3e3"
title: "Improving Frame-Online Neural Speech Enhancement With Overlapped-Frame Prediction"
publication: "IEEE Signal Processing Letters"
year: 2022
external_url: https://www.semanticscholar.org/paper/982bdaf9d19fd89d55ed88fcae35a5c4d7c5a3e3
authors: "Zhong-Qiu Wang, Shinji Watanabe"
publication_date: "2022-04-15"
---

Frame-online speech enhancement systems in the short-time Fourier transform (STFT) domain usually have an algorithmic latency equal to the window size due to the use of overlap-add in the inverse STFT (iSTFT). This algorithmic latency allows the enhancement models to leverage future contextual information up to a length equal to the window size. However, this information is only partially leveraged by current frame-online systems. To fully exploit it, we propose an overlapped-frame prediction technique for deep learning based frame-online speech enhancement, where at each frame our deep neural network (DNN) predicts the current and several past frames that are necessary for overlap-add, instead of only predicting the current frame. In addition, we propose a loss function to account for the scale difference between predicted and oracle target signals. Experiments on a noisy-reverberant speech enhancement task show the effectiveness of the proposed algorithms.
