class Triatleta:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ").strip()
        self.favorita = None          # va a ser un diccionario {disciplina: record}
        self.distancias = []          # lista de strings o tuplas

    def registrar_favorita(self):
        while True:
            print("\n¿Cuál es tu disciplina favorita?")
            print("1. Natación")
            print("2. Ciclismo")
            print("3. Trote")
            
            opcion = input("→ ").strip()
            
            if opcion == "1":
                disciplina = "Natación"
                break
            elif opcion == "2":
                disciplina = "Ciclismo"
                break
            elif opcion == "3":
                disciplina = "Trote"
                break
            else:
                print("Opción no válida, intenta de nuevo...\n")

        record = input(f"¿Cuál es tu record personal en {disciplina}? ").strip()
        self.favorita = {disciplina: record}
        print(f"¡Perfecto! Registrado: {disciplina} → {record}\n")

    def registrar_distancias(self):
        print("\n¿Qué distancias has competido? (puedes poner varias)")
        print("1. Sprint")
        print("2. Olímpico")
        print("3. 70.3 / Half")
        print("4. Full / Ironman")
        print("(escribe los números juntos, ej: 124 o uno por uno y enter vacío para terminar)\n")

        while True:
            entrada = input("→ ").strip()
            if not entrada:  # enter vacío → termina
                break
                
            if entrada == "1":
                self.distancias.append("Sprint")
            elif entrada == "2":
                self.distancias.append("Olímpico")
            elif entrada == "3":
                self.distancias.append("70.3 / Half")
            elif entrada == "4":
                self.distancias.append("Full / Ironman")
            else:
                print("Opción no válida, intenta de nuevo...\n")


        print("Distancias registradas:", ", ".join(self.distancias) if self.distancias else "ninguna")

    def __str__(self):
        fav_str = "Aún no registrada" 
        if self.favorita:
            disc, tiempo = next(iter(self.favorita.items()))
            fav_str = f"{disc} ({tiempo})"

        distancias_str = ", ".join(self.distancias) if self.distancias else "ninguna"

        return (f"Triatleta: {self.nombre}\n"
                f"Disciplina favorita: {fav_str}\n"
                f"Distancias competidas: {distancias_str}")


# Uso
atleta = Triatleta()
atleta.registrar_favorita()
atleta.registrar_distancias()

print("\n" + "="*50)
print(atleta)