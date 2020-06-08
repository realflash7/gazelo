Django
------
------
```sh
$ python3 -m django --version
```
> Pycharrm config - https://medium.com/@srijan.pydev_21998/configure-pycharm-for-python-django-and-introduction-to-django-rest-framework-f9c1a7cb4ba0

Principles
-----------
* Productivity - With less code
* Good, clean code - https://docs.djangoproject.com/en/dev/misc/design-philosophies/
* Fun
* Great Documentation - https://www.djangoproject.com/


Model-Template-View Pattern
---------------------------
* Model - Represents your data, Maps model classes to database tables
* View [In MVC-Controller] - Takes HTTP request and returns a response, may call template and/or model
* Template [In MVC-View] - Generates HTML, Presentation Logic only



Create Virtual env - 
```sh
$ python3 -m venv <env_name>
```

Activate Virtual Env
```sh
$ . django-env/bin/activate
```
for fish  :
```sh
$ django-env/bin/activate.fish
```
Leave Env
```sh
	$ deactivate
```

Install django 
```sh
	$ pip install django
	$ pip install django==<VERSION>
```



Creating a project
```sh
$ django-admin startproject gazelo
```

For this project - (post clone setup)  
Running the project
```sh
$ cd <project_name>
$ python manage.py runsserver
```



Models and Migrations
----------------------
* Models - 
  * Python classes mapped to database tables
  * Each object is a row in a table
* Migrations -
  * Python scripts
  * Keep db structure in sync with code
  * Auto-generated (but not always)

Django Apps
------------
* Python package
* Contains models, views, templates, urls
* Most django projects contain several apps
* Apps can be reused between projects
* Better to keep apps small and simple
should be clear, simple purpose
* Check migrations
```sh
$ python manage.py showmigrations
```
Run Migration
```sh
$ python manage.py migrate
```
Create app- 
```sh
$ python manage.py startapp <app_name>
```
Create migrations
```sh
$ python manage.py makemigrations
```
creating actual SQL, MySQL, postgres scripts-
like for SQL - 
```sh
$ python manage.py sqlmigrate <app_name> <migration_name> 
```
eg : 
```sh
$ python manage.py sqlmigrate outset 0001
```

> To make sure this package is actually imported by Django, add your app to INSTALLED_APPS in setttings.py

* Django doesnot take null values by default for a field, so when we add new field to a table, we should provide a default value for migration
* Migrations are ordered, obviously
* Order is determined by dependencies

> Using manage.py in commands is preferred while working on django projects as it is coupled to our project and loads setttings.py among other things

Django ORM
------------
* Interacts from persistent data from Python (we think in classes and objects)
* Generates Database and SQL
* Backends supported - MySQL, Postgres, Oracle, SQLite

Model Fields
--------------
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
$ python manage.py makemigrations
```
* (Optional) Show migrations
```sh
$ python manage.py showmigrations
```
* (Optional) Show SQL for specific migrations
```sh
$ python manage.py sqlmigrate <appname> migration
```
* Run migrations
```sh
$ pyhton manage.py migrate
```
---- https://dillinger.io/

