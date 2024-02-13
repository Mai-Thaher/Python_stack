class User:
    def __init__(self, name, email_address):
        self.name=name
        self.email=email_address
        self.balance=BankAccount()
        
    def make_deposit(self, amount):
        self.balance.balance+=amount
        return self

    def make_withdraw(self, amount):
        self.balance.balance-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance.balance}$")
        return self

    def transfer_money(self, other_user, amount):
        other_user.balance.balance+=amount
        self.balance.balance-=amount
        return self

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
    
mai=User("Mai Thaher", "maithaher79@gmail.com")  
ameed=User("Ameed Abubaker", "ameed_abubaker@gmail.com")
omar=User("Omar Abubaker", "Omer-22@gmail.com")  

mai.make_deposit(100).make_deposit(500).make_deposit(500).make_withdraw(300).display_user_balance().transfer_money(omar, 200) 
ameed.make_deposit(500).display_user_balance().make_deposit(300)
