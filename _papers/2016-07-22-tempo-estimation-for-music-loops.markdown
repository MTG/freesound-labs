---
layout: post
title:  "Tempo Estimation for Music Loops and a Simple Confidence Measure"
date:   2016-07-22 12:30:00
publication_date: 2016-07-22 12:30:00
publication: International Society of Music Information Retrieval conference (ISMIR)
categories: 
- research
tags:
- tempo-estimation
- loops
- bpm
- confidence-measure
project_url: http://mtg.upf.edu/node/3479
code: https://github.com/ffont/ismir2016
authors: Frederic Font, Xavier Serra
---

**Abstract**<br>
Tempo estimation is a common task within the music information retrieval community, but existing works are rarely evaluated with datasets of music loops and the algorithms are not tailored to this particular type of content. In addition to this, existing works on tempo estimation do not put an emphasis on providing a confidence value that indicates how reliable their tempo estimations are. In current music creation contexts, it is common for users to search for and use loops shared in online repositories.
These loops are typically not produced by professionals and lack annotations. Hence, the existence of reliable tempo estimation algorithms becomes necessary to enhance the reusability of loops shared in such repositories. In this paper, we test six existing tempo estimation algorithms against four music loop datasets containing more than 35k loops. We also propose a simple and computationally cheap confidence measure that can be applied to any existing algorithm to estimate the reliability of their tempo predictions when applied to music loops. We analyse the accuracy of the algorithms in combination with our proposed confidence measure, and see that we can significantly improve the algorithms' performance when only considering music loops with high estimated confidence.

