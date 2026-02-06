#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 04: CONDICIONALES (if, elif, else)                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

Las condicionales permiten ejecutar código solo cuando se cumple una condición.
Recuerda: la indentación define qué está "dentro" del if.
"""

# =============================================================================
# IF SIMPLE
# =============================================================================
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

# =============================================================================
# IF - ELSE
# =============================================================================
if edad >= 18:
    print("Puedes votar.")
else:
    print("Aún no puedes votar.")

# =============================================================================
# IF - ELIF - ELSE (varias condiciones)
# =============================================================================
nota = 75

if nota >= 90:
    print("Excelente (A)")
elif nota >= 80:
    print("Muy bien (B)")
elif nota >= 70:
    print("Bien (C)")
elif nota >= 60:
    print("Suficiente (D)")
else:
    print("Insuficiente (F)")

# =============================================================================
# CONDICIONES ANIDADAS
# =============================================================================
tiene_entrada = True
es_vip = False

if tiene_entrada:
    if es_vip:
        print("Pasa por la puerta VIP.")
    else:
        print("Pasa por la entrada general.")
else:
    print("Necesitas una entrada.")

# =============================================================================
# OPERADOR TERNARIO (expresión condicional en una línea)
# =============================================================================
# resultado = valor_si_true if condicion else valor_si_false

edad = 20
mensaje = "Mayor" if edad >= 18 else "Menor"
print(mensaje)  # Mayor

# =============================================================================
# VALORES "FALSY" Y "TRUTHY"
# =============================================================================
# En Python, en un if se evalúa la "veracidad" del valor.
# Falsy: False, 0, 0.0, "", None, [], {}, ()
# Casi todo lo demás es truthy.

lista = []
if lista:
    print("La lista tiene elementos")
else:
    print("La lista está vacía")  # Se ejecuta esto

if "hola":
    print("Una cadena no vacía es truthy")  # Se ejecuta

# =============================================================================
# COMPARACIONES EN CADENA
# =============================================================================
# Puedes escribir:  a < b < c  en vez de  a < b and b < c

x = 5
if 0 < x < 10:
    print("x está entre 0 y 10")

"""
SIGUIENTE: 05_bucles.py — for y while.
"""
