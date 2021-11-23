---
layout: post
title: "ARCA23K"
date: 2021-09-15
project_url: https://zenodo.org/record/5117901
institutions:
- University of Surrey, Centre for Vision, Speech and Signal Processing, Audio Research Group
authors: 
- Turab Iqbal
- Tin Cao
- Andrew Bailey
- Mark D. Plumbley
- Wenwu Wang
---

ARCA23K is a dataset of labelled sound events created to investigate real-world label noise. It contains 23,727 audio clips originating from Freesound, and each clip belongs to one of 70 classes taken from the AudioSet ontology. The dataset was created using an entirely automated process with no manual verification of the data. For this reason, many clips are expected to be labelled incorrectly.

In addition to ARCA23K, this release includes a companion dataset called ARCA23K-FSD, which is a single-label subset of the FSD50K dataset. ARCA23K-FSD contains the same sound classes as ARCA23K and the same number of audio clips per class. As it is a subset of FSD50K, each clip and its label have been manually verified. Note that only the ground truth data of ARCA23K-FSD is distributed in this release. To download the audio clips, please visit the Zenodo page for FSD50K.

The source code used to create the datasets is available: https://github.com/tqbl/arca23k-dataset