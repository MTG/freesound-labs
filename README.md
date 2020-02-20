# Freesound Labs

This repository contains code for the frontpage of the Freesound Labs website (https://labs.freesound.org).
It uses Jekyll to generate a static blog-like website.

Here is an example template for new posts (which should be placed in the `_posts` folder):

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

New papers should be added in the `_papers_manual` section using the following template:

```
---
layout: paper
type: inproceedings
id: "meutzner2016non"
title: "A non-speech audio CAPTCHA based on acoustic event detection and classification"
publication: "2016 24th European Signal Processing Conference (EUSIPCO)"
year: 2016
external_url: https://ieeexplore.ieee.org/abstract/document/7760649/
authors: "Meutzner, Hendrik and Kolossa, Dorothea"
---
```

Currently papers can be automatically added automatycally using the `retrieve_papers.py` script. The script will combine the
papers manually introduced in the `_papers_mannual` folder with automatic citations found using Google Scholar API. See
instructions below for tunning the script.
    

## Development

Freesound Labs website can be build using a Dockerized Jekyll installation which comes with all necessary dependencies bundled in.

First you'll need to build the "builder" image (in case it has not been built already). Simply run:

    docker build -t fslabs-builder .  


Then you can build the Freesound Labs website with the command:

    docker run --rm --volume="$PWD:/srv/jekyll" -it fslabs-builder jekyll build


You can run the development server with the command:

    docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it fslabs-builder jekyll serve

...and point your browser to `http://0.0.0.0:4000`. Changes in will trigger the re-generation of the site.


The `retrieve_papers.py` script can be run with the following command:


    docker run --rm --volume="$PWD:/srv/jekyll" -it fslabs-builder python3 retrieve_papers.py --remote --local

It should be run before building the site for the papers to appear in it.

NOTE: all commands above should be run from the root of the repository


## Deployment

Deploy commands use Python's Fabric (v1.x) and can be found in `fabfile.py`. Use `fab deploy` to deploy. 
Currently, Jekyll site is built remotely in the server.
