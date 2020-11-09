from random import choice

lol = ['1', '2', '3']

for i in lol:
    print(choice(i))


class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        amount_deposit = amount + self.balance
        print(f"Amount Deposited: ${amount_deposit}")

    def withdraw(self, amount):
        amount_withdraw = self.balance - amount
        if amount_withdraw <= 0:
            self.balance - 10
            print('Insufficient funds.')
        else:
            print(f'Amount Withdrawn: ${amount_withdraw}')

    def get_balance(self):
        print(f'Your balance is: {self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083

    def print_receipt(self):
        print(f'{self.full_name}')
        print(f'Account No.: {self.account_number}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${float(self.balance)}')


bing_bong = BankAccount('Bing Bong', 17701342, 123456789, 0)
