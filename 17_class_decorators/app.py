# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
p = Person("Ramillea")

# Call the added greet() method
print(p.greet())
