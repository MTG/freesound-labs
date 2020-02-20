---
layout: post
title:  "Shortest Path Techniques for Annotation and Retrieval of Environmental Sounds"
date:   2012-10-08 12:30:00
publication_date: 2012-10-08 12:30:00
publication: International Society for Music Information Retrieval Conference
categories: 
- research
tags:
- environmental-sounds
project_url: http://ismir2012.ismir.net/event/papers/541_ISMIR_2012.pdf
authors: Brandon Mechtley , Perry Cook , Andreas Spanias
---

**Abstract**<br>
Many techniques for text-based retrieval and automatic annotation of music and sound effects rely on learning with explicit generalization, training individual classifiers for each tag. Non-parametric approaches, where queries are individually compared to training instances, can provide added flexibility, both in terms of robustness to shifts in database content and support for foreign queries, such as concepts not yet included in the database. In this paper, we build upon prior work in designing an ontological framework for annotation and retrieval of environmental sounds, where shortest paths are used to navigate a network containing edges that represent content-based similarity, semantic similarity, and user tagging data. We evaluate novel techniques for ordering query results using weights of both shortest paths and minimum cost paths of specified lengths, pruning outbound edges by nodes ’ K nearest neighbors, and adjusting edge weights depending on type (acoustic, semantic, or user tagging). We evaluate these methods both through traditional cross-validation and through simulation of live systems containing a complete collection of sounds and tags but incomplete tagging data.
