---
layout: paper
id: "ded66d6a7de954939fe145faa63c8ae6730c7f1f"
title: "Do Bioacoustic Foundation Models Hear Through The Noise ? Snr And Generalization In Underwater Detection"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/ded66d6a7de954939fe145faa63c8ae6730c7f1f
authors: "Lucie Jean-Labadye, Nicolas Farrugia, Axel Marmoret, D. Cazau, Olivier Adam"
publication_date: "2026-10-20"
---

Bioacoustic foundation models are claimed to generalize across taxa and recording conditions, but are trained mainly on terrestrial archives of focal, high-quality recordings and evaluated on benchmarks emphasizing architecture over data conditions. We evaluate four such models as frozen encoders on an underwater detection task, using linear probing on continuously recorded data from the Kerguelen Plateau. Four datasets of identical size were built to differ only in the signal-to-noise ratio (SNR) of their positive segments, and probes were trained and evaluated across all combinations. Evaluation SNR accounts for more variation in average precision (AP) than model choice, and performance peaks when training and evaluation share a noise regime --- the configuration least representative of a continuous deployment. Training on mixed SNR redistributes performance toward low-SNR conditions without improving it overall, and AP remains low throughout. In light of these results, we call for evaluation standards grounded in realistic noise and deployment conditions rather than curated, high-quality recordings.
