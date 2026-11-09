---
layout: paper
id: "6d44d7cb5e2cb0f9b36eca65ecec1d2e5cfcc827"
title: "Tinyclap: Distilling Constrastive Language-Audio Pretrained Models"
publication: "Interspeech 2024"
year: 2023
external_url: https://www.semanticscholar.org/paper/6d44d7cb5e2cb0f9b36eca65ecec1d2e5cfcc827
authors: "F. Paissan, Elisabetta Farella"
---

Contrastive Language-Audio Pretraining (CLAP) became of crucial importance in the field of audio and speech processing. Its employment ranges from sound event detection to text-to-audio generation. However, one of the main limitations is the considerable amount of data required in the training process and the overall computational complexity during inference. This paper investigates how we can reduce the complexity of contrastive language-audio pre-trained models, yielding an efficient model that we call tinyCLAP. We derive an unimodal distillation loss from first principles and explore how the dimensionality of the shared, multimodal latent space can be reduced via pruning. TinyCLAP uses only 6% of the original Microsoft CLAP parameters with a minimal reduction (less than 5%) in zero-shot classification performance across the three sound event detection datasets on which it was tested
