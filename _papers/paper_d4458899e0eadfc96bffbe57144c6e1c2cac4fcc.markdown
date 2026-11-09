---
layout: paper
id: "d4458899e0eadfc96bffbe57144c6e1c2cac4fcc"
title: "Learning Deep Modality-Shared Self-Expressiveness For Image Clustering With Textual Information"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/d4458899e0eadfc96bffbe57144c6e1c2cac4fcc
authors: "Xiang-Han Meng, Wei He, Zhi-Yuan Huang, Chun-Guang Li"
---

Leveraging textual information for image clustering has emerged as a promising direction, largely owing to the powerful representations learned by Vision-Language Models (VLMs). Existing approaches typically retrieve a textual counterpart for each image and then refine multimodal representations by directly enforcing cross-modal agreement, e.g., maximizing image-text similarity inherited from pretrained VLMs. However, such a strategy aligns heterogeneous representations across modalities without explicitly modeling the intrinsic structure within each modality and thus might yield unreliable alignment or distort modality-specific structures that are crucial for clustering. In this paper, we propose a simple but principled approach, termed deep modality-shared self-expressive model (DeepMORSE), which discovers cross-modal structures via a modality-shared self-expressive model and simultaneously learns structured representations that conform to a union of modality-specific subspaces. Moreover, we theoretically justify that the modality-shared self-expressive coefficients suppress inter-class noise towards a subspace-preserving solution, and show that mini-batch optimization procedure introduces an implicit regularization onto the self-expressive model. We evaluate our DeepMORSE on six widely used image clustering benchmarks and observe performance improvements exceeding 3% on the UCF-101, DTD-47, and ImageNet-Dogs datasets. In addition, we demonstrate the strong transferability of the learned representations by achieving state-of-the-art performance on downstream tasks such as image retrieval and zero-shot classification---without requiring any task-specific losses or post-processing. The code is available at: https://github.com/mengxianghan123/DeepMORSE.
