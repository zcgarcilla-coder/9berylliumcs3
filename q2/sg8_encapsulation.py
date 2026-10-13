class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number # Private attribute
        self.__balance = float(balance)  # Private attribute, makes the proeperty a float

    def deposit(self, amount):
        if amount > 0:
            self.__balance += float(amount)

    def set_account_number(self, account_number):
        self.__account_number = account_number  # Public method to set private attribute

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative.")
            return
        self.__balance = float(balance)  # Public method to set private attribute

    @property
    def get_account_number(self):
        return self.__account_number  # Public method to access private attribute

    @property
    def get_balance(self):
        return self.__balance  # Public method to access private attribute

a1 = BankAccount(12345, 1000)

print("Account 1")
print(f"Account Number: {a1.get_account_number}") # Accessing the private attribute through a public method
print(f"Balance: {a1.get_balance}") # Accessing the private attribute through a public method

print("\nUpdate balance to -100")
a1.set_balance(-100) # Uses the set_balance method
print(f"Account Number: {a1.get_account_number}") # Accessing the private attribute through a public method
print(f"Balance: {a1.get_balance}") # Accessing the private attribute through a public method



  
