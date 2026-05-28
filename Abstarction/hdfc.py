from bank import Bank

class HDFC(Bank):
    def loan_interest(self):
        return 10
    
    def calculate_emi(self):
        return self.loan_amount/10
    
    def account_type(self):
        return "Current Account"