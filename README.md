Django Image Upload
================================

Setup
-----

### Installation

This project is a very minimal Python setup. You are free to set 
it up locally in your own way (`virtualenv`, `venv`, `pyenv`, `poetry`, 
Docker, etc.). 

### Database setup

Setup your initial database (SQLite).
    
    $ ./manage.py migrate
    
Create your first superuser.

    $ ./manage.py createsuperuser
    
Load initial seed data.

    $ ./manage.py loaddata images
    
### S3 Config

Define S3 Bucket Details and Credentials as environment variables;

```
AWS_DEFAULT_REGION = os.environ['AWS_DEFAULT_REGION']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
```

Development
-----------

### Running the server

    $ ./manage.py runserver


MySQL DB
--------

- Install requirements in `requirements_mysql.txt`
- Set `DJANGO_SETTINGS_MODULE=imagedb.settings.mysql`


Unit Testing
------------

- Install requirements in `requirements_unit_test.txt`. This installs a library to overrides storage to Memory implementation
- Set `DJANGO_SETTINGS_MODULE=imagedb.settings.unit_test` to ensure SQLLite DB is used.


Project Information
-------------------

This is a Django example project (`imagedb`) that includes one Django 
app called `images`.

The `images` app uses two models, `Image` and `ImageLabel`.

* `Image` - refers to an image that you can upload/download.
* `ImageLabel` - refers to a label of an object inside the image.

An `Image` can have multiple `ImageLabel`s. An `ImageLabel` belongs to 
only one `Image`.

A basic Django admin page is available at http://localhost:8000/admin. 
