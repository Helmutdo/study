#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 02: OPERADORES                                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

Los operadores permiten realizar operaciones con valores y variables.
"""

# =============================================================================
# OPERADORES ARITMÉTICOS
# =============================================================================
a, b = 10, 3  # Asignación múltiple: a=10, b=3

print("--- Aritméticos ---")
print("a + b =", a + b)   # 13  — suma
print("a - b =", a - b)   # 7   — resta
print("a * b =", a * b)   # 30  — multiplicación
print("a / b =", a / b)   # 3.333... — división siempre devuelve float
print("a // b =", a // b) # 3   — división entera (trunca)
print("a % b =", a % b)   # 1   — módulo (resto)
print("a ** b =", a ** b) # 1000 — potencia (10^3)

# Operadores de asignación compuesta
x = 5
x += 2   # x = x + 2  -> 7
x -= 1   # x = x - 1  -> 6
x *= 3   # x = x * 3  -> 18
print("x después de +=, -=, *= :", x)

# =============================================================================
# OPERADORES DE COMPARACIÓN
# =============================================================================
# Devuelven True o False.

print("\n--- Comparación ---")
print("5 == 5   ->", 5 == 5)    # True  — igual
print("5 != 3   ->", 5 != 3)    # True  — distinto
print("5 > 3    ->", 5 > 3)     # True  — mayor
print("5 < 3    ->", 5 < 3)     # False — menor
print("5 >= 5   ->", 5 >= 5)    # True  — mayor o igual
print("5 <= 4   ->", 5 <= 4)    # False — menor o igual

# Cadenas se comparan alfabéticamente
print("'abc' < 'abd' ->", "abc" < "abd")  # True

# =============================================================================
# OPERADORES LÓGICOS
# =============================================================================
# and, or, not — trabajan con booleanos.

print("\n--- Lógicos ---")
print("True and False ->", True and False)   # False
print("True or False  ->", True or False)    # True
print("not True       ->", not True)         # False

# Ejemplo práctico
edad = 20
tiene_permiso = True
puede_entrar = edad >= 18 and tiene_permiso
print("¿Puede entrar? (edad>=18 y permiso):", puede_entrar)

# =============================================================================
# OPERADORES DE IDENTIDAD: is / is not
# =============================================================================
# Comprueban si dos variables apuntan al MISMO objeto en memoria.
# No confundir con == (que compara VALORES).

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print("\n--- Identidad ---")
print("lista1 == lista2 ->", lista1 == lista2)  # True (mismos valores)
print("lista1 is lista2 ->", lista1 is lista2)  # False (objetos distintos)
print("lista1 is lista3 ->", lista1 is lista3)  # True (mismo objeto)

# =============================================================================
# OPERADORES DE PERTENENCIA: in / not in
# =============================================================================
# ¿Está un valor dentro de una secuencia (cadena, lista, etc.)?

print("\n--- Pertenencia ---")
print("'a' in 'hola'    ->", "a" in "hola")     # True
print("'z' not in 'hola' ->", "z" not in "hola") # True
print("3 in [1, 2, 3]   ->", 3 in [1, 2, 3])   # True

# =============================================================================
# PRECEDENCIA (ORDEN DE EVALUACIÓN)
# =============================================================================
# De mayor a menor: **  ->  * / // %  ->  + -  ->  == != < >  ->  not  ->  and  ->  or
# Usa paréntesis cuando quieras dejar claro el orden:  (a + b) * c

print("\n2 + 3 * 4 =", 2 + 3 * 4)       # 14 (primero 3*4)
print("(2 + 3) * 4 =", (2 + 3) * 4)   # 20

"""
SIGUIENTE: 03_entrada_salida.py — input(), print() y formateo de cadenas.
"""
