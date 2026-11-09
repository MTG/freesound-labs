---
layout: paper
id: "482af9f67d4642b305bc5e5242e1dfd6ce1eeb1b"
title: "Single-Ended Quality Measurement Of A Music Content Via Convolutional Recurrent Neural Networks"
publication: "Metrology and Measurement Systems"
year: 2023
external_url: https://www.semanticscholar.org/paper/482af9f67d4642b305bc5e5242e1dfd6ce1eeb1b
authors: "Kamila Organiściak, J. Borkowski"
publication_date: "2023-07-20"
---

The paper examines the usage of Convolutional Bidirectional Recurrent Neural Network (CBRNN) for a problem of quality measurement in a music content. The key contribution in this approach, compared to the existing research, is that the examined model is evaluated in terms of detecting acoustic anomalies without the requirement to provide a reference (clean) signal. Since real music content may include some modes of instrumental sounds, speech and singing voice or diﬀerent audio eﬀects, it is more complex to analyze than clean speech or artiﬁcial signals, especially without a comparison to the known reference content. The presented results might be treated as a proof of concept, since some speciﬁc types of artefacts are covered in this paper (examples of quantization defect, missing sound, distortion of gain characteristics, extra noise sound). However, the described model can be easily expanded to detect other impairments or used as a pre-trained model for other transfer learning processes. To examine the model eﬃciency several experiments have been performed and reported in the paper. The raw audio samples were transformed into Mel-scaled spectrograms and transferred as input to the model, ﬁrst independently, then along with additional features (Zero Crossing Rate, Spectral Contrast). According to the obtained results, there is a signiﬁcant increase in overall accuracy (by 10.1%), if Spectral Contrast information is provided together with Mel-scaled spectrograms. The paper examines also the inﬂuence of recursive layers on eﬀectiveness of the artefact classiﬁcation
