from django.urls import path
from . import views

# Configuration of the urls
urlpatterns = [
    path('', views.index, name='index'), # Index  url
]
