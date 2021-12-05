
class BankAccount:


    def __init__(self, name): 
        self.name = name
        self.int_rate = 1.5
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.intrest_balance = self.balance * self.int_rate
            return self

    def display_account_info(self):
        print(f"Bank Account: {self.name}, Balance: {self.intrest_balance}")
        return self

robert = BankAccount("123")
mike = BankAccount("678")


robert.deposit(2000).deposit(1300).deposit(750).withdrawl(325).yield_interest().display_account_info()

mike.deposit(3500).deposit(2900).withdrawl(400).withdrawl(175).withdrawl(400).withdrawl(175).yield_interest().display_account_info()


