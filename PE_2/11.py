# 11. Static Methods and Class Methods in Python OOP
# Static methods belong to the class and don't require an instance.
# Class methods receive the class as the first argument and can modify class state.

class Example:
    @staticmethod
    def static_method():
        return "This is a static method"

    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

# Example usage
print(Example.static_method())
print(Example.class_method())

# Using lambda and list comprehension in static method
class MathUtils:
    @staticmethod
    def apply_operation(numbers, operation):
        return [operation(x) for x in numbers]  # list comprehension with lambda

# Example
nums = [1, 2, 3, 4]
squared = MathUtils.apply_operation(nums, lambda x: x**2)
print(squared)

# Try except in class method
class SafeMath:
    @classmethod
    def divide(cls, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

print(SafeMath.divide(10, 2))
print(SafeMath.divide(10, 0))