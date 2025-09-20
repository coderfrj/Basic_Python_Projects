import random

symbols = {"rock": '🗿' , "paper": '📄', "scissors": '✂'}
choices = ["rock", "paper", "scissors"]

def winner(user, computer):
    statuse = ''
    if user == 'rock':
        if computer == 'scissors':
            statuse = 'win'
        elif computer == 'paper':
            statuse = 'lose'
        elif computer == 'rock':
            statuse = 'tie'
    elif user == 'paper':
        if computer == 'scissors':
            statuse = 'lose'
        elif computer == 'rock':
            statuse = 'win'
        elif computer == 'paper':
            statuse = 'tie'
    elif user == 'scissors':
        if computer == 'rock':
            statuse = 'lose'
        elif computer == 'paper':
            statuse = 'win'
        elif computer == 'scissors':
            statuse = 'tie'

    return statuse

def play():
    win = 0
    lose = 0
    tie = 0

    playing = True
    while playing:
        user = input('Rock, paper,  scissors? ').lower()
        computer = random.choice(choices)

        if user == 'r':
            user = 'rock'
        elif user == 'p':
            user = 'paper'
        elif user == 's' or 'scissors':
            user = 'scissors'

        print(f'user: {symbols[user]}')
        print(f'computer: {symbols[computer]}')

        status = winner(user, computer)
        if status == 'win':
            win += 1
            print('You won!')
        elif status == 'lose':
            lose += 1
            print('You lost!')
        elif status == 'tie':
            tie += 1
            print("It's a tie!")

        print(f'******SCORS: >>win={win}, >>lose={lose}, >>tie={tie}******')

        next_play = input('Would you like to play again? (y / n): ').lower()
        if next_play == 'n':
            play = False
        else:
            continue




play()


