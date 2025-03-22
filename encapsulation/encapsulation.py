class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,deposite):
        self.__balance=self.__balance + deposite

    def withdraw(self,amount):
        if amount<=self.__balance:
            print(f"{amount} successfully withdrawn")
            self.__balance -= amount
        else:
            print("you don't have enough balance.. Your balance is ",self.__balance)
    def get_balance(self):
        return self.__balance

b=BankAccount(10000)

while True:
    print(" 1.Deposit \n 2.Withdraw \n 3.GetBalance \n 4.Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        a=int(input("Enter amount you want deposite:"))
        b.deposit(a)
        print("")
    elif choice==2:
        a = int(input("Enter amount you want withdraw:"))
        b.withdraw(a)
        print("")
    elif choice==3:
        print(f"Your remaining balance is :{b.get_balance()}")
        print("")
    elif choice==4:
        print("Thank you for using our service")
        break
    else:
        print("Invalid choice")
        print("")