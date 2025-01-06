import random
from django.shortcuts import render

# Define consonants and vowels
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'

# Helper functions for generating random consonants and vowels
def generate_random_consonant():
    return random.choice(consonants)

def generate_random_vowel():
    return random.choice(vowels)

# Functions to generate names based on consonants or vowels
def names_with_consonants(original_name):
    new_consonant = generate_random_consonant()
    while new_consonant == original_name[0].lower():
        new_consonant = generate_random_consonant()
    new_name = new_consonant.upper() + original_name[1:]
    return new_name

def names_with_vowels(original_name):
    new_vowel = generate_random_vowel()
    while new_vowel == original_name[0].lower():
        new_vowel = generate_random_vowel()
    new_name = new_vowel.upper() + original_name[1:]
    return new_name

# Function to generate the fantasy name based on the first character
def generate_fantasy_name(original_name):
    if original_name[0].lower() in consonants:
        return names_with_consonants(original_name)
    else:
        return names_with_vowels(original_name)

# Main view to handle name generation and acceptance
def index(request):
    result = None
    original_name = request.POST.get('original_name')
    suggestion_count = int(request.POST.get('suggestion_count', 0))
    show_buttons = False  # Flag to control visibility of accept/reject buttons
    fallback_name = "Kevin"  # Fallback name if rejected too many times

    # Handle POST requests for generating names and accepting/rejecting
    if request.method == 'POST':
        if 'generate' in request.POST:
            if not original_name.isalpha():
                result = "The name can only contain letters from the Roman alphabet."
            else:
                result = generate_fantasy_name(original_name)
                suggestion_count = 1  # Reset on first generation
                show_buttons = True  # Show the buttons once a name is generated

        elif 'accept' in request.POST:
            result = f"Congrats! Your character's new name is {original_name}! 🎉"
            show_buttons = False  # Hide buttons after acceptance

        elif 'reject' in request.POST:
            suggestion_count += 1
            if suggestion_count >= 4:
                result = f"You have rejected too many suggestions! Your character's name will be {fallback_name}."
                show_buttons = False  # Hide buttons after 3 rejections
            else:
                result = generate_fantasy_name(original_name)
                show_buttons = True  # Keep buttons visible after rejection for another suggestion

    # Render the template with the necessary context
    return render(request, 'index.html', {
        'result': result,
        'original_name': original_name,
        'suggestion_count': suggestion_count,
        'show_buttons': show_buttons,  # Pass the flag to the template
        'fallback_name': fallback_name
    })
