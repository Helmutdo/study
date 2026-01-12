class Triatleta:
    def __init__(self, nombre, nado=0, ciclismo=0, trote=0):
        self.nombre = nombre          
        self.nado = nado
        self.ciclismo = ciclismo
        self.trote = trote

    def preguntar_datos(self):
        """Pregunta TODOS los récords de una vez"""
        print(f"\nHola {self.nombre}! Vamos a registrar tus marcas personales:")
        self.nado = float(input("Récord nadando (metros): "))
        self.ciclismo = float(input("Distancia máxima en bici (km): "))
        self.trote = float(input("Distancia máxima corriendo (km): "))
        print("¡Datos guardados! ✅\n")

    def __str__(self):
        return (f"Triatleta: {self.nombre}\n"
                f"  🏊  Natación : {self.nado} m\n"
                f"  🚴  Ciclismo : {self.ciclismo} km\n"
                f"  🏃  Carrera  : {self.trote} km")


# Uso
helmut = Triatleta("Helmut")
print(helmut)          # muestra valores iniciales (0)

helmut.preguntar_datos()     # ← aquí está la interacción
print(helmut)          # muestra los valores actualizados