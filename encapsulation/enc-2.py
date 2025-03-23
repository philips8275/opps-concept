#Question:
# Modify the BankAccount class. Add a set_balance() method to update the balance, but only if the amount is positive.
# Prevent direct modification of _balance.
# Hint: Use getter and setter methods.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, newbalance):
        if newbalance > 0:
            self._balance = newbalance
            return "balance updated successfully"
        else:
            return "Balance cannot be negative or zero"


acc = BankAccount(5000)

print(acc.set_balance(-3000))

print(f"your balance is {acc.get_balance()}")

print(acc.set_balance(-9000))

