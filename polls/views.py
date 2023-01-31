from django.shortcuts import render

# Function index assigned to urls.py (index)
def index(request):
  return render(request, 'index.html')


# Function counter returns the /counter page
def counter(request):
  return render(request, 'counter.html')