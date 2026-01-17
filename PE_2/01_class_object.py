# 01_class_object.py
# Concept: Basic Class and Object Creation

# 1. Defining a simple class
# A class is a blueprint for creating objects (instances).
# It defines a set of attributes that an object will have and methods that an object can perform.
class MyClass:
    pass  # 'pass' is a null operation; nothing happens when it executes.
          # It's used here to define an empty class.

# 2. Creating objects (instances) of MyClass
# An object is an instance of a class. When a class is defined, no memory is allocated
# until an object is created.
obj1 = MyClass()
obj2 = MyClass()

# 3. Verifying the objects
# Each object is a distinct instance in memory.
print(f"Object 1: {obj1}")
print(f"Object 2: {obj2}")
print(f"Are obj1 and obj2 the same object? {obj1 is obj2}")

# You can add attributes to objects dynamically, though it's generally better
# to define them within the class, especially in the constructor.
obj1.name = "First Object"
obj2.id = 123

print(f"obj1.name: {obj1.name}")
print(f"obj2.id: {obj2.id}")

# Attempting to access an attribute that does not exist will raise an AttributeError
try:
    print(obj1.id)
except AttributeError as e:
    print(f"Error accessing obj1.id: {e}")

try:
    print(obj2.name)
except AttributeError as e:
    print(f"Error accessing obj2.name: {e}")
