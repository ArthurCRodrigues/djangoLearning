<h1 align="center">Django Notes 👋</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Django-3.2-green" alt="Django Version" />
  <img src="https://img.shields.io/badge/Python-3.8-blue" alt="Python Version" />
  <a href="https://docs.djangoproject.com/en/3.2/">
    <img alt="Documentation" src="https://img.shields.io/badge/docs-Django-green" target="_blank" />
  </a>
  <a href="https://github.com/django/django/blob/main/LICENSE">
    <img alt="License: BSD" src="https://img.shields.io/badge/license-BSD-yellow.svg" target="_blank" />
  </a>
</p>

> A quick reference guide for key concepts in Django, including migrations, projects vs. applications, views, URLs, and templates.

## ✨ Migrations

**Migrations** are used to modify your database schema over time. They allow you to:

- **Move databases** from one design to another.
- **Revert** to previous states, making database changes reversible.

## 🔧 Django Project vs. Django Application

### Django Project
- A **Django Project** is a collection of applications and configurations that, when combined, create a full web application.
- Your complete website running on Django is essentially a project.

### Django Application
- A **Django Application** is created to perform a specific functionality within your web application.
- Examples include:
  - Registration App
  - Polling App
  - Comments App
- **Reusability**: These apps can be reused across different Django Projects.

**To create a new Django Application:**
```sh
python manage.py startapp appname
