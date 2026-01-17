# PE_2/M4/015.py

# --- Herencia Múltiple ---

# Python permite que una clase herede de más de una clase padre.
# Esto se conoce como herencia múltiple y puede ser útil para crear clases
# que combinan funcionalidades de diferentes "familias".

# Sin embargo, debe usarse con precaución, ya que puede llevar a problemas
# como el "problema del diamante" si no se entiende bien el Orden de Resolución de Métodos (MRO).

# --- Definición de Clases Padre ---

class Radio:
    def __init__(self, banda="FM"):
        self.banda = banda
        self.frecuencia = 87.5  # Frecuencia inicial
        print("Radio inicializada.")

    def sintonizar(self, frecuencia):
        self.frecuencia = frecuencia
        print(f"Sintonizando la banda {self.banda} en la frecuencia {self.frecuencia} MHz.")

class ReproductorCD:
    def __init__(self, capacidad_cds=1):
        self.capacidad_cds = capacidad_cds
        self.cd_cargado = False
        print("Reproductor de CD inicializado.")

    def cargar_cd(self):
        self.cd_cargado = True
        print("CD cargado en el reproductor.")

    def reproducir_cd(self):
        if self.cd_cargado:
            print("Reproduciendo música desde el CD...")
        else:
            print("No hay ningún CD cargado.")

# --- Clase Hija con Herencia Múltiple ---

# Para heredar de varias clases, las listamos separadas por comas.
class EquipoDeMusica(Radio, ReproductorCD):

    def __init__(self, banda, capacidad_cds, marca):
        # Al usar herencia múltiple, es importante llamar a los constructores
        # de cada clase padre para asegurar que todas se inicialicen correctamente.
        Radio.__init__(self, banda)
        ReproductorCD.__init__(self, capacidad_cds)
        self.marca = marca # Atributo propio de la clase hija
        print(f"Equipo de música marca '{self.marca}' creado.")


# --- Uso de la Clase Combinada ---

mi_equipo = EquipoDeMusica(banda="AM/FM", capacidad_cds=5, marca="Sony")

print("-" * 20)

# Podemos usar métodos de la clase Radio
mi_equipo.sintonizar(101.3)
print(f"Banda del equipo: {mi_equipo.banda}")

print("-" * 20)

# Y también podemos usar métodos de la clase ReproductorCD
print(f"¿Hay un CD cargado? {'Sí' if mi_equipo.cd_cargado else 'No'}")
mi_equipo.cargar_cd()
mi_equipo.reproducir_cd()
print(f"Capacidad de CDs: {mi_equipo.capacidad_cds}")


# --- Orden de Resolución de Métodos (MRO) ---
# Si ambas clases padre tuvieran un método con el mismo nombre, Python
# seguiría un orden específico para decidir cuál ejecutar.
# Este orden se puede consultar con el atributo __mro__ o la función help().

# El MRO para EquipoDeMusica será:
# EquipoDeMusica -> Radio -> ReproductorCD -> object
# Esto significa que si un método existe en Radio y en ReproductorCD, se usará el de Radio.
print("\nOrden de Resolución de Métodos (MRO) para EquipoDeMusica:")
print(EquipoDeMusica.__mro__)
