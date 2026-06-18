class Account:
    def __init__(self, account_number):
        account_number = self.account_number
        balance = 0  #sets starting balance
    
    def deposit(amount):
        if amount > 0:
            balance = balance + amount
            print(f"Deposited £{amount}. Your current balance is £{balance}.")
            return balance
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(amount):
        if amount <= balance:
            balance = balance - amount
            print(f"Withdrew £{amount}. Your current balance is £{balance}.")
            return balance
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            print("Insufficient funds")