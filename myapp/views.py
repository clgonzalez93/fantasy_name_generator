import random
from django.shortcuts import render

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'


def generate_random_consonant():
    return random.choice(consonants)


def generate_random_vowel():
    return random.choice(vowels)


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


def generate_fantasy_name(original_name):
    if original_name[0].lower() in consonants:
        return names_with_consonants(original_name)
    else:
        return names_with_vowels(original_name)


def index(request):
    """ Main Django view for name generation and acceptance """
    result = None
    original_name = request.POST.get('original_name')
    suggestion_count = int(request.POST.get('suggestion_count', 0))
    show_buttons = False  # Flag to control visibility of accept/reject buttons

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

        elif 'reject' in request.POST:
            suggestion_count += 1
            if suggestion_count >= 3:
                result = "You have rejected too many suggestions! Your character's name will be Kevin."
            else:
                result = generate_fantasy_name(original_name)

    return render(request, 'index.html', {
        'result': result,
        'original_name': original_name,
        'suggestion_count': suggestion_count,
        'show_buttons': show_buttons  # Pass the flag to the template
    })
