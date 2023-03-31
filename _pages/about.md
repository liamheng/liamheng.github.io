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
* PhD  in Beijing Institute of Technology, 2012/09-2018/07
* Visiting PhD. in MD Anderson Cancer Center, 2016/10-2017/09
* B.S. in Zhengzhou University, 2008/09-2012/07


Work experience
======
* 2018/07-2020/06: Postdoctoral Fellow
  * Beijing Institute of Technology
  * Duties included: Intelligent diagnosis and treatment algorithm and Surgical robot development
  * Supervisor: Professor Yongtian Wang

* 2020/07-: Associate Researcher
  * Southern University of Science and Technology
  * Duties included: Trustworthy intelligent healthcare
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
* Reviewer of TMI, CMPB, PMB, SREP
* Reviewer of MICCAI 2023
* Reviewer of OMIA 2022
* Reviewer of BMVC 2021

