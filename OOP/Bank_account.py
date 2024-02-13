class BankAccount:
    def __init__(self):
        self.int_rate=0.01
        self.balance=0

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee") 
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
            print(self.balance)
        return self
    
account1=BankAccount()
account2=BankAccount()

account1.deposit(100).deposit(500).deposit(300).withdraw(200).display_account_info().yield_interest()
account2.deposit(300).deposit(500).withdraw(100).withdraw(200).withdraw(200).withdraw(600).display_account_info().yield_interest()
