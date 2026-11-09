---
layout: paper
id: "328a7e66c102c18edc66cddf4bf7a831522f6edf"
title: "Phasecoder: Microphone Geometry-Agnostic Spatial Audio Understanding For Multimodal Llms"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/328a7e66c102c18edc66cddf4bf7a831522f6edf
authors: "Artem Dementyev, W. Zulfikar, Sinan Hersek, Pascal Getreuer, Anurag Kumar, Vivek Kumar"
---

Current multimodal LLMs process audio as a mono stream, ignoring the rich spatial information essential for embodied AI. Existing spatial audio models, conversely, are constrained to fixed microphone geometries, preventing deployment across diverse devices. We present PhaseCoder, a transformer-only spatial audio encoder that is agnostic to microphone geometry. PhaseCoder takes raw multichannel audio and microphone coordinates as inputs to perform localization and produces robust spatial embeddings. We demonstrate that Gemma 3n LLM can be fine-tuned to reason over"Spatial Audio Tokens"produced by PhaseCoder. We show our encoder achieves state-of-the-art results on microphone-invariant localization benchmarks and, for the first time, enables an LLM to perform complex spatial reasoning and targeted transcription tasks from an arbitrary microphone array.
