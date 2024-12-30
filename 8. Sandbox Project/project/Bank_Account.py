import os
import uuid

class BankAccount:
    """
    Class to simulate bank account operations.
    """
    def __init__(self, name, accountType, balance=0):
        """
        Constructor to initialize a new bank account.
        """
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = str(uuid.uuid4().hex[:8])  # Generate a unique ID
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        
        # Initialize transaction history file
        with open(self.filename, 'w') as file:
            file.write(f"Account Created\nName: {self.name}\nAccount Type: {self.accountType}\nAccount Number: {self.accountNumber}\nStarting Balance: {self.balance}\n")
            file.write("-" * 40 + "\n")

    def deposit(self, amount):
        """
        Function to deposit money into the account.
        """
        if amount > 0:
            self.balance += amount
            with open(self.filename, 'a') as file:
                file.write(f"Deposit: +${amount:.2f}\nNew Balance: ${self.balance:.2f}\n")
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Function to withdraw money from the account.
        """
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            with open(self.filename, 'a') as file:
                file.write(f"Withdrawal: -${amount:.2f}\nNew Balance: ${self.balance:.2f}\n")
            print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Function to retrieve the account balance.
        """
        return self.balance

    def get_account_number(self):
        """
        Function to retrieve the account number.
        """
        return self.accountNumber

    def get_name(self):
        """
        Function to retrieve the account holder's name.
        """
        return self.name

    def get_account_type(self):
        """
        Function to retrieve the account type.
        """
        return self.accountType

    def get_transaction_history(self):
        """
        Function to retrieve the transaction history.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                history = file.read()
            return history
        else:
            return "Transaction history file not found."


# Testing the BankAccount class
def main():
    # Create accounts
    account1 = BankAccount("Alice", "savings", 1000)
    account2 = BankAccount("Bob", "chequing")

    # Deposit money
    account1.deposit(500)
    account2.deposit(1000)

    # Withdraw money
    account1.withdraw(300)
    account2.withdraw(1500)  # Insufficient balance

    # Check balances
    print(f"{account1.get_name()}'s balance: ${account1.get_balance():.2f}")
    print(f"{account2.get_name()}'s balance: ${account2.get_balance():.2f}")

    # Get transaction history
    print("\nTransaction History for Alice:")
    print(account1.get_transaction_history())

    print("\nTransaction History for Bob:")
    print(account2.get_transaction_history())

main()
