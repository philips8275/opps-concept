from threading import *

class Mythread:
    def __init__(self, str1):
        self.str=str1
    def display(self,n1,n2):
        print(self.str)
        print("print value= ",n1,n2)

obj = Mythread("hello world..!")
t1= Thread(target=obj.display(2,3))
t1.start()

