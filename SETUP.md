Django Project Setup
====================

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

Verify
```sh
python -m django --version
```

Creating a project(Not required if cloned)

```sh
django-admin startproject gazelo
```

For this project - (post clone setup)  

```shell script
python manage.py migrate
```

Now, you need to create a super user
  
```sh
python manage.py createsuperuser
```

Running the project

```sh
cd <project_name>
python manage.py runserver
```

> Pycharrm config - [https://medium.com/@srijan.pydev_21998/configure-pycharm-for-python-django-and-introduction-to-django-rest-framework-f9c1a7cb4ba0](https://medium.com/@srijan.pydev_21998/configure-pycharm-for-python-django-and-introduction-to-django-rest-framework-f9c1a7cb4ba0)


