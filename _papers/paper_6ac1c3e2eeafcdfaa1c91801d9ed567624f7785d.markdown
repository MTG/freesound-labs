---
layout: paper
id: "6ac1c3e2eeafcdfaa1c91801d9ed567624f7785d"
title: "Remixit: Continual Self-Training Of Speech Enhancement Models Via Bootstrapped Remixing"
publication: "IEEE Journal of Selected Topics in Signal Processing"
year: 2022
external_url: https://www.semanticscholar.org/paper/6ac1c3e2eeafcdfaa1c91801d9ed567624f7785d
authors: "Efthymios Tzinis, Yossi Adi, V. Ithapu, Buye Xu, P. Smaragdis, Anurag Kumar"
publication_date: "2022-02-17"
---

We present RemixIT, a simple yet effective self-supervised method for training speech enhancement without the need of a single isolated in-domain speech nor a noise waveform. Our approach overcomes limitations of previous methods which make them dependent on clean in-domain target signals and thus, sensitive to any domain mismatch between train and test samples. RemixIT is based on a continuous self-training scheme in which a pre-trained teacher model on out-of-domain data infers estimated pseudo-target signals for in-domain mixtures. Then, by permuting the estimated clean and noise signals and remixing them together, we generate a new set of bootstrapped mixtures and corresponding pseudo-targets which are used to train the student network. Vice-versa, the teacher periodically refines its estimates using the updated parameters of the latest student models. Experimental results on multiple speech enhancement datasets and tasks not only show the superiority of our method over prior approaches but also showcase that RemixIT can be combined with any separation model as well as be applied towards any semi-supervised and unsupervised domain adaptation task. Our analysis, paired with empirical evidence, sheds light on the inside functioning of our self-training scheme wherein the student model keeps obtaining better performance while observing severely degraded pseudo-targets.
