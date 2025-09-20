import random

def guess_number():
    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)
        answer = input(f'Computer guessed {guess}; is it correct, low or high? (c / l / h): ').lower()
        attempts += 1
        if answer == 'c':
            break
        elif answer == 'l':
            low = guess + 1
        elif answer == 'h':
            high = guess - 1
        else:
            print(f'Sorry {answer} is not a valid answer.')
            continue

    return guess, attempts

guess, attempts = guess_number()
print(f'Computer guessed {guess} in {attempts} attempts.')