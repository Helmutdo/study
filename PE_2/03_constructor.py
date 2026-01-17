# 03_constructor.py
# Concept: Class with a Constructor (__init__)

# 1. Defining a class with a constructor
# The __init__ method is a special method, also known as the constructor.
# It is automatically called when a new object is created from the class.
# Its primary purpose is to initialize the attributes of the object.
class Car:
    def __init__(self, brand, model, year, color="red"):
        # 'self' refers to the newly created instance of the Car class.
        # We use 'self' to set instance attributes.
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False # Default state for a new car

    # Method to display car information
    def display_info(self):
        return f"Car: {self.color} {self.brand} {self.model} ({self.year})"

    # Method to start the car
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"The {self.brand} {self.model}'s engine started."
        else:
            return f"The {self.brand} {self.model}'s engine is already running."

    # Method to stop the car
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"The {self.brand} {self.model}'s engine stopped."
        else:
            return f"The {self.brand} {self.model}'s engine is already off."


# 2. Creating objects with different initial states using the constructor
car1 = Car("Toyota", "Camry", 2020) # 'color' will be default "red"
car2 = Car("Honda", "Civic", 2022, "blue")
car3 = Car("Ford", "Mustang", 1969, "black")

# 3. Accessing attributes and calling methods
print(car1.display_info())
print(car2.display_info())
print(car3.display_info())

print("\n--- Engine Operations ---")
print(car1.start_engine())
print(car1.start_engine()) # Try starting again
print(f"Is car1 running? {car1.is_running}")

print(car2.stop_engine()) # Try stopping an already stopped car
print(car2.start_engine())
print(f"Is car2 running? {car2.is_running}")
print(car2.stop_engine())
print(f"Is car2 running? {car2.is_running}")
