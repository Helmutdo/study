

# PE_2/M4/020.py

# --- El decorador @property: Getters, Setters y Deleters ---

# El decorador @property nos permite tratar un método de una clase como si fuera un atributo.
# Esto es útil para:
# 1.  **Getters**: Exponer un atributo "calculado" o "derivado" que parece un atributo normal.
# 2.  **Setters**: Controlar la asignación de valor a un atributo, permitiendo validaciones.
# 3.  **Deleters**: Definir una acción personalizada cuando se intenta borrar un atributo.

# Esto se considera más "pythónico" que crear métodos explícitos como get_nombre() o set_nombre().

class Empleado:
    def __init__(self, nombre, apellido, salario_mensual):
        self.nombre = nombre
        self.apellido = apellido
        # Usamos un guión bajo para el atributo "real" que almacena el salario.
        # Es una convención para indicar que no debe ser modificado directamente.
        self._salario_mensual = salario_mensual

    # --- Getter con @property ---
    # Este método se comporta como un atributo de solo lectura.
    # Podemos acceder a `empleado.email` como si fuera una variable.
    @property
    def email(self):
        """Genera el email del empleado a partir del nombre y apellido."""
        return f"{self.nombre.lower()}.{self.apellido.lower()}@empresa.com"

    # Este es otro getter para el nombre completo.
    @property
    def nombre_completo(self):
        """Devuelve el nombre completo del empleado."""
        return f"{self.nombre} {self.apellido}"

    # --- Setter para nombre_completo ---
    # Para crear un "setter" para una property, usamos @<nombre_property>.setter
    @nombre_completo.setter
    def nombre_completo(self, nuevo_nombre):
        """Permite cambiar el nombre y apellido a partir de un nombre completo."""
        try:
            nombre, apellido = nuevo_nombre.split(' ')
            self.nombre = nombre
            self.apellido = apellido
            print(f"El nombre se ha actualizado a: {self.nombre} {self.apellido}")
        except ValueError:
            print("Error: Por favor, proporciona el nombre y el apellido separados por un espacio.")

    # --- Deleter para nombre_completo ---
    # Se usa @<nombre_property>.deleter para definir qué pasa si se usa `del`.
    @nombre_completo.deleter
    def nombre_completo(self):
        """Acción a realizar al intentar borrar el nombre completo."""
        print("¡Borrando nombre y apellido!")
        self.nombre = None
        self.apellido = None


# --- Uso de @property ---

emp = Empleado("Juan", "Pérez", 5000)

# 1. Usando el "getter" como un atributo
# No se usan paréntesis, se accede como si fuera una variable.
print(f"Nombre: {emp.nombre_completo}")  # Salida: Juan Pérez
print(f"Email: {emp.email}")            # Salida: juan.perez@empresa.com

# 2. Usando el "setter"
# La asignación `emp.nombre_completo = ...` llama al método setter.
print("\n--- Actualizando nombre ---")
emp.nombre_completo = "Carlos Sánchez"

# El email se actualiza automáticamente porque depende de nombre y apellido.
print(f"Nuevo nombre: {emp.nombre_completo}") # Salida: Carlos Sánchez
print(f"Nuevo email: {emp.email}")           # Salida: carlos.sanchez@empresa.com

# Intentando una asignación inválida
emp.nombre_completo = "Ana" # Salida: Error: Por favor, proporciona el nombre y el apellido...

# 3. Usando el "deleter"
# La instrucción `del emp.nombre_completo` llama al método deleter.
print("\n--- Borrando nombre ---")
del emp.nombre_completo # Salida: ¡Borrando nombre y apellido!

print(f"Nombre después de borrar: {emp.nombre}")     # Salida: None
print(f"Apellido después de borrar: {emp.apellido}") # Salida: None


# Beneficios de @property:
# - **API Limpia**: Permite acceder a los métodos como si fueran atributos.
# - **Flexibilidad**: Puedes empezar con un atributo público simple y luego, si necesitas
#   añadir lógica (como validación), puedes convertirlo en una property sin cambiar
#   la forma en que se accede a él desde fuera de la clase.
