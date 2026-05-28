from patient import Patient


print("🏥 Welcome to Hospital Management System")

patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))


# Create Patient Object
patient = Patient(patient_id, name, age)


while True:
    print("\n===== HOSPITAL MENU =====")
    print("1. Show Patient Details")
    print("2. Add Diagnosis")
    print("3. Add Bill")
    print("4. Pay Bill")
    print("5. View Medical History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # SHOW DETAILS
    if choice == "1":
        patient.show_patient_details()

    # ADD DIAGNOSIS
    elif choice == "2":
        diagnosis = input("Enter diagnosis: ")
        patient.add_diagnosis(diagnosis)

    # ADD BILL
    elif choice == "3":
        amount = float(input("Enter bill amount: "))
        patient.add_bill(amount)

    # PAY BILL
    elif choice == "4":
        amount = float(input("Enter payment amount: "))
        patient.pay_bill(amount)

    # VIEW HISTORY
    elif choice == "5":
        history = patient.get_history()
        print("\n===== MEDICAL HISTORY =====")
        for item in history:
            print(f"- {item}")

    # EXIT
    elif choice == "6":
        print("Exiting Hospital System...... bye :)")
        break

    else:
        print("Invalid option")