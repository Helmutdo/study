class Triatleta:
    def __init__(self, nombre="", nado=0, ciclismo=0, trote=0):
        self.__nombre = nombre
        self.__nado = nado
        self.__ciclismo = ciclismo
        self.__trote = trote

    def ingresar_nombre(self):
        self.__nombre = input("Ingresa tu nombre: ")

    def ingresar_nado(self):
        self.__nado = input("¿Cuál es tu récord nadando? ")

    def ingresar_ciclismo(self):
        self.__ciclismo = input("¿Cuál es tu distancia máxima en bici? ")

    def ingresar_trote(self):
        self.__trote = input("¿Cuál es tu distancia máxima de trote? ")

    def __str__(self):
        return (
            f"{self.__nombre}, tus marcas son:\n"
            f"Nado: {self.__nado}\n"
            f"Ciclismo: {self.__ciclismo}\n"
            f"Trote: {self.__trote}"
        )



atleta_01 = Triatleta()

atleta_01.ingresar_nombre()
atleta_01.ingresar_nado()
atleta_01.ingresar_ciclismo()
atleta_01.ingresar_trote()

print(atleta_01)

