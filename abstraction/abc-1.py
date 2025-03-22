# Create an abstract class Shape with an abstract method area().
# Then, create two subclasses Circle and Rectangle that implement the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r**2

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w

obj_Cir = Circle(4)

obj_Rect = Rectangle(20,30)

print(f"Area of circle is {obj_Cir.area()}")
print(f"Area of Rectangle is {obj_Rect.area()}")