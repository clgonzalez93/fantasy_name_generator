import random

""" Fantasy name generator"""
# take name input - DONE
# check input has only characters
# make input lowercase
# check if name begins with consonant or vowel
# let user get 3 new name suggestions
# function to replace vowel with new vowel
# function to replace consonant with new consonant
# suggest new name and check if user is happy
# if user is not happy after 3 suggestions, fall back to Kevin
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'


def generate_random_consonant():
    return random.choice(consonants)


def generate_random_vowel():
    return random.choice(vowels)


def generate_fallback_name():
    print("Your character's name will be Kevin.")


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


""" Main function/programme """
def generate_fantasy_name():
    suggestions = 0
    try:
        original_name = input("Hello! What's your male fantasy characters current name?\n")
        if not original_name.isalpha():
            print("The name can only contain letters from the Roman alphabet.")
            return
        # function if first letter is a consonant
        if original_name[0].lower() in consonants:
            names_with_consonants(original_name)
        # function if first letter is a vowel
        else:
            names_with_vowels(original_name)
    except Exception as e:
        error_message = "Oops! An error occurred: " + str(e)


def check_name_acceptance(suggestion_count):
    pass


if __name__ == "__main__":
    generate_fantasy_name()