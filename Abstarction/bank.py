from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self,customer_name,loan_amount):
        self.customer_name = customer_name
        self.loan_amount = loan_amount
        
    @abstractmethod
    def loan_interest(self):
        pass
    
    @abstractmethod
    def calculate_emi(self):
        pass
    
    @abstractmethod
    def account_type(self):
        pass
    
    