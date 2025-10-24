import django
from django.http import HttpResponse


def welcome(request, name):
    '''A view that welcomes a user by name.'''
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")
