---
layout: paper
id: "c603b10d9f904dbb8db7f4ba982ede6756fbbcde"
title: "Soniccaps: Large-Scale Diverse And Fine-Grained Captioning For Improved Audio-Retrieval"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/c603b10d9f904dbb8db7f4ba982ede6756fbbcde
authors: "Zineb Lahrichi, Marc Ferras, G. Richard, Geoffroy Peeters"
---

Recent advances in audio-language modeling have been driven by large-scale audio captioning datasets. However, existing datasets remain limited by low semantic diversity, generic descriptions lacking acoustic details, and one-to-one audio-caption mappings that poorly reflect the inherent ambiguity of auditory perception. We introduce SonicCaps, a large-scale audio captioning dataset comprising ~15M captions paired with ~700k audio clips, generated using a multi-modal large language model (Qwen3-Omni) conditioned on both audio and text. To explicitly promote diversity, we generate around 24 captions per audio via structured prompt engineering and few- shot generation, spanning main descriptions, rephrased variants (verbosity, style) and semantic tags. Human evaluation shows that SonicCaps is rated significantly higher than existing captioning datasets, with fine-grained analyses indicating that our captions are perceived as more descriptive and precise, which strongly correlates with quality judgments. Finally, training CLAP models on SonicCaps with a multi-caption sampling strategy consistently improves audio retrieval and zero-shot classification, with stronger generalization across public and commercial benchmarks. We release both SonicCaps and two specialized CLAP models on hugging face: https://huggingface.co/datasets/Zineb/SonicCaps.
