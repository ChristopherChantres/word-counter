# Pulga Word Counter
---

https://github.com/user-attachments/assets/15e9eff2-ece8-41ea-a0ce-d1939f01d150

---
## Overview

Pulga Word Counter is a simple Django-based web application that takes an input text from the user and provides a detailed analysis of the word count, including:

  - The total number of words.
  - The count of words starting with a vowel.
  - The count of words starting with a consonant.

The application includes two main views:

    index view for users to input their text.
    counter view to display the results after submission.

## Features

    Text Analysis: Counts the total number of words in the input text.
    Vowel & Consonant Classification: Classifies words based on whether they start with a vowel or consonant.
    Easy-to-use Interface: Users can enter text and view analysis results instantly by clicking the "Count!" button.

## How It Works

    The user enters the text in the input box and clicks on the Count! button.
    The app takes the input and calculates:
        The total number of words.
        The number of words starting with a vowel.
        The number of words starting with a consonant.
    The results are displayed on the counter.html page.

## Installation

    Python 3.6 or higher
    Django 4.0 or higher

Clone the Repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

## Install Dependencies

Install Django via pip:

```bash
pip install django
```

Run the Development Server:

```bash
python manage.py runserver
```

Access the Application. Open your web browser and go to:
```bash
http://127.0.0.1:8000/
```
