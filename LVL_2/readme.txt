An essential part of any website is the ability to accept information from a user and input it into a database and
retrieve information from a database and use it to generate content for the user

We use MODELS to incorporate a database into a Django Project
Django comes equipped with SQLite
SQLite will work for our simple examples, but Django can connect to a variety of SQL engine backends!

In the settings.py file you can edit the ENGINE parameter used for DATABASES.
To create an actual model, we use a class structure inside of the relevant applications models.py file.

This class object will be a subclass of Django's built in class (inherit):
    django.db.models.model
Then each attribute of the class represents a field, which is just like a column name with constraints in SQL

WHAT A SQL DATABASE IS LIKE

SQL operates like a giant table, with each column representing a field, and each row representing an
entry

table
websiteID   WebSiteName URL
1           Google      www.google.com
2           Facebook    www.facebook.com

Each column has a type of field, such as a CharField, IntegerField, DateField, etc.
Each field can also have constraints

PRIMARY_KEY -> Unique identifier for each row in a table
FOREIGN_KEY -> Just denotes that the column coincides with a primary key of another table

 Example of the models class that would go into the models.py file of your application
 
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique = True)
class WebPage(models.Model):
    category = models.ForeignKey(topic)
    name = models.CharField(max_length = 264)
    url = models.URLField()
    def __str__(self):
        return self.name

After setting up the models, we can migrate the database
Basically let's Django do the heavy lifting of creating SQL databases that correspond to
the models we created, with a simple command:
    python manage.py migrate
Then register the changes to your app, shown here with some generic "app1":
    python manage.py makemigrations app1
In order to use the more convenient Admin interface with the models however, we need to register
them to our application's admin.py file
    from django.contrib import admin
    from app.models import Model1, Model2
        admin.site.register(Model1)
        admin.site.register(Model2)
Then with the models and database create, we can use Django's Admin Interface to interact with the database
In order to fully use the database and the Admin, we will need to create a "superuser"
    python manage.py createsuperuser
Once we ve set up the models, it's always a good idea to populate them with some test data using the Faker Library

