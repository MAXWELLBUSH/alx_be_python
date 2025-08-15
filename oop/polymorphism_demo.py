# oop/polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Placeholder method. Must be overridden."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of circle using π * r²."""
        return math.pi * (self.radius ** 2)