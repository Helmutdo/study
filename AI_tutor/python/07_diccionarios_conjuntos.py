#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 07: DICCIONARIOS Y CONJUNTOS                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

DICCIONARIOS {}
--------------
Estructura clave -> valor. Las claves deben ser inmutables (str, int, tuple).
Muy útiles para datos asociativos (JSON, config, etc.).
"""

# =============================================================================
# CREAR Y ACCEDER
# =============================================================================
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

print(persona["nombre"])   # Ana
# print(persona["apellido"])  # KeyError si no existe

# Forma segura: .get(clave, valor_por_defecto)
print(persona.get("apellido", "N/A"))

# =============================================================================
# MODIFICAR DICCIONARIOS
# =============================================================================
persona["edad"] = 31
persona["email"] = "ana@mail.com"  # añadir nueva clave
del persona["ciudad"]              # eliminar clave
print(persona)

# =============================================================================
# MÉTODOS ÚTILES
# =============================================================================
print(persona.keys())    # dict_keys(['nombre', 'edad', 'email'])
print(persona.values())  # dict_values([...])
print(persona.items())   # pares (clave, valor)

for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# =============================================================================
# DICT POR COMPRENSIÓN
# =============================================================================
cuadrados = {n: n ** 2 for n in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# =============================================================================
# CONJUNTOS (set) {}
# =============================================================================
# Colección NO ordenada, SIN duplicados. Útil para eliminar repes y "pertenencia".

nums = {1, 2, 3, 2, 1}
print(nums)  # {1, 2, 3} — sin duplicados

# Crear desde lista para quitar duplicados
lista = [1, 2, 2, 3, 3, 3]
unicos = set(lista)
print(unicos)

# Operaciones de conjuntos
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # unión: {1, 2, 3, 4}
print(a & b)   # intersección: {2, 3}
print(a - b)   # diferencia: {1}
print(a ^ b)   # diferencia simétrica: {1, 4}

# Añadir / quitar
s = {1, 2}
s.add(3)
s.remove(2)  # KeyError si no existe; use .discard(2) para evitar

# =============================================================================
# FROZENSET — conjuntos inmutables
# =============================================================================
# Como set pero no se puede modificar. Puede usarse como clave de dict.

fs = frozenset([1, 2, 3])
print(fs)

"""
SIGUIENTE: 08_funciones.py — def, parámetros, return.
"""
