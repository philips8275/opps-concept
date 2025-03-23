# Question:
# Create a class Person with a protected variable _age.
# Create a subclass Student that modifies _age using a method.
# Hint: Use protected variables and inheritance.

class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age

class Student(Person):
    def update_age(self,age):
        if age>0:
            self._age=age
        else:
            print("Age cannot be negative")
    def get_age(self):
        return self._age

p=Student("philips",25)

p.update_age(-26)

print("Student age is ",p.get_age())
        