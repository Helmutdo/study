# 07_polymorphism_basic.py
# Concept: Basic Polymorphism with Method Overriding

# Polymorphism means "many forms". In OOP, it refers to the ability of different
# classes to be treated as instances of a common interface (often a parent class)
# and for methods to behave differently based on the actual object's type.
# Method overriding is a key mechanism to achieve polymorphism.

# 1. Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This is a generic implementation
        raise NotImplementedError("Subclass must implement abstract method")

# 2. Derived Class: Dog
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Woof!"

# 3. Derived Class: Cat
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Meow!"

# 4. Derived Class: Duck
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Overriding the speak method
    def speak(self):
        return f"{self.name} says Quack!"

# 5. Function that takes an Animal object (polymorphic behavior)
def make_animal_speak(animal):
    """
    This function accepts any object that is a subclass of Animal
    and calls its speak method. The specific implementation of speak
    will depend on the actual type of the animal object.
    """
    print(animal.speak())

# 6. Creating objects of different classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Donald")

# 7. Demonstrating polymorphism
print("--- Demonstrating Polymorphism ---")
make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)

# We can also put them in a list and iterate
print("\n--- Polymorphism with a list ---")
animals = [dog, cat, duck]
for animal in animals:
    make_animal_speak(animal)

# Attempting to create a generic Animal directly would raise an error if speak is called
try:
    generic_animal = Animal("Creature")
    generic_animal.speak()
except NotImplementedError as e:
    print(f"\nError: {e}")
