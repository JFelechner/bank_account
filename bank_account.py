
#Create a BankAccount class with the attributes interest rate and balance


#Add a deposit method to the BankAccount class


#Add a withdraw method to the BankAccount class


#Add a display_account_info method to the BankAccount class


#Add a yield_interest method to the BankAccount class


#Create 2 accounts


#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)


#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)


#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info


class BankAccount:

    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    def display_account_info(self):
        print(f"Bank Account: {self.name}, Balance: {self.balance}")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account1 = BankAccount( 1.5, 0)
account2 = BankAccount( 1.5, 0)


account1.deposit(2000).deposit(1300).deposit(750).withdrawl(325).yield_interest().display_account_info()

account2.deposit(3500).deposit(2900).withdrawl(400).withdrawl(175).withdrawl(400).withdrawl(175).yield_interest().display_account_info()


BankAccount.print_all_accounts()