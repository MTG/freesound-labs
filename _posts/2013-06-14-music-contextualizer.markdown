---
layout: post
title:  "Music Contextualizr"
date:   2013-06-14  12:00:00
release_date: 2013-06-14 12:00:00
categories: 
- Apps
tags:
- music-hackday 
- lyrics
- music
by: 
- Quim Llimona
code: https://github.com/lemonzi/MusicContextualizer
---

Don't you think that sometimes songs (musically speaking) have nothing to do with their lyrics? Well, **Music Contextualizr** tries to solves this, although it's a bit extreme.

Give it a sound file, and it will give you back another sound that contains Freesound samples with tags that actually match the lyrics.

On the backend, it basically fingerprints the audio with the Echonest ENMFP, queries it in their server to find out the track, from this it derives possible MusixMatch IDs, fetches lyrics from them, processes them using a linguistic model and queries the main words to Freesound. The number of sounds assigned to each main word depends on its weight.