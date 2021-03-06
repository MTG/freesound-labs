---
layout: post
title:  "Freesound Loop Generator"
date:   2020-03-04 12:00:00
release_date: 2020-03-04 12:00:00
categories: 
- Apps
tags:
- music-hackday 
- drum-machine
- music-creation
- freesound-api 
project_url: https://ffont.github.io/freesound-loop-generator
code: https://github.com/ffont/freesound-loop-generator
image: /flg.png
by: 
- Frederic Font
---

The **Freesound Loop Generator** (FLG) is a tool to create music loops using Freesound sounds. It contains a 16 pads, 
a simple 16-step sequencer and several methods to load Freesound sounds into the pads. FLG allows you to export
the loops you make as WAV files and also allows you to download the sounds loaded in each pad rendered as a single
32-seconds long WAV file with sounds spaced every 2 seconds so you can easily load the sounds in your sampler of chocie. 
Additionally, the sequences made in FLG can also be exported as MIDI files so you can recreate the loops in your favorite software.

Some example loops generated with FLG:

<iframe src="https://freesound.org/embed/sound/iframe/507689/simple/full_size/" width="650" height="200" frameborder="0" scrolling="no"></iframe>

<iframe src="https://freesound.org/embed/sound/iframe/507684/simple/full_size/" width="650" height="200" frameborder="0" scrolling="no"></iframe>

<iframe src="https://freesound.org/embed/sound/iframe/507681/simple/full_size/" width="650" height="200" frameborder="0" scrolling="no"></iframe>

For more examples you can check [this pack of sounds](https://freesound.org/people/frederic.font/packs/28449/) in Freesound.

FLG is a newer version (2020 update) of the old **FreeMaschine!** hack developed by Javi Agenjo, Bram de Jong and Frederic 
Font at Barcelona Music Hack Day 2014 ([see video here](https://www.youtube.com/watch?v=NCYBjv2wDAw)). It includes a bit 
(not too much) of code refactoring, but most of the code is still pretty old and probably contains many bugs.
