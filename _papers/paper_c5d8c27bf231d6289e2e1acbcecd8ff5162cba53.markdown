---
layout: paper
id: "c5d8c27bf231d6289e2e1acbcecd8ff5162cba53"
title: "Clotho-Aqa: A Crowdsourced Dataset For Audio Question Answering"
publication: "ArXiv"
year: 2022
external_url: https://www.semanticscholar.org/paper/c5d8c27bf231d6289e2e1acbcecd8ff5162cba53
authors: "Samuel Lipping, Parthasaarathy Sudarsanam, K. Drossos, T. Virtanen"
---

Audio question answering (AQA) is a multimodal translation task where a system analyzes an audio signal and a natural language question, to generate a desirable natural language answer. In this paper, we introduce Clotho-AQA, a dataset for Audio question answering consisting of 1991 audio files each between 15 to 30 seconds duration selected from the Clotho dataset. For each audio file, we collect six different questions and corresponding answers by crowdsourcing using Amazon Mechanical Turk. The questions and answers are produced by different annotators. Out of the six questions for each audio, two questions each are designed to have ‘yes’ and ‘no’ as answers, while the remaining two questions have other single-word answers. For each question, we collect answers from three different annotators. We also present two baseline experiments to describe the usage of our dataset for the AQA task — a Long short-term memory (LSTM) based multimodal binary classifier for ‘yes’ or ‘no’ type answers and an LSTM based multimodal multi-class classifier for 828 single-word answers. The binary classifier achieved an accuracy of 62.7% and the multi-class classifier achieved a top-1 accuracy of 54.2% and a top-5 accuracy of 93.7%. Clotho-AQA dataset is freely available online at https://zenodo.org/record/6473207.
