class BankAccount:
    # interest_rate = 0
    # balance = 0
    accounts = []

    def __init__(self, int_rate, balance=0):
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if( amount > self.balance):
            print('insufficient funds error')
            return
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance:,.2f}  Interest rate: {self.interest_rate}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.interest_rate)
        return self

    @classmethod
    def print_all(cls):
        for a in cls.accounts:
            a.display_account_info()


ac1 = BankAccount(.05, 1000)
ac2 = BankAccount(.05)

ac1.deposit(100).deposit(500).deposit(400).withdraw(1).yield_interest().display_account_info()
ac2.deposit(30_000).deposit(4_000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
BankAccount.print_all()