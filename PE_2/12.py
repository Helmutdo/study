# 12. Properties in Python OOP
# Properties allow controlled access to class attributes.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# Example
c = Circle(5)
print(f"Area: {c.area}")
c.radius = 10
print(f"New area: {c.area}")

# List comprehension with properties
circles = [Circle(r) for r in range(1, 6)]  # list comprehension
areas = [c.area for c in circles]
print(areas)

# Try except with property
try:
    c.radius = -1
except ValueError as e:
    print(e)