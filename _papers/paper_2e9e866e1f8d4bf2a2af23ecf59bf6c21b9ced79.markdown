---
layout: paper
id: "2e9e866e1f8d4bf2a2af23ecf59bf6c21b9ced79"
title: "Subaru: A Practical Approach To Power Saving In Hearables Using Sub-Nyquist Audio Resolution Upsampling"
publication: ""
year: 2025
external_url: https://www.semanticscholar.org/paper/2e9e866e1f8d4bf2a2af23ecf59bf6c21b9ced79
authors: "Tarikul Islam Tamiti, Sajid Fardin Dipto, Luke Benjamin Baja-Ricketts, David C Vergano, Anomadarshi Barua"
---

Hearables are wearable computers that are worn on the ear. Bone conduction microphones (BCMs) are used with air conduction microphones (ACMs) in hearables as a supporting modality for multimodal speech enhancement (SE) in noisy conditions. However, existing works don't consider the following practical aspects for low-power implementations on hearables: (i) They do not explore how lowering the sampling frequencies and bit resolutions in analog-to-digital converters (ADCs) of hearables jointly impact low-power processing and multimodal SE in terms of speech quality and intelligibility. And (iii) They don't process signals from ACMs/BCMs at a sub-Nyquist sampling rate because, in their frameworks, they lack a wideband reconstruction methodology from their narrowband parts. We propose SUBARU (\textbf{Sub}-Nyquist \textbf{A}udio \textbf{R}esolution \textbf{U}psampling), which achieves the following: SUBARU (i) intentionally uses sub-Nyquist sampling and low bit resolution in ADCs, achieving a 3.31x reduction in power consumption; and (ii) achieves streaming operations on mobile platforms and SE in in-the-wild noisy conditions with an inference time of 1.74ms and a memory footprint of less than 13.77MB.
