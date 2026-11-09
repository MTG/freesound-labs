---
layout: paper
id: "c85097baa2f23cae8a81d8a6d35fce8d42d1761b"
title: "Guiding Audio Editing With Audio Language Model"
publication: "arXiv.org"
year: 2025
external_url: https://www.semanticscholar.org/paper/c85097baa2f23cae8a81d8a6d35fce8d42d1761b
authors: "Zitong Lan, Yiduo Hao, Min-Fang Zhao"
---

Audio editing plays a central role in VR/AR immersion, virtual conferencing, sound design, and other interactive media. However, recent generative audio editing models depend on template-like instruction formats and are restricted to mono-channel audio. These models fail to deal with declarative audio editing, where the user declares what the desired outcome should be, while leaving the details of editing operations to the system. We introduce SmartDJ, a novel framework for stereo audio editing that combines the reasoning capability of audio language models with the generative power of latent diffusion. Given a high-level instruction, SmartDJ decomposes it into a sequence of atomic edit operations, such as adding, removing, or spatially relocating events. These operations are then executed by a diffusion model trained to manipulate stereo audio. To support this, we design a data synthesis pipeline that produces paired examples of high-level instructions, atomic edit operations, and audios before and after each edit operation. Experiments demonstrate that SmartDJ achieves superior perceptual quality, spatial realism, and semantic alignment compared to prior audio editing methods. Demos are available at https://zitonglan.github.io/project/smartdj/smartdj.html.
