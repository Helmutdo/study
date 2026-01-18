

# PE_2/M4/019.py

# --- Métodos de Clase (@classmethod) ---

# Un método de clase es un método que está ligado a la clase y no a la instancia (objeto).
# Recibe la clase misma como primer argumento, por convención llamado `cls`.

# A diferencia de los métodos estáticos, los métodos de clase SÍ tienen acceso a la clase.
# Esto les permite trabajar con atributos de la clase o llamar a otros métodos de la clase.

# Son muy utilizados para crear "factory methods" (métodos fábrica), que son métodos
# que devuelven instancias de la clase, pero construidas de una manera alternativa.

class Persona:
    # Atributo de clase: es compartido por todas las instancias de la clase.
    planeta = "Tierra"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años."

    # Un método de instancia normal.
    def es_mayor_de_edad(self):
        return self.edad >= 18

    # Para definir un método de clase, usamos el decorador @classmethod.
    # El primer argumento es `cls`, que representa a la clase (en este caso, Persona).
    @classmethod
    def get_planeta(cls):
        """Devuelve el valor del atributo de clase 'planeta'."""
        # A través de `cls`, podemos acceder a los atributos de la clase.
        return cls.planeta

    # --- Factory Method ---
    # Este método de clase crea una instancia de Persona a partir de un año de nacimiento.
    # Es una alternativa al constructor __init__ normal.
    @classmethod
    def desde_anio_nacimiento(cls, nombre, anio_nacimiento):
        """
        Crea una instancia de Persona calculando la edad a partir del año de nacimiento.
        """
        from datetime import date
        anio_actual = date.today().year
        edad = anio_actual - anio_nacimiento
        # `cls(nombre, edad)` es lo mismo que `Persona(nombre, edad)`.
        # Usar `cls` es preferible porque si la clase es heredada, `cls` se referirá
        # a la subclase, haciendo el factory method más flexible.
        return cls(nombre, edad)


# --- Uso de Métodos de Clase ---

# Podemos llamar al método de clase directamente desde la clase.
print(f"Todas las personas viven en el planeta {Persona.get_planeta()}.")

# --- Uso del Factory Method ---

# Creamos una instancia de la forma tradicional.
persona_1 = Persona("Ana", 30)
print(persona_1)

# Creamos otra instancia usando nuestro nuevo método de clase "fábrica".
# No necesitamos calcular la edad nosotros mismos.
persona_2 = Persona.desde_anio_nacimiento("Carlos", 1990)
print(persona_2)


# --- Herencia y Métodos de Clase ---

class Empleado(Persona):
    # Atributo de clase propio de Empleado
    rol = "Empleado"

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    
    # Sobrescribimos __str__
    def __str__(self):
        return f"Empleado {self.nombre}, {self.edad} años, salario: ${self.salario}"

    @classmethod
    def get_rol(cls):
        return cls.rol


# El factory method `desde_anio_nacimiento` fue heredado por Empleado.
# Cuando lo llamamos desde `Empleado`, `cls` dentro del método será la clase `Empleado`.
# PERO, `Empleado.__init__` espera un argumento `salario` que `Persona.desde_anio_nacimiento` no provee.
# Esto causaría un error.

# Para solucionarlo, podemos sobrescribir el factory method en la clase hija.
class EmpleadoMejorado(Persona):
    rol = "Empleado"
    
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def __str__(self):
        return f"Empleado {self.nombre}, {self.edad} años, salario: ${self.salario}"
    
    @classmethod
    def desde_anio_nacimiento(cls, nombre, anio_nacimiento, salario):
        # Reutilizamos la lógica del padre para calcular la edad
        persona_temporal = super().desde_anio_nacimiento(nombre, anio_nacimiento)
        # Y creamos la instancia de la clase hija con el nuevo atributo
        return cls(persona_temporal.nombre, persona_temporal.edad, salario)


print("\n--- Herencia con Factory Methods ---")
empleado = EmpleadoMejorado.desde_anio_nacimiento("Elena", 1985, 50000)
print(empleado)
print(f"¿El objeto es una instancia de EmpleadoMejorado? {isinstance(empleado, EmpleadoMejorado)}")
print(f"¿El objeto es una instancia de Persona? {isinstance(empleado, Persona)}")

# En resumen:
# - @staticmethod: Función normal agrupada en una clase. No sabe nada de la clase o la instancia.
# - @classmethod: Ligado a la clase. Recibe `cls`. Útil para factory methods y operar sobre atributos de clase.
# - Método de instancia: El más común. Ligado al objeto. Recibe `self` y opera sobre el estado del objeto.
