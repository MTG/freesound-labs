---
layout: post
title: "SimSceneTVB Learning"
date: 2019-06-18
project_url: https://zenodo.org/record/3248703#.XlzBhabRZUQ
institutions:
- Ecole Centrale de Nantes
- University of Paris Seine, University of Cergy-Pontoise, ENSEA
authors: 
- Felix Gontier 
- Mathieu Lagrange
- Pierre Aumond
- Catherine Lavandier
- Jean-François Petiot
---
This is a dataset of 600 simulated sound scenes of 45s each representing urban sound environments, simulated using the [simScene Matlab library](https://bitbucket.org/mlagrange/simscene). The dataset is divided in two parts with a train subset (400 scenes) and a test subset (200 scenes) for the development of learning-based models. Each scene is composed of three main sources (traffic, human voices and birds) according to an original scenario, which is composed semi-randomly conditionally to five ambiances: park, quiet street, noisy street, very noisy street and square. Separate channels for the contribution of each source are available. The base audio files used for simulation are obtained from [Freesound](https://freesound.org) and [LibriSpeech](http://www.openslr.org/12). The sound scenes are scaled according to a playback sound level in dB, which is drawn randomly but remains plausible according to the ambiance.
