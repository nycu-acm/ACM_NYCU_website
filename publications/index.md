---
title: Publications
nav:
  order: 4
  tooltip: Published works
---

{% include section.html background="images/pages-title-background/publications.jpg" dark=true %}
# {% include icon.html icon="fa-solid fa-microscope" %}Publications

Our laboratory actively contributes to the scientific community through a range of peer-reviewed publications, showcasing our latest research advancements, and fostering innovation in Applied Computing and Multimedia.

{%
  include button.html
  type="link"
  text="International Conferences"
  link="publications/#international-conferences"
%}

{%
  include button.html
  type="link"
  text="International Journals"
  link="publications/#international-journals"
%}

{%
  include button.html
  type="link"
  text="Invention Patents"
  link="publications/#invention-patents"
%}

{% include section.html %}

## International Conferences

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" filters="type: conference" %}

{% include section.html %}

## International Journals

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" filters="type: journal" %}

## Invention Patents

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" filters="type: invention" %}
