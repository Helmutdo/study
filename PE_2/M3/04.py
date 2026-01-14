class Triatleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nado = 0
        self.ciclismo = 0
        self.trote = 0

    def registrar_nado(self):
        self.nado = float(input(f"{self.nombre}, ¿cuál es tu récord nadando (m)? "))

    def registrar_ciclismo(self):
        self.ciclismo = float(input(f"{self.nombre}, ¿distancia máxima en bici (km)? "))

    def registrar_trote(self):
        self.trote = float(input(f"{self.nombre}, ¿distancia máxima corriendo (km)? "))

    def mostrar_marcas(self):
        print(f"\n{self.nombre} - Marcas personales:")
        print(f"  Natación   → {self.nado:6.1f} m")
        print(f"  Ciclismo   → {self.ciclismo:6.1f} km")
        print(f"  Carrera    → {self.trote:6.1f} km\n")

    def __str__(self):
        return f"Triatleta {self.nombre} (nado:{self.nado}m, bici:{self.ciclismo}km, trote:{self.trote}km)"


# Ejemplo de uso
atleta = Triatleta("Helmut")
atleta.mostrar_marcas()           # valores iniciales

atleta.registrar_nado()
atleta.registrar_ciclismo()
atleta.registrar_trote()

atleta.mostrar_marcas()           # valores actualizados
print(atleta)                     # versión corta