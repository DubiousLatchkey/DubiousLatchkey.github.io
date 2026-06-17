---
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
