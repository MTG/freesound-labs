---
layout: paper
id: "0cad4b3f8581cf5c31580ca0d67ce9b90e0afbec"
title: "Towards An Ultra-Low-Delay Neural Audio Coding With Computational Efficiency"
publication: "Interspeech"
year: 2025
external_url: https://www.semanticscholar.org/paper/0cad4b3f8581cf5c31580ca0d67ce9b90e0afbec
authors: "Byeong Hyeon Kim, Hyungseob Lim, Inseon Jang, Hong-Goo Kang"
publication_date: "2025-08-17"
---

Recent studies on neural audio codecs (NACs) have primarily focused on improving audio quality in extremely low bit-rate scenarios. However, they have not thoroughly explored the impact of latency. In this work, we first demonstrate that NACs can achieve high-quality reconstruction with an algorithmic delay below 1 ms, albeit at substantial computational costs. To address this challenge, we propose DualStream, a novel framework designed to significantly reduce computational costs in ultra-low-delay settings. DualStream integrates a lightweight encoding module with a small down-sampling ratio to maintain low algorithmic delay, combined with a larger module with a higher down-sampling ratio that processes time-delayed inputs to improve efficiency without introducing additional delay. Experimental results demonstrate that DualStream, with an algorithmic delay of 0.7 ms, achieves comparable performance to conventional NACs while reducing computational costs by approximately 40%.
