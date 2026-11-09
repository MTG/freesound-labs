---
layout: paper
id: "048cb4d1b7712b7499a9d7db6d24caaab5ddd9ce"
title: "Separate But Together: Unsupervised Federated Learning For Speech Enhancement From Non-Iid Data"
publication: "ArXiv"
year: 2021
external_url: https://www.semanticscholar.org/paper/048cb4d1b7712b7499a9d7db6d24caaab5ddd9ce
authors: "Efthymios Tzinis, Jonah Casebeer, Zhepei Wang, P. Smaragdis"
publication_date: "2021-05-11"
---

We propose FedEnhance, an unsupervised federated learning (FL) approach for speech enhancement and separation with non-IID distributed data across multiple clients. We simulate a realworld scenario where each client only has access to a few noisy recordings from a limited and disjoint number of speakers (hence non-IID). Each client trains their model in isolation using mixture invariant training while periodically providing updates to a central server. Our experiments show that our approach achieves competitive enhancement performance compared to IID training on a single device and that we can further facilitate the convergence speed and the overall performance using transfer learning on the server-side. Moreover, we show that we can effectively combine updates from clients trained locally with supervised and unsupervised losses. We also release a new dataset LibriFSD50K and its creation recipe in order to facilitate FL research for source separation problems.
