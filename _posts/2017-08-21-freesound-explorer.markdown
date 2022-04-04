---
layout: post
title:  "Freesound Explorer"
date:   2017-08-21 12:30:00
release_date: 2017-08-21 12:30:00
categories: 
- Apps
tags:
- visualization 
- sound-exploration
- music creation
- audiocommons
project_url: http://labs.freesound.org/fse/
code: http://github.com/ffont/freesound-explorer/
image: /freesound_explorer2.png
by: 
- Frederic Font
- Giuseppe Bandiera
---

**Freesound Explorer** is a visual interface for exploring [Freesound](https://freesound.org) in a 2-dimensional space and create music at the same time :)

Using Freesound Explorer you can perform text-based queries in Freesound, and see the results arranged in a 2-dimensional space. A well known dimensionality reduction technique is used ([tSNEJS](https://github.com/karpathy/tsnejs)) to learn a space from spectral audio features provided by Freesound. In this way, sounds are self-organised according to some sort of timbre similarity.

Freesound Explorer is implemented as a web application which takes advantage of modern web technologies including the [Web Audio API](https://www.w3.org/TR/webaudio/) and the [Web MIDI API](https://www.w3.org/TR/webmidi/). Freesound Explorer also uses a Python [Flask](http://flask.pocoo.org) backend for handling user accounts, but it can also be run statically without the backend (with reduced functionality and no user handling).

More information can be found in the [demo paper](https://repositori.upf.edu/handle/10230/32538?locale-attribute=en) that was presented at the Web Audio Conference 2017 held at Queen Mary University of London.

Freesound Explorer has been (so far) developed by Frederic Font and Giuseppe Bandiera, researchers at the [Music Technology Group](http://mtg.upf.edu) of Universitat Pompeu Fabra, Barcelona. External contributions are welcome!

