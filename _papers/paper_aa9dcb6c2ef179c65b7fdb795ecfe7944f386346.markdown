---
layout: paper
id: "aa9dcb6c2ef179c65b7fdb795ecfe7944f386346"
title: "What Do Language Models Hear? Probing For Auditory Representations In Language Models"
publication: "ArXiv"
year: 2024
external_url: https://www.semanticscholar.org/paper/aa9dcb6c2ef179c65b7fdb795ecfe7944f386346
authors: "Jerry Ngo, Yoon Kim"
publication_date: "2024-02-26"
---

This work explores whether language models encode meaningfully grounded representations of sounds of objects. We learn a linear probe that retrieves the correct text representation of an object given a snippet of audio related to that object, where the sound representation is given by a pretrained audio model. This probe is trained via a contrastive loss that pushes the language representations and sound representations of an object to be close to one another. After training, the probe is tested on its ability to generalize to objects that were not seen during training. Across different language models and audio models, we find that the probe generalization is above chance in many cases, indicating that despite being trained only on raw text, language models encode grounded knowledge of sounds for some objects.
