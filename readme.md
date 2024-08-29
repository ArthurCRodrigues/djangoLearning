## Migrations

A migration allows you to move databases from one design to another. This process is also reversible, so you can "migrate" databases back if needed.

## Django Project vs Django Application

- **Django Project**: A Django project is a collection of applications and configurations that, when combined together, will make up the full web application (your complete website running with Django).

- **Django Application**: A Django application is created to perform a particular functionality for your entire web application.
  - For example: You could have a registration app, a polling app, comments app, etc.
  - These Django apps can then be plugged into other Django projects, so you can reuse them!

### Creating a Simple Application

You can create a simple application with the following command:

\`\`\`bash
python manage.py startapp appname
\`\`\`

**IMPORTANT**: After creating your application, add your app's name to the \`INSTALLED_APPS\` list in \`settings.py\`.

## Mapping Views to URLs

After creating a view, you must map it to the \`urls.py\` file.

**Note**: Instead of using \`django.conf.urls\`, use \`django.urls\` (\`include\`, \`repath\`).

## Templates

Templates will contain the static parts of an HTML page (skeleton).

### Template Tags

Template tags have their own special syntax. This syntax allows you to inject dynamic content that your Django app's views will produce, affecting the final HTML.

To get started with templates, you first need to create a \`templates\` directory and then a subdirectory for each specific app's templates:

\`\`\`bash
first_project/templates
\`\`\`
