#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 01: VARIABLES Y TIPOS DE DATOS                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

VARIABLES
---------
Una variable es un nombre que guarda un valor en memoria. En Python NO declaras
el tipo: el tipo se infiere del valor que asignas. Eso se llama "tipado dinámico".

Crear variable:  nombre = valor
"""

# =============================================================================
# TIPOS BÁSICOS (PRIMITIVOS)
# =============================================================================

# --- int (enteros) ---
edad = 25
cantidad = -100
grande = 1_000_000  # Los _ ayudan a leer; Python los ignora
print("Enteros:", edad, cantidad, grande)
print("Tipo de 'edad':", type(edad))  # <class 'int'>

# --- float (decimales) ---
precio = 19.99
pi = 3.14159
cientifico = 1.5e3  # 1.5 * 10^3 = 1500.0
print("Flotantes:", precio, pi, cientifico)
print("Tipo de 'precio':", type(precio))  # <class 'float'>

# --- str (cadenas de texto) ---
nombre = "Alice"
saludo = 'Hola'  # Comillas simples o dobles, da igual
parrafo = """Línea 1
Línea 2
Línea 3"""
print("Cadenas:", nombre, saludo)
print("Tipo de 'nombre':", type(nombre))  # <class 'str'>

# Concatenar cadenas
full = nombre + " dice " + saludo
print(full)

# --- bool (booleanos: True / False) ---
activo = True
vacio = False
print("Booleanos:", activo, vacio)
print("Tipo de 'activo':", type(activo))  # <class 'bool'>

# =============================================================================
# NONE (ausencia de valor)
# =============================================================================
# None es un valor especial que indica "nada" o "vacío". Útil para inicializar.

resultado = None
print("None:", resultado, "| Tipo:", type(resultado))  # <class 'NoneType'>

# =============================================================================
# REASIGNAR Y CAMBIAR TIPO
# =============================================================================
# Una misma variable puede guardar distintos tipos a lo largo del programa.

x = 10
print(x, type(x))  # 10 <class 'int'>

x = "ahora soy texto"
print(x, type(x))  # ahora soy texto <class 'str'>

# =============================================================================
# CONVERSIÓN DE TIPOS (CASTING)
# =============================================================================
# int(), float(), str(), bool() convierten entre tipos.

texto_num = "42"
numero = int(texto_num)   # "42" -> 42
decimal = float("3.14")   # "3.14" -> 3.14
cadena = str(100)         # 100 -> "100"
print("Conversiones:", numero, decimal, cadena)

# =============================================================================
# BUENAS PRÁCTICAS
# =============================================================================
# • Nombres descriptivos:  total_ventas  en vez de  t  o  x1
# • No usar palabras reservadas: if, for, class, def, etc.
# • Python es case-sensitive:  nombre  y  Nombre  son distintas.
"""

SIGUIENTE: 02_operadores.py — operadores aritméticos, comparación y lógicos.
"""
