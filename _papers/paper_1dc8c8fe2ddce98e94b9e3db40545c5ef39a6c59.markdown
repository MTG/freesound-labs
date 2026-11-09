---
layout: paper
id: "1dc8c8fe2ddce98e94b9e3db40545c5ef39a6c59"
title: "Overcoming Label Noise In Audio Event Detection Using Sequential Labeling"
publication: "ArXiv"
year: 2020
external_url: https://www.semanticscholar.org/paper/1dc8c8fe2ddce98e94b9e3db40545c5ef39a6c59
authors: "Jae-Bin Kim, Seongkyu Mun, Myungwoo Oh, Soyeon Choe, Yong-Hyeok Lee, Hyung-Min Park"
publication_date: "2020-07-10"
---

This paper addresses the noisy label issue in audio event detection (AED) by refining strong labels as sequential labels with inaccurate timestamps removed. In AED, strong labels contain the occurrence of a specific event and its timestamps corresponding to the start and end of the event in an audio clip. The timestamps depend on subjectivity of each annotator, and their label noise is inevitable. Contrary to the strong labels, weak labels indicate only the occurrence of a specific event. They do not have the label noise caused by the timestamps, but the time information is excluded. To fully exploit information from available strong and weak labels, we propose an AED scheme to train with sequential labels in addition to the given strong and weak labels after converting the strong labels into the sequential labels. Using sequential labels consistently improved the performance particularly with the segment-based F-score by focusing on occurrences of events. In the mean-teacher-based approach for semi-supervised learning, including an early step with sequential prediction in addition to supervised learning with sequential labels mitigated label noise and inaccurate prediction of the teacher model and improved the segment-based F-score significantly while maintaining the event-based F-score.
