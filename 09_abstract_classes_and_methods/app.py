from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Derived class implementing the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Create a Rectangle object and calculate area
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
