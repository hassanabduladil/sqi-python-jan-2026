class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"""Account owner: {self.owner}"
Account balance: {self.balance}"""
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Acepted")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable")
            
        else:
            self.balance -= amount
            print("Withdrawal Acepted")

# Instantiate the class
acct1 = Account('Winnie', 100)

#2. Print the object
print(acct1)
# Output:
# Account owner: Winnie
# Account balance: $100

#3. Show the account owner attribute
print(acct1.owner)  # Winnie

#4. Show the account balance attribute 
print(acct1.balance)  # 100

#5. Make a series of deposits and withdrawals 
acct1.deposit(50)  # Output: Deposit Accepted

acct1.withdraw(15)  # Output: Withdrawal Accepted

#6. Make a withdrawal that exceeds the available balance 
acct1.withdraw(500)  # Output: Funds Unavailable!
