class Triatleta:
    lista_atletas = {}

    def __init__(self):
        self.nombre = input("Ingresa el nombre del Triatleta: ")
        self.edad = int(input("Ingresa edad: "))
        self.estado = input("Ingresa tu estado físico: ")

        Triatleta.lista_atletas[self.nombre] = {
            "edad": self.edad,
            "estado": self.estado
        }

    def __str__(self):
        return (
            f"Se han ingresado {len(Triatleta.lista_atletas)} triatletas:\n"
            f"{Triatleta.lista_atletas}"
        )


atl = Triatleta()
atl1 = Triatleta()
atl2 = Triatleta()
atl3 = Triatleta()
atl4 = Triatleta()

print(Triatleta.lista_atletas)
