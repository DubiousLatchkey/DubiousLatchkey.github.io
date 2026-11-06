---
description: Software projects by Matthew Chen, including hackathon winners, network auditing, Minecraft automation, and creative experiments.
image:
  path: /assets/images/social/portfolio.jpg
  width: 1200
  height: 630
  alt: Screenshot of Matthew Chen's project portfolio
title: Projects
icon: fas fa-code
order: 1
---

<div class="project-grid">
  {% assign projects = site.projects | sort: "title" %}
  {% for project in projects %}
    <article class="project-card">
      <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
      <div class="project-excerpt">
        {{ project.excerpt }}
      </div>
      <a class="project-link" href="{{ project.url | relative_url }}">View project</a>
    </article>
  {% endfor %}
</div>
