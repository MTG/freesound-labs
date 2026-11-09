---
layout: paper
id: "9f1c9c44c3ab7eeb43693d174edca0a1600ff19a"
title: "Conette: An Efficient Audio Captioning System Leveraging Multiple Datasets With Task Embedding"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/9f1c9c44c3ab7eeb43693d174edca0a1600ff19a
authors: "Etienne Labbé, Thomas Pellegrini, J. Pinquier"
publication_date: "2023-09-01"
---

Automated Audio Captioning (AAC) involves generating natural language descriptions of audio content, using encoder-decoder architectures. An audio encoder produces audio embeddings fed to a decoder, usually a Transformer decoder, for caption generation. In this work, we describe our model, which novelty, compared to existing models, lies in the use of a ConvNeXt architecture as audio encoder, adapted from the vision domain to audio classification. This model, called CNext-trans, achieved state-of-the-art scores on the AudioCaps (AC) dataset and performed competitively on Clotho (CL), while using four to forty times fewer parameters than existing models. We examine potential biases in the AC dataset due to its origin from AudioSet by investigating unbiased encoder's impact on performance. Using the well-known PANN's CNN14, for instance, as an unbiased encoder, we observed a 0.017 absolute reduction in SPIDEr score (where higher scores indicate better performance). To improve cross-dataset performance, we conducted experiments by combining multiple AAC datasets (AC, CL, MACS, WavCaps) for training. Although this strategy enhanced overall model performance across datasets, it still fell short compared to models trained specifically on a single target dataset, indicating the absence of a one-size-fits-all model. To mitigate performance gaps between datasets, we introduced a Task Embedding (TE) token, allowing the model to identify the source dataset for each input sample. We provide insights into the impact of these TEs on both the form (words) and content (sound event types) of the generated captions. The resulting model, named CoNeTTE, an unbiased CNext-trans model enriched with dataset-specific Task Embeddings, achieved SPIDEr scores of 0.467 and 0.310 on AC and CL, respectively.
