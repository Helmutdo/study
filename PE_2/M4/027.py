# PE_2/M4/027.py

# --- Patrones de Diseño: Patrón Fábrica (Factory Pattern) ---

# El Patrón Fábrica es un patrón creacional que proporciona una interfaz
# para crear objetos en una superclase, pero permite a las subclases
# alterar el tipo de objetos que se crearán.

# Esencialmente, encapsula la lógica de creación de objetos. En lugar de
# llamar directamente al constructor de una clase (ej: `Coche()`, `Bicicleta()`),
# llamas a un método "fábrica" y le dices qué tipo de objeto quieres.

# Ventajas:
# - Desacopla el código cliente de las clases concretas que se están instanciando.
#   El cliente solo necesita saber qué "pedir" a la fábrica, no cómo construirlo.
# - Facilita la adición de nuevos tipos de productos sin modificar el código cliente.
#   Solo necesitas actualizar la fábrica.
# - Centraliza la lógica de creación, lo que hace el código más mantenible.

from abc import ABC, abstractmethod

# --- 1. La Interfaz del Producto ---
# Define la interfaz común para todos los objetos que la fábrica puede crear.

class MedioDeTransporte(ABC):
    @abstractmethod
    def entregar(self, paquete):
        """Define la acción que todos los medios de transporte deben poder hacer."""
        pass

# --- 2. Los Productos Concretos ---
# Son las implementaciones de la interfaz del producto.

class Camion(MedioDeTransporte):
    def entregar(self, paquete):
        print(f"Entregando el paquete '{paquete}' por tierra en un camión.")

class Barco(MedioDeTransporte):
    def entregar(self, paquete):
        print(f"Entregando el paquete '{paquete}' por mar en un barco.")

class Avion(MedioDeTransporte):
    def entregar(self, paquete):
        print(f"Entregando el paquete '{paquete}' por aire en un avión.")

# --- 3. La Fábrica (Factory) ---
# Contiene el método que crea y devuelve los objetos.

class FabricaDeTransporte:
    def crear_transporte(self, tipo_transporte):
        """
        Este es el método fábrica. Recibe un identificador y devuelve
        la instancia del objeto correspondiente.
        """
        if tipo_transporte == 'tierra':
            return Camion()
        elif tipo_transporte == 'mar':
            return Barco()
        elif tipo_transporte == 'aire':
            return Avion()
        else:
            raise ValueError(f"Tipo de transporte desconocido: {tipo_transporte}")


# --- 4. El Código Cliente ---
# El cliente usa la fábrica para obtener los objetos que necesita, sin
# preocuparse por los detalles de su creación.

def gestionar_envio(tipo_envio, paquete):
    # El cliente no sabe si recibirá un Camion, Barco o Avion.
    # Solo sabe que recibirá un objeto que tiene un método `entregar`.
    fabrica = FabricaDeTransporte()
    transporte = fabrica.crear_transporte(tipo_envio)
    
    # Gracias a la interfaz común, podemos usar el método `entregar` con confianza.
    transporte.entregar(paquete)


# --- Demostración ---
print("--- Gestión de envíos usando la fábrica ---")
gestionar_envio('tierra', "Caja de herramientas")
gestionar_envio('mar', "Contenedor de coches")
gestionar_envio('aire', "Documentos urgentes")

print("\n--- ¿Qué pasa si añadimos un nuevo tipo de transporte? ---")
# Por ejemplo, un Dron.
class Dron(MedioDeTransporte):
    def entregar(self, paquete):
        print(f"Entregando el paquete '{paquete}' con un dron autónomo.")

# Solo necesitamos modificar la fábrica para que lo conozca.
# El código cliente (`gestionar_envio`) no necesita ningún cambio.
class FabricaDeTransporteMejorada:
    def crear_transporte(self, tipo_transporte):
        transportes = {
            'tierra': Camion,
            'mar': Barco,
            'aire': Avion,
            'dron': Dron # Nueva opción
        }
        clase_a_crear = transportes.get(tipo_transporte)
        if clase_a_crear:
            return clase_a_crear()
        raise ValueError(f"Tipo de transporte desconocido: {tipo_transporte}")

# Función cliente actualizada para usar la nueva fábrica
def gestionar_envio_mejorado(tipo_envio, paquete):
    fabrica = FabricaDeTransporteMejorada()
    transporte = fabrica.crear_transporte(tipo_envio)
    transporte.entregar(paquete)

print("Probando el nuevo tipo de transporte:")
gestionar_envio_mejorado('dron', "Paquete pequeño")
