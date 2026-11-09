---
layout: paper
id: "2e6b5f1fd3bd2b6624b28960dba9aa15c45f8b1c"
title: "Few-Shot Learning Of New Sound Classes For Target Sound Extraction"
publication: "Interspeech 2021"
year: 2021
external_url: https://www.semanticscholar.org/paper/2e6b5f1fd3bd2b6624b28960dba9aa15c45f8b1c
authors: "M. Delcroix, Jorge Bennasar V'azquez, Tsubasa Ochiai, K. Kinoshita, S. Araki"
---

Target sound extraction consists of extracting the sound of a target acoustic event (AE) class from a mixture of AE sounds. It can be realized using a neural network that extracts the target sound conditioned on a 1-hot vector that represents the desired AE class. With this approach, embedding vectors associated with the AE classes are directly optimized for the extraction of sound classes seen during training. However, it is not easy to extend this framework to new AE classes, i.e. unseen during training. Recently, speech, music, or AE sound extraction based on enrollment audio of the desired sound offers the potential of extracting any target sound in a mixture given only a short audio signal of a similar sound. In this work, we propose combining 1-hot- and enrollment-based target sound extraction, allowing optimal performance for seen AE classes and simple extension to new classes. In experiments with synthesized sound mixtures generated with the Freesound Dataset (FSD) datasets, we demonstrate the benefit of the combined framework for both seen and new AE classes. Besides, we also propose adapting the embedding vectors obtained from a few enrollment audio samples (few-shot) to further improve performance on new classes.
