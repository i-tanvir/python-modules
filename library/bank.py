from .account import Account
from .customer import Customer

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.next = 1001
    
    def add_customer(self, name):
        customer = Customer(name)
        self.customers.append(customer)
        return customer
    
    def open_account(self, customer):
        account = Account(self.next)
        next += 1
        customer.add_account(account)
        return account
    
    def show_customers(self):
        print(f"Customers at {self.name}\n")
        for customer in self.customers:
            print(f"- {customer.self.name}")