# 10_composition.py
# Concept: Composition as an Alternative to Inheritance

# Composition is a design principle where a class contains objects of other classes
# as its attributes. It's often preferred over inheritance for "has-a" relationships
# (e.g., a car "has an" engine) rather than "is-a" relationships (e.g., a dog "is an" animal).
# Composition allows for greater flexibility and reduces coupling between classes.

# 1. Component Class: Engine
class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def start(self):
        return f"Engine ({self.fuel_type}, {self.horsepower}hp) started."

    def stop(self):
        return "Engine stopped."

    def get_info(self):
        return f"{self.fuel_type} engine with {self.horsepower} horsepower."

# 2. Component Class: Wheels
class Wheels:
    def __init__(self, count, material):
        self.count = count
        self.material = material

    def rotate(self):
        return f"{self.count} {self.material} wheels are rotating."

    def get_info(self):
        return f"{self.count} {self.material} wheels."

# 3. Main Class: Car (uses composition)
class Car:
    def __init__(self, brand, model, year, engine_fuel, engine_hp, wheel_material):
        self.brand = brand
        self.model = model
        self.year = year
        # Composition: Car "has an" Engine and "has" Wheels
        self.engine = Engine(engine_fuel, engine_hp)
        self.wheels = Wheels(4, wheel_material)

    def start_car(self):
        return f"{self.brand} {self.model}: {self.engine.start()}"

    def stop_car(self):
        return f"{self.brand} {self.model}: {self.engine.stop()}"

    def drive(self):
        return f"{self.brand} {self.model} is driving with its {self.wheels.rotate()}"

    def display_car_info(self):
        return (f"Car: {self.brand} {self.model} ({self.year})\n"
                f"  - {self.engine.get_info()}\n"
                f"  - {self.wheels.get_info()}")

# 4. Creating objects and demonstrating composition
print("--- Creating a Sedan Car ---")
sedan = Car("Toyota", "Camry", 2023, "Gasoline", 200, "Alloy")
print(sedan.display_car_info())
print(sedan.start_car())
print(sedan.drive())
print(sedan.stop_car())

print("\n--- Creating an Electric Car ---")
electric_car = Car("Tesla", "Model S", 2024, "Electric", 670, "Aluminum")
print(electric_car.display_car_info())
print(electric_car.start_car())
print(electric_car.drive())
print(electric_car.stop_car())

# You can access component methods directly through the composed object
print(f"\nSedan engine info: {sedan.engine.get_info()}")
print(f"Electric car wheels: {electric_car.wheels.get_info()}")
