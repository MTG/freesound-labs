---
layout: paper
id: "4ccf44fb59df0cddfebc0dc338e097a6d5fd982b"
title: "Semantic Grouping Network For Audio Source Separation"
publication: "ArXiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/4ccf44fb59df0cddfebc0dc338e097a6d5fd982b
authors: "Shentong Mo, Yapeng Tian"
---

Recently, audio-visual separation approaches have taken advantage of the natural synchronization between the two modalities to boost audio source separation performance. They extracted high-level semantics from visual inputs as the guidance to help disentangle sound representation for individual sources. Can we directly learn to disentangle the individual semantics from the sound itself? The dilemma is that multiple sound sources are mixed together in the original space. To tackle the difficulty, in this paper, we present a novel Semantic Grouping Network, termed as SGN, that can directly disentangle sound representations and extract high-level semantic information for each source from input audio mixture. Specifically, SGN aggregates category-wise source features through learnable class tokens of sounds. Then, the aggregated semantic features can be used as the guidance to separate the corresponding audio sources from the mixture. We conducted extensive experiments on music-only and universal sound separation benchmarks: MUSIC, FUSS, MUSDB18, and VGG-Sound. The results demonstrate that our SGN significantly outperforms previous audio-only methods and audio-visual models without utilizing additional visual cues.
