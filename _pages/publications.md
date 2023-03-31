---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- {% for post in site.publications reversed %}
  {% assign year=}
  {% include archive-single.html %}
{% endfor %} -->


{{ assign pubs = site.publications | group_by:"year" | reverse }}
{% for pub in pubs %}
  {% assign posts = pub.items %}
  <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ pub.name }}</h2>
  <ul>
  {% for post in posts %}
    <li>{{ post.citition }}</li>
  {% endfor %}
  </ul>
{% endfor %}