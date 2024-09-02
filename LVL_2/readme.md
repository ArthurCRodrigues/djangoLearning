## Incorporating a Database into a Django Project

An essential part of any website is the ability to accept information from a user, input it into a database, and retrieve information from a database to generate content for the user.

### Using Models in Django

To incorporate a database into a Django project, we use **models**. Django comes equipped with **SQLite**, which is suitable for simple examples, but it can also connect to a variety of SQL engine backends.

### Configuring the Database Engine

In the `settings.py` file, you can edit the `ENGINE` parameter used for `DATABASES` to specify the SQL engine.

### Creating a Model

To create an actual model, we use a class structure inside the relevant application's `models.py` file. This class object will be a subclass of Django's built-in class (`django.db.models.Model`), allowing us to define fields and constraints.

#### Example of a Model Class

```python
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True) 

class WebPage(models.Model):
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    url = models.URLField()

    def __str__(self):
        return self.name
```
``unique = True`` denotes a primary key

### SQL Database Overview

SQL operates like a giant table:

- Each column represents a field, such as a `CharField`, `IntegerField`, `DateField`, etc.
- Each row represents an entry in the table.
- Fields can also have constraints like `PRIMARY_KEY` (unique identifier for each row) and `FOREIGN_KEY` (denotes a relationship to a primary key in another table).

#### Example SQL Table

| websiteID | WebSiteName | URL                |
|-----------|-------------|--------------------|
| 1         | Google      | www.google.com     |
| 2         | Facebook    | www.facebook.com   |

### Migrating the Database

After setting up the models, we can migrate the database, allowing Django to handle the creation of the SQL databases corresponding to the models we created with a simple command:

```bash
python manage.py migrate
```

### Registering Changes to Your App

To register the changes to your app, shown here with some generic `app1`:

```bash
python manage.py makemigrations app1
```

### Using the Admin Interface

To use the more convenient Admin interface with the models, you need to register them in your application's `admin.py` file:

```python
from django.contrib import admin
from app.models import Model1, Model2

admin.site.register(Model1)
admin.site.register(Model2)
```

### Creating a Superuser

With the models and database created, you can use Django's Admin Interface to interact with the database. In order to fully use the database and the Admin, you will need to create a "superuser":

```bash
python manage.py createsuperuser
```
You will have to provide a name, email and password, make sure to remember them.

### Populating the Database with Test Data

Once you've set up the models, it's always a good idea to populate them with some test data using the Faker Library.
It is usually a good idea to create a script that will populate your models with some "dummy" data.

```bash
pip install Faker
```

