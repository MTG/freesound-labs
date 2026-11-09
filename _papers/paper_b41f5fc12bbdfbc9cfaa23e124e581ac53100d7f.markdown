---
layout: paper
id: "b41f5fc12bbdfbc9cfaa23e124e581ac53100d7f"
title: "Investigating Invariances In Auditory Event Categorization With Model Metamers"
publication: "bioRxiv"
year: 2026
external_url: https://www.semanticscholar.org/paper/b41f5fc12bbdfbc9cfaa23e124e581ac53100d7f
authors: "Hee So Kim, E. Lee, Malinda J. McPherson-McNato, Abigail Noyce, J. Feather"
publication_date: "2026-08-05"
---

Real-world acoustic inputs contain rich sensory information that we parse into discrete auditory objects and categories. Although deep neural networks (DNNs) are increasingly used to model auditory perception, the field lacks rigorous behavioral benchmarks, particularly for auditory event categorization. Here, we developed a 25-way categorization paradigm for broad classes of natural sounds to test whether categorical invariances of DNNs align with those of human observers. We first confirmed that humans could reliably categorize the natural sounds, demonstrating that our paradigm is well-suited for testing invariances in auditory categories. To probe model invariances, we evaluated human recognition of ‘model metamers’ (synthetic stimuli matched to the model’s internal activations for each natural stimulus) for a wide range of architectures trained on speech or auditory event recognition. Evaluating widely-used public models, we found that human recognition of auditory event model metamers was generally influenced by the training task and data distribution; speech models trained on standard, curated datasets produced less recognizable metamers than auditory event recognition models. We additionally analyzed a controlled set of models to directly investigate the influence of training task and adversarial training, revealing that improved metamer recognition induced by adversarial training is task-dependent. However, even in the best-performing models, we observed a sharp decline in human recognition at the final classification layer compared to the penultimate representation layer. Overall, our results suggest that while invariances in modern architectures better align with human observers for auditory event categorization, there is still a large discrepancy between the categorical invariances of auditory neural networks and the invariances of human observers. Code and models are available at https://github.com/Feather-Lab/env-sound-metamers
