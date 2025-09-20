
balance = 1000
def show_balance():
    global balance
    return balance

def deposite():
    amount = input("Enter amount to deposite: ")
    if not amount.isdigit():
        print("Please enter a valid amount.")
        return 0
    amount = int(amount)
    return amount

def withdraw():
    global balance
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit():
        print("Please enter a valid amount.")
    amount = int(amount)
    if amount > balance:
        print('You cannot withdraw more than balance.')
        return 0
    return amount


print('Welcome to Bank Account App')
def main():
    global balance
    while True:
        print('Which operation would you like to do?')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        operation = int(input('Enter your choice: '))
        if operation == 1:
            print(f'Your balance is {show_balance()}$')
        elif operation == 2:
            amount = deposite()
            balance = show_balance() + amount
        elif operation == 3:
            amount = withdraw()
            balance = show_balance() - amount
        elif operation == 4:
            print('Thank you!')
            break
        else:
            print('Please enter a valid choice.')
            continue

        next_operation = input('Do you want to do another operation? (y/n): ') == 'y'
        if next_operation:
            continue
        else:
            print('Thank you!')
            break

main()



