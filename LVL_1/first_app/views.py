from django.shortcuts import render
from django.http import HttpResponse #mandatory

'''

Each view takes at least one argument (any name)
Each view must return HttpResponse objects 
HttpResponse take on a string parameter representing a content of the page -> Can add HTML

'''

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello! I am from view.py!"}
    return render(request, 'first_app/index.html', context = my_dict)
