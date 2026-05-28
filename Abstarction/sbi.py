from bank import Bank

class SBI(Bank):
    def loan_interest(self):
        return 8
    
    def calculate_emi(self):
        emi = self.loan_amount / 12
        return emi
    
    def account_type(self):
        return "Saving Account"