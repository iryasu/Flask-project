class Account():

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print('Cannot deposit negative amount')
        else:
            self.balance += amount
            print(f' You have deposited {amount}$')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Cannot withdraw more than balance')
        elif amount < 0:
            print('Cannot whithdraw negative amount')
        else:
            self.balance -= amount
            print(f' You have whithrawed {amount}$')
