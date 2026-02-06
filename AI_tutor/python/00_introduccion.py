#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 00: INTRODUCCIÓN A PYTHON                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ ES PYTHON?
---------------
Python es un lenguaje de programación interpretado, de alto nivel y de propósito
general. Fue creado por Guido van Rossum y lanzado en 1991.

Características principales:
  • Sintaxis clara y legible (fácil de aprender)
  • Multiparadigma: soporta programación orientada a objetos, funcional e imperativa
  • Gran ecosistema de bibliotecas (data science, web, IA, automatización...)
  • Es interpretado: no compilas, ejecutas directamente con el intérprete
  • Indentación obligatoria: los bloques se definen con espacios/tabs (no llaves {})

¿CÓMO EJECUTAR ESTE ARCHIVO?
-----------------------------
Desde la terminal:  python3 00_introduccion.py
O simplemente:      python 00_introduccion.py

COMENTARIOS EN PYTHON
---------------------
  # Una sola línea: todo después del # se ignora
  
  \"\"\"
  Comentarios de varias líneas:
  Se usan tres comillas dobles (o simples) al inicio y al final.
  Ideales para documentar funciones, clases o explicaciones largas.
  \"\"\"
"""

# =============================================================================
# TU PRIMER PROGRAMA
# =============================================================================
# La función print() muestra texto en la consola. Es lo más básico para "salida".

print("¡Hola! Bienvenido al AI Tutor de Python.")
print("Si ves este mensaje, Python está funcionando correctamente.")

# Puedes imprimir números directamente (sin comillas)
print(42)
print(3.14159)

# Puedes imprimir varias cosas separadas por comas (print añade espacio entre ellas)
print("La respuesta es:", 42, "y pi es", 3.14159)

# print() por defecto termina con un salto de línea. Puedes cambiarlo:
print("Sin salto ", end="")
print("al final.")

# =============================================================================
# INDENTACIÓN (MUY IMPORTANTE EN PYTHON)
# =============================================================================
# En otros lenguajes se usan { } para bloques. En Python, la INDENTACIÓN define
# el bloque. Normalmente usamos 4 espacios. ¡No mezcles tabs y espacios!

if True:
    print("Esto está dentro del 'if' (indentado)")
    print("Esto también.")
print("Esto está fuera del 'if'.")

# =============================================================================
# CONVENciones DE NOMBRES
# =============================================================================
# • Variables y funciones: snake_case (minúsculas_con_guiones_bajos)
# • Clases: PascalCase (CadaPalabraConMayúscula)
# • Constantes: MAYÚSCULAS_CON_GUIONES (por convención)

# =============================================================================
# SIGUIENTE LECCIÓN: 01_variables_tipos.py
# =============================================================================
