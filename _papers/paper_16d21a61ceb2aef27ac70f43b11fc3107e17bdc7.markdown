---
layout: paper
id: "16d21a61ceb2aef27ac70f43b11fc3107e17bdc7"
title: "Wham: Towards A Translative Model Of Sperm Whale Vocalization"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/16d21a61ceb2aef27ac70f43b11fc3107e17bdc7
authors: "Orr Paradise, Pranav Muralikrishnan, Liangyu Chen, H. F. García, Bryan Pardo, Roee Diamant, David F. Gruber, Shane Gero, S. Goldwasser"
---

Sperm whales communicate in short sequences of clicks known as codas. We present WhAM (Whale Acoustics Model), the first transformer-based model capable of generating synthetic sperm whale codas from any audio prompt. WhAM is built by finetuning VampNet, a masked acoustic token model pretrained on musical audio, using 10k coda recordings collected over the past two decades. Through iterative masked token prediction, WhAM generates high-fidelity synthetic codas that preserve key acoustic features of the source recordings. We evaluate WhAM's synthetic codas using Fr\'echet Audio Distance and through perceptual studies with expert marine biologists. On downstream classification tasks including rhythm, social unit, and vowel classification, WhAM's learned representations achieve strong performance, despite being trained for generation rather than classification. Our code is available at https://github.com/Project-CETI/wham
