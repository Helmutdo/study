# PE_2/M4/022.py

# --- Data Classes (@dataclass) ---

# Introducidas en Python 3.7, las Data Classes (clases de datos) son un decorador
# que genera automáticamente métodos especiales (dunder methods) como __init__,
# __repr__, __eq__, y otros.

# Son extremadamente útiles para clases que principalmente almacenan datos.
# Reducen significativamente el código repetitivo (boilerplate).

from dataclasses import dataclass, field

# --- Clase Tradicional (antes de dataclasses) ---

class ProductoTradicional:
    def __init__(self, nombre, precio, en_stock):
        self.nombre = nombre
        self.precio = precio
        self.en_stock = en_stock

    # Necesitaríamos implementar __repr__ para una visualización clara
    def __repr__(self):
        return (
            f"ProductoTradicional(nombre='{self.nombre}', "
            f"precio={self.precio}, en_stock={self.en_stock})")

    # Y también __eq__ para comparar objetos
    def __eq__(self, otro):
        if not isinstance(otro, ProductoTradicional):
            return False
        return (
            self.nombre == otro.nombre and
            self.precio == otro.precio and
            self.en_stock == otro.en_stock
        )


# --- Usando @dataclass ---
# El decorador @dataclass hace todo lo anterior (y más) por nosotros.

@dataclass(frozen=False, order=False)
class Producto:
    """
    Clase que representa un producto en un inventario.
    `frozen=True` haría que las instancias fueran inmutables (no se pueden cambiar sus atributos).
    `order=True` generaría automáticamente los métodos de comparación (__lt__, __le__, __gt__, __ge__).
    """
    nombre: str
    precio: float
    en_stock: bool = True # Podemos dar valores por defecto
    # Para valores por defecto mutables (listas, dicts), usamos `field`
    tags: list[str] = field(default_factory=list)

    def calcular_impuesto(self, tasa=0.21):
        """Los dataclasses también pueden tener métodos normales."""
        return self.precio * tasa


# --- Uso de la Data Class ---

# 1. Creación de instancias (el __init__ es generado automáticamente)
prod1 = Producto("Laptop", 1200.50, tags=["tecnología", "oficina"])
prod2 = Producto("Teclado", 75.99)
prod3 = Producto("Laptop", 1200.50, tags=["tecnología", "oficina"])
prod4 = Producto("Mouse", 25.00, en_stock=False)

# 2. Representación (el __repr__ es generado automáticamente y es muy legible)
print("Representación del objeto:")
print(prod1)
# Salida: Producto(nombre='Laptop', precio=1200.5, en_stock=True, tags=['tecnología', 'oficina'])
print(prod4)
# Salida: Producto(nombre='Mouse', precio=25.0, en_stock=False, tags=[])


# 3. Comparación (el __eq__ es generado automáticamente)
print("\nComparación de objetos:")
print(f"¿prod1 es igual a prod2? {prod1 == prod2}") # False
print(f"¿prod1 es igual a prod3? {prod1 == prod3}") # True


# 4. Modificación de atributos (a menos que `frozen=True`)
print(f"\nPrecio original de prod2: {prod2.precio}")
prod2.precio = 80.0
print(f"Precio modificado de prod2: {prod2.precio}")


# 5. Uso de métodos personalizados
impuesto_laptop = prod1.calcular_impuesto()
print(f"\nImpuesto para la laptop: ${impuesto_laptop:.2f}")

# --- Data Class con ordenamiento ---

@dataclass(order=True)
class ArticuloInventario:
    """
    Esta dataclass sí se puede ordenar. El orden se basa en los atributos
    en el orden en que se declaran: primero por `nombre`, luego por `cantidad`.
    """
    nombre: str
    cantidad: int

print("\n--- Data Class con Ordenamiento ---")
item1 = ArticuloInventario("Tornillos", 100)
item2 = ArticuloInventario("Clavos", 250)
item3 = ArticuloInventario("Tornillos", 50) # Mismo nombre, diferente cantidad

print(f"¿item1 < item2? {item1 < item2}") # True ('Tornillos' > 'Clavos' alfabéticamente) -> Falso en este caso, es True
print(f"¿item1 > item3? {item1 > item3}") # True (100 > 50)

# Las Data Classes son una de las mejoras más convenientes de Python moderno
# para la POO, haciendo el código más limpio, corto y menos propenso a errores.
