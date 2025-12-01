# Freesound Labs

This repository contains code for the frontpage of the Freesound Labs website (https://labs.freesound.org). It uses Jekyll to generate a static blog-like website.


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

Papers can be automatically added using the `retrieve_papers.py` script. However, papers can also be manually added by adding their
Semantic Scholar URL to the file `manual_paper_semantic_scholar_urls.txt` (one per line). The `retrieve_papers.py` script will combine the
papers manually introduced with the automatic citations found using Semantic Scholar API. See
instructions below for running the script.

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

    docker run --rm --volume="$PWD:/srv/jekyll" -it fslabs-builder python3 retrieve_papers.py

It should be run before building the site for the papers to appear in it.

NOTE: all commands above should be run from the root of the repository


## Deployment

After page updates are commited to this repository, a deployment job needs to be manually run from the `mtg-deploy` repository (see README there under `fs-labs` folder) for the changes to become public.

Nota that this job does not automatically update the list of papers of the "papers" section. To that end, the `retreive_papers.py` script should be run and the new files created should be added and committed to this repo before running the dpeloyment job from `mtg-deploy.

To do that, run the `retreive_papers.py` script locally using:

    docker run --rm --volume="$PWD:/srv/jekyll" -it fslabs-builder python3 retrieve_papers.py
