# PE_2/M4/024.py

# --- Descriptores: Control Avanzado de Atributos ---

# Un descriptor es un objeto que personaliza el acceso a un atributo en otra clase.
# Permiten "enganchar" lógica que se ejecuta automáticamente cuando se accede,
# se asigna o se borra un atributo.

# Son una de las características más avanzadas y potentes de la POO en Python.
# De hecho, características como @property, @staticmethod y @classmethod
# se implementan internamente usando descriptores.

# --- ¿Cómo funciona un descriptor? ---
# Un objeto es un descriptor si implementa alguno de los siguientes métodos:
#   - `__get__(self, instance, owner)`: para obtener el valor del atributo.
#   - `__set__(self, instance, value)`: para asignar un valor al atributo.
#   - `__delete__(self, instance)`: para borrar el atributo.

# --- Ejemplo: Validador de Tipo ---
# Crearemos un descriptor que asegura que un atributo solo puede aceptar valores de un tipo específico.

class Typed:
    def __init__(self, name, expected_type):
        self.name = name  # Nombre del atributo en la clase que lo usa
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Obtenemos el valor del diccionario de la instancia para evitar recursión infinita
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Se esperaba un valor de tipo {self.expected_type}, pero se recibió {type(value)}")
        # Guardamos el valor en el diccionario de la instancia
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]

# --- Usando el Descriptor ---

class Persona:
    # Creamos instancias del descriptor como atributos de clase.
    # Cuando se accede a `persona.nombre`, Python detecta que `nombre` es un descriptor
    # y llama a su método `__get__` o `__set__` en su lugar.
    nombre = Typed("nombre", str)
    edad = Typed("edad", int)
    salario = Typed("salario", (int, float)) # Puede ser int o float

    def __init__(self, nombre, edad, salario):
        # La asignación aquí dispara el método __set__ del descriptor
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

# --- Pruebas de funcionamiento ---


print("Creando una instancia válida:")
p = Persona("Ana", 30, 50000.0)
print(f"Nombre: {p.nombre}, Edad: {p.edad}, Salario: {p.salario}")

# Acceder al atributo llama a __get__
print(f"\nEl nombre es {p.nombre}")

# Asignar un valor llama a __set__
p.edad = 31
print(f"La nueva edad es {p.edad}")

# --- Provocando errores de tipo ---

print("\n--- Intentando asignaciones inválidas ---")
try:
    p.nombre = 123
except TypeError as e:
    print(f"Error al asignar nombre: {e}")

try:
    p.edad = "cuarenta"
except TypeError as e:
    print(f"Error al asignar edad: {e}")

try:
    # El salario no puede ser un string
    p.salario = "mucho dinero"
except TypeError as e:
    print(f"Error al asignar salario: {e}")


# Este es un ejemplo simplificado. Los descriptores pueden ser mucho más complejos,
# gestionando conexiones a bases de datos, caching de valores, etc.

# La clave es entender que los descriptores nos dan un control muy fino sobre
# lo que ocurre cuando interactuamos con los atributos de un objeto, permitiendo
# crear código reutilizable y robusto para la gestión de atributos.
# El decorador @property es, en esencia, una forma fácil y rápida de crear un descriptor
