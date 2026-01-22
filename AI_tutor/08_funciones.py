#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 08: FUNCIONES                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

Las funciones agrupan código reutilizable. Se definen con def.
"""

# =============================================================================
# FUNCIÓN BÁSICA
# =============================================================================
def saludar():
    print("Hola desde la función")

saludar()

# =============================================================================
# PARÁMETROS Y return
# =============================================================================
def suma(a, b):
    return a + b

r = suma(3, 5)
print(r)  # 8

# Sin return devuelve None
def solo_imprime():
    print("No devuelvo nada")

print(solo_imprime())  # None

# =============================================================================
# PARÁMETROS POR DEFECTO
# =============================================================================
def saludar_nombre(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

print(saludar_nombre("Ana"))                    # Hola, Ana
print(saludar_nombre("Bob", mensaje="Hey"))     # Hey, Bob

# =============================================================================
# ARGUMENTOS POSICIONALES Y POR NOMBRE
# =============================================================================
def info(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, {ciudad}"

print(info("Carlos", 25, "Lima"))
print(info(edad=25, ciudad="Lima", nombre="Carlos"))

# =============================================================================
# *args — NÚMERO VARIABLE DE ARGUMENTOS POSICIONALES
# =============================================================================
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3, 4, 5))  # 15

# =============================================================================
# **kwargs — ARGUMENTOS POR NOMBRE VARIABLES
# =============================================================================
def mostrar_info(**kwargs):
    for k, v in kwargs.items():
        print(f"  {k}: {v}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")

# =============================================================================
# COMBINAR (orden típico: posicionales, *args, por defecto, **kwargs)
# =============================================================================
def ej(a, b, *args, opcion=True, **kwargs):
    print(a, b, args, opcion, kwargs)

ej(1, 2, 3, 4, opcion=False, x=10)  # 1 2 (3, 4) False {'x': 10}

# =============================================================================
# ÁMBITO (scope): LOCAL vs GLOBAL
# =============================================================================
x_global = 10

def f():
    x_local = 5
    print(x_local)   # 5
    print(x_global)  # 10 — se puede leer

def g():
    global x_global
    x_global = 20    # modificar la global (evitar si no es necesario)

# =============================================================================
# FUNCIONES COMO OBJETOS / LAMBDA
# =============================================================================
# Las funciones son objetos. Puedes asignarlas, pasarlas como argumentos, etc.

def cuadrado(x):
    return x ** 2

f = cuadrado
print(f(4))  # 16

# lambda: función anónima de una sola expresión
doblar = lambda x: x * 2
print(doblar(7))  # 14

# Útil para sort, map, filter:
lista = [(1, "b"), (2, "a")]
lista.sort(key=lambda p: p[1])
print(lista)  # [(2, 'a'), (1, 'b')]

"""
SIGUIENTE: 09_manejo_archivos.py — abrir, leer y escribir archivos.
"""
