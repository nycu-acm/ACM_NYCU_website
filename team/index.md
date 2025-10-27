---
title: Team
nav:
  order: 2
  tooltip: About our members
---

{% include section.html background="images/pages-title-background/team.jpg" dark=true %}
# {% include icon.html icon="fa-solid fa-users" %}Team
Our team consists of passionate scientists, postdocs, and students who work together to push the boundaries of Applied Computing and Multimedia. Each member contributes specialized knowledge and creativity, forming a collaborative group dedicated to scientific discovery and innovation.

{% include section.html %}

## Advisor

{% include list.html data="members" component="portrait" filters="role: prof" %}

## Co-Advisors

{% include list.html data="members" component="portrait" filters="role: co-ad" %}

## PhD students

{% include list.html data="members" component="portrait" filters="role: current-phd, enteryear: 2023" %}
{% include list.html data="members" component="portrait" filters="role: current-phd, enteryear: 2024" %}

## Master students

{% include list.html data="members" component="portrait" filters="role: current-master, enteryear: 2023" %}
{% include list.html data="members" component="portrait" filters="role: current-master, enteryear: 2024" %}
{% include list.html data="members" component="portrait" filters="role: current-master, enteryear: 2025" %}

## Undergraduate members

{% include list.html data="members" component="portrait" filters="role: current-undergrad, enteryear: 2025" %}

## Interns
{% include list.html data="members" component="portrait" filters="role: current-intern, enteryear: 2025" %}

## Former Master students

{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2011" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2012" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2013" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2014" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2015" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2016" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2017" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2018" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2019" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2020" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2021" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2022" %}
{% include list.html data="members" component="portrait" filters="role: alumni-master, enteryear: 2023" %}

## Former Undergraduate students

{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2008" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2009" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2010" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2011" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2012" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2013" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2014" %}
{% include list.html data="members" component="portrait" filters="role: alumni-undergraduate, enteryear: 2015" %}

## Former Visiting Members

{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2006" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2007" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2008" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2009" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2010" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2011" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2012" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2013" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2014" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2015" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2016" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2017" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2018" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2019" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2020" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2021" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2022" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2023" %}
{% include list.html data="members" component="portrait" filters="role: formerMem, enteryear: 2024" %}

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
