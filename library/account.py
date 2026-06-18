class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0  #sets starting balance
    
    def deposit(self, amount):
        self.amount = amount
        if self.amount > 0:
            self.balance += amount
            print(f"Deposited £{amount}. Your current balance is £{self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew £{amount}. Your current balance is £{self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            print("Insufficient funds")