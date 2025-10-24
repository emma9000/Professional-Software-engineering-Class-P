# myapp/urls.py
from django.urls import path
from .views import welcome

urlpatterns = [
    path("welcome/<str:name>/", welcome, name="welcome"),
]
