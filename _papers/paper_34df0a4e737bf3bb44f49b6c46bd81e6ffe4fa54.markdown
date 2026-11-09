---
layout: paper
id: "34df0a4e737bf3bb44f49b6c46bd81e6ffe4fa54"
title: "Better Audio Representations Are More Brain-Like: Linking Model-Brain Alignment With Performance In Downstream Auditory Tasks"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/34df0a4e737bf3bb44f49b6c46bd81e6ffe4fa54
authors: "Leonardo Pepino, P. Riera, J. Kamienkowski, Luciana Ferrer"
publication_date: "2025-11-20"
---

Artificial neural networks are increasingly powerful models of brain computation, yet it remains unclear whether improving their performance in downstream tasks also makes their internal representations more similar to brain signals. To address this question in the auditory domain, we quantified the alignment between the internal representations of 36 different audio models and brain activity from two independent fMRI datasets. Using voxel-wise and component-wise regression, and representation similarity analysis, we found that recent self-supervised audio models with strong performance in diverse downstream tasks are better predictors of auditory cortex activity than previously studied models. To assess the quality of the audio representations, we evaluated these models in 6 auditory tasks from the HEAREval benchmark, spanning music, speech, and environmental sounds. This revealed strong positive Pearson correlations (r>0.8) between a model's overall task performance and its alignment with brain representations. Finally, we analyzed the evolution of the similarity between audio and brain representations during the pretraining of EnCodecMAE, a recent audio representation model. We discovered that brain similarity increases progressively and emerges early during pretraining, despite the model not being explicitly optimized for this objective. This suggests that brain-like representations can be an emergent byproduct of learning to reconstruct missing information from naturalistic audio data.
