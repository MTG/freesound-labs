---
layout: paper
id: "a899d32cdbdb26a580dd3b1a8b0e0af49eb1446f"
title: "Optimization Techniques For A Physical Model Of Human Vocalisation"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/a899d32cdbdb26a580dd3b1a8b0e0af49eb1446f
authors: "Mateo C'amara, Zhiyuan Xu, Yi-Chen Zong, Jos'e Luis Blanco, J. Reiss"
publication_date: "2023-09-26"
---

We present a non-supervised approach to optimize and evaluate the synthesis of non-speech audio effects from a speech production model. We use the Pink Trombone synthesizer as a case study of a simplified production model of the vocal tract to target non-speech human audio signals --yawnings. We selected and optimized the control parameters of the synthesizer to minimize the difference between real and generated audio. We validated the most common optimization techniques reported in the literature and a specifically designed neural network. We evaluated several popular quality metrics as error functions. These include both objective quality metrics and subjective-equivalent metrics. We compared the results in terms of total error and computational demand. Results show that genetic and swarm optimizers outperform least squares algorithms at the cost of executing slower and that specific combinations of optimizers and audio representations offer significantly different results. The proposed methodology could be used in benchmarking other physical models and audio types.
