---
layout: paper
id: "f0f6d2799a1cf0b1d5cb8e6d826cfd3fa6dfba2f"
title: "Array Agnostic Multi-Channel Speech Presence Probability Estimation"
publication: "European Signal Processing Conference"
year: 2025
external_url: https://www.semanticscholar.org/paper/f0f6d2799a1cf0b1d5cb8e6d826cfd3fa6dfba2f
authors: "Shuai Tao, Kaixuan Yang, Stijn Kindt, Jesper Rindom Jensen, M. G. Christensen, Nilesh Madhu"
---

In this work, a novel array-agnostic approach is proposed for multi-channel speech presence probability (MCSPP) estimation. A neural architecture used in our previous work for array-fixed MC-SPP estimation is adapted to accommodate a variable number of microphone channels and guarantee permutation invariance of the inputs. Specifically, convolution and Transformer-based layers are modified to perform channelwise spectral and temporal processing, followed by Mean Pooling for channel fusion. Transform-Average-Concatenate layers are inserted to effectively aggregate array-level information added to channel-wise independent features. The previously proposed modified minimum variance distortionless response beamformer is then cascaded to produce spatially filtered outputs. Our benchmarking results demonstrate that the proposed approach achieves performance highly comparable to the array-fixed counterpart on known array geometries, while generalizing better to unseen array geometries. Notably, under microphone index permutation conditions, our method significantly outperforms the array-fixed approach, maintaining a much lower complexity in terms of model size and MACs.
