#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 09: MANEJO DE ARCHIVOS                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

Para leer y escribir archivos usamos la función open().
Es buena práctica usar el contexto with para que el archivo se cierre solo.
"""

# =============================================================================
# ABRIR Y CERRAR: open() y with
# =============================================================================
# open(ruta, modo) — modos comunes: "r" leer, "w" escribir (sobrescribe),
# "a" añadir, "rb"/"wb" binario. Por defecto es "r" (texto).

# Ruta junto a este script (funciona desde cualquier directorio)
from pathlib import Path
_ruta = Path(__file__).parent / "ejemplo_lectura.txt"

# Forma recomendada: with asegura que el archivo se cierre al salir del bloque
with open(_ruta, "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")
    f.write("Línea 3\n")

# =============================================================================
# LEER ARCHIVO
# =============================================================================
# Crea el archivo si no existe (lo hicimos arriba). Si no, usa uno existente.
# Para este ejemplo, leemos el que acabamos de escribir.

try:
    with open(_ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("--- read() (todo el archivo) ---")
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado. Ejecuta primero la parte de escritura.")

# =============================================================================
# LEER LÍNEA A LÍNEA
# =============================================================================
print("--- readline() / readlines() ---")
try:
    with open(_ruta, "r", encoding="utf-8") as f:
        linea = f.readline()
        while linea:
            print(repr(linea))  # incluye \n
            linea = f.readline()
except FileNotFoundError:
    pass

# O iterar directamente sobre el archivo (eficiente en memoria)
print("--- iterar sobre f ---")
try:
    with open(_ruta, "r", encoding="utf-8") as f:
        for linea in f:
            print(linea.rstrip())  # quita \n al imprimir
except FileNotFoundError:
    pass

# readlines() devuelve lista de líneas
try:
    with open(_ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    print("Lista de líneas:", lineas)
except FileNotFoundError:
    pass

# =============================================================================
# ESCRIBIR EN ARCHIVO
# =============================================================================
# "w" borra el archivo si existe. "a" añade al final.

_ruta_esc = Path(__file__).parent / "ejemplo_escritura.txt"
with open(_ruta_esc, "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

with open(_ruta_esc, "a", encoding="utf-8") as f:
    f.write("Añadida con append\n")

# =============================================================================
# BUENAS PRÁCTICAS
# =============================================================================
# • Usa with para que se cierre el archivo automáticamente.
# • Especifica encoding="utf-8" para texto (evita problemas con acentos).
# • Rutas: "carpeta/archivo.txt" o r"C:\ruta\archivo.txt" en Windows.
# • pathlib.Path es una alternativa moderna: Path("carpeta") / "archivo.txt"

"""
SIGUIENTE: 10_clases_objetos.py — programación orientada a objetos.
"""
