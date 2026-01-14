class Triatleta:
    def __init__(self):
        self.nombre = input("Tu nombre: ").strip()
        self.favorita = None
        self.distancias = []

    def agregar_favorita(self):
        opc = input("Favorita (1=nado, 2=bici, 3=trote): ")
        disc = {"1":"Natación", "2":"Ciclismo", "3":"Trote"}.get(opc)
        if disc:
            tiempo = input(f"Record en {disc}: ")
            self.favorita = (disc, tiempo)
        else:
            print("Opción inválida")

    def agregar_distancias(self):
        mapa = {"1":"Sprint", "2":"Olímpico", "3":"70.3", "4":"Full"}
        nums = input("Números de distancias (ej: 124): ")
        for n in nums:
            if n in mapa:
                self.distancias.append(mapa[n])

    def __str__(self):
        fav = f"{self.favorita[0]} ({self.favorita[1]})" if self.favorita else "sin registrar"
        dist = ", ".join(self.distancias) or "ninguna"
        return f"{self.nombre} → Fav: {fav} | Distancias: {dist}"


p = Triatleta()
p.agregar_favorita()
p.agregar_distancias()
print(p)