---
layout: paper
id: "1d9cf44556595ac8f5ca7fae4f06dcf4f7c59e35"
title: "Data Leakage In Cross-Modal Retrieval Training: A Case Study"
publication: "ArXiv"
year: 2023
external_url: https://www.semanticscholar.org/paper/1d9cf44556595ac8f5ca7fae4f06dcf4f7c59e35
authors: "B. Weck, Xavier Serra"
publication_date: "2023-02-23"
---

The recent progress in text-based audio retrieval was largely propelled by the release of suitable datasets. Since the manual creation of such datasets is a laborious task, obtaining data from online resources can be a cheap solution to create large-scale datasets. We study the recently proposed SoundDesc benchmark dataset, which was automatically sourced from the BBC Sound Effects web page. In our analysis, we find that SoundDesc contains several duplicates that cause leakage of training data to the evaluation data. This data leakage ultimately leads to overly optimistic retrieval performance estimates in previous benchmarks. We propose new training, validation, and testing splits for the dataset that we make available online. To avoid weak contamination of the test data, we pool audio files that share similar recording setups. In our experiments, we find that the new splits serve as a more challenging benchmark.
