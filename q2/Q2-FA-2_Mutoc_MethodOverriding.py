# hospital billing system
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


name = input("Welcome to PhilHealth, please enter patient name: ")
bill = float(input("Please, enter bill amount: "))

print("\n1. regular patient")
print("2. senior citizen")
print("3. philhealth member")

choice = input("Enter your choice: ")

if choice == "Option 1":
    patient = Patient(name, bill)
elif choice == "Option 2":
    patient = SeniorPatient(name, bill)
elif choice == "Option 3":
    patient = PhilHealthPatient(name, bill)
else:
    print("Invalid choice!")
    exit()

print("\n--- HOSPITAL BILL ---")
print("Patient Name:", patient.get_name())
print("Original Bill: PHP", patient.get_bill_amount())
print("Final Bill: PHP", round(patient.calculate_bill(), 2))
