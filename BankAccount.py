from random import choice

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


class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0:
            self.balance -= 10
            print('Insufficient funds.')
        else:
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f'Your balance is: ${self.balance}')
        return self.balance

    def add_interest(self):
        self.balance = round(self.balance * 1.00083, 2)

    def print_receipt(self):
        safe = []
        for i in range(len(str(self.account_number))):
            if i <= 3:

                safe.append('*')
            elif i > 3:
                safe.append(str(self.account_number)[i])
        asterisks = ''.join(safe)

        print(f'{self.full_name}')
        print(f'Account No.: {asterisks}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${float(self.balance)}')


bing_bong = BankAccount('Bing Bong', fullNumbaFinal, 123456789, 0)

bing_bong.deposit(100)

bing_bong.get_balance()

bing_bong.withdraw(50)

bing_bong.get_balance()

bing_bong.add_interest()

bing_bong.get_balance()

bing_bong.print_receipt()
