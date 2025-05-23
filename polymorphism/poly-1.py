#Write a program to demonstrate method overriding with a Parent and Child class.
class Parent:
    def show(self):
        print("This is parent class")

class child(Parent):
    def show(self):
        print("This is child Class")


c=child()
c.show() #since child class holds the same method it will override the parent class
        # although we have inherited the parent class in the child class


p=Parent()
p.show() #since we have directly called the parent class it just print parent class