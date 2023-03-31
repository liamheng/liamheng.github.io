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
{% capture year %}'None'{% endcapture %}
{% for post in site.publications reversed %}
  <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ post.year }}</h2>
  {% include archive-single.html %}
{% endfor %}

