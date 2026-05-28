from bank import Bank 

class ICICI(Bank):
    def loan_interest(self):
        return 12
    
    def calculate_emi(self):
        return self.loan_amount/8
    
    def account_type(self):
        return "Bussiness account"
    
    