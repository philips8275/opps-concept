# Create an abstract class Animal with two abstract methods sound() and move().
# Implement subclasses Dog and Bird with their own versions of these methods.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bhav bhav"
    def move(self):
        return "Run"
class Bird(Animal):
    def sound(self):
        return "chiv chiv"
    def move(self):
        return "Fly high in the sky"

obj_dog = Dog()
obj_bird = Bird()

print(f"Dog sounds --> {obj_dog.sound()} and move --> {obj_dog.move()}")
print(f"Dog sounds --> {obj_bird.sound()} and move --> {obj_bird.move()}")