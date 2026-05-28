from payment import Payment

class Card(Payment):
    def pay(self, amount):
        print(f"💳 Card Payment of ₹{amount} successful")