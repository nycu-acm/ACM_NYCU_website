---
title: Home
nav:
  order: 1
  tooltip: Homepage
---

{% include section.html %}

{% capture lorem %}
ACM 2025 Recruitment for Internship / Master / Ph.D. program / Full-time researcher is open! [Join us](join-us)
{% endcapture %}
{% capture content %}**Announcement:** {{ lorem }}{% endcapture %}
{% include alert.html type="info" content=content %}

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

## Latest News
{% include list_show_only_five.html data="posts" component="post-excerpt" style="small" %}

{%
  include button.html
  link="news"
  text="Watch more news"
  icon="fa-solid fa-newspaper"
%}

<!--- END HIGHLIGHT -->

<!--- START 'ABOUT US' -->

{% include section.html %}

## About us

<!--- Part "Our research" -->

{% capture text %}

<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. -->

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

<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. -->

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

<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. -->

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
