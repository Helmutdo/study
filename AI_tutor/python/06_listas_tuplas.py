#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 06: LISTAS Y TUPLAS                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

LISTAS []
--------
Ordenadas, mutables (puedes cambiar, añadir, quitar elementos).
Pueden contener elementos de distintos tipos.
"""

# =============================================================================
# CREAR Y ACCEDER A LISTAS
# =============================================================================
numeros = [1, 2, 3, 4, 5]
mezcla = [1, "hola", 3.14, True, None]
vacia = []

# Índices: 0-based. Negativos cuentan desde el final.
print(numeros[0])    # 1  — primer elemento
print(numeros[-1])   # 5  — último
print(numeros[-2])   # 4  — penúltimo

# Slicing: lista[inicio:fin:paso] — fin NO incluido
print(numeros[1:4])   # [2, 3, 4]
print(numeros[:3])    # [1, 2, 3] — desde el inicio
print(numeros[2:])    # [3, 4, 5] — hasta el final
print(numeros[::2])   # [1, 3, 5] — cada 2
print(numeros[::-1])  # [5, 4, 3, 2, 1] — invertida

# =============================================================================
# MODIFICAR LISTAS (mutables)
# =============================================================================
lista = [10, 20, 30]
lista[1] = 99
print(lista)  # [10, 99, 30]

lista.append(40)       # añade al final
lista.insert(0, 5)     # inserta en índice 0
print(lista)  # [5, 10, 99, 30, 40]

eliminado = lista.pop()      # quita y devuelve el último
eliminado2 = lista.pop(1)    # quita el del índice 1
lista.remove(99)             # quita la primera aparición de 99
print(lista)

# =============================================================================
# MÉTODOS ÚTILES DE LISTAS
# =============================================================================
L = [3, 1, 4, 1, 5]
print(len(L))        # 5 — longitud
print(sum(L))        # 14
print(min(L), max(L))
L.sort()             # ordena in-place
print(L)
L.reverse()          # invierte in-place
print(L)

# =============================================================================
# TUPLAS ()
# =============================================================================
# Ordenadas, INMUTABLES (no puedes cambiar contenido después de crearlas).
# Útiles para datos que no deben cambiar (coordenadas, config, etc.).

coord = (10, 20)
rgb = (255, 128, 0)
un_solo = (42,)      # tupla de un elemento: lleva coma

print(coord[0], coord[1])
# coord[0] = 5  # ERROR: las tuplas son inmutables

# Desempaquetado
x, y = coord
print(x, y)

# Útil para devolver varios valores desde una función
def min_max(lst):
    return min(lst), max(lst)
mi, ma = min_max([1, 5, 3])
print(mi, ma)

# =============================================================================
# LISTAS POR COMPRENSIÓN (list comprehensions)
# =============================================================================
# Forma compacta de crear listas a partir de otras.

cuadrados = [x ** 2 for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25]

pares = [n for n in range(10) if n % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Equivalente "normal":
# cuadrados = []
# for x in range(6):
#     cuadrados.append(x ** 2)

"""
SIGUIENTE: 07_diccionarios_conjuntos.py — dict y set.
"""
