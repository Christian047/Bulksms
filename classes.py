class BankAccount:
    # we used init method to initialize the object of the class i.e name and balance
    def __init__(self, name, balance): 
        self.name = name
        self.balance = balance

    # we created a method that add funds
    def add_funds(self, amount): 
        self.balance += amount   
          
    # we created a method that debits a user    
    def debit_funds(self, amount):  
        if self.balance >= amount:  
            self.balance -= amount
        else:
            print("Insufficient funds")
            
    def delete_account(self):
        del self
        
# Example usage:
account = BankAccount("John Smith", 1000)

# Add funds
account.add_funds(500)
print(account.balance) # Output: 1500

# Debit funds
account.debit_funds(200)
print(account.balance) # Output: 1300

# Attempt to debit more funds than available
account.debit_funds(2000) # Output: "Insufficient funds"

# Delete account
account.delete_account()
print(account) # Output: NameError: name 'account' is not defined