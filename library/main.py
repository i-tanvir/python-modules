from bank import Bank

# Create bank
ucl_bank = Bank("ARC Bank")

# Create customers
tanvir = ucl_bank.add_customer("Tanvir")
david = ucl_bank.add_customer("David")

# Create accounts for customers at bank
tanvir_one = ucl_bank.open_account(tanvir)
tanvir_two = ucl_bank.open_account(tanvir)
david_one = ucl_bank.open_account(david)

tanvir_one.deposit(100)
tanvir_one.withdraw(40)
tanvir_one.withdraw(100)

tanvir_two.deposit(200)
david_one.deposit(500)

print()

ucl_bank.show_customers()

print()

tanvir.show_accounts()

print()

david.show_accounts()
