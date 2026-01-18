

# PE_2/M4/023.py

# --- `__slots__`: Optimización de Memoria y Atributos ---

# Por defecto, Python utiliza un diccionario (`__dict__`) para almacenar los atributos de cada objeto.
# Esto es muy flexible, ya que nos permite añadir nuevos atributos a un objeto en cualquier momento.

class PuntoNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = PuntoNormal(10, 20)
print(f"Atributos de p1: {p1.__dict__}") # Salida: {'x': 10, 'y': 20}
# Podemos añadir atributos dinámicamente
p1.z = 30
print(f"Atributos de p1 después de añadir 'z': {p1.__dict__}") # Salida: {'x': 10, 'y': 20, 'z': 30}


# El problema es que los diccionarios consumen una cantidad de memoria considerable.
# Si vas a crear miles o millones de objetos de una clase con pocos atributos,
# este consumo de memoria puede convertirse en un problema.

# --- Usando `__slots__` ---

# `__slots__` es un atributo especial de clase que nos permite definir explícitamente
# los atributos que un objeto tendrá. Al hacerlo, Python no usará `__dict__`
# para cada instancia, sino que reservará un espacio fijo en memoria para esos atributos.

class PuntoConSlots:
    # Se define una tupla con los nombres de los atributos permitidos.
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = PuntoConSlots(10, 20)
print(f"\nValor de p2.x: {p2.x}")

# 1. Ahorro de memoria:
# La instancia `p2` ocupa significativamente menos memoria que `p1`.
# Esta es la principal razón para usar `__slots__`.

# 2. No más `__dict__`:
# Las instancias de clases con `__slots__` no tienen un `__dict__` por defecto.
# try:
#     print(p2.__dict__)
# except AttributeError as e:
#     print(f"Error esperado al acceder a __dict__: {e}")

# 3. No se pueden añadir nuevos atributos:
# `__slots__` "congela" la estructura del objeto. Intentar añadir un atributo
# que no esté en `__slots__` lanzará un AttributeError.
# try:
#     p2.z = 30
# except AttributeError as e:
#     print(f"Error esperado al añadir un atributo: {e}")


# --- Comparación de Memoria ---
import sys

p_normal = PuntoNormal(1, 2)
p_slots = PuntoConSlots(1, 2)

# getsizeof no siempre es preciso para objetos complejos, pero da una idea.
memoria_normal = sys.getsizeof(p_normal) + sys.getsizeof(p_normal.__dict__)
memoria_slots = sys.getsizeof(p_slots)

print(f"\nTamaño en memoria de PuntoNormal (aprox): {memoria_normal} bytes")
print(f"Tamaño en memoria de PuntoConSlots (aprox): {memoria_slots} bytes")


# --- Desventajas y Consideraciones ---

# - **Herencia**: Si una clase hija quiere añadir más atributos, también debe definir
#   `__slots__`. Si una clase padre no tiene `__slots__`, la hija sí tendrá `__dict__`
#   y no se obtendrá el beneficio de memoria completo.

# - **Incompatibilidad**: Algunas librerías pueden requerir que los objetos tengan `__dict__`.

# - **Menos flexible**: Se pierde la capacidad de añadir atributos dinámicamente,
#   lo cual es una característica muy útil de Python en muchos contextos.


# En resumen, `__slots__` es una herramienta de optimización.
# No debe usarse por defecto, sino solo cuando se ha identificado que el consumo
# de memoria de un gran número de objetos es un cuello de botella en la aplicación.

