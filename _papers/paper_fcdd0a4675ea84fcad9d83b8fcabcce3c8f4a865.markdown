---
layout: paper
id: "fcdd0a4675ea84fcad9d83b8fcabcce3c8f4a865"
title: "Autosynth: Learning To Generate Editable Synthesizer Programs From Audio And Text"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/fcdd0a4675ea84fcad9d83b8fcabcce3c8f4a865
authors: "Tristan Wu, Daniel Chin, Li-Wei Lin, Ju-Nan Zhang, Gus G. Xia"
---

Audio generation models can translate natural-language descriptions into sound, but their outputs are typically waveforms. Their audio quality is constrained by audio compression, and their outputs do not readily support direct edits to notes, timbral parameters, or modulation relationships. We present AutoSynth, which represents MIDI performance events, fixed synthesizer parameters, and variable-length modulation routes as a unified sequence for a synthesizer, and learns their dependencies with an audio-conditioned autoregressive model. A single model supports both tasks. Given reference audio, the model directly predicts a synthesizer program; given text, it uses a pretrained audio generation model and converts the generated audio into a program. Training consists of two stages: supervised learning on large-scale audio-program pairs automatically constructed from a small set of native presets, followed by group-relative policy optimization with a mixed reward combining semantic similarity, pitch-related features, acoustic similarity, and sound usefulness. The pipeline requires neither paired text-target-program annotations nor a differentiable synthesizer. Experiments show that AutoSynth produces complete, editable synthesizer programs and achieves competitive results in both synthesizer inversion and text-driven generation. Audio demos and source code are available at https://auto-synth.github.io/.
