import random

""" Fantasy name generator"""
# take name input - DONE
# check input has only characters - DONE
# make input lowercase - DONE
# check if name begins with consonant or vowel - DONE
# let user get 3 new name suggestions
# function to replace vowel with new vowel - DONE
# function to replace consonant with new consonant - DONE
# suggest new name and check if user is happy
# check suggestion count at some point
# if user is not happy after 3 suggestions, fall back to Kevin

####### LATER
# convert user instance/attempts to object
# integrate with flask
# database? if so, what could it be?
# an interesting end? Other than just giving a name

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'


def generate_random_consonant():
    return random.choice(consonants)


def generate_random_vowel():
    return random.choice(vowels)


def generate_fallback_name():
    print("Your character's name will be Kevin.")
    return


def names_with_consonants(original_name, suggestions):
    new_consonant = generate_random_consonant()
    while new_consonant == original_name[0].lower():
        new_consonant = generate_random_consonant()
    new_name = new_consonant.upper() + original_name[1:]
    return check_name_acceptance(new_name, suggestions)


def names_with_vowels(original_name, suggestions):
    new_vowel = generate_random_vowel()
    while new_vowel == original_name[0].lower():
        new_vowel = generate_random_vowel()
    new_name = new_vowel.upper() + original_name[1:]
    return check_name_acceptance(new_name, suggestions)


def check_name_acceptance(new_name, suggestion_count):
    accept = input(f"Your character's new name is {new_name}. Do you like it? Reply with 'Yes' or 'No'\n")
    if accept != "Yes" and accept != "No":
        print("Please reply with only 'Yes' or 'No'.")
        check_name_acceptance(new_name, suggestion_count)
    elif accept == 'No':
        suggestion_count += 1
        if suggestion_count >= 3:
            generate_fallback_name()
        generate_fantasy_name(new_name, suggestion_count)
    # Move the part where user accepts into the main function?
    else:
        print(f"Congrats! Your character's new name is {new_name}. May they embark on a fantastic adventure 😁\n")
        return


""" Main function/programme """


def welcome():
    suggestion_count = 0
    try:
        original_name = input("Hello! What's your male fantasy characters current name?\n")
        if not original_name.isalpha():
            print("The name can only contain letters from the Roman alphabet.")
            return
        generate_fantasy_name(original_name, suggestion_count)
    except Exception as e:
        error_message = "Oops! An error occurred: " + str(e)


def generate_fantasy_name(original_name, suggestion_count):
    # function if first letter is a consonant
    if original_name[0].lower() in consonants:
        names_with_consonants(original_name, suggestion_count)
    # function if first letter is a vowel
    else:
        names_with_vowels(original_name, suggestion_count)
    # can the finale be inserted here instead of in the acceptance check function?


if __name__ == "__main__":
    welcome()
