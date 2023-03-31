---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
layout: archive
redirect_from: 
  - /about
---

Education
======
* B.S. in Internet of Things, University of South China, 2016-2020


Work experience
======
* Jun. 2020 -: Research Assistant
  * Southern University of Science and Technology
  * Duties included: Assitant with the teching and study
  * Supervisor: Professor Jiang Liu
  
Publications
======
  <ul>{% for year in group_names %}
  {% assign posts = group_items[forloop.index0] %}
  <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
  {% for post in posts %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}
  </ul>
  
Projects
======
{% include projects.html %}

Academic Services
======
* Reviewer of CVPR 2023
* Reviewer of ECCV 2022
* Contributer of [MegCC](https://github.com/MegEngine/MegCC)
* Contributer of [MegEngine](https://github.com/MegEngine/MegEngine)
