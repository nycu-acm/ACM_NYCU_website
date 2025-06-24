---
title: Natural Language Processing
---

{% include section.html background="images/research/nlp.jpg" dark=true %}
# {% include icon.html icon="fa-solid fa-wrench" %}Natural Language Process

{% include section.html %}

## Verilog Code Generation
__Goal:__ Focus on an 8-bit RISC architecture CPU using the Verilog hardware description language, based on a Finite State Machine (FSM).

__Challenges:__
* Generating Verilog code with LLMs requires deep domain knowledge of hardware architecture, circuit design, and low-level implementation constraints, which is difficult to capture with standard LLM training datasets.

* While LLMs can learn HDL syntax due to its similarity with software languages, they often struggle to generate functionally correct and high-quality hardware designs.

* Achieving reliable Verilog code generation typically demands additional domain-specific processing, fine-tuning, and tailored datasets beyond what is used for general code generation.


## Text-Image Watermarking
### Image Watermarking
__Goal:__
The primary goal of image watermarking is to embed information within digital images in a manner that ensures both copyright protection and traceability, without compromising image quality. In the context of generative models, this includes integrating watermarks directly into the image generation process to enable robust model ownership verification and resistance against a wide range of attacks.

__Challenges:__
Achieving a balance between robustness, imperceptibility, and adaptability remains a core challenge. Traditional methods often require complex synchronization or template mechanisms and may focus only on output images, limiting traceability to the model itself. Watermarking approaches must withstand diverse manipulations such as compression, rotation, and blurring while maintaining high visual fidelity. Furthermore, adapting watermarking techniques to different generative architectures and simplifying the encoding/decoding process, all while providing standardized benchmarks for evaluation, continue to be significant research hurdles.

### Text Watermarking
__Goal:__
To embed robust and imperceptible identifiers within textual content in order to preserve integrity, authenticate documents, and protect ownership—particularly in the context of modern applications involving large language models (LLMs).

__Challenges:__

Ensuring that watermarks remain both robust against attacks and inconspicuous to maintain readability and meaning.

Adapting watermarking techniques to evolving text generation scenarios introduced by LLMs, such as embedding watermarks during LLM-based text generation.

Addressing new risks and complexities brought by powerful LLMs, including watermark removal, unauthorized usage, and the need for algorithms that work reliably across diverse generative models and application settings.


## Time Series Forecasting
__Goal:__
To effectively leverage large language models (LLMs) for time series forecasting by developing approaches that can generalize across domains, adapt to diverse scenarios, and perform robustly without the need for extensive retraining or fine-tuning.

__Challenges:__
The application of LLMs to time series forecasting is controversial, as recent studies suggest that simpler architectures may offer similar or even better performance. Main challenges include aligning time series data with language model representations, handling non-stationarity and long forecasting horizons, ensuring adaptability to domain shifts, and achieving reliable performance with limited or zero additional training—all while maintaining computational efficiency.

## Meeting Minutes

__Goal:__
To create effective meeting recaps that document key decisions and discussions, support collaboration, and facilitate information sharing. Recaps help both newcomers and experts by aiding memory, onboarding, and deeper understanding of meeting topics.

__Challenges:__
The value and needs for meeting recaps vary based on organizational culture, meeting goals, participant roles, and expectations. There is no universal standard for a good recap; too much detail can cause information overload, while too little can omit important context. Non-linear meeting structures and back-channel communications further complicate the process of creating recaps that are both useful and manageable for all participants.