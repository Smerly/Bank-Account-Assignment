from random import choice

# Making the randomizer variable

numba = ['1', '2', '3', '4', '5', '6', '7', '8']

one = choice(numba)
two = choice(numba)
three = choice(numba)
four = choice(numba)
five = choice(numba)
six = choice(numba)
seven = choice(numba)
eight = choice(numba)

fullNumba = [one, two, three, four, five, six, seven, eight]

fullNumbaString = ''.join(fullNumba)

fullNumbaFinal = int(fullNumbaString)


# ------------------------------------------------------------------------------------------------------------------------------

# Class

class BankAccount:

    # Properties

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = 0

    # Methods

        # Allows an amount to be deposited

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${self.balance}")

        # Allows an amount to be withdrawn

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0:
            self.balance -= 10
            print('Insufficient funds.')
        else:
            print(f'Amount Withdrawn: ${amount}')

        # Checks the balance of your bank account

    def get_balance(self):
        print(f'Your balance is: ${self.balance}')
        return self.balance

        # Adds the monthly interest to your bank account

    def add_interest(self):
        self.balance = round(self.balance * 1.00083, 2)

        # Prints your receipt

    def print_receipt(self):

        # Making the Account number's first 4 numbers asterisks

        safe = []
        for i in range(len(str(self.account_number))):
            if i <= 3:

                safe.append('*')
            elif i > 3:
                safe.append(str(self.account_number)[i])
        asterisks = ''.join(safe)

        # The printing of the receipt (added the prints with nothing to make indents to make it look nicer)
        print('')
        print(f'{self.full_name}')
        print(f'Account No.: {asterisks}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${float(self.balance)}')
        print('')

# Making it work or testing it


bing_bong = BankAccount('Bing Bong', fullNumbaFinal, 123456789, 0)

bing_bong.deposit(100)

bing_bong.get_balance()

bing_bong.withdraw(50)

bing_bong.get_balance()

bing_bong.add_interest()

bing_bong.get_balance()

bing_bong.print_receipt()
