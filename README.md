## Installation

This is developed for Python 3 and Django 4.2.

It is recommended that you setup a `pipenv` before development. Then install dependencies, migrate, and runserver to get started:

```bash
❯ pip install pipenv
❯ pipenv install django shell
❯ python3 manage.py migrate
❯ python3 manage.py createsuperuser
❯ python3 manage.py runserver
```

You can now visit your site at http://localhost:8000/.

Admin interface is available at http://localhost:8000/admin/. 
Use the superuser created in step three of the commands above.

## TODO
```commandline
❯ django-admin startapp guests
❯ django-admin startapp rsvp
```