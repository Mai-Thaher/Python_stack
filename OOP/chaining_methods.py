class User:
    def __init__(self, name, email_address):
        self.name=name
        self.email=email_address
        self.account_balance=0


    def make_deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}$")
        return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance +=amount
        self.account_balance -=amount
        return self

mai=User("Mai Thaher", "maithaher79@gmail.com")
ameed=User("Ameed Abubaker", "ameed_abubaker@gmail.com")
omar=User("Omar Abubaker", "Omer-22@gmail.com")

mai.make_deposit(100).make_deposit(500).make_deposit(500).make_withdrawal(300).display_user_balance().transfer_money(omar, 200).display_user_balance()

ameed.make_deposit(300).make_deposit(700).make_withdrawal(50).make_withdrawal(100).display_user_balance()

omar.make_deposit(2000).make_withdrawal(200).make_withdrawal(100).make_withdrawal(50).display_user_balance().display_user_balance()

