"""
INCLUDE() FUNCTION allows us to look for a match with regular expressions and link back to
our application's own url.py file
This would allow us to look for any url that has the pattern:
    www.domainname.com/first_app
If we match that pattern, the include() function basically tells Django to go look at the urls.py file
inside of first_app folder. So we set a reference to the app, instead of listing them all in the main URLs


"""
from django.contrib import admin
from django.urls import include, re_path

from LVL_1.first_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'), #added function in view here
    re_path(r'^first_app/', include('LVL_1.first_app.urls')),
    re_path(r'^admin/', admin.site.urls),
]
