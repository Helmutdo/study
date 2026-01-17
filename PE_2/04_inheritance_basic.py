# 04_inheritance_basic.py
# Concept: Basic Single Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties
# from another class. The original class is called the parent class (or base class),
# and the new class is called the child class (or derived class).

# 1. Parent Class (Base Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Generic animal sound"

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}"

# 2. Child Class (Derived Class) - inherits from Animal
# The 'Dog' class inherits 'name' and 'species' attributes,
# and 'make_sound', 'display_info' methods from the 'Animal' class.
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor to initialize parent attributes
        # super() refers to the parent class.
        super().__init__(name, species="Dog")
        self.breed = breed

    # The Dog class can have its own methods
    def bark(self):
        return f"{self.name} barks loudly!"

    # We can also override parent methods if needed (see next example for more detail)
    # def make_sound(self):
    #     return "Woof woof!"

# 3. Another Child Class (Derived Class) - inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def meow(self):
        return f"{self.name} says Meow!"

# 4. Creating objects and demonstrating inheritance
print("--- Animal Object ---")
generic_animal = Animal("Leo", "Lion")
print(generic_animal.display_info())
print(generic_animal.make_sound())

print("\n--- Dog Object ---")
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.display_info()) # Inherited from Animal
print(my_dog.make_sound())   # Inherited from Animal
print(my_dog.bark())         # Specific to Dog class
print(f"My dog's breed: {my_dog.breed}")

print("\n--- Cat Object ---")
my_cat = Cat("Whiskers", "Tabby")
print(my_cat.display_info()) # Inherited from Animal
print(my_cat.make_sound())   # Inherited from Animal
print(my_cat.meow())         # Specific to Cat class
print(f"My cat's color: {my_cat.color}")

# Verify types
print(f"\nIs my_dog an instance of Dog? {isinstance(my_dog, Dog)}")
print(f"Is my_dog an instance of Animal? {isinstance(my_dog, Animal)}")
print(f"Is generic_animal an instance of Dog? {isinstance(generic_animal, Dog)}")
