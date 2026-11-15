print("Hospital Billing System")
print("-----------------------")

class Patient: # Creates the parent class
    def __init__(self, name, bill_amount): # The constructor method that creates the attributes
        self.name = name
        self.bill_amount = float(bill_amount)

    # Getter of name
    def get_name(self):
        return self.name

    # Setter of name
    def set_name(self, name):
        self.name = name
    
    # Getter of bill_amount
    def get_bill_amount(self):
        return self.bill_amount

    # Setter of bill_amount
    def set_bill_amount(self, bill_amount):
        self.bill_amount = float(bill_amount)

    # Creates a method to calculate the bill amount, which can be overridden by child classes
    def calculate_bill(self):
        print(f"Calculated Bill: Php {self.bill_amount}")
        return self.bill_amount

    # Creates a method to display the patient type
    def display_patient_type(self):
        patient_type = "Regular Patient"
        print(f"Patient Type: {patient_type}")


class Senior_Patient(Patient): # Creates the child class that inherits from the parent class
    def __init__(self, name, bill_amount): # Creates the constructor method that creates the attributes
        super().__init__(name, bill_amount) # Calls the constructor of the parent class
    def calculate_bill(self): # Creates a method to calculate the bill amount, which overrides the method in the parent class
        discount = 0.20 
        discounted_amount = self.bill_amount * (1 - discount) # Calculates the discounted amount
        print(f"Calculated Bill: Php {discounted_amount}")
        return discounted_amount
    def display_patient_type(self): # Creates a method to display the patient type
        patient_type = "Senior Patient"
        print(f"Patient Type: {patient_type}") 

class PhilHealth_Patient(Patient): # Creates the child class that inherits from the parent class
    def __init__(self, name, bill_amount): # Creates the constructor method that creates the attributes
        super().__init__(name, bill_amount) # Calls the constructor of the parent class
    def calculate_bill(self): # Creates a method to calculate the bill amount, which overrides the method in the parent class
        discount = 0.15 
        discounted_amount = self.bill_amount * (1 - discount) # Calculates the discounted amount
        print(f"Calculated Bill: Php {discounted_amount}")
        return discounted_amount
    def display_patient_type(self): # Creates a method to display the patient type
        patient_type = "PhilHealth Member"
        print(f"Patient Type: {patient_type}") 

# Creates objects of the child classes
patient1 = Patient("Juan Dela Cruz", 15000.00) 
patient2 = Senior_Patient("Maria Santos", 15000.00)
patient3 = PhilHealth_Patient("Pedro Reyes", 15000.00)

# Calls the methods of the child class 1 and prints the output
patient1.set_name("Juan Dela Cruz")
print(f"Patient Name: {patient1.get_name()}")
patient1.display_patient_type()
patient1.set_bill_amount(15000.00)
print(f"Original Bill: Php {patient1.get_bill_amount()}")
patient1.calculate_bill()

# Calls the methods of the child class 2 and prints the output
patient2.set_name("Maria Santos")
print(f"\nPatient Name: {patient2.get_name()}")
patient2.display_patient_type()
patient2.set_bill_amount(15000.00)
print(f"Original Bill: Php {patient2.get_bill_amount()}")
patient2.calculate_bill()

# Calls the methods of the child class 3 and prints the output
patient3.set_name("Pedro Reyes")
print(f"\nPatient Name: {patient3.get_name()}")
patient3.display_patient_type()
patient3.set_bill_amount(15000.00)
print(f"Original Bill: Php {patient3.get_bill_amount()}")
patient3.calculate_bill()
