import random

def main():
    colors = ['R', 'G', 'B', 'Y', 'W']
    pallet = random.choices(colors, k=4)
    print(pallet)
    chances = 5
    print(f'Colors have been chosen among this group: {colors}')

    while chances > 0:
        guess = [color.upper() for color in input('Guess a 4 colored pallet(with space): ').split()]
        chances -= 1
        if guess == pallet:
            break

        correct_positions = 0
        incorrect_positions = 0
        temp = list(pallet)

        for i in range(4):
            if guess[i] == pallet[i]:
                correct_positions += 1

            elif guess[i] in pallet and guess[i] in temp:
                incorrect_positions += 1
                temp.remove(guess[i])

        print(f'correct positions: {correct_positions} | incorrect positions: {incorrect_positions}')
        print(f'You have {chances} chances left!')

    if chances == 0:
        print(f'You lose! pallet was {pallet}')
    else:
        print(f'You win! with {5 - chances} guesses.')

main()
answer = input('Do you want to play again? (y/n): ')
if answer == 'y':
    main()
else:
    print('Thank you for playing!')

