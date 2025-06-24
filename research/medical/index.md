---
title: Medical Imaging
---

{% include section.html background="images/research/medical.jpg" dark=true %}
# {% include icon.html icon="fa-solid fa-wrench" %}Medical Imaging

{% include section.html %}

## ITRI: Finetuning and Enhancement using Latent Diffusion for medical image

Goal: Fine-tune a pretrained diffusion model on a new medical domain (different organ) and use the adapted model for image enhancement.

Motivation: Medical imaging data for certain organs is often limited. To address this, we propose leveraging the prior knowledge embedded in pretrained diffusion models from other organs. By fine-tuning on the target organ, the model can better generalize, enabling effective image enhancement and synthetic data generation in data-scarce settings.

## Style transfer using transformer-based for ultrasound medical image

Goal: Improve ultrasound image translation to enhance downstream task performance across devices.

Motivation: Different ultrasound devices produce varying styles, which hinder model generalization. Existing UI2I methods overlook task-relevant style filtering, leading to suboptimal results. Our proposed approach addresses this by preserving content and selectively transferring useful style features.

## Document QA dataset generation
