# PE_2/M4/014.py

# La herencia es un pilar fundamental de la POO que permite a una clase (hija)
# heredar atributos y métodos de otra clase (padre).
# Esto promueve la reutilización de código y establece una relación "es un" entre clases.

# --- Clase Padre (Superclase) ---

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_movimiento = False

    def iniciar_movimiento(self):
        if not self.en_movimiento:
            self.en_movimiento = True
            print(f"El vehículo {self.marca} {self.modelo} ha iniciado su movimiento.")
        else:
            print("El vehículo ya está en movimiento.")

    def detener_movimiento(self):
        if self.en_movimiento:
            self.en_movimiento = False
            print(f"El vehículo {self.marca} {self.modelo} se ha detenido.")
        else:
            print("El vehículo ya está detenido.")

# --- Clase Hija (Subclase) ---

# Para indicar que una clase hereda de otra, se pone el nombre de la clase padre entre paréntesis.
class Coche(Vehiculo):
    # La clase Coche hereda __init__, iniciar_movimiento y detener_movimiento de Vehiculo.

    def __init__(self, marca, modelo, numero_puertas):
        # Para inicializar los atributos de la clase padre, usamos super().__init__().
        # super() nos da una referencia a la clase padre (Vehiculo).
        super().__init__(marca, modelo)
        # Atributo específico de la clase Coche
        self.numero_puertas = numero_puertas

    # Método específico de la clase Coche
    def tocar_bocina(self):
        print("¡Pip, pip!")
        
    # --- Sobrescritura de Métodos (Overriding) ---
    # Podemos modificar un método heredado para que se comporte de manera diferente en la clase hija.
    def iniciar_movimiento(self):
        # Podemos llamar al método original del padre si es necesario.
        super().iniciar_movimiento()
        # Y luego añadir la nueva funcionalidad.
        print(f"El coche {self.marca} {self.modelo} acelera por la carretera.")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo # Ej: "Deportiva", "Urbana" 

    def hacer_wheelie(self):
        print("¡La motocicleta hace un caballito!")


# --- Uso de las Clases ---

mi_coche = Coche("Renault", "Clio", 5)
mi_moto = Motocicleta("Harley-Davidson", "Street 750", "Cruiser")

# El objeto mi_coche tiene acceso a métodos de Vehiculo y de Coche
mi_coche.iniciar_movimiento()   # Llama al método sobrescrito en Coche
mi_coche.tocar_bocina()        # Llama al método propio de Coche
mi_coche.detener_movimiento()  # Llama al método heredado de Vehiculo

print("-" * 20)

# El objeto mi_moto tiene acceso a métodos de Vehiculo y de Motocicleta
mi_moto.iniciar_movimiento()   # Llama al método original de Vehiculo
mi_moto.hacer_wheelie()      # Llama al método propio de Motocicleta
mi_moto.detener_movimiento() # Llama al método heredado de Vehiculo

# La función isinstance() nos permite verificar si un objeto es una instancia de una clase particular,
# incluyendo sus clases padre.
print(f"\n¿Es mi_coche una instancia de Coche? {isinstance(mi_coche, Coche)}") # True
print(f"¿Es mi_coche una instancia de Vehiculo? {isinstance(mi_coche, Vehiculo)}") # True
print(f"¿Es mi_coche una instancia de Motocicleta? {isinstance(mi_coche, Motocicleta)}") # False
