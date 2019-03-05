---
layout: post
title:  "Freesound Timeline"
date:   2017-11-23 12:30:00
release_date: 2017-11-23 12:30:00
categories: 
- Apps
tags: 
- sound-exploration
- soundscape
- radio
- spatalization
project_url: https://ffont.github.io/freesound-timeline/
code: http://github.com/ffont/freesound-timeline/
image: /freesound_timeline.png
by: 
- Frederic Font
- Tony Martinez
---

**Freesound Timeline** is an app that automatically generates soundscapes using the most popular sounds from [Freesound](https://freesound.org) for a given year and month. I originally implemented Freesound Timeline back in 2011 when I was starting to learn about web technologies. 
In 2018 I updated it to make use <a href="https://freesound.org" target="_blank">Freesound</a> APIv2 and the Web Audio API, and to add new killer features such as random spacialization of sounds in a 3D space (using WebAudio's HRTF panning), and the <i>autoadvance</i> mode to let Freesound Timeline automatically advance through Freesound history. A new shiny interface was added in 2019, designed by the great **Tony Martinez**.

I hoped usage instructions would not be needed, but just in case: 
 
 * Choose a **year** an and a **month** and hit the play button. Freesound Timeline will start playing a soundscape based on popular sounds added to Freesound during that year and month.

 * Set the **density** to a value between 5 and 100. The higher the value, the more *dense* will be the generated soundscape (i.e. more sounds playing at the same time).

 * Switch between **RT** and **DL** modes to change the way in which Freesound Timeline chooses the most popular sounds for a given month an year. *DL* mode will select sounds based on number of downloads. *RT* will do it based on average rating.

 * Turn **autoadvance** mode on or off to let Freesound Timeline slowly move ahead in time starting on the year and month you previously selected.

Here are a couple of examples of soundscapes that I generated with Freesound Timeline:

<p><iframe src="https://freesound.org/embed/sound/iframe/456500/simple/full_size/" width="650" height="200" frameborder="0" scrolling="no"></iframe></p>
<p><iframe src="https://freesound.org/embed/sound/iframe/456501/simple/full_size/" width="650" height="200" frameborder="0" scrolling="no"></iframe></p>

You can [access Freesound Timeline here](https://ffont.github.io/freesound-timeline/). Enjoy!




