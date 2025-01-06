from django.shortcuts import render

# Create your views here.
import random
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world!")

# Consonants and vowels for the generator
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'


def generate_random_consonant():
    return random.choice(consonants)


def generate_random_vowel():
    return random.choice(vowels)


def generate_fallback_name():
    return "Your character's name will be Kevin."


def names_with_consonants(original_name, suggestions):
    new_consonant = generate_random_consonant()
    while new_consonant == original_name[0].lower():
        new_consonant = generate_random_consonant()
    new_name = new_consonant.upper() + original_name[1:]
    return new_name


def names_with_vowels(original_name, suggestions):
    new_vowel = generate_random_vowel()
    while new_vowel == original_name[0].lower():
        new_vowel = generate_random_vowel()
    new_name = new_vowel.upper() + original_name[1:]
    return new_name


def generate_fantasy_name(original_name, suggestion_count):
    if original_name[0].lower() in consonants:
        return names_with_consonants(original_name, suggestion_count)
    else:
        return names_with_vowels(original_name, suggestion_count)


# 🌟 Django view to show the index page and handle form submission
def index(request):
    if request.method == 'POST':
        original_name = request.POST.get('original_name')
        suggestion_count = 0

        if not original_name.isalpha():
            result = "The name can only contain letters from the Roman alphabet."
        else:
            result = generate_fantasy_name(original_name, suggestion_count)

        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')