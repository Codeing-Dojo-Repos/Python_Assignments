import BankAccount as bank

class User:
    bank_name = 'Bank of El Passo'

    def __init__(self, name, email_address, int_rate, balance=0, num_accounts=1):
        self.name = name
        self.email = email_address
        self.account = []
        for i in range(1, num_accounts+1):
            print(f'adding account {i}:')
            self.account.append(bank.BankAccount(int_rate, balance))

    def make_deposit(self, amount, account_num=0):
        self.account[account_num].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_num=0):
        self.account[account_num].withdraw(amount)
        return self
    
    def display_user_balance(self, account_num=0):
        self.account[account_num].display_account_info()
        return self
    
    def transfer_money(self, other_user, amount ):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

jerry = User('jerry', 'jerry@gmail.com', .05, num_accounts=2)

jerry.make_deposit(100, account_num=0)
jerry.make_deposit(200, account_num=1)
jerry.display_user_balance(account_num=0)
jerry.display_user_balance(account_num=1)
