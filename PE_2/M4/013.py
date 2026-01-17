
# PE_2/M4/013.py

# Las clases son plantillas para crear objetos. 
# Definen un conjunto de atributos y métodos que los objetos de esa clase tendrán.

# En Python, todo es un objeto. Las clases nos permiten crear nuestros propios tipos de objetos.

class Coche:
    # El método __init__ es el constructor de la clase. Se llama automáticamente cuando se crea un nuevo objeto.
    # 'self' se refiere a la instancia actual del objeto y se usa para acceder a sus atributos y métodos.
    def __init__(self, marca, modelo, anio):
        # Los atributos son variables que pertenecen a un objeto.
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False  # Atributo con valor inicial por defecto

    # Los métodos son funciones que pertenecen a una clase.
    def arrancar(self):
        """Este método cambia el estado del coche a encendido."""
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El coche ya está en marcha.")

    def apagar(self):
        """Este método cambia el estado del coche a apagado."""
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El coche ya está apagado.")

    def descripcion(self):
        """Devuelve una descripción del coche."""
        estado = "encendido" if self.encendido else "apagado"
        return f"Coche: {self.marca} {self.modelo} del año {self.anio}. Estado: {estado}."

# --- Creación de Objetos (Instanciación) ---

# Para crear un objeto de una clase, llamamos a la clase como si fuera una función,
# pasando los argumentos requeridos por el constructor __init__.

mi_coche = Coche("Toyota", "Corolla", 2021)
coche_de_ana = Coche("Ford", "Mustang", 1968)

# --- Uso de Atributos y Métodos ---

# Accedemos a los atributos y métodos de un objeto usando la notación de punto (.).
print(mi_coche.marca)  # Salida: Toyota
print(coche_de_ana.modelo)  # Salida: Mustang

print(mi_coche.descripcion())  # Salida: Coche: Toyota Corolla del año 2021. Estado: apagado.

mi_coche.arrancar()  # Salida: El Toyota Corolla ha arrancado.
print(mi_coche.descripcion())  # Salida: Coche: Toyota Corolla del año 2021. Estado: encendido.

coche_de_ana.arrancar() # Salida: El Ford Mustang ha arrancado.

# Podemos modificar los atributos de un objeto directamente.
mi_coche.anio = 2022
print(f"El año de mi coche ha sido actualizado a {mi_coche.anio}.")
