from django.shortcuts import render
from django.http import HttpResponse

# Function index assigned to urls.py (index)
def index(request):
  return HttpResponse('<h1>World Counter Index</h1>')