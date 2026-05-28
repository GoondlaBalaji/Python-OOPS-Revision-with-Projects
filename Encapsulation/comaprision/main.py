# comparision code with private var and not private var

""" WITHOUT PRIVATE VARIABLES
class Patient:
    def __init__(self):
        self.bill = 0
    def add_bill(self, amount):
        if amount > 0:
            self.bill += amount
            print("Bill Added Successfully")
        else:
            print("Invalid amount")

# OBJECT

p1 = Patient()
p1.add_bill(5000)
print("Current Bill:", p1.bill)

# 😈 USER BYPASSES METHOD
p1.bill = -999999
print("Hacked Bill:", p1.bill)

OUTPUT:
Bill Added Successfully
Current Bill: 5000
Hacked Bill: -999999

"""
#-------------------------------------------------------------------------------------------------------------#

""" WITH PRIVATE VARIABLES
class Patient:
    def __init__(self):
        self.__bill = 0

    def add_bill(self, amount):
        if amount > 0:
            self.__bill += amount
            print("Bill Added Successfully")
        else:
            print("Invalid amount")

    def show_bill(self):
        print("Current Bill:", self.__bill)

# OBJECT

p1 = Patient()
p1.add_bill(5000)
p1.show_bill()


# 😈 USER TRIES TO BYPASS
p1.__bill = -999999
print(p1.__bill)
p1.show_bill()

OUTPUT:
Bill Added Successfully
Current Bill: 5000

-999999

Current Bill: 5000
WAIT WTF JUST HAPPENED?

"""