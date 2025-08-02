  # Simple Bank Account Class :

class BankAccount:

    def __init__(self, account_balance = 0):
        self.balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.display_balance()


# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated with double underscore

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")
