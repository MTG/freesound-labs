---
layout: post
title:  "Freesound Trip"
date:   2017-06-17 12:30:00
release_date: 2017-06-17 12:30:00
categories: 
- Apps
tags:
- visualization 
- sound-exploration
project_url: http://5.2.16.88/Freesound-Trip/
code: https://github.com/dnlopez/Freesound-Trip
image: /freesound_trip_space.png
by: 
- CJ Carr
- Daniel Lopez
- Emilio Molina
- Mónica Rikić
- Lefteris Stamellos
---

**Freesound Trip** is a web application that automatically arranges the sounds from [Freesound](http://www.freesound.org) in a three-dimensional space and lets the user fly manually through this space with a first-person perspective, hearing sounds as they get close.

Sounds are prearranged in the space by a process of t-Distributed Stochastic Neighbor Embedding (t-SNE) on MIR descriptors in order to cluster sounds with similar sonic qualities together. Furthermore, the user can choose to filter what sounds get included in their space by Freesound tags.

On approaching a sound, it is automatically played in a sequenced loop at pseudorandom intervals, for rhythmic effect. (The sounds were also prefiltered to include the shorter sounds only, to suit their percussive usage.)

Freesound Trip was created for the [Audio Commons](http://www.audiocommons.org) challenge of the [Sónar Innovation Challenge](http://sic.upf.edu) 2017.
