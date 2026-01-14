class Triatleta:
    def __init__(self, nombre=0, nado=0, ciclismo=0, trote=0):
        self.__nombre = nombre 
        self.__nado = nado
        self.__ciclismo = ciclismo
        self.__trote = trote
        
    
    def id(self):
        nombre = input("ingresa tu nombre: ")
        return nombre

    def nadar(self, nado):
        nado = input("cual es tu record nadando?")
        return nado

    def ciclismo(self, ciclismo):
        ciclismo = input("cual es tu recorrido max en bici? ")
        return ciclismo

    def trote(self, trote):
        trote = input("typea tu max distancia de trote")
        return trote

    def __str__(self, nombre, nado, ciclismo, trote):
        return nombre + " estos son tus distancias maximas en " + nado + "" + ciclismo + "" + trote + ""

helmut = Triatleta("helmut", 10, 30 , 40)

print(helmut)
