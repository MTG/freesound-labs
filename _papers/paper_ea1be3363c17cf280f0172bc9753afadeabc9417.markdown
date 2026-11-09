---
layout: paper
id: "ea1be3363c17cf280f0172bc9753afadeabc9417"
title: "Task-Aware Unified Source Separation"
publication: "ArXiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/ea1be3363c17cf280f0172bc9753afadeabc9417
authors: "Kohei Saijo, Janek Ebbers, Franccois G. Germain, Gordon Wichern, J. L. Roux"
---

Several attempts have been made to handle multiple source separation tasks such as speech enhancement, speech separation, sound event separation, music source separation (MSS), or cinematic audio source separation (CASS) with a single model. These models are trained on large-scale data including speech, instruments, or sound events and can often successfully separate a wide range of sources. However, it is still challenging for such models to cover all separation tasks because some of them are contradictory (e.g., musical instruments are separated in MSS while they have to be grouped in CASS). To overcome this issue and support all the major separation tasks, we propose a task-aware unified source separation (TUSS) model. The model uses a variable number of learnable prompts to specify which source to separate, and changes its behavior depending on the given prompts, enabling it to handle all the major separation tasks including contradictory ones. Experimental results demonstrate that the proposed TUSS model successfully handles the five major separation tasks mentioned earlier. We also provide some audio examples, including both synthetic mixtures and real recordings, to demonstrate how flexibly the TUSS model changes its behavior at inference depending on the prompts.
