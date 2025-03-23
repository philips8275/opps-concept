# Create a class BankAccount with a private variable _balance.
# Initialize it using a constructor and ensure balance cannot be accessed directly.
# Add a method get_balance() to return the balance.
# Hint: Use private attributes and a getter method.

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #using double underscore makes variable private

    def get_balance(self):
        return self.__balance #getter method to access variable
acc=BankAccount(5000)

print("Your balance is",acc.get_balance()) #can access variable only through get method

# print(""your balance is ",acc._balance()) we error here.
#if we see, here we are not able to access variable directly since it is protected