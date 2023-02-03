from django.shortcuts import render

# Function index assigned to urls.py (index)
def index(request):
  return render(request, 'index.html')


# Function counter returns the /counter page
def counter(request):
  text = request.POST['text'] # Get the data from the textarea by GET
  amount_of_words = len(text.split()) # Count the number of words in the text

  consonant_box =[] # Array to store all consonant words
  vowel_box = [] # Array to store all vowel words
  vowels = ('a', 'e', 'i', 'o', 'u') # Vowels tuple
  words_isolated = text.split() # Isolate each word from the text

  # Iterating in the array from all the isolated words (from the text)
  for word in words_isolated:
    checking_first_word = word[0] # Gettin the firs letter of the word
    if checking_first_word not in vowels:
      print(f'"{word}" CONSONANT')
      consonant_box.append(checking_first_word) # Appending the consonant to the consonant_box
    else:
      print(f'"{word}" VOWEL')
      vowel_box.append(checking_first_word) # Appending the vowel to the vowel_box

  return render(request, 'counter.html', {'amount': amount_of_words, 'vowel_words': len(vowel_box), 'consonant_words': len(consonant_box)}) # Send the amount of words, vowel_words and consonant_words to counter.html