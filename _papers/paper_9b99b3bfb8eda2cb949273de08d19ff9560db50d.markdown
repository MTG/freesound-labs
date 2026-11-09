---
layout: paper
id: "9b99b3bfb8eda2cb949273de08d19ff9560db50d"
title: "Unikw-At: Unified Keyword Spotting And Audio Tagging"
publication: "INTERSPEECH"
year: 2022
external_url: https://www.semanticscholar.org/paper/9b99b3bfb8eda2cb949273de08d19ff9560db50d
authors: "Heinrich Dinkel, Yongqing Wang, Zhiyong Yan, Junbo Zhang, Yujun Wang"
publication_date: "2022-09-18"
---

Within the audio research community and the industry, keyword spotting (KWS) and audio tagging (AT) are seen as two distinct tasks and research ﬁelds. However, from a technical point of view, both of these tasks are identical: they predict a label (key-word in KWS, sound event in AT) for some ﬁxed-sized input audio segment. This work proposes UniKW-AT: An initial approach for jointly training both KWS and AT. UniKW-AT enhances the noise-robustness for KWS, while also being able to predict speciﬁc sound events and enabling conditional wake-ups on sound events. Our approach extends the AT pipeline with additional labels describing the presence of a keyword. Experiments are conducted on the Google Speech Commands V1 (GSCV1) and the balanced Audioset (AS) datasets. The proposed MobileNetV2 model achieves an accuracy of 97.53% on the GSCV1 dataset and an mAP of 33.4 on the AS evaluation set. Further, we show that signiﬁcant noise-robustness gains can be observed on a real-world KWS dataset, greatly outperforming standard KWS approaches. Our study shows that KWS and AT can be merged into a single framework without signiﬁcant performance degradation.
