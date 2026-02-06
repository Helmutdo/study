#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 03: ENTRADA Y SALIDA                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

SALIDA: print()
--------------
Ya viste print() en la lección 00. Aquí ampliamos: separador, fin de línea,
formateo.
"""

# =============================================================================
# PRINT: sep y end
# =============================================================================
print(1, 2, 3)                    # 1 2 3  (sep por defecto es " ")
print(1, 2, 3, sep=" | ")         # 1 | 2 | 3
print("línea 1", end=" -> ")
print("línea 2")                  # línea 1 -> línea 2

# =============================================================================
# FORMATEO DE CADENAS (f-strings) — RECOMENDADO EN PYTHON 3.6+
# =============================================================================
# Pon 'f' antes de las comillas y usa {variable} dentro.

nombre = "Ana"
edad = 30
print(f"\n{nombre} tiene {edad} años.")

# Expresiones dentro de {}
print(f"Dentro de 5 años tendrá {edad + 5}.")

# Formato numérico
precio = 19.5
print(f"Precio: {precio:.2f}")    # 2 decimales
print(f"Porcentaje: {0.856:.1%}") # 85.6%

# =============================================================================
# OTROS FORMATEOS (por si los ves en código antiguo)
# =============================================================================
# .format()
print("Hola, {}. Tienes {} años.".format(nombre, edad))

# % (estilo C, antiguo)
print("Hola, %s. Tienes %d años." % (nombre, edad))

# =============================================================================
# ENTRADA: input()
# =============================================================================
# input() lee una línea de texto desde la consola. Siempre devuelve str.
# Opcionalmente puedes mostrar un mensaje (prompt).

# DESCOMENTA LAS SIGUIENTES LÍNEAS PARA PROBAR EN LA TERMINAL:
# usuario = input("¿Cómo te llamas? ")
# print(f"Hola, {usuario}!")

# Si necesitas un número, debes convertir:
# num = int(input("Dame un número: "))
# print("El doble es", num * 2)

# =============================================================================
# EJEMPLO COMPLETO (descomenta para ejecutar de forma interactiva)
# =============================================================================
"""
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print(f"Hola {nombre}. En 10 años tendrás {edad + 10}.")
"""

# Versión no interactiva para que el script siempre funcione:
print("\n--- Ejemplo simulado ---")
nombre_ej = "Usuario"
edad_ej = 25
print(f"Hola {nombre_ej}. En 10 años tendrás {edad_ej + 10}.")

"""
SIGUIENTE: 04_condicionales.py — if, elif, else.
"""
