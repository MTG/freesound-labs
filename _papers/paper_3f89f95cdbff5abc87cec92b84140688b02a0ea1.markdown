---
layout: paper
id: "3f89f95cdbff5abc87cec92b84140688b02a0ea1"
title: "Decay-Region Group Delay As A Forensic Cue For Ai-Generated Impulsive Sounds"
publication: "arXiv.org"
year: 2026
external_url: https://www.semanticscholar.org/paper/3f89f95cdbff5abc87cec92b84140688b02a0ea1
authors: "JaeHyeong Chang, Cheng-Zhe Sun, Siwei Lyu"
---

We investigate whether AI-generated impulsive sounds can be distinguished from real ones through group delay analysis. Our central finding is that AI-generated impulsive sounds show near-identical onset-region group-delay distributions but exhibit measurably different group-delay behavior in the late decay region: decay-region KL divergence reaches $0.322$ compared to near-zero onset divergence ($0.022$). Cross-band GD variability achieves single-feature AUC~=~0.720, and a Random Forest (RF) over nine decay-region features reaches AUC~$=$~0.884 under sample-disjoint evaluation. A group delay map used as a standalone 2D input to CNN classifiers achieves 90--94\% accuracy, demonstrating that group delay carries substantial discriminative information. Under generator hold-out, CNN and transformer classifiers show highly variable AUC (0.457--0.918). The group delay RF achieves the highest average hold-out accuracy among the evaluated methods ($66.7\%$) and avoids extreme below-random collapse, although its average AUC (0.731) is lower than CNN avg (0.762) and AST (0.772). Parameter sensitivity analysis across 27 STFT configurations confirms that the RF AUC remains stable (0.700--0.847, std~=~0.035). These results suggest that decay-region group delay can serve as a physically interpretable forensic cue that complements magnitude-based classifiers, while broader validation remains necessary.
