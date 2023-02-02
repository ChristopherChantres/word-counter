from django.shortcuts import render

# Function index assigned to urls.py (index)
def index(request):
  return render(request, 'index.html')


# Function counter returns the /counter page
def counter(request):
  text = request.POST['text'] # Get the data from the textarea by GET
  amount_of_words = len(text.split()) # Count the number of words in the text
  return render(request, 'counter.html', {'amount': amount_of_words}) # Send the amount of words to counter.html