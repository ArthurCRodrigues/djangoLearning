
## Migrations

A migration allows you to move databases from one design to another. This process is also reversible, so you can "migrate" databases back if needed.

## Django Project vs Django Application

- **Django Project**: A Django project is a collection of applications and configurations that, when combined together, will make up the full web application (your complete website running with Django).

- **Django Application**: A Django application is created to perform a particular functionality for your entire web application.
  - For example: You could have a registration app, a polling app, comments app, etc.
  - These Django apps can then be plugged into other Django projects, so you can reuse them!

### Creating a Simple Application

You can create a simple application with the following command:

```bash
python manage.py startapp appname
```
> ### Files and their purpose
> When creating your first Django project, you may find yourself with a bunch of unknown files and folder and get yourself asking what they're for. Here's what
> all the files are made for: 
> - `__init__.py`<br>
> Blank Python script that due to its special name let's python know that this
> directory can be treated as a package

> - `admin.py` <br>
> Register your models which Django will then use with Django's admin interfaced

> - `app.py` <br>
> place application specific configuration

> - `models.py` <br>
> Store the application's data models
> specify entities and relationships between the data

> - `tests.py` <br>
> add a series of functions to test application's code

> - `views.py` <br>
> Function that handle requests and return responses

> **migrations folder**
> stores database specific information as it relates to the models






**IMPORTANT**: After creating your application, add your app's name to the \`INSTALLED_APPS\` list in \`settings.py\`.
## Django Views
Django views are python functions that take HTTP requests and return HTTP response, like HTML documents.
A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called `views.py` located on your app's folder.
Here's a basic view called index: 
```python
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!)

```

## Mapping Views to URLs

After creating a view, you must map it to the `urls.py` file.

**Note**: Instead of using `django.conf.urls`, use `django.urls` (`include`, `repath`).

## Templates

Templates will contain the static parts of an HTML page (skeleton). By combining views to templates, you're able to generate dynamic HTML content after API calls. You can do this by using template tags.

### Template Tags

Template tags have their own special syntax. This syntax allows you to inject dynamic content that your Django app's views will produce, affecting the final HTML.

To get started with templates, you first need to create a \`templates\` directory and then a subdirectory for each specific app's templates:

```bash
first_project/templates
```

## Serving Static Media Files in Django

To serve static and media files in a Django application, follow these steps:

### 1. Define the Static and Media URL and Root in `settings.py`

In your `settings.py`, add the following lines:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 2. Create Static and Media Directories

In your project directory, create the following directories:

```bash
mkdir static
mkdir media
```

### 3. Use `static` Template Tag in Your HTML Files

In your templates, use the \`{% static %}\` tag to link to static files:

```html
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### 4. Configure `urls.py` to Serve Media Files in Development

In your project's `urls.py` file, add the following lines to serve media files during development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your URL patterns here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 5. Collect Static Files (Optional)

If you're deploying your Django application, you may need to collect all static files into a single directory. Use the following command:

```bash
python manage.py collectstatic
```

This will gather all static files from your apps into the directory specified in `STATIC_ROOT`.

### 6. Access Media Files in Your Views

In your views, you can handle media files by using the \`MEDIA_URL\` as a prefix for file paths.

```python
from django.conf import settings

def my_view(request):
    image_url = settings.MEDIA_URL + 'images/myimage.jpg'
    return render(request, 'my_template.html', {'image_url': image_url})
```
