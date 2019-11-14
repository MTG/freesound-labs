---
layout: post
title:  "Freesound API JUCE examples"
date:   2019-11-14 10:30:00
release_date: 2019-11-14 10:30:00
categories: 
- Apps
tags: 
- freesound-api
- sampler
- uploader
- development
project_url: https://github.com/mtg/freesound-juce
code: https://github.com/mtg/freesound-juce
image: /juce_examples.png
by: 
- Antonio Ramires
- Frederic Font
---

[JUCE](https://juce.com) is probably the most popular framework for developing audio apps and an standard in the industry. For the [Audio Developers Conference 2019](https://adc19.sched.com), we prepared a JUCE client for the Freesound API that facilitates the integration of Freesound content in audio applications developed using the JUCE framework.

Together with the release of the JUCE client we included two example plugins named [FreesoundUploader](https://github.com/aframires/FreesoundUploader) and [FreesoundSimpleSampler](https://github.com/ffont/FreesoundSimpleSampler). The first one allows you to login to Freesound within the plugin and to upload sounds to Freesound by dragging clips from the host DAW. You can add metadata and choose license as you'd do normally using Freesound's web interface. The second example is a simple sampler that allows users to make a query to Freesound and build a sampler based on the first 16 results. Sounds are automatically mapped in the full MIDI note range. These two plugins ara available for your use but you'll need to compile them following the instructions in the code repositories linked above.