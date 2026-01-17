# 09_abstract_classes.py
# Concept: Abstract Classes and Methods

# An abstract class is a class that cannot be instantiated directly.
# It is meant to be a blueprint for other classes, providing a common interface
# for its subclasses. An abstract method is a method declared in an abstract class
# but has no implementation. Subclasses are required to provide an implementation
# for all abstract methods.

# In Python, we use the `abc` (Abstract Base Classes) module to create abstract classes.

from abc import ABC, abstractmethod

# 1. Define an Abstract Base Class (ABC)
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method: Subclasses MUST implement this method
    @abstractmethod
    def area(self):
        pass # No implementation in the abstract class

    # Abstract method: Subclasses MUST implement this method
    @abstractmethod
    def perimeter(self):
        pass # No implementation in the abstract class

    # Regular (concrete) method: Can be inherited and used directly or overridden
    def describe(self):
        return f"This is a {self.name} shape."

# 2. Concrete Class: Circle (inherits from Shape)
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    # Implementing the abstract method 'area'
    def area(self):
        import math
        return math.pi * self.radius**2

    # Implementing the abstract method 'perimeter'
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 3. Concrete Class: Rectangle (inherits from Shape)
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    # Implementing the abstract method 'area'
    def area(self):
        return self.width * self.height

    # Implementing the abstract method 'perimeter'
    def perimeter(self):
        return 2 * (self.width + self.height)

# 4. Demonstrating Abstract Classes

# Cannot instantiate an abstract class directly
try:
    # my_shape = Shape("Generic") # This would raise a TypeError
    pass
except TypeError as e:
    print(f"Error trying to instantiate abstract class Shape: {e}")

# Creating instances of concrete subclasses
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

print(circle.describe())
print(f"Circle Area: {circle.area():.2f}")
print(f"Circle Perimeter: {circle.perimeter():.2f}")

print("\n" + rectangle.describe())
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

# Polymorphic behavior with abstract classes
print("\n--- Polymorphic behavior ---")
shapes = [circle, rectangle]
for shape in shapes:
    print(f"{shape.name} Area: {shape.area():.2f}")
    print(f"{shape.name} Perimeter: {shape.perimeter():.2f}")
