import random

def guess_number():
    low = 1
    high = 100
    number = random.randint(low, high)
    attempts = 0

    while True:
        guess = int(input(f'guess a number betweeen {low} and {high}: '))
        attempts += 1
        if guess == number:
            break
        elif guess < number:
            print('Too low!')
            low = guess + 1
        elif guess > number:
            print('Too high!')
            high = guess - 1

    return number, attempts

number, attempts = guess_number()
print(f'Congratulations! You guessed the number "{number}" correctly in {attempts} tries.')