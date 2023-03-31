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
* PhD  in , The University of Tokyo, 2013/04-2016.03
* M.S. in Department of Computer, Northeast Normal University, 2008/09-2011/07
* B.S. in Department of Computer, Northeast Normal University, 2004/09-2008/07


Work experience
======
* Jun. 2020 -: Research Assistant
  * Southern University of Science and Technology
  * Duties included: Assitant with the teching and study
  * Supervisor: Professor Jiang Liu
  
Publications(recent three years)
======
  {% assign pubs = site.publications | where_exp: "item", "item.year > 2020" | group_by: "year" | reverse %}
{% for pub in pubs %}
  {% assign posts = pub.items %}
  <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ pub.name }}</h2>
  <ul>
  {% for post in posts %}
    <li>{{ post.citation }}</li>
  {% endfor %}
  </ul>
{% endfor %}
  
Projects
======
{% include projects.html %}

Academic Services
======
* Reviewer of CVPR 2023
* Reviewer of ECCV 2022
* Contributer of [MegCC](https://github.com/MegEngine/MegCC)
* Contributer of [MegEngine](https://github.com/MegEngine/MegEngine)
