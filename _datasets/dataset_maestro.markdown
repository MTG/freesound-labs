---
layout: post
title: "MAESTRO Synthetic - Multi-Annotator Estimated Strong Labels"
date: 2021-9-5
project_url: https://zenodo.org/record/5126478#.YTX0vi0Ro-W
institutions:
- Machine Listening Group, Tampere University
authors: 
- Irene Martin Morato
- Manu Harju
- Annamaria Mesaros
---

MAESTRO synthetic contains 20 synthetic audio files created using [Scaper](https://github.com/justinsalamon/scaper), each of them 3 minutes long. The dataset was created for studying annotation procedures for strong labels using crowdsourcing.
The audio files contain sounds from the following classes: car_horn, children_voices, dog_bark, engine_idling, siren, street_music.
Audio files contain excerpts of recordings uploaded to [Freesound](https://freesound.org). Please see FREESOUNDCREDITS.txt for an attribution list. 

Audio files are generated using Scaper, with small changes to the synthesis procedure: Sounds were placed at random intervals, controlling for a maximum polyphony of 2. Intervals between two consecutive events are selected at random, but limited to 2-10 seconds. Event classes and event instances are chosen uniformly, and mixed with a signal-to-noise ratio (SNR) randomly selected between 0 and 20 dB over a Brownian noise background. Having two overlapping events from the same class is avoided.
