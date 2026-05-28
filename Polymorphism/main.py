from upi import UPI
from card import Card
from crypto import Crypto

print("💳 Welcome to Payment Gateway System")

print("\nChoose Payment Method")
print("1. UPI")
print("2. Card")
print("3. Crypto")

choice = input("Enter choice: ")
amount = float(input("Enter payment amount: "))


if choice == "1":
    payment = UPI()

elif choice == "2":
    payment = Card()

elif choice == "3":
    payment = Crypto()

else:
    print("Invalid choice")
    exit()

payment.pay(amount)