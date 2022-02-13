# TinyApp Project

TinyApp is a full stack web application built with Python and Django 4 that allows users to shorten long URLs (like bit.ly).

## Final Product

!["Create"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/create.png)
!["URL Listings"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/urls-page.png)
!["Register"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/register.png)
!["Login"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/login-page.png)
!["Edit URL"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/edit-url.png)
!["User List"](https://github.com/KrunchMuffin/TinyAppLighthouse/blob/master/docs/users-list.png)

## Dependencies

- crispy-forms
- asgiref==3.5.0
- bcrypt==3.2.0
- beautifulsoup4==4.10.0
- cffi==1.15.0
- Django==4.0.2
- django-bootstrap-v5==1.0.10
- django-crispy-forms==1.14.0
- django-environ==0.8.1
- psycopg2==2.9.3
- pycparser==2.21
- six==1.16.0
- soupsieve==2.3.1
- sqlparse==0.4.2

## Getting Started

- Set up a virtual environment
- Install all dependencies (using the pip install requirements.txt command).
- Set up a postgres or sqlite database. If a postgres database is being used, make sure to populate the secrets in a .env file
- Run the development web server using the `python manage.py runserver` command.
- Run the migrations using the `python manage.py migrate` command.
- Create a superuser to access the /admin page
