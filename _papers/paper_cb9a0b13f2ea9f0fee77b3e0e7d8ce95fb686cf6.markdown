---
layout: paper
id: "cb9a0b13f2ea9f0fee77b3e0e7d8ce95fb686cf6"
title: "Grammar-Guided Hierarchical Parsing For Long-Form Audio Activity Recognition"
publication: "Interspeech"
year: 2026
external_url: https://www.semanticscholar.org/paper/cb9a0b13f2ea9f0fee77b3e0e7d8ce95fb686cf6
authors: "Peng Zhang, Qing-Yu Luo, Philip J. B. Jackson, Wen-Wu Wang"
---

Long-form audio exhibits an inherent hierarchy: fine-grained events form sub-activities, which in turn constitute higher-level activities. Prior work often models these levels separately, leading to cross-level inconsistencies and requiring supervision at multiple levels. We formulate the problem as hierarchical parsing from event-level evidence: given detected event segments with class posteriors, we infer an order-consistent Act-Sub-Event parse tree. We propose Hierarchical Activity Grammar, encoding hierarchical composition and temporal-order constraints, and perform grammar-guided decoding that combines event evidence with a grammar prior. This yields a temporally grounded parse tree from which sub-activity segmentation and activity classification are derived, without requiring sub-activity or activity labels for training. Experiments on the long-form MultiAct audio dataset demonstrate improved temporal-order consistency (Edit score) and produces interpretable hierarchies.
