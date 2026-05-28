from payment import Payment


class UPI(Payment):

    def pay(self, amount):
        print(f"📱 UPI Payment of ₹{amount} successful")