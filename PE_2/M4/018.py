

# PE_2/M4/018.py

# --- Métodos Estáticos (@staticmethod) ---

# Un método estático es un método que pertenece a una clase, pero no depende
# de ninguna instancia (objeto) de esa clase. No recibe la instancia (`self`)
# ni la clase (`cls`) como primer argumento.

# Son esencialmente funciones normales que están agrupadas dentro de una clase
# porque tienen una conexión lógica con ella, pero no modifican ni acceden
# al estado de un objeto o de la clase.

class Calculadora:

    def __init__(self, marca):
        self.marca = marca

    def sumar_instancia(self, a, b):
        # Este es un método de instancia normal, necesita 'self'.
        print(f"Suma realizada por la calculadora {self.marca}")
        return a + b

    # Para definir un método estático, usamos el decorador @staticmethod.
    @staticmethod
    def sumar(a, b):
        # Este método no tiene acceso a 'self' o a 'self.marca'.
        # Intentar acceder a 'self' aquí daría un error.
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: División por cero no permitida."
        return a / b

# --- Uso de Métodos Estáticos ---

# Podemos llamar a un método estático directamente desde la clase,
# sin necesidad de crear un objeto.
resultado_suma = Calculadora.sumar(10, 5)
print(f"Resultado de la suma estática: {resultado_suma}") # Salida: 15

resultado_division = Calculadora.dividir(10, 2)
print(f"Resultado de la división estática: {resultado_division}") # Salida: 5.0


# También se pueden llamar desde una instancia, pero no es lo común y
# el método sigue sin tener acceso al estado de la instancia.
mi_calculadora = Calculadora("Casio")

# Llamando al método de instancia (necesita el objeto)
resultado_con_instancia = mi_calculadora.sumar_instancia(7, 3) # Salida: Suma realizada por la calculadora Casio
print(f"Resultado de la suma de instancia: {resultado_con_instancia}") # Salida: 10

# Llamando al método estático desde la instancia
# (funciona, pero 'sumar' no sabe nada sobre 'mi_calculadora')
resultado_estatico_desde_instancia = mi_calculadora.sumar(8, 2)
print(f"Resultado de la suma estática (desde instancia): {resultado_estatico_desde_instancia}") # Salida: 10


# ¿Cuándo usar métodos estáticos?
# - Cuando una funcionalidad está relacionada con la clase, pero no necesita
#   acceder a ningún dato de la clase o de sus instancias.
# - Para crear funciones de utilidad que tienen sentido que estén "dentro" de la clase.
# - Por ejemplo, una clase 'Fecha' podría tener un método estático 'es_bisiesto(anio)'
#   que solo necesita el año para hacer su cálculo.

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    @staticmethod
    def es_bisiesto(anio):
        """Verifica si un año es bisiesto."""
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

print("\nVerificación de año bisiesto:")
print(f"¿2024 es un año bisiesto? {Fecha.es_bisiesto(2024)}") # True
print(f"¿1900 es un año bisiesto? {Fecha.es_bisiesto(1900)}") # False
print(f"¿2000 es un año bisiesto? {Fecha.es_bisiesto(2000)}") # True
