---
layout: post
title:  "SOURCE, a Freesound Community Sampler"
date:   2021-05-28 06:00:00
release_date: 2021-05-28 06:00:00
categories: 
- Apps
tags:
- freesound-api
- hardware
- elk
- sampler
- music-creation
code: https://github.com/ffont/source
image: /source.png
by: 
- Frederic Font
---

SOURCE is an open-source music sampler powered by [Freesound](https://freesound.org)'s collection of 500k Creative Commons sounds contributed by a community of thousands of people around the world. SOURCE is a sampler that *does not sample*. Instead, it provides different ways to load sounds from Freesound and instantly generate new sound palettes to enrich the creative process and bring an endless SOURCE of inspiration.

SOURCE is designed to run as a stand-alone device on a hardware solution based on a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), the [Elk Pi](https://elk.audio/extended-dev-kit) hat for the Raspberry Pi (which provides low-latency multi-channel audio I/O), and the [Elk BLACKBOARD](https://elk.audio/blackboard) controller board (which provides the user interface elements including buttons, faders, a display, and the audio I/O connectors). However, the core of SOURCE is implemented as a standard audio plugin using [JUCE](https://juce.com). That allows SOURCE to also be loaded in DAWs that support VST/AU plugins, or even run as a stand-alone and cross-platform application in desktop computers (eventhough with somewhat limited functionality). The picture below shows the looks of SOURCE as deployed with the Elk hardware stack:

Here is a video demonstrating some features of SOURCE in action:

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=7EXMY0AvBxo" frameborder="0" allowfullscreen></iframe>

SOURCE implements audio playback functionality which is common in many existing music samplers. Perhaps more interesting and unique are the capabilities of SOURCE for interacting with Freesound, searching and retrieving sounds. The SOURCE demonstration video above showcases some of this possibilities. Here is a (potentially incomplete) list of features:

* Search sounds in Freesound in real-time and download them to the sampler
* Filter sounds by:
 * Textual query terms
 * Duration
 * Creartive Commons license
 * Perceptual qualities like: *brightness*, *hardness* and *depth*
* Replace loaded sounds by other sounds that are acoustically similar (using Freesound's similarity search feature)
* Random search mode that will retrieve unexpected sounds from Freesound
* Load any number of sounds (only limited by RAM memory)
* Map loaded sounds to MIDI notes automatically using *contiguous* or *interleaved* modes, or map them arbitrarily using a mapping editor
* For each sound loaded, configure sound paramters such as:
 * Start and end position
 * Play modes including looping and slicing
 * Loop start and end positions
 * ADSR amplitude envelope
 * Low-pass filter with ADSR envelope
 * MIDI root note and global pitch shift (based on playback speed)
 * Freeze mode in which the playhead position can be controlled as a sound parameter
 * Modulation of some of the above parameters with velocity and aftertouch (including support for polyhonic aftertouch)
 * Control some of the above parameters with MIDI Control Change
* Get a *sound usage log* which lists the historic of sounds that have been used and can help in the Creative Commons attribution process

More information in the source code page!