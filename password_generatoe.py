import random
import string

def password_generator(min_length, letter=True, special=True):
    numbers = string.digits
    letters = string.ascii_letters
    specials = string.punctuation

    characters = numbers
    if letter:
        characters += letters
    if special:
        characters += specials

    psw = ''
    has_letters = False
    has_specials = False
    meets_criteria = False
    while len(psw) < min_length or not meets_criteria:
        new_char = random.choice(characters)
        psw += new_char

        if new_char in letters:
            has_letters = True
        elif new_char in specials:
            has_specials = True

        meets_criteria = True
        if letter:
            meets_criteria = has_letters
        if special:
            meets_criteria = meets_criteria and has_specials

    return psw

min_length = int(input('Enter minimum password length: '))
has_letters = input('Do you want to include letters? (y/n): ').lower() == 'y'
has_specials = input('Do you want to include specials? (y/n): ').lower() == 'y'
print(f'Your password is: {password_generator(min_length, has_letters, has_specials)}')