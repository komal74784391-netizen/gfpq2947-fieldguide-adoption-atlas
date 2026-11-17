---
title: Reading curriculum
layout: default
permalink: /curriculum/
---

# Reading curriculum

We read one adopted upstream project per quarter.

{% for tool in site.data.adopted_tools %}
- **{{ tool.name }}** — {{ tool.note }}
{% endfor %}
