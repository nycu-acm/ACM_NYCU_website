---
title: Join us
nav:
  order: 7
  tooltip: Our contact information
---

{% include section.html background="images/pages-title-background/joinus.jpg" dark=true %}
# {% include icon.html icon="fa-regular fa-envelope" %}Join us

Become a part of our collaborative and forward-thinking research community. At our lab, we are dedicated to pushing the boundaries of science and discovery. 

{%
  include button.html
  type="email"
  text="chingchun@cs.nycu.edu.tw"
  link="chingchun@cs.nycu.edu.tw"
%}

{%
  include button.html
  type="phone"
  text="+886-3-5712121#54769"
  link="+886-3-5712121#54769"
%}

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  text="EC129, Engineering Building 3, NYCU Guangfu Campus"
  link="https://maps.app.goo.gl/GwHsfWVduyaE4DCMA"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/pages-title-background/team.jpg"
  caption=""
  link="team"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/pages-title-background/publications.jpg"
  caption=""
  link="team"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html %}
## More info
* [NYCU Admission for International Students](https://oia.nycu.edu.tw/oia/en/app/folder/781)
* [Taiwan Experience Education Program (TEEP)]https://teep.studyintaiwan.org/program/273

{% include section.html dark=true %}
## Life at ACM Lab
{% include list.html data="posts" component="post-excerpt" filters="tags: internal-activity" %}

