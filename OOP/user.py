class User:
    def __init__(self, name, email_address):
        self.name=name
        self.email=email_address
        self.account_balance=0


    def make_deposit(self, amount):
        self.account_balance+=amount

    def make_withdrawal(self, amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}$")

    def transfer_money(self, other_user, amount):
        other_user.account_balance +=amount
        self.account_balance -=amount

mai=User("Mai Thaher", "maithaher79@gmail.com")
ameed=User("Ameed Abubaker", "ameed_abubaker@gmail.com")
omar=User("Omar Abubaker", "Omer-22@gmail.com")

mai.make_deposit(100)
mai.make_deposit(500)
mai.make_deposit(500)
mai.make_withdrawal(300)

mai.display_user_balance()

ameed.make_deposit(300)
ameed.make_deposit(700)
ameed.make_withdrawal(50)
ameed.make_withdrawal(100)

ameed.display_user_balance()

omar.make_deposit(2000)
omar.make_withdrawal(200)
omar.make_withdrawal(100)
omar.make_withdrawal(50)

omar.display_user_balance()

mai.transfer_money(omar, 200)
mai.display_user_balance()
omar.display_user_balance()