---
layout: paper
id: "5a4e89fddc9acef5c7191f188dcb896a4a50de79"
title: "Decoupling Conversational Dynamics In Full-Duplex Spoken Models Through Reinforcement Learning"
publication: ""
year: 2026
external_url: https://www.semanticscholar.org/paper/5a4e89fddc9acef5c7191f188dcb896a4a50de79
authors: "Yuxin Li, Donghang Wu, Guan-Ting Lin, Hung-yi Lee, Cheng-Wei Qin, Zhe-Huai Chen, Chen Chen"
---

Recent full-duplex spoken dialogue models have demonstrated compelling progress toward human-like interaction, enabling agents to respond with low latency, produce backchannels, and handle user barge-ins. Yet these improvements in conversational dynamics often come with weaker reasoning and instruction-following abilities, revealing a potential tension between interactive dynamics and intelligence capability. In this paper, we argue that such an intelligence--dynamics trade-off is not fundamental: conversational dynamics can instead be learned as a separate real-time decision policy from human dialogue data. To this end, we propose DuplexPO, a reinforcement learning (RL) framework that decouples when to speak from what to say. It preserves the semantic response capability of an instruction-tuned assistant, while optimizing its temporal interaction behavior over selected high-impact windows from long human conversations. To quantitatively optimize these dynamics, we formulate the Factorized Conversational Dynamics Reward (FCDR) to enable fine-grained temporal credit assignment for turn initiation, backchanneling, yielding, and regularized participation. The policy is then optimized with a GRPO-style objective. Experiments show that DuplexPO substantially improves full-duplex behaviors, including timely backchannels, smooth turn-taking, and barge-in handling, while maintaining strong reasoning and instruction-following performance. Moreover, improvements in dynamics-oriented metrics are reflected in better user experience, suggesting that optimizing conversational timing as a standalone objective can promote more natural full-duplex interaction.
