---
layout: paper
id: "c460ba5c1cabc04aff9b0c09138e4fc8015bdd7a"
title: "Environmental Sound Recognition On Embedded Systems: From Fpgas To Tpus"
publication: "Electronics"
year: 2021
external_url: https://www.semanticscholar.org/paper/c460ba5c1cabc04aff9b0c09138e4fc8015bdd7a
authors: "Jurgen Vandendriessche, Nick Wouters, Bruno da Silva, Mimoun Lamrini, Mohamed Yassin Chkouri, Abdellah Touhafi"
publication_date: "2021-10-27"
---

In recent years, Environmental Sound Recognition (ESR) has become a relevant capability for urban monitoring applications. The techniques for automated sound recognition often rely on machine learning approaches, which have increased in complexity in order to achieve higher accuracy. Nonetheless, such machine learning techniques often have to be deployed on resource and power-constrained embedded devices, which has become a challenge with the adoption of deep learning approaches based on Convolutional Neural Networks (CNNs). Field-Programmable Gate Arrays (FPGAs) are power efficient and highly suitable for computationally intensive algorithms like CNNs. By fully exploiting their parallel nature, they have the potential to accelerate the inference time as compared to other embedded devices. Similarly, dedicated architectures to accelerate Artificial Intelligence (AI) such as Tensor Processing Units (TPUs) promise to deliver high accuracy while achieving high performance. In this work, we evaluate existing tool flows to deploy CNN models on FPGAs as well as on TPU platforms. We propose and adjust several CNN-based sound classifiers to be embedded on such hardware accelerators. The results demonstrate the maturity of the existing tools and how FPGAs can be exploited to outperform TPUs.
