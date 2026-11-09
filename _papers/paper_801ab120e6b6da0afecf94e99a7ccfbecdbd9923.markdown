---
layout: paper
id: "801ab120e6b6da0afecf94e99a7ccfbecdbd9923"
title: "Stft-Domain Neural Speech Enhancement With Very Low Algorithmic Latency"
publication: "IEEE/ACM Transactions on Audio, Speech, and Language Processing"
year: 2022
external_url: https://www.semanticscholar.org/paper/801ab120e6b6da0afecf94e99a7ccfbecdbd9923
authors: "Zhong-Qiu Wang, G. Wichern, Shinji Watanabe, Jonathan Le Roux"
---

Deep learning based speech enhancement in the short-time Fourier transform (STFT) domain typically uses a large window length such as 32 ms. A larger window can lead to higher frequency resolution and potentially better enhancement. This however incurs an algorithmic latency of 32 ms in an online setup, because the overlap-add algorithm used in the inverse STFT (iSTFT) is also performed using the same window size. To reduce this inherent latency, we adapt a conventional dual-window-size approach, where a regular input window size is used for STFT but a shorter output window is used for overlap-add, for STFT-domain deep learning based frame-online speech enhancement. Based on this STFT-iSTFT configuration, we employ complex spectral mapping for frame-online enhancement, where a deep neural network (DNN) is trained to predict the real and imaginary (RI) components of target speech from the mixture RI components. In addition, we use the DNN-predicted RI components to conduct frame-online beamforming, the results of which are used as extra features for a second DNN to perform frame-online postfiltering. The frequency-domain beamformer can be easily integrated with our DNNs and is designed to not incur any algorithmic latency. Additionally, we propose a future-frame prediction technique to further reduce the algorithmic latency. Evaluation on noisy-reverberant speech enhancement shows the effectiveness of the proposed algorithms. Compared with Conv-TasNet, our STFT-domain system can achieve better enhancement performance for a comparable amount of computation, or comparable performance with less computation, maintaining strong performance at an algorithmic latency as low as 2 ms.
