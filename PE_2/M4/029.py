# PE_2/M4/029.py

# --- Patrones de Diseño: Decorador (Decorator Pattern) ---

# No confundir con los "decoradores" de Python (`@mi_decorador`). Aunque la idea es similar,
# el Patrón Decorador es un patrón de diseño estructural que permite añadir
# funcionalidades a un objeto dinámicamente, sin alterar su estructura.

# El patrón funciona "envolviendo" un objeto con otro objeto "decorador" que
# tiene la misma interfaz. El decorador puede añadir su propia funcionalidad
# antes o después de delegar la llamada al objeto original envuelto.

# Es una alternativa flexible a la herencia para extender la funcionalidad.

from abc import ABC, abstractmethod

# --- 1. La Interfaz del Componente ---
# Define la interfaz común tanto para el objeto original como para los decoradores.

class Cafe(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_costo(self):
        pass

# --- 2. El Componente Concreto ---
# Es el objeto original al que le vamos a añadir funcionalidades.

class CafeSimple(Cafe):
    def get_descripcion(self):
        return "Café simple"

    def get_costo(self):
        return 5.0

# --- 3. El Decorador Base (Abstracto) ---
# Esta clase mantiene una referencia al objeto componente y se conforma a la
# interfaz del componente. Delega todo el trabajo al componente envuelto.

class IngredienteDecorador(Cafe, ABC):
    def __init__(self, cafe_a_decorar: Cafe):
        self._cafe_envuelto = cafe_a_decorar

    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_costo(self):
        pass

# --- 4. Los Decoradores Concretos ---
# Estos son los objetos que añaden la nueva funcionalidad.
# Cada uno envuelve al componente (que puede ser el café simple u otro decorador).

class ConLeche(IngredienteDecorador):
    def get_descripcion(self):
        # Añade "con Leche" a la descripción del café envuelto
        return self._cafe_envuelto.get_descripcion() + ", con Leche"

    def get_costo(self):
        # Añade el costo de la leche al costo del café envuelto
        return self._cafe_envuelto.get_costo() + 1.5

class ConChocolate(IngredienteDecorador):
    def get_descripcion(self):
        return self._cafe_envuelto.get_descripcion() + ", con Chocolate"

    def get_costo(self):
        return self._cafe_envuelto.get_costo() + 2.0

class ConCrema(IngredienteDecorador):
    def get_descripcion(self):
        return self._cafe_envuelto.get_descripcion() + ", con Crema"

    def get_costo(self):
        return self._cafe_envuelto.get_costo() + 2.5


# --- Demostración ---
# El cliente puede componer diferentes combinaciones de cafés dinámicamente.

# Empezamos con un café simple.
mi_cafe = CafeSimple()
print(f"Producto: {mi_cafe.get_descripcion()} \nCosto: ${mi_cafe.get_costo():.2f}")

print("-" * 20)

# Ahora lo decoramos.
# 1. Envolvemos el café simple con el decorador de Leche.
mi_cafe = ConLeche(mi_cafe)
print(f"Producto: {mi_cafe.get_descripcion()} \nCosto: ${mi_cafe.get_costo():.2f}")

print("-" * 20)

# 2. Podemos seguir decorando el objeto ya decorado.
# Ahora envolvemos el café con leche con el decorador de Chocolate.
mi_cafe = ConChocolate(mi_cafe)
print(f"Producto: {mi_cafe.get_descripcion()} \nCosto: ${mi_cafe.get_costo():.2f}")

print("-" * 20)

# 3. Y una vez más con Crema.
mi_cafe = ConCrema(mi_cafe)
print(f"Producto: {mi_cafe.get_descripcion()} \nCosto: ${mi_cafe.get_costo():.2f}")

print("\n" + "=" * 20 + "\n")

# Creando otra combinación desde cero:
# Un café simple con doble chocolate y crema.
otro_cafe = CafeSimple()
otro_cafe = ConChocolate(otro_cafe)
otro_cafe = ConChocolate(otro_cafe) # Se puede aplicar el mismo decorador varias veces
otro_cafe = ConCrema(otro_cafe)
print(f"Otro producto: {otro_cafe.get_descripcion()} \nCosto: ${otro_cafe.get_costo():.2f}")


# La gran ventaja es la flexibilidad. En lugar de crear una clase para cada
# combinación posible (`CafeConLeche`, `CafeConChocolate`, `CafeConLecheYChocolate`, etc.),
# podemos crear estas combinaciones al momento, en tiempo de ejecución.
# Esto evita una explosión de subclases.
