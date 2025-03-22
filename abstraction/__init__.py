#Create an abstract class Vehicle with an abstract method max_speed().
# Also, add a constructor to initialize brand.
# Create two subclasses Car and Bike to implement max_speed().

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self,brand):
        self.brand=brand

    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)
        
    def max_speed(self):
        return "200km/h"

class Bike(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    def max_speed(self):
        return "250km/h"

obj_car=Car(brand="toyota")
obj_bike=Bike(brand="Yamaha")

print(f" car company--> {obj_car.brand} ---> max speed {obj_car.max_speed()}")
print(f" car company--> {obj_bike.brand} ---> max speed {obj_bike.max_speed()}")
