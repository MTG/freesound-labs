# Freesound Labs

This repository contains code for the frontpage of the Freesound Labs website (https://labs.freesound.org). It uses Jekyll to generate a static blog-like website.

Contents of this readme file:

<!-- TOC depthFrom:2 -->

- [Adding content](#adding-content)
    - [Posts](#posts)
    - [Papers](#papers)
    - [Datasets](#datasets)
- [Development](#development)
- [Deployment](#deployment)

<!-- /TOC -->


## Adding content

To add new **posts**, **papers** or **datasets**, please create Markdown files using the instructions below and **open a new pull request** with the changes.


### Posts

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

### Papers

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
    

### Datasets

New dataset entries should be added to the `_datasets` folder using the following template:

```
---
layout: post
title: "Dataset name"
date: 2018-03-15
project_url: https://dataset.url/with/description/and/download
image: /optional_image.png
institutions:
- Music Technology Group of Universitat Pompeu Fabra
- Institution 2
authors: 
- Name Surname
- Name Surname
- Name Surname
---
DatasetX is an audio dataset containing 11,073 audio files annotated with 41 labels of the [AudioSet Ontology](https://research.google.com/audioset////////ontology/index.html). FSDKaggle2018 has been used for the [DCASE Challenge 2018 Task 2](http://dcase.community/challenge2018/task-general-purpose-audio-tagging), which was run as a Kaggle competition titled [Freesound General-Purpose Audio Tagging Challenge](https://www.kaggle.com/c/freesound-audio-tagging). The description should not be very long or it will look bad in the website ;)

```


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
