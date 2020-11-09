class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(amount):
        amount_deposit = amount + self.balance
        print(f"Amount Deposited: ${amount_deposit}")

    def withdraw(amount):
        amount_withdraw = self.balance - amount
        if amount_withdraw <= 0:
            self.balance - 10
            print('Insufficient funds.')
        else:
            print(f'Amount Withdrawn: ${amount_withdraw}')

    def get_balance():
        print(f'Your balance is: {self.balance}')
        return self.balance

    def add_interest():
        interest = self.balance * 0.00083

    def print_receipt():
        print(f'{self.full_name}')
        print(f'Account No.: {self.account_number}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: ${float(self.balance)}')
