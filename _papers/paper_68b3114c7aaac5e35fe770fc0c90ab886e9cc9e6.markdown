---
layout: paper
id: "68b3114c7aaac5e35fe770fc0c90ab886e9cc9e6"
title: "Efficient Face Detection With Audio-Based Region Proposals"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/68b3114c7aaac5e35fe770fc0c90ab886e9cc9e6
authors: "William Aris, Franccois Grondin"
publication_date: "2023-09-14"
---

Efficient face detection is critical to provide natural human-robot interactions. However, computer vision tends to involve a large computational load due to the amount of data (i.e. pixels) that needs to be processed in a short amount of time. This is undesirable on robotics platforms where multiple processes need to run in parallel and where the processing power is limited by portability constraints. Existing solutions often involve reducing image quality which can negatively impact processing. The literature also reports methods to generate regions of interest in images from pixel data. Although it is a promising idea, these methods often involve heavy vision algorithms. In this paper, we evaluate how audio can be used to generate regions of interest in optical images to reduce the number of pixels to process with computer vision. Thereby, we propose a unique attention mechanism to localize a speech source and evaluate its impact on an existing face detection algorithm. Our results show that the attention mechanism reduces the computational load and offers an interesting trade-off between speed and accuracy. The proposed pipeline is flexible and can be easily adapted to other applications such as robot surveillance, video conferences or smart glasses.
