---
layout: paper
id: "7f9c8cdc55ad005fc0e13d925f9bb36a0726ecef"
title: "Longaudio-Rag: Event-Grounded Question Answering Over Multi-Hour Long Audio"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/7f9c8cdc55ad005fc0e13d925f9bb36a0726ecef
authors: "Naveen Vakada, K. Hegde, A. Sridhar, Yinyi Guo, Erik Visser"
---

Answering natural-language questions over multi-hour audio requires reliable event recognition, temporal grounding, and efficient retrieval. We present LA-RAG (Long Audio Retrieval-Augmented Generation), a structured framework that converts audio into timestamped event records, stores them in an event database, and answers questions using intent-aware retrieval and LLM-based generation. LA-RAG supports two deployment settings: offline grounding mode, in which long recordings are pre-indexed for low-latency querying, and inference-time grounding mode, which performs query-conditioned grounding over shorter, open-ended clips. We evaluate LA-RAG on controlled 24-hour Home-IoT and Industrial-IoT benchmarks and on CASTELLA-QA, derived from real-world audio recordings. The results demonstrate effective long-audio question answering with low query-time latency after grounding and indexing. They also reveal a substantial gap between event detection and temporal localization in current large audio-language models, while showing that explicit timestamped grounding consistently improves temporal reasoning. These findings establish structured grounding and retrieval as a practical complement to generative audio-language models for deployment-oriented long-audio understanding.
