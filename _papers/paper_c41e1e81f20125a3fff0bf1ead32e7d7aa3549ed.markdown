---
layout: paper
id: "c41e1e81f20125a3fff0bf1ead32e7d7aa3549ed"
title: "Interaural Time Difference Loss For Binaural Target Sound Extraction"
publication: "ArXiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/c41e1e81f20125a3fff0bf1ead32e7d7aa3549ed
authors: "Carlos Hernandez-Olivan, Marc Delcroix, Tsubasa Ochiai, Naohiro Tawara, Tomohiro Nakatani, Shoko Araki"
publication_date: "2024-08-01"
---

Binaural target sound extraction (TSE) aims to extract a desired sound from a binaural mixture of arbitrary sounds while preserving the spatial cues of the desired sound. Indeed, for many applications, the target sound signal and its spatial cues carry important information about the sound source. Binaural TSE can be realized with a neural network trained to output only the desired sound given a binaural mixture and an embedding characterizing the desired sound class as inputs. Conventional TSE systems are trained using signal-level losses, which measure the difference between the extracted and reference signals for the left and right channels. In this paper, we propose adding explicit spatial losses to better preserve the spatial cues of the target sound. In particular, we explore losses aiming at preserving the interaural level (ILD), phase (IPD), and time differences (ITD). We show experimentally that adding such spatial losses, particularly our newly proposed ITD loss, helps preserve better spatial cues while maintaining the signal-level metrics.
