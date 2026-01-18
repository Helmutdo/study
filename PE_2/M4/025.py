
# PE_2/M4/025.py

# --- Metaclases: Las Clases que Crean Clases ---

# Este es uno de los conceptos más avanzados de Python. Si los descriptores son
# para controlar el acceso a atributos, las metaclases son para controlar la
# creación de las propias clases.

# En Python, todo es un objeto. Las clases también son objetos.
# ¿Y quién crea a esos objetos "clase"? Las metaclases.
# La metaclase por defecto en Python es `type`.

class MiClase:
    pass

# `type(MiClase)` nos dice quién creó a MiClase
print(f"La clase 'MiClase' es un objeto de tipo: {type(MiClase)}") # Salida: <class 'type'>

# Podemos crear clases dinámicamente usando `type` directamente.
# type('NombreClase', (ClasesPadre,), {diccionario de atributos})
MiClaseDinamica = type('MiClaseDinamica', (), {'x': 100})
instancia = MiClaseDinamica()
print(f"Atributo 'x' de la clase dinámica: {instancia.x}")


# --- Creando nuestra propia Metaclase ---
# Una metaclase personalizada nos permite interceptar el proceso de creación de una clase
# para modificarla o validarla. Para ello, creamos una clase que hereda de `type`.

# Ejemplo: Una metaclase que obliga a que todas las clases que la usen
# tengan docstrings (cadenas de documentación).

class MetaForzarDocstrings(type):
    # El método __new__ de una metaclase se ejecuta ANTES de que la clase sea creada.
    # Recibe:
    # - cls: la propia metaclase (MetaForzarDocstrings)
    # - name: el nombre de la clase que se está creando (ej: "ClaseDePrueba")
    # - bases: una tupla con las clases padre
    # - attrs: un diccionario con todos los atributos y métodos de la nueva clase
    def __new__(cls, name, bases, attrs):
        print(f"\n--- Metaclase {cls.__name__} creando la clase '{name}' ---")

        # Verificamos si la clase en sí tiene un docstring
        if not attrs.get('__doc__'):
            raise TypeError(f"La clase '{name}' debe tener un docstring.")

        # Verificamos si cada método tiene un docstring
        for nombre_attr, valor_attr in attrs.items():
            if callable(valor_attr): # Si es una función/método
                if not getattr(valor_attr, '__doc__'):
                    raise TypeError(f"El método '{nombre_attr}' de la clase '{name}' debe tener un docstring.")
        
        # Si todo está bien, llamamos al __new__ de la metaclase padre (`type`)
        # para que proceda con la creación normal de la clase.
        return super().__new__(cls, name, bases, attrs)

# --- Usando la Metaclase ---
# Para usar una metaclase, la especificamos en la definición de la clase.

print("Intentando crear una clase que cumple con la metaclase:")
class ClaseCorrecta(metaclass=MetaForzarDocstrings):
    """Esta es una clase de ejemplo que sigue las reglas."""
    
    def mi_metodo(self):
        """Este método está bien documentado."""
        pass

print("Clase 'ClaseCorrecta' creada con éxito.")


print("\nIntentando crear una clase SIN docstring:")
try:
    class ClaseSinDocstring(metaclass=MetaForzarDocstrings):
        # Falta el docstring de la clase
        def metodo_valido(self):
            """Docstring válido."""
            pass
except TypeError as e:
    print(f"Error esperado: {e}")


print("\nIntentando crear una clase con un método SIN docstring:")
try:
    class ClaseConMetodoSinDocstring(metaclass=MetaForzarDocstrings):
        """Docstring de clase válido."""
        
        def metodo_sin_docstring(self):
            # A este método le falta su docstring
            pass
except TypeError as e:
    print(f"Error esperado: {e}")


# ¿Cuándo usar metaclases?
# Son una herramienta muy poderosa, pero también compleja y que puede hacer el código
# difícil de entender. La mayoría de las veces, NO necesitas una metaclase.
# 
# Se usan principalmente en:
# - **Frameworks y ORMs**: Como Django o SQLAlchemy, para crear APIs declarativas
#   y convertir definiciones de clases en comportamientos complejos (ej: mapear una clase a una tabla de BD).
# - **Validación de APIs**: Para asegurar que las clases que extienden un framework
#   cumplan con un contrato estricto.
# - **Registros automáticos**: Para registrar clases automáticamente en un sistema
#   cuando son definidas.
#
# En muchos casos, los decoradores de clase o las ABCs son una solución más simple y legible.
# La famosa cita de Tim Peters: "Las metaclases son magia negra y el 99% de los usuarios
# no deberían preocuparse por ellas. Si te preguntas si necesitas una, probablemente no."