---
layout: paper
id: "a20cec8b7db16b1b5d061ad2a01ce77aadcc1b20"
title: "Ontology-Based Target Sound Extraction"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/a20cec8b7db16b1b5d061ad2a01ce77aadcc1b20
authors: "Carlos Hernandez-Olivan, Marc Delcroix, Tsubasa Ochiai, Naohiro Tawara, Shoko Araki"
---

Target sound extraction (TSE) aims to isolate a sound source of interest from a mixture, given a semantic query. Existing TSE systems are conditioned on fixed class representations tied to individual sound categories, limiting their ability to handle the hierarchical relationships that naturally organize environmental sounds. In this paper, we introduce ontology-based TSE, a new task formulation in which a single model extracts sounds queried at any level of a sound ontology, from fine-grained leaf classes such as cat and dog to high-level categories such as animal. We propose a learnable class embedding table defined over all nodes of an AudioSet-derived ontology, regularized with a Cophenetic Correlation Coefficient (CPCC) loss that aligns embedding distances with shortest-path distances in the ontology tree. Our experiments across different approaches show the benefit of considering the ontology structure when training TSE systems.
