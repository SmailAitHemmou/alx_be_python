  # Simple Bank Account Class :

class BankAccount:

    def __init__(self, account_balance = 0):
        self.balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            amount = float(input("Enter deposit amount: "))
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            amount = float(input("Enter withdrawal amount: "))
            return True
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")