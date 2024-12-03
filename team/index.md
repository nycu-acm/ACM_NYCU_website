---
title: Team
nav:
  order: 2
  tooltip: About our team
---

{% include section.html background="images/pages-title-background/team.jpg" dark=true %}
# {% include icon.html icon="fa-solid fa-users" %}Team
Our team consists of passionate scientists, postdocs, and students who work together to push the boundaries of Applied Computing and Multimedia. Each member contributes specialized knowledge and creativity, forming a collaborative group dedicated to scientific discovery and innovation.

{% include section.html %}

## Advisor

{% include list.html data="members" component="portrait" filters="role: prof" %}

## Co-Advisor

{% include list.html data="members" component="portrait" filters="role: co-ad" %}

## PhD students

{% include list.html data="members" component="portrait" filters="role: phd" %}

## Master students

{% include list.html data="members" component="portrait" filters="role: master" %}

## Former Members

{% include list.html data="members" component="portrait" filters="role: formerMem" %}

{% include section.html background="images/background.jpg" dark=true %}

<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. -->

{% include section.html %}

{% capture content %}

<!-- {% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %} -->

{% endcapture %}

{% include grid.html style="square" content=content %}
