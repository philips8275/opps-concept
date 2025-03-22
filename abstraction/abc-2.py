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