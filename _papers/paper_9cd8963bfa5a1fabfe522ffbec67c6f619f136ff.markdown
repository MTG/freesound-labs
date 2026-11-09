---
layout: paper
id: "9cd8963bfa5a1fabfe522ffbec67c6f619f136ff"
title: "Coarsesoundnet: Building A Reliable Model For Ecological Soundscape Analysis"
publication: "Ecological Informatics"
year: 2026
external_url: https://www.semanticscholar.org/paper/9cd8963bfa5a1fabfe522ffbec67c6f619f136ff
authors: "Alexander Gebhard, Andreas Triantafyllopoulos, Dominik Arend, Sandra Müller, Svenja Schmidt, Michael Scherer-Lorenzen, Björn Schuller"
publication_date: "2026-05-20"
---

A soundscape is composed of three types of sound: biophony (sounds made by animals), geophony (natural abiotic sounds) and anthropophony (sounds made by humans). A key research question in the field of soundscape ecology is how these components interact with each other, specifically how biophony responds to geophony and anthropophony. Nevertheless, as of today, there are not many analytical instruments that enable the distinct quantification of these elements. Recent machine learning (ML) approaches aim to support automated analysis but often rely on task-specific or clean data, limiting generalisation to noisy passive acoustic monitoring (PAM) recordings. This study presents a reproducible framework to build ML models for coarse soundscape classification and introduces CoarseSoundNet, a deep learning model trained to distinguish biophony, geophony, and anthropophony under realistic terrestrial PAM conditions. We systematically investigate model architectures, the influence of an additional training class, data composition, and evaluation strategies. Our findings suggest that model performance improves with additional PAM data, especially when similar to the target domain, and by introducing an explicit silence class during training. Post-hoc target-domain calibration employing class-specific decision thresholds further enhance performance, while incorporating minimum annotation durations yields higher scores for anthropophony and geophony. Error analyses exhibit challenges for anthropophony due to masking effects and confusions for silence and insect sounds for geophony and biophony. Finally, we conduct an ecological case study showing that pre-filtering recordings with CoarseSoundNet yields acoustic index trends broadly similar to ground-truth filtering, although the resulting improvements in their relationships with avian alpha-diversity were limited.
