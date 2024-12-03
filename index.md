---
title: Home
nav:
  order: 1
  tooltip: Homepage
---

{% include section.html background="images/background.jpg" dark=true %}

{% include img-slideshow.html %}

{% include section.html %}
# ACM Lab - National Yang Ming Chiao Tung University

Our lab works on a wide range of projects in computer vision and multimedia. Currently, we employ advanced machine learning techniques such as deep learning to develop our systems.

Some of our applications include museum guidance, autonomous vehicle, parking lot management system ... Most of them are confirmed and supported by industry. Through the process of completing the projects, the student will be equipped the self-studying ability as well as the teamwork skill to adapt to an ever-changing world.

Besides, we also try to build an international environment in our lab, you may find that our lab members come from many countries such as Taiwan, Vietnam and Indonesia. Therefore, working in our lab, you also can experience different cultures.

{%
  include button.html
  tooltip="GitHub"
  text="GitHub"
  icon="fa-brands fa-github"
  link="https://github.com/nycu-acm"
%}
{%
  include button.html
  tooltip="Our fanpage"
  text="Fanpage"
  icon="fa-brands fa-facebook"
  link="https://www.facebook.com/profile.php?id=100057112133591"
%}

<!--- START HIGHLIGHT -->

{% include section.html %}

## Highlights

<!--- Highlight 1 -->

### We are at ICIP 2024!
Professor and our lab members attend ICIP 2024 with three works: 
* Lipface: Lipschitz-Conditioned for Resolution Robus Face Recognition
* Aerial view river landform video segmentation: A weakly supervised context-aware temporal consistency distillation approach
* Two Heads Better than One: Dual Degradation Representation for Blind Super-Resolution

{% capture col1 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ICIP_1.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% capture col2 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ICIP_2.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% capture col3 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ICIP_3.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

<!--- Highlight 2 -->

{% include section.html %}

### We are at ACM Multimedia 2024!
Our lab members attend ACM Multimedia 2024 with the work "TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views".

{% capture col1 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ACM_MULTIMEDIA_1.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% capture col2 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ACM_MULTIMEDIA_2.jpg"
  caption=""
  link="team"
%}
{% endcapture %}


{% include cols.html col1=col1 col2=col2}

### ECCV 2024, here we come!
Our lab members with the work "DetailSemNet: Elevating Signature Verification with Captured Details and Semantics by Feature Disentanglement and Re-entanglement".

{% capture col1 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ECCV_1.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% capture col2 %}
{%
  include figure.html
  image="images/homepage-highlight/2024_ECCV_2.jpg"
  caption=""
  link="team"
%}
{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

<!--- END HIGHLIGHT -->

<!--- START 'ABOUT US' -->

{% include section.html %}

## About us

<!--- Part "Our research" -->

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
%}

{% endcapture %}

{%
  include feature.html
  image="images/research/image_processing.jpg"
  link="research"
  title="Our Research"
  text=text
%}

<!--- Part "Browse our projects" --> 

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="publications"
  text="Browse our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
%}

{% endcapture %}

{%
  include feature.html
  image="images/international-journals/01-indirect.webp"
  link="publications"
  title="Our Publications"
  style="bare"
  text=text
%}

<!--- Part "Meet our team" --> 

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
%}

{% endcapture %}

{%
  include feature.html
  image="images/pages-title-background/team.jpg"
  link="team"
  title="Our Team"
  text=text
%}
