from sbi import SBI
from hdfc import HDFC
from icici import ICICI

print("🏦 Welcome to Multi-Balzzzz-Bank Loan System")

name = input("Enter Your name: ")
print(f"hello {name}")

loan_amount = int(input("How much loan amount do you need: "))

print("1. SBI")
print("2. HDFC")
print("3. ICICI")

choose = input("\nchoose account: ")


if choose == "1":
    bank = SBI(name,loan_amount)
        
elif choose == "2":
    bank = HDFC(name,loan_amount)
            
elif choose == "3":
    bank = ICICI(name,loan_amount)
        
else:
    print("Invalid option")
    exit()
        
print(f"Customer name: {bank.customer_name}")
print(f"Loan Amount: {bank.loan_amount} Rs")
print(f"Loan interest: {bank.loan_interest()}%")
print(f"Monthly EMI: {bank.calculate_emi()} Rs")
print(f"Account Type: {bank.account_type()}")

