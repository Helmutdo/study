# 02_attributes_methods.py
# Concept: Class with Attributes and Methods

# 1. Defining a class with attributes and methods
# Attributes are variables associated with the class, representing its state.
# Methods are functions defined inside the class, representing its behavior.
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Instance method: '__init__' is a special method called a constructor.
    # It's automatically called when a new object is created.
    # 'self' refers to the instance of the class itself.
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Another instance method
    def get_info(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."

# 2. Creating objects and accessing their attributes and methods
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(f"My dog's name: {my_dog.name}")
print(f"My dog's age: {my_dog.age}")
print(f"My dog's species: {my_dog.species}")
print(my_dog.bark())
print(my_dog.get_info())

print("\n--- Your Dog ---")
print(f"Your dog's name: {your_dog.name}")
print(f"Your dog's age: {your_dog.age}")
print(f"Your dog's species: {your_dog.species}")
print(your_dog.bark())
print(your_dog.get_info())

# 3. Modifying instance attributes
my_dog.age = 4
print(f"\nMy dog's new age: {my_dog.age}")

# Class attributes can also be accessed directly from the class
print(f"\nDog class species: {Dog.species}")
