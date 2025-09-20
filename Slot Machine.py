import random

balance = 100

def spin():
    symbols = ['🍒', '🍕', '🎃', '🔔', '💵']
    this_round = random.choices(symbols, k=3)
    return this_round

def get_pay(rows):
    prizes = {'🍒': 3, '🍕': 7, '🎃': 5, '🔔': 10, '💵': 25}
    if rows[0] == rows[1] == rows[2]:
        pay = prizes[rows[0]] * 3
        return pay
    else:
        return 0

def show_rows(rows):
    print(f'{rows[0]} | {rows[1]} | {rows[2]}')


print('***************************************')
print('Welcome to Python Slot Machine!')
print('Symbols are: 🍒, 🍕, 🎃, 🔔, 💵')
print('***************************************')

def play():
    global balance
    if balance > 0:
        bet = int(input('How much money would you like to bet? '))
        if bet > balance or bet < 0:
            print('please enter a valid number')
            return balance
        balance -= bet

        print('Spinning...\n')

        this_round = spin()
        show_rows(this_round)

        pay = get_pay(this_round)
        if pay > 0:
            print(f'You win! {pay}$')
            balance += pay

        print(f'Your balance is: {balance}')
    return balance

playing = True
while playing:
    balance = play()
    if balance > 0:
        playing = input('Would you like to play again? (y / n): ').lower() == 'y'

    if balance <= 0 or not playing:
        print('Thanks for playing!')
        playing = False


