from payment import Payment

class Crypto(Payment):
    def pay(self, amount):
        print(f"🪙 Crypto Payment of ₹{amount} successful")