---
layout: paper
id: "00f129a430d86bf3c6ddb9bed40bccba04b253a9"
title: "Re-Purposing Multimodal Large Language Models For Audio-Text Retrieval"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/00f129a430d86bf3c6ddb9bed40bccba04b253a9
authors: "Ji-Lan Xu, Carl Thomé, Danijela Horak, Wei-Di Xie, A. Zisserman"
---

Audio-text retrieval is crucial for bridging acoustic signals and natural language. While contrastive dual-encoder architectures like CLAP have shown promise, they are fundamentally limited by the capacity of small-scale encoders. Specifically, the text encoders struggle to understand complex queries that require reasoning or world knowledge. In this paper, we propose AuroLA, a novel contrastive language-audio pre-trained model that re-purposes Multimodal Large Language Models (MLLMs) as a unified backbone for audio-text retrieval. Specifically, we make the following contributions: (i) we construct a scalable data pipeline that curates diverse audio from multiple sources and generates multi-granular captions, ranging from long descriptions to structured tags, via automated annotation; (ii) we adapt an MLLM for retrieval by prompting it to summarise the audio/text input and using the hidden state of a special token as audio/text embeddings. (iii) extensive experiments demonstrate that AuroLA consistently outperforms state-of-the-art dual-encoder models, including the recent PE-AV. This validates the effectiveness of MLLM as a unified backbone for audio-text retrieval.
