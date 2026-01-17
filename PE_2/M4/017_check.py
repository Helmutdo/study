
# PE_2/M4/017_check.py

# --- Clases Base Abstractas (Abstract Base Classes - ABCs) ---

# Una clase base abstracta (ABC) es una clase que no se puede instanciar.
# Su propósito es servir como una plantilla para otras clases, forzando a las
# clases hijas a implementar ciertos métodos.

# Las ABCs son una forma de establecer un "contrato" o una interfaz que las subclases deben seguir.
# Se utilizan para asegurar que una clase derivada implemente todos los métodos necesarios.

# Para crear una ABC, usamos el módulo `abc` de Python.
from abc import ABC, abstractmethod

# --- Definiendo una Clase Abstracta ---

# La clase debe heredar de ABC.
class FormaGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # El decorador @abstractmethod marca un método como abstracto.
    # Las clases hijas ESTÁN OBLIGADAS a implementar este método.
    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área. Debe ser implementado por las subclases."""
        pass

    # También podemos tener métodos concretos en una clase abstracta.
    # Estos métodos son heredados y pueden ser usados directamente.
    def describir(self):
        return f"Soy una forma geométrica llamada {self.nombre}."


# --- Intentando instanciar una clase abstracta ---
# Esto dará un error, porque las clases abstractas no pueden ser instanciadas.
# try:
#     forma_indefinida = FormaGeometrica("Indefinida")
# except TypeError as e:
#     print(f"Error esperado: {e}")


# --- Implementando la Clase Abstracta ---

class Rectangulo(FormaGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    # Debemos implementar el método abstracto 'calcular_area'.
    # Si no lo hacemos, Rectangulo también será una clase abstracta y no podrá ser instanciada.
    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    # Implementación específica para Círculo.
    def calcular_area(self):
        import math
        return math.pi * (self.radio ** 2)


# --- Uso de las Clases Concretas ---

mi_rectangulo = Rectangulo("Rectángulo Azul", 10, 5)
mi_circulo = Circulo("Círculo Rojo", 7)

# Podemos llamar tanto a los métodos heredados como a los implementados.
print(mi_rectangulo.describir())
print(f"El área de mi rectángulo es: {mi_rectangulo.calcular_area()}")

print("-" * 20)

print(mi_circulo.describir())
print(f"El área de mi círculo es: {mi_circulo.calcular_area():.2f}")


# Las ABCs son muy útiles para frameworks y librerías, donde se quiere
# asegurar que el usuario que extiende el framework implemente funcionalidades clave.
# Por ejemplo, para definir que cualquier "vehículo" debe tener un método "acelerar".
