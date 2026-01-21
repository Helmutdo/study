# PE_2/M4/030.py

# --- Principio de Diseño: Composición sobre Herencia ---

# "Composición sobre herencia" (o "Composite Reuse Principle") es un principio de
# diseño en POO que recomienda priorizar la composición de objetos sobre la herencia
# de clases para reutilizar funcionalidades.

# - **Herencia (relación "ES UN")**: Una clase `Coche` hereda de `Vehiculo`.
#   Un coche ES UN vehículo. La herencia es una relación fuerte y estática
#   (definida en tiempo de compilación).

# - **Composición (relación "TIENE UN")**: Una clase `Coche` tiene un objeto `Motor`.
#   Un coche TIENE UN motor. La composición es más flexible, ya que las
#   partes ("tiene un") pueden ser cambiadas en tiempo de ejecución.

# --- El Problema con la Herencia Excesiva ---

# Imagina que queremos modelar diferentes tipos de empleados.

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        print(f"{self.nombre} está realizando tareas generales de empleado.")

# Ahora, algunos empleados pueden programar. Podríamos usar herencia.
class Programador(Empleado):
    def trabajar(self):
        print(f"{self.nombre} está escribiendo código.")

# Otros pueden gestionar equipos.
class Manager(Empleado):
    def trabajar(self):
        print(f"{self.nombre} está gestionando un equipo.")

# ¿Qué pasa si tenemos un "Tech Lead", que es un programador Y un manager?
# La herencia múltiple (`class TechLead(Programador, Manager):`) puede traer
# problemas (como el problema del diamante) y no es siempre la mejor solución.
# Además, ¿qué pasa si un programador es ascendido a manager? Su "tipo" (clase)
# tendría que cambiar, lo cual es complicado.

# --- Solución con Composición ---

# En lugar de que los empleados *SEAN* su rol, los empleados *TIENEN* roles o habilidades.

# 1. Definimos las "habilidades" o "comportamientos" como clases separadas.
class HabilidadDeProgramar:
    def ejecutar(self):
        return "escribiendo código."

class HabilidadDeGestionar:
    def ejecutar(self):
        return "gestionando un equipo."

class HabilidadDeProbarSoftware:
    def ejecutar(self):
        return "probando el software."

# 2. La clase principal (`EmpleadoConComposicion`) *tiene una* habilidad.
class EmpleadoConComposicion:
    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        # El empleado "tiene una" habilidad. Este es el núcleo de la composición.
        self.habilidad = habilidad

    def trabajar(self):
        # Delega la acción de "trabajar" al objeto de habilidad que posee.
        accion = self.habilidad.ejecutar()
        print(f"{self.nombre} está {accion}")

    def cambiar_habilidad(self, nueva_habilidad):
        # La flexibilidad de la composición permite cambiar el comportamiento en tiempo de ejecución.
        print(f"---{self.nombre} ha cambiado de rol. ---")
        self.habilidad = nueva_habilidad

# --- Demostración ---

# Creamos las habilidades que vamos a necesitar
habilidad_programar = HabilidadDeProgramar()
habilidad_gestionar = HabilidadDeGestionar()
habilidad_probar = HabilidadDeProbarSoftware()

print("--- Creando empleados con composición ---")
# Creamos empleados asignándoles una habilidad en el constructor.
programador = EmpleadoConComposicion("Ana", habilidad_programar)
manager = EmpleadoConComposicion("Carlos", habilidad_gestionar)

programador.trabajar()
manager.trabajar()

print("\n--- Promocionando a Ana ---")
# Ana es ascendida. En lugar de cambiar el tipo de objeto, simplemente
# cambiamos el objeto "habilidad" que contiene.
programador.cambiar_habilidad(habilidad_gestionar)
programador.trabajar()

# ¿Y el Tech Lead? Simplemente sería un empleado que tiene múltiples habilidades.
class EmpleadoConMultiplesHabilidades:
    def __init__(self, nombre, habilidades: list):
        self.nombre = nombre
        self.habilidades = habilidades

    def trabajar(self):
        print(f"{self.nombre} tiene múltiples responsabilidades:")
        for habilidad in self.habilidades:
            accion = habilidad.ejecutar()
            print(f"  - Está {accion}")

print("\n--- Creando un Tech Lead ---")
tech_lead = EmpleadoConMultiplesHabilidades("Elena", [habilidad_programar, habilidad_gestionar, habilidad_probar])
tech_lead.trabajar()


# Ventajas de la Composición:
# - **Flexibilidad**: El comportamiento se puede cambiar en tiempo de ejecución.
# - **Desacoplamiento**: Las clases son más independientes. `EmpleadoConComposicion` no
#   depende de `HabilidadDeProgramar`, solo de la interfaz que provee (el método `ejecutar`).
# - **Evita jerarquías complejas**: Previene la creación de jerarquías de herencia frágiles y profundas.
# - **Mejor modelado**: A menudo, la relación "TIENE UN" modela el mundo real de forma más precisa.
