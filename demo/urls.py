from unicodedata import name
from django.urls import path
from django.views import View

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('getpath', views.path, name="path")
]
