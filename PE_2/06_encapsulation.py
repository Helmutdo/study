# 06_encapsulation.py
# Concept: Encapsulation with Public, Protected, and Private Members

# Encapsulation is the bundling of data (attributes) and methods that operate on the data
# within a single unit (class). It restricts direct access to some of an object's
# components, which means that the internal representation of an object is hidden
# from the outside.

# In Python, encapsulation is achieved by convention rather than strict enforcement
# like in some other languages (e.g., Java with private/public keywords).

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner  # Public attribute: accessible from anywhere

        # Protected attribute: prefixed with a single underscore (_). 
        # By convention, indicates that it should not be accessed directly from outside
        # the class or its subclasses, but it's still technically accessible.
        self._account_number = self._generate_account_number()

        # Private attribute: prefixed with a double underscore (__).
        # Python "name-mangles" these attributes, making them harder to access directly
        # from outside the class. They are still accessible, but the mechanism
        # is more cumbersome (e.g., _ClassName__private_attribute).
        if initial_balance >= 0:
            self.__balance = initial_balance
        else:
            self.__balance = 0
            print("Initial balance cannot be negative. Setting to 0.")

    def _generate_account_number(self):
        # A protected helper method
        import random
        return f"ACC-{random.randint(10000, 99999)}"

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            print("Insufficient funds.")
            return False

    # Public method (getter) to safely access the private balance
    def get_balance(self):
        return self.__balance

    # Public method (getter) for the protected account number
    def get_account_number(self):
        return self._account_number

# 1. Creating an object
account = BankAccount("Alice Smith", 1000)

print(f"Owner: {account.owner}")
print(f"Account Number (via getter): {account.get_account_number()}")
print(f"Initial Balance (via getter): ${account.get_balance()}")

# 2. Demonstrating public access
account.owner = "Alice Johnson" # Public attribute can be directly modified
print(f"New Owner: {account.owner}")

# 3. Demonstrating protected access (by convention, avoid direct access)
# While technically accessible, it's not recommended to do this directly.
print(f"Protected account number (direct access - generally avoided): {account._account_number}")
# account._account_number = "NEW-12345" # Can be changed, but breaks convention

# 4. Demonstrating private access (via name mangling)
# Direct access to __balance would raise an AttributeError
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Attempt to directly access __balance failed: {e}")

# Accessing the "private" attribute via name mangling (not recommended for general use)
print(f"Private balance (via name mangling - generally avoided): ${account._BankAccount__balance}")
account._BankAccount__balance = 5000 # Can be modified, but breaks encapsulation principles
print(f"Balance after direct modification (via mangling): ${account.get_balance()}")


# 5. Using public methods to interact with the balance
account.deposit(500)
account.withdraw(200)
account.withdraw(6000) # Insufficient funds

print(f"Final Balance (via getter): ${account.get_balance()}")

# Example with negative initial balance
print("\n--- Testing negative initial balance ---")
bad_account = BankAccount("Bob", -100)
print(f"Bob's initial balance: ${bad_account.get_balance()}")
bad_account.deposit(200)
print(f"Bob's new balance: ${bad_account.get_balance()}")
