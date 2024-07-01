# Abstraction:-
# Abstraction - OOPs
# Hiding the details and showing what is required.
#To force something to the user in abstract method

from abc import ABC, abstractmethod  #module


class Animal(ABC):  #abstractmethod will always use ABC class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):   #inherit from abstract method
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


dog = Dog("rancho")
print(dog.sound())

cat = Cat("CAT")
print(cat.sound())
