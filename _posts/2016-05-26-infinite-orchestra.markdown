---
layout: post
title:  "Infinite Orcherstra"
date:   2016-05-26 12:00:00
release_date: 2016-05-26 12:00:00
categories: 
- Apps
tags:
- python
- freesound-api
- performance
code: https://github.com/hellska/InfiniteOrchestra
project_url: http://labs.freesound.org/api_demos/
image: /infinite_orchestra.png
by: 
- Daniele Scarano
- Chromahelix
---


The InfinitOrchestra app is designed for audience interaction during a live act, each user that interacts with the app is an active member in the performance and there is no limit to the number of performers. This application is used by [Chromahelix](http://chromahelix.com/) during their live acts, through the application interface the Freesound ids selected by the audience are accessed to download, play and manipulate the correspondent samples. The interface permit the user to search a sound from Freesound using a simple text search. The search is accomplished using the freesound-python client and the parameters of the search are fixed, but can be edited in the app source code. The Freesound text search is very powerful and returns all the sounds that contain the used word in the filename, in the description and in the tags so based on this behaviour a randomization mechanism avoids the download of the same sound even if the same search text is used. 
