#Banking account System
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount 
        print(f"{amount} Rs is deposited Successfully and current balance is {self.balance}")
        
    def withdraw(self, amount):
        if amount>self.balance:
            print(f"Insufficient balance")
        else:
            self.balance -= amount
            print(f"Current balance is {self.balance} Rs")
    
    def checkbalance(self):
        print(f"Balance is {self.balance} Rs")
            
name = input("Enter the account holder name: ")
print(f"Hello {name}")
initial_balance = int(input("Enter the initial amount: "))

user1 = BankAccount(name,initial_balance)

print("account is created successfully")

while True:
    print("\n--- BALZZZZ BANK ---")
    print("1. check balance")
    print("2. deposit amount")
    print("3. withdraw amount")
    print("4. exit")
    
    choice = input("Enter your choice: ")
    
    if choice=="1":
        user1.checkbalance()
    
    elif choice=="2":
        amount = int(input("Enter the deposit amount: "))
        user1.deposit(amount)
        
    elif choice=="3":
        amount = int(input("Enter the withdraw amount: "))
        user1.withdraw(amount)
    
    elif choice=="4":
        print("\nThank you for being a part of our bank")
        break
    
    else:
        print("\nInvalid Choice")
        exit()