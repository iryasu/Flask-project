class Account()

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else :
            raise 'Cannot deposit negative amount'
    
    def withdraw(self, amount):
        if amount > balance:
            raise 'Cannot withdraw more than balance'
        if amount < 0:
            raise 'Cannot whithdraw negative amount'
        balance -= amount
        print(f' You have whithrawed {amount}$')