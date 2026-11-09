---
layout: paper
id: "59a0ef2d3bccebb544a2df4ad0453d49cc8e731f"
title: "Soundstream: An End-To-End Neural Audio Codec"
publication: "IEEE/ACM Transactions on Audio, Speech, and Language Processing"
year: 2021
external_url: https://www.semanticscholar.org/paper/59a0ef2d3bccebb544a2df4ad0453d49cc8e731f
authors: "Neil Zeghidour, Alejandro Luebs, Ahmed Omran, J. Skoglund, M. Tagliasacchi"
---

We present SoundStream, a novel neural audio codec that can efficiently compress speech, music and general audio at bitrates normally targeted by speech-tailored codecs. SoundStream relies on a model architecture composed by a fully convolutional encoder/decoder network and a residual vector quantizer, which are trained jointly end-to-end. Training leverages recent advances in text-to-speech and speech enhancement, which combine adversarial and reconstruction losses to allow the generation of high-quality audio content from quantized embeddings. By training with structured dropout applied to quantizer layers, a single model can operate across variable bitrates from 3 kbps to 18 kbps, with a negligible quality loss when compared with models trained at fixed bitrates. In addition, the model is amenable to a low latency implementation, which supports streamable inference and runs in real time on a smartphone CPU. In subjective evaluations using audio at 24 kHz sampling rate, SoundStream at 3 kbps outperforms Opus at 12 kbps and approaches EVS at 9.6 kbps. Moreover, we are able to perform joint compression and enhancement either at the encoder or at the decoder side with no additional latency, which we demonstrate through background noise suppression for speech.
