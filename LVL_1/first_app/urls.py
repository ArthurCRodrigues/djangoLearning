from django.urls import re_path
from LVL_1.first_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]