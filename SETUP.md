Django
======

```sh
python3 -m django --version
```

> Pycharrm config - [https://medium.com/@srijan.pydev_21998/configure-pycharm-for-python-django-and-introduction-to-django-rest-framework-f9c1a7cb4ba0](https://medium.com/@srijan.pydev_21998/configure-pycharm-for-python-django-and-introduction-to-django-rest-framework-f9c1a7cb4ba0)

Principles
----------

* Productivity - With less code
* Good, clean code - [https://docs.djangoproject.com/en/dev/misc/design-philosophies/](https://docs.djangoproject.com/en/dev/misc/design-philosophies/)
* Fun
* Great Documentation - [https://www.djangoproject.com/](https://www.djangoproject.com/)

Model-Template-View Pattern
---------------------------

* Model - Represents your data, Maps model classes to database tables
* View [In MVC-Controller] - Takes HTTP request and returns a response, may call template and/or model
* Template [In MVC-View] - Generates HTML, Presentation Logic only

Create Virtual env -

```sh
python3 -m venv <env_name>
```

Activate Virtual Env

```sh
. django-env/bin/activate
```

for fish  :

```sh
django-env/bin/activate.fish
```

Leave Env

```sh
deactivate
```

Install django

```sh
pip install django
pip install django==<VERSION>
```

Creating a project

```sh
django-admin startproject gazelo
```

For this project - (post clone setup)  
Running the project

```sh
cd <project_name>
python manage.py runserver
```

Models and Migrations
---------------------

* Models -
  * Python classes mapped to database tables
  * Each object is a row in a table
* Migrations -
  * Python scripts
  * Keep db structure in sync with code
  * Auto-generated (but not always)

Django Apps
-----------

* Python package
* Contains models, views, templates, urls
* Most django projects contain several apps
* Apps can be reused between projects
* Better to keep apps small and simple should be clear, simple purpose
* Check migrations
  
```sh
python manage.py showmigrations
```

Run Migration

```sh
python manage.py migrate
```

Create app-

```sh
python manage.py startapp <app_name>
```

Create migrations

```sh
python manage.py makemigrations
```

creating actual SQL, MySQL, postgres scripts-
like for SQL -

```sh
 python manage.py sqlmigrate <app_name> <migration_name>
```

eg :

```sh
python manage.py sqlmigrate outset 0001
```

> To make sure this package is actually imported by Django, add your app to INSTALLED_APPS in setttings.py

* Django doesnot take null values by default for a field, so when we add new field to a table, we should provide a default value for migration
* Migrations are ordered, obviously
* Order is determined by dependencies

> Using manage.py in commands is preferred while working on django projects as it is coupled to our project and loads setttings.py among other things

Django ORM
----------

* Interacts from persistent data from Python (we think in classes and objects)
* Generates Database and SQL
* Backends supported - MySQL, Postgres, Oracle, SQLite

Model Fields
------------

* Class attributes are mapped to DB columns
* Should be instances of a Field class
  * Eg. IntegerField, CharField
* Field class determines
  * Database column type (INTEGER, VARCHAR)
  * How the field is rendered in a form

Migration Workflow
------------------

* Change the model code
* Generate MIgration Script (check it)
  
```sh
python manage.py makemigrations
```

* (Optional) Show migrations

```sh
python manage.py showmigrations
```

* (Optional) Show SQL for specific migrations
  
```sh
python manage.py sqlmigrate <appname> migration
```

* Run migrations

```sh
python manage.py migrate
```

1. Django Admin Site

   * Auto-generated UI to edit our data
   * Registering models with admin site
   * Creating a super user
   * Very customizable
  
2. Model API

   * Work with data from Python
   * Query data
   * Save/Update/Delete
   * Relations (foreign keys)

Admin Interface
---------------

To enable a User interface for our models, we need to register them with admin interface.

In your app go to admin.py -

```sh
from django.contrib import admin
from .models import User, Video, View, Like, Comment, Following
admin.site.register(User)
admin.site.register(Video)
admin.site.register(View)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)
```

* Now if you run your server and go to /admin  you need to login
* You need to create a super user
* go to terminal
  
```sh
python manage.py createsuperuser
```

Model API
---------

```sh
python manage.py shell
```

```sh
>>> from outset.models import User,Video
>>> Video.objects
<django.db.models.manager.Manager object at 0x10b78b850>
>>> Video.objects.all()
<QuerySet [<Video: Spring vacation>, <Video: marvel superheros review>, <Video: Cute dogs>]>
>>> Video.objects.count()
3
<QuerySet [<Video: Cute dogs>]>
>>> Video.objects.exclude(name="Cute dogs")
<QuerySet [<Video: Spring vacation>, <Video: marvel superheros review>]>
```

For foreign keys - two params req

```sh
>>> Video.objects.filter(user__user_name="Ryan")
<QuerySet [<Video: marvel superheros review>, <Video: Cute dogs>]>
```

 Updating a record

```sh
>>> v = Video.objects.get(id=1)
>>> v.name
'Spring vacation'
>>> v.name = "My spring vacation"
>>> v.name
'My spring vacation'
>>> v.save()
```

Create a record

```sh
>>> u = User.objects.get(id=1)
>>> v = Video(name="yoga today", user=u, size=23, views_count=0, likes_count=0, comments_count=0)
>>> v.save()
```

> Django runs the queries in lazy way

* Manager Object
  * For each model class, there's a manager object which allows us to create queries and execute them

Templates and Static Content
----------------------------------------

* it is best practice to keep all template files under a separate folder(your app name maybe) inside templates folder to avoid name clashes.

Passing data from View to Template
----------------------------------

* it is responsibility of view to collect the data that needs to be shown to the user and pass it to template
* its better to leave to the responsibility of dealing with the database to model, than doing it in views

OneToOneField (One to One relationship) - [https://docs.djangoproject.com/en/3.0/topics/db/examples/one_to_one/](https://docs.djangoproject.com/en/3.0/topics/db/examples/one_to_one/)

Passing Data to a Template

* pass data as a dictionary as third argument to render()
* Data will be available in template context
* Context contains other data too like logged in user
  
```sh
return render(request, "video_stream/home.html",
       {'nvideos': Video.objects.count(), 'my_videos': user_videos, 'all_videos': all_videos})
```

[https://dillinger.io/](https://dillinger.io/)
