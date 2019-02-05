# Freesound Labs

Frontpage of the Freesound Labs website (https://labs.freesound.org).
It uses Jekyll to generate static blog-like website.
Deploy commands use Python's Fabric (v1.x) and can be found in `fabfile.py`. Use `fab deploy` to deploy. 
Jekyll site is built in the remote server.

Use the following as a template for new posts:

```
---
layout: post
title:  "Title of the entry"
date:   YYYY-MM-DD 12:00:00
release_date: YYYY-MM-DD 12:00:00
categories: 
- Apps
- Research
- Educational
tags: 
- freesound-api
- music-creation
project_url: https://...
code: https://...
image: /filename.png
by: 
- Name Surname
- Name Surname
---

Description for the entry.


<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUTUBE_ID" frameborder="0" allowfullscreen></iframe>


```
