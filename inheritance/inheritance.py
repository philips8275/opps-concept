# Design a system where a Vehicle class contains an attribute max_speed.
# A Car class inherits from Vehicle and adds an attribute fuel_type.
# A SportsCar class further extends Car and includes an attribute turbo.
# Implement these classes using multilevel inheritance and show how an
# instance of SportsCar can access attributes from Vehicle and Car.

class Vehical:
    def __init__(self,max_speed):
        self.max_speed=max_speed

class Car(Vehical):
    def __init__(self,fuel_type):
        self.fuel_type=fuel_type


class SportsCar(Car,Vehical):
    def __init__(self,max_speed,fuel_type,turbo):
        self.turbo=turbo
        Car.__init__(self,fuel_type)
        Vehical.__init__(self,max_speed)
    def get_info(self):
        return f"Car max speed:{self.max_speed} fuel_type ={self.fuel_type} and turbo:{self.turbo}"

obj_SC=SportsCar(max_speed="120",fuel_type="petrol",turbo="V8")
print(obj_SC.get_info())
