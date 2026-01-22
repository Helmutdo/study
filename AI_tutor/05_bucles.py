#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 05: BUCLES (for y while)                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

Los bucles repiten un bloque de código varias veces.
  • for: iterar sobre una secuencia (lista, rango, cadena, etc.)
  • while: repetir mientras se cumpla una condición
"""

# =============================================================================
# BUCLE for CON range()
# =============================================================================
# range(inicio, fin, paso) — genera números. fin NO está incluido.

print("--- for con range ---")
for i in range(5):           # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 6):        # 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8 (paso 2)
    print(i, end=" ")
print()

# =============================================================================
# for SOBRE UNA LISTA (o cualquier iterable)
# =============================================================================
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Si necesitas el índice: enumerate()
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# =============================================================================
# for SOBRE UNA CADENA
# =============================================================================
for letra in "Hola":
    print(letra, end=" ")
print()

# =============================================================================
# BUCLE while
# =============================================================================
# Se ejecuta mientras la condición sea True. ¡Cuidado con bucles infinitos!

print("\n--- while ---")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# =============================================================================
# break — SALIR DEL BUCLE
# =============================================================================
# Termina el bucle inmediatamente (for o while).

print("\n--- break ---")
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")  # 0 1 2 3 4
print()

# =============================================================================
# continue — SALTAR A LA SIGUIENTE ITERACIÓN
# =============================================================================
# No ejecuta el resto del cuerpo; pasa a la siguiente vuelta.

print("--- continue ---")
for n in range(5):
    if n == 2:
        continue
    print(n, end=" ")  # 0 1 3 4 (salta el 2)
print()

# =============================================================================
# else EN BUCLES (peculiaridad de Python)
# =============================================================================
# El else de un for/while se ejecuta si el bucle terminó "normalmente"
# (sin break). Poco usado, pero existe.

for x in range(3):
    print(x, end=" ")
else:
    print("\nBucle terminado sin break")

# Con break, el else NO se ejecuta:
for x in range(5):
    if x == 2:
        break
    print(x, end=" ")
else:
    print("Esto no se imprime")
print()

"""
SIGUIENTE: 06_listas_tuplas.py — listas, tuplas y secuencias.
"""
