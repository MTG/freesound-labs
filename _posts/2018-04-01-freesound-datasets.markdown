---
layout: post
title:  "Freesound Datasets"
date:   2018-04-01 12:00:00
release_date: 2018-04-01 12:00:00
categories: 
- Apps
tags: 
- research
- dataset
project_url: https://datasets.freesound.org
code: https://github.com/MTG/freesound-datasets
image: /freesound_datasets.png
by: 
- Xavier Favory
- Eduardo Fonseca
- Jordi Pons
- Frederic Font
---

**Freesound Datasets** is an online platform for the collaborative creation of open audio collections. It hosts several microtasks which enable people to contribute to the creation of datasets.

<a href="/assets/FSD_validation_task.png" target="blank"><img style="margin:auto;margin-bottom:25px;margin-top:25px;max-width:640px;" class="img-responsive" src="/assets/FSD_validation_task.png" alt="Validation task">
</a>

Openly available datasets are a key factor in the advancement of sound and music computing technologies. Quite a number of audio datasets are now available but often their creation process lack of transparency and they are not completly open and sharable. Moreover, they are often not large enough for supporting current machine learning needs. These shortcomings motivated our initiative in creating **Freesound Datasets**, an online platform for the collaborative creation of open audio collections. It leverages Freesound (>400k sounds) as a source of open audio content, relies on a community to sustainably crowdsource high-quality sound annotations, and it follows the principles of transparency, openness, dynamic character, and sustainability.

<a href="/assets/FSD_familiarisation_interface.png" target="blank"><img style="margin:auto;margin-bottom:25px;margin-top:25px;max-width:640px;" class="img-responsive" src="/assets/FSD_familiarisation_interface.png" alt="Familiarisation interface">
</a>

In particular, we started the creation of **FSD**, a dataset of everyday sounds, containing thousands of audio samples from Freesound and organised following the <a href="https://research.google.com/audioset/" target="_blank">AudioSet Ontology</a>. FSD presents annotations that express the presence of a sound category in audio samples. The creation of FSD started with the automatic population of each category in the AudioSet Ontology with a number of candidate audio samples from Freesound. This process automatically generated over 600k candidate annotations. To verify the validity of these automatically generated
annotations, we developed a validation tool with an interface that helps users to understand a category and its context in the AudioSet Ontology.

More information can be found in our [ISMIR2017 paper](https://repositori.upf.edu/handle/10230/33299).
