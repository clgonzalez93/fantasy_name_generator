import random

""" Fantasy name generator"""
# take name input
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

""" generator for names beginning with consonants """
def generate_fantasy_name():
    suggestions = 0
    original_name = input("Hello! What's your male fantasy characters current name?/n")
    if original_name[0] in consonants:
        new_consonant = generate_random_consonant()
        while new_consonant == original_name[0]:
            new_consonant = generate_random_consonant()
        # replace using slicing or converting to list
        # original_name[0] = new_consonant
        pass
        #generate new consonant
    pass
    #replace existing first letter (for example Xaden becomes Caden)

def check_name_acceptance(suggestion_count):
    pass