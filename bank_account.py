class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def details(self):
        print(f"your account is created with name '{self.account_holder}' account number '{self.account_number}' ")

    def show_balance(self):
        print(f"your balance is {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit amount is {amount} new balance is {self.balance}")
        else:
            print("amount should be greater than 0")

    def debit(self, amount):
        if 0<amount <=self.balance:
            self.balance-= amount
            print(f"debited amount {amount} new balance is {self.balance}")
        else:
            print("invalid amount")

acc_name = input("Enter your name: ")
acc_number = input("Enter you account number: ")
acc_balance = float(input("Enter your account balance: "))

acc = BankAccount(acc_number, acc_name, acc_balance)
acc.details()
acc.show_balance()

choice = int(input("Press '1' for Deposit OR Press '2' for Debit amount: "))
if choice == 1:
    acc_deposit = float(input("deposit amount: "))
    acc.deposit(acc_deposit)
elif choice == 2:
    acc_debit = float(input("debit amount: "))
    acc.debit(acc_debit)
else:
    print("Enter a valid option")

acc.show_balance()




