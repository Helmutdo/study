
# PE_2/M4/021.py

# --- Sobrecarga de Operadores (Operator Overloading) ---

# La sobrecarga de operadores permite que nuestros objetos personalizados
# respondan a los operadores nativos de Python, como +, -, *, /, ==, <, >, etc.

# Esto se logra implementando "métodos mágicos" (magic methods) o "dunder methods"
# (double underscore methods) en nuestra clase.

# Por ejemplo, para que el operador `+` funcione entre dos objetos,
# debemos implementar el método `__add__`.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- Sobrecarga para Representación ---
    # __str__ es llamado por str() y print(). Devuelve una representación "amigable".
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # __repr__ es llamado por repr(). Devuelve una representación "inequívoca"
    # que idealmente podría recrear el objeto. Es un buen fallback para __str__.
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # --- Sobrecarga de Operadores Aritméticos ---
    # self es el operando de la izquierda (v1), other es el de la derecha (v2) en v1 + v2
    def __add__(self, otro_vector):
        if isinstance(otro_vector, Vector2D):
            # Suma de dos vectores
            nuevo_x = self.x + otro_vector.x
            nuevo_y = self.y + otro_vector.y
            return Vector2D(nuevo_x, nuevo_y)
        else:
            # NotImplemented le indica a Python que pruebe la operación inversa si está disponible.
            return NotImplemented

    def __sub__(self, otro_vector):
        if isinstance(otro_vector, Vector2D):
            nuevo_x = self.x - otro_vector.x
            nuevo_y = self.y - otro_vector.y
            return Vector2D(nuevo_x, nuevo_y)
        return NotImplemented

    # Multiplicación por un escalar (un número)
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector2D(self.x * escalar, self.y * escalar)
        return NotImplemented

    # --- Sobrecarga de Operadores de Comparación ---
    def __eq__(self, otro_vector):
        """Sobrecarga para el operador de igualdad (==)"""
        if isinstance(otro_vector, Vector2D):
            return self.x == otro_vector.x and self.y == otro_vector.y
        return False

    def __abs__(self):
        """Sobrecarga para la función abs(), que calcula la magnitud del vector."""
        import math
        return math.sqrt(self.x**2 + self.y**2)


# --- Uso de la clase con operadores sobrecargados ---

v1 = Vector2D(2, 3)
v2 = Vector2D(5, 1)

# Usando __str__
print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

# 1. Suma de vectores (llama a v1.__add__(v2))
v_suma = v1 + v2
print(f"Suma (v1 + v2): {v_suma}")

# 2. Resta de vectores (llama a v1.__sub__(v2))
v_resta = v1 - v2
print(f"Resta (v1 - v2): {v_resta}")

# 3. Multiplicación por escalar (llama a v1.__mul__(3))
v_mult = v1 * 3
print(f"Multiplicación (v1 * 3): {v_mult}")

# 4. Comparación de igualdad (llama a v1.__eq__(v3))
v3 = Vector2D(2, 3)
print(f"\n¿Es v1 igual a v2? {v1 == v2}") # False
print(f"¿Es v1 igual a v3? {v1 == v3}") # True

# 5. Magnitud del vector (llama a v1.__abs__())
print(f"Magnitud de v1: {abs(v1):.2f}")


# La sobrecarga de operadores hace que nuestras clases se sientan más intuitivas
# y se integren mejor con el lenguaje. Es una herramienta poderosa para crear
# APIs expresivas, especialmente en dominios matemáticos o científicos.
