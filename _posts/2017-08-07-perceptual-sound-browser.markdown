---
layout: post
title:  "Perceptual Sound Browser"
date:   2017-08-31 12:30:00
release_date: 2017-08-31 12:30:00
categories: 
- Apps
tags:
- perceptual
- sound-postproduction
- browsing
- audiocommons
code: https://github.com/albincorreya/PerceptualSoundBrowser
image: /perceptual_sound_browser.png
by: 
- Albin Andrew Correya
---

**Percetual Sound Browser** is a demo prototype of a sound browser which enables you browsing sounds by their high-level acoustic/perceptual qualities such as brightness, roughness, hardness and depth. All these features are computed from the original audio content itself, locally. This was developed as a probe system in further investigating the scope of integrating high-level semantic features into audio production environments. 

The entire project was developed in Max-MSP environment. This project uses [Freesound Max-MSP modules](https://github.com/albincorreya/Freesound_Max-MSP_Modules) for accessing [Freesound](https://freesound.org) API services. 

For the moment, this patch only uses a small customised dataset of 700 sounds (7 classes) from Freesound. But, you can integrate any freesound collections by using the attached feature extraction python scripts in the instructions.

This project uses [timbral sound models](https://github.com/AudioCommons/timbral_models) developed by Andy Pearce for off-line feature extraction. It was developed by [Albin Andrew Correya](https://albincorreya.wordpress.com) at the [Music Technology Group](http://mtg.upf.edu) of Universitat Pompeu Fabra as part of the [AudioCommons](https://www.audiocommons.org) project.

<iframe src="https://player.vimeo.com/video/231350962" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/231350962">Perceptual Sound Browser - Demo</a> from <a href="https://vimeo.com/user64899531">Albin Correya</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
