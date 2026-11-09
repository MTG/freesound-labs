---
layout: paper
id: "7e199fdde14e5e628730e1ad54ff4724ebafae6c"
title: "Gram: Spatial General-Purpose Audio Representations For Real-World Environments"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/7e199fdde14e5e628730e1ad54ff4724ebafae6c
authors: "Goksenin Yuksel, M. Gerven, Kiki van der Heijden"
---

Audio foundation models learn general-purpose audio representations that facilitate a wide range of downstream tasks. While the performance of these models has greatly increased for conventional single-channel, dry audio clips, their success in real-world acoustic environments with reverberation and noise is limited. Furthermore, most audio foundation models ignore the spatial dimension of real-world acoustic environments, ruling out tasks involving sound localization. To address these limitations, we propose GRAM: a general-purpose real-world audio model that employs a multi-channel masked autoencoder to efficiently learn spatial audio representations. We evaluated GRAM and other audio foundation models in a standardized manner on high-quality simulations of naturalistic, spatial acoustic environments as well as recordings of real-world environments and release these two complementary benchmark task suites: NatHEAR and RealSELD. Our results demonstrate that GRAM outperforms all state-of-the-art self-supervised audio foundation models on NatHEAR and the clean, single-channel version HEAR, while using only a fraction of the training data. GRAM also shows state-of-the-art localization performance in simulated environments and generalizes efficiently to real-world recordings in RealSELD. Taken together, GRAM presents a significant advance toward robust spatial audio foundation models for real-world environments.
