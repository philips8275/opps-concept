# Question:
# Modify the BankAccount class so _balance is fully private (__balance).
# Try accessing it directly and using _classname__attributeName.
# Hint: Use double underscore __ for private variables.
# Expected Output:
# acc = BankAccount(5000)
# print(acc.__balance)  # Should raise an AttributeError
# print(acc._BankAccount__balance)  # Output: 5000 (Using name mangling)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


acc = BankAccount(5000)
#print(acc.__balance)  # you will get error
print(acc._BankAccount__balance) #using name mangling
