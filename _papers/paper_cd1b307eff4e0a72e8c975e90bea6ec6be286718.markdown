---
layout: paper
id: "cd1b307eff4e0a72e8c975e90bea6ec6be286718"
title: "A Transformer-Based Audio Captioning Model With Keyword Estimation"
publication: "INTERSPEECH"
year: 2020
external_url: https://www.semanticscholar.org/paper/cd1b307eff4e0a72e8c975e90bea6ec6be286718
authors: "Y. Koizumi, Ryo Masumura, Kyosuke Nishida, M. Yasuda, S. Saito"
---

One of the problems with automated audio captioning (AAC) is the indeterminacy in word selection corresponding to the audio event/scene. Since one acoustic event/scene can be described with several words, it results in a combinatorial explosion of possible captions and difficulty in training. To solve this problem, we propose a Transformer-based audio-captioning model with keyword estimation called TRACKE. It simultaneously solves the word-selection indeterminacy problem with the main task of AAC while executing the sub-task of acoustic event detection/acoustic scene classification (i.e., keyword estimation). TRACKE estimates keywords, which comprise a word set corresponding to audio events/scenes in the input audio, and generates the caption while referring to the estimated keywords to reduce word-selection indeterminacy. Experimental results on a public AAC dataset indicate that TRACKE achieved state-of-the-art performance and successfully estimated both the caption and its keywords.
