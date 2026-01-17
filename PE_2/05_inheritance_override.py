# 05_inheritance_override.py
# Concept: Inheritance with Method Overriding

# Method overriding is an ability of a class to change the implementation of a method
# provided by one of its ancestors. When a method in a subclass has the same name,
# same parameters, and same return type as a method in its superclass, then the method
# in the subclass is said to override the method in the superclass.

# 1. Parent Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model} ({self.year})"

    def start_engine(self):
        return f"The {self.brand} {self.model}'s engine starts with a generic sound."

# 2. Child Class - Car (overrides start_engine)
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    # Overriding the start_engine method from the Vehicle class
    def start_engine(self):
        return f"The {self.brand} {self.model}'s {self.fuel_type} engine roars to life!"

    def drive(self):
        return f"The {self.brand} {self.model} is driving."

# 3. Child Class - ElectricCar (overrides start_engine differently)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        # Electric cars are still cars, so we call Car's constructor
        super().__init__(brand, model, year, "Electric")
        self.battery_capacity = battery_capacity

    # Overriding the start_engine method again for electric cars
    def start_engine(self):
        return f"The {self.brand} {self.model} (Electric) silently powers on."

    def charge(self):
        return f"The {self.brand} {self.model} is charging its {self.battery_capacity}kWh battery."

# 4. Creating objects and demonstrating method overriding
print("--- Vehicle Object ---")
gen_vehicle = Vehicle("Generic", "ModelX", 2020)
print(gen_vehicle.display_info())
print(gen_vehicle.start_engine())

print("\n--- Car Object ---")
my_car = Car("Honda", "Civic", 2022, "Gasoline")
print(my_car.display_info())
print(my_car.start_engine()) # Calls Car's start_engine
print(my_car.drive())

print("\n--- ElectricCar Object ---")
my_ev = ElectricCar("Tesla", "Model 3", 2023, 75)
print(my_ev.display_info())
print(my_ev.start_engine()) # Calls ElectricCar's start_engine
print(my_ev.drive())        # Inherited from Car
print(my_ev.charge())
