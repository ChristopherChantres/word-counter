from django.urls import path
from . import views

# Configuration of the urls
urlpatterns = [
    path('', views.index, name='index'), # index ('/')  url
    path('counter', views.counter, name='counter'), # counter/ url
]
