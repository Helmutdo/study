

# PE_2/M4/016.py

# --- Orden de Resolución de Métodos (MRO) y el Problema del Diamante ---

# El MRO (Method Resolution Order) es el orden en que Python busca un método en una jerarquía de clases.
# Es crucial en la herencia múltiple, especialmente para resolver el "problema del diamante".

# El problema del diamante ocurre cuando una clase hereda de dos clases que a su vez
# tienen un ancestro común. Esto crea una ambigüedad: si la clase hija llama a un método
# definido en el ancestro común, ¿qué versión del método debería usar si las clases intermedias
# lo han sobrescrito?

# --- Creando la Estructura del Diamante ---

class A:
    def quien_soy(self):
        print("Soy la clase A")

class B(A):
    def quien_soy(self):
        print("Soy la clase B")

class C(A):
    def quien_soy(self):
        print("Soy la clase C")

# La clase D hereda de B y C, que a su vez heredan de A.
# D
# / \
# B   C
# \ /
#   A
class D(B, C):
    pass # No tiene métodos propios

# --- ¿Qué método se ejecuta? ---
# Gracias al algoritmo C3 linearization (usado por Python para calcular el MRO),
# el orden está bien definido y no es ambiguo. El MRO garantiza que cada clase
# aparezca una sola vez en el orden y que se preserve el orden de herencia local.

instancia_d = D()
instancia_d.quien_soy()

# Salida: "Soy la clase B"

# ¿Por qué? Porque el MRO de D es [D, B, C, A, object].
# Python busca `quien_soy` en el siguiente orden:
# 1. ¿Está en D? No.
# 2. ¿Está en B? Sí. Lo ejecuta y para.
# Nunca llega a buscar en C o en A. El orden se define por cómo se listan las clases
# padre en la definición de la clase hija (`class D(B, C):`). Si fuera `class D(C, B):`,
# el resultado sería "Soy la clase C".

# --- Visualizando el MRO ---

# Podemos ver el MRO de una clase usando el atributo especial `__mro__`.
print("\nMRO de la clase D:", D.__mro__)
# Salida: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# La función `help()` también muestra el MRO de una forma legible.
# help(D)

# --- Uso de super() en un MRO complejo ---

# `super()` es inteligente y sigue el MRO. Cuando llamas a `super().<metodo>()`,
# Python busca ese método en la *siguiente* clase del MRO, no necesariamente en la clase padre directa.

class B_super(A):
    def quien_soy(self):
        print("Inicio en B")
        super().quien_soy() # Llama al método de la siguiente clase en el MRO de D (que es C)
        print("Fin en B")

class C_super(A):
    def quien_soy(self):
        print("Inicio en C")
        super().quien_soy() # Llama al método de la siguiente clase en el MRO de D (que es A)
        print("Fin en C")

class D_super(B_super, C_super):
    def quien_soy(self):
        print("Inicio en D")
        super().quien_soy() # Llama al método de la siguiente clase en el MRO de D (que es B_super)
        print("Fin en D")

print("\n--- Demostración de super() con MRO ---")
instancia_d_super = D_super()
instancia_d_super.quien_soy()
# El MRO de D_super es: D_super -> B_super -> C_super -> A -> object

# El resultado del print será:
# Inicio en D
# Inicio en B
# Inicio en C
# Soy la clase A
# Fin en C
# Fin en B
# Fin en D
#
# Esto demuestra cómo `super()` navega la cadena del MRO, permitiendo que todas
# las implementaciones del método en la jerarquía se ejecuten de manera predecible.
