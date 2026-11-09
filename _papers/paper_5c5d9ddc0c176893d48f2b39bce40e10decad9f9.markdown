---
layout: paper
id: "5c5d9ddc0c176893d48f2b39bce40e10decad9f9"
title: "Gass: Generalizing Audio Source Separation With Large-Scale Data"
publication: "ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"
year: 2023
external_url: https://www.semanticscholar.org/paper/5c5d9ddc0c176893d48f2b39bce40e10decad9f9
authors: "Jordi Pons, Xiaoyu Liu, Santiago Pascual, Joan Serra"
---

Universal source separation targets at separating the audio sources of an arbitrary mix, removing the constraint to operate on a specific domain like speech or music. Yet, the potential of universal source separation is limited because most existing works focus on mixes with predominantly sound events, and small training datasets also limit its potential for supervised learning. Here, we study a single general audio source separation (GASS) model trained to separate speech, music, and sound events in a supervised fashion with a large-scale dataset. We assess GASS models on a diverse set of tasks. Our strong in-distribution results show the feasibility of GASS models, and the competitive out-of-distribution performance in sound event and speech separation shows its generalization abilities. Yet, it is challenging for GASS models to generalize for separating out-of-distribution cinematic and music content. We also fine-tune GASS models on each dataset and consistently outperform the ones without pre-training. All fine-tuned models (except the music separation one) obtain state-of-the-art results in their respective benchmarks.
