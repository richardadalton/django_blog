# Stack - The Django Blog Project

## Overview
Stack is a multiuser django blog project. The purpose of the project is to demonstrate django features in the context of a full application.

## Implementation
The project currently uses Django 5.  It consists of an 'accounts' app that deals with User Registration, Sign-On, Password Reset, etc.
There is also a 'blog' project that deals with writing and publishing blog posts.

## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/django_blog.git
```

Create the virtual environment, and install dependencies.

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```

Run migrations to create local sqlite database.

```bash
$ python manage.py migrate --settings=django_blog.settings.dev
```

