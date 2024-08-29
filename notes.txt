Migrations:
A migration allows you to move databases from one design to another, this is also reversible
So you can "migrate" databases

Django Project != Django Application:
    A django project is a collection of applications and configurations that when combined
together will make up the full web application ( your complete website running with Django)
    A Django Application is created to perform a particular functionality for your entire web application.
        For example: You could have a registration app, a polling app, comments app, etc.
    These Django Apps can then be plugged into other Django Projects, sou you can reuse them!
Create a simple application with:
    python manage.py startapp appname
IMPORTANT: After creating your application, add your app's name to settings.py INSTALLED_APPS list

After creating a view, you must map it to the urls.py file

INSTEAD OF USING django.conf.urls, use django.urls (include,repath)

TEMPLATES
will contain the static parts of an HTML page (skeleton)
template tags -> Have their own special Syntax
Syntax allows you to inject dynamic content that your Django App's views will produce, effecting the final HTML
To get started with templates, you first need to create a "templates" directory and then a subdirectory
for each specific app's templates
   first_project/templates/first_app
Now, let Django know of the templates by editing the DIR key inside of the TEMPLATES dictionary in settings.py
We can now create an HTML file called index.html inside of the templates/first_app directory
Inside this HTML we will insert template tag (a.k.a Django Template Variable)
these template variables will allow us to inject content into the HTML directly from Django
In order to achieve this, we will use the render() function and place int our original index() function in view.py









