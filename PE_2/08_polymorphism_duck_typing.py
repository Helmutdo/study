# 08_polymorphism_duck_typing.py
# Concept: Polymorphism using Duck Typing

# Duck typing is a programming concept related to dynamic typing.
# In duck typing, if an object walks like a duck and talks like a duck, then it must be a duck.
# In Python, you don't need to explicitly declare that a class implements an interface
# or inherits from a specific base class to achieve polymorphism. As long as an object
# has the required methods (or attributes), it can be used in a polymorphic way.

# 1. Define classes that are not related by inheritance but share common method names
class Duck:
    def speak(self):
        return "Quack!"

    def fly(self):
        return "Duck flying high!"

class Person:
    def speak(self):
        return "Hello there!"

    def walk(self):
        return "Person walking."

class Robot:
    def speak(self):
        return "Beep boop!"

    def process_data(self):
        return "Robot processing data."

# 2. A function that uses duck typing
def make_it_speak(entity):
    """
    This function expects an object that has a 'speak' method.
    It doesn't care about the object's type, only its behavior.
    """
    if hasattr(entity, 'speak') and callable(getattr(entity, 'speak')):
        print(f"{type(entity).__name__} says: {entity.speak()}")
    else:
        print(f"Cannot make {type(entity).__name__} speak.")

def make_it_fly(entity):
    """
    This function expects an object that has a 'fly' method.
    """
    if hasattr(entity, 'fly') and callable(getattr(entity, 'fly')):
        print(f"{type(entity).__name__} is: {entity.fly()}")
    else:
        print(f"Cannot make {type(entity).__name__} fly.")

# 3. Create instances of different classes
duck_obj = Duck()
person_obj = Person()
robot_obj = Robot()
some_number = 123 # An object without a 'speak' or 'fly' method

# 4. Demonstrate duck typing
print("--- Demonstrating 'make_it_speak' ---")
make_it_speak(duck_obj)
make_it_speak(person_obj)
make_it_speak(robot_obj)
make_it_speak(some_number)

print("\n--- Demonstrating 'make_it_fly' ---")
make_it_fly(duck_obj)
make_it_fly(person_obj)
make_it_fly(robot_obj)
make_it_fly(some_number)

# You can also use a list of diverse objects
print("\n--- Duck Typing with a list ---")
entities = [duck_obj, person_obj, robot_obj, some_number]
for entity in entities:
    make_it_speak(entity)
