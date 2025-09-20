import random

words = ['computer', 'library', 'wizards', 'carwash', 'rainbow', 'scientist', 'teacher',
         'mechanic', 'lemonade', 'coffeeshop', 'university', 'success']

def pick_word():
    word = random.choice(words)
    return word

def show_hint(word):
    length = len(word)
    letters_holder = ["_"] * length
    return letters_holder

def show_hangman(wrong_answers):
    hangman = {0: ('+-------+   \n'
                   '|           \n'
                   '|           \n'
                   '|           \n'
                   '|_________ '),
               1: ('+-------+   \n'
                   '|       O    \n'
                   '|           \n'
                   '|           \n'
                   '|_________ '),
               2: ('+-------+   \n'
                   '|       O    \n'
                   '|       |   \n'
                   '|           \n'
                   '|_________ '),
               3: ('+-------+   \n'
                   '|       O    \n'
                   '|      /|   \n'
                   '|           \n'
                   '|_________ '),
               4: ('+-------+   \n'
                   '|       O    \n'
                   '|      /|\\  \n'
                   '|           \n'
                   '|_________ '),
               5: ('+-------+   \n'
                   '|       O    \n'
                   '|      /|\\ \n'
                   '|      /    \n'
                   '|_________ '),
               6: ('+-------+   \n'
                   '|       O    \n'
                   '|      /|\\ \n'
                   '|      / \\\n'
                   '|_________ ')}
    print(hangman[wrong_answers])

print('<<<<<<< Welcome to Hangman game! >>>>>>>')
def main():
    word = pick_word()
    word_holder = show_hint(word)
    print(word_holder)
    wrong_answers = 0

    while wrong_answers < 6 and '_' in word_holder:
        guess = input('Guess a letter: ')

        if guess == word:
            break

        length = len(word)
        if guess in word:
            print(f"That's right '{guess}' is in the word!")
            for i in range(length):
                if word[i] == guess:
                    word_holder[i] = guess
        else:
            print('Wrong guess')
            wrong_answers += 1

        print(f'you have {6 - wrong_answers} chances left')
        print(word_holder)

    if wrong_answers < 6:
        print('You Win!')
    else:
        print('You Lose!')

    show_hangman(wrong_answers)




if __name__ == '__main__':
    playing = True
    while playing:
        main()
        playing = input('Do you want to play again? (y/n): ').lower() == 'y'
