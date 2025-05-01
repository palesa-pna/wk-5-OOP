from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def move(self):
        pass
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Concrete implementations
class Dog(Animal):
    def move(self):
        print(f"{self.name} runs happily! 🐕")
    
    def speak(self):
        print(f"{self.name} says: Woof! 🐶")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims gracefully! 🐟")
    
    def speak(self):
        print(f"{self.name} says: Blub blub! 🐠")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies high! 🦅")
    
    def speak(self):
        print(f"{self.name} says: Tweet! 🐦")

# Polymorphism in action
def animal_showcase(animals):
    for animal in animals:
        animal.move()
        animal.speak()
        print("---")

# Create animal objects
buddy = Dog("Buddy")
nemo = Fish("Nemo")
eagle = Bird("Thor")

animal_showcase([buddy, nemo, eagle])