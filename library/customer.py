class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        if len(self.accounts) == 0:
            print(f"{self.name} has no accounts.")
        elif len(self.accounts) > 0:
            for account in self.accounts:
                print(f"- Account {account.account_number}: £{account.balance} \n")
        else:
            pass
    