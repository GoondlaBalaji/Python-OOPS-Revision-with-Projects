class Patient:
    def __init__ (self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        
        self.__medical_history=[]
        self.__bill_amount=0
        self.__diagnosis="Not Diagonised"
    # getters to show values outside class because variables are private
    def get_bill(self):
        return self.__bill_amount
        
    def get_history(self):
        return self.__medical_history
        
    def get_diagnosis(self):
        return self.__diagnosis
        
    #operation we are doing below
    def add_diagnosis(self,diagnosis):
        if diagnosis.strip()=="":
            print("Diagnosis cannot be empty")
            return
        self.__diagnosis = diagnosis
        self.__medical_history.append(diagnosis)
        print("Diagnosis is updated Sucessfully")
                    
    def add_bill(self,amount):
        if amount<=0:
            print("Invalid bill amount")
            return
        self.__bill_amount += amount
        print(f"{amount} Rs added to patient bill")
            
    def pay_bill(self,amount):
        if amount<=0:
            print("Invalid bill amount")
            return
        if amount > self.__bill_amount:
            print("Payment exceeds current bill")
            return

        self.__bill_amount -= amount
        print(f"{amount} Rs bill paid successfully")
            
    #display the details   
    def show_patient_details(self):
        print("\n===== PATIENT DETAILS =====")
        print(f"Patient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Diagnosis  : {self.__diagnosis}")
        print(f"Bill       : ₹{self.__bill_amount}")
        print("\nMedical History: ")
        for history in self.__medical_history:
            print(f"\n- {history}")