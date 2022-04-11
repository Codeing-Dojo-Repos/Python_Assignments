class User:
    bank_name = 'Bank of El Passo'

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("{} balance is {}".format(self.name, self.account_balance))
        return self
    
    def transfer_money(self, other_user, amount ):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

jerry = User('jerry', 'jerry@gmail.com')
george = User('george', 'george@gmail.com')
kramer = User('kramer', 'kramer@gmail.com')

jerry.make_deposit(100).make_deposit(150).make_deposit(175).make_withdrawal(125).display_user_balance()
george.make_deposit(1000).make_deposit(1).make_withdrawal(501).make_withdrawal(500).display_user_balance()
kramer.make_deposit(500).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

jerry.transfer_money(george, 100)
jerry.display_user_balance()
george.display_user_balance()
kramer.display_user_balance()