class BankAccount:
    bank_name = 'First National Dojo'

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance - 5
            print('Insufficient funds: Charging a $5 fee')
        return self

    def display_account_info(self):
        balance = self.balance
        print('Balance:', balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    # Methods
    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print('Balance:',self.account.balance)


Yang = User('Jason', 'jason@email.com')

Yang.make_deposit(75)
Yang.make_withdrawal(25)
Yang.display_user_balance()