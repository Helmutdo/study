#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 11: MÓDULOS Y PAQUETES                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

Un MÓDULO es un archivo .py que puedes importar.
Un PAQUETE es una carpeta con __init__.py (y opcionalmente otros módulos).
Así organizas y reutilizas código.
"""

# =============================================================================
# IMPORTAR MÓDULOS ESTÁNDAR
# =============================================================================
import math
print(math.pi, math.sqrt(16))

import math as m
print(m.pi)

from math import pi, sqrt
print(pi, sqrt(9))

from math import *  # trae todo (evitar: nombres pueden chocar)

# =============================================================================
# IMPORTAR TU PROPIO MÓDULO
# =============================================================================
# Si tienes mi_modulo.py en la misma carpeta o en el path:
#   import mi_modulo
#   from mi_modulo import mi_funcion

# Ejemplo con un módulo estándar que "parece" propio:
import random
print(random.randint(1, 10))

# =============================================================================
# __name__ Y EJECUCIÓN COMO SCRIPT
# =============================================================================
# Cuando ejecutas un archivo directamente: __name__ == "__main__"
# Cuando lo importas desde otro: __name__ == "nombre_del_modulo"
# Útil para poner código que solo corre si ejecutas el archivo, no si lo importas.

def utilidad():
    return "Soy una utilidad"

if __name__ == "__main__":
    print("Este archivo se está ejecutando como script.")
    print(utilidad())
else:
    print("Este archivo fue importado como módulo.")

# =============================================================================
# PAQUETES
# =============================================================================
# Estructura típica:
#   mi_paquete/
#     __init__.py    # puede estar vacío o inicializar el paquete
#     modulo_a.py
#     modulo_b.py
#
# Uso:
#   import mi_paquete.modulo_a
#   from mi_paquete.modulo_a import alguna_funcion
#   from mi_paquete import modulo_b

# =============================================================================
# PYTHON PATH
# =============================================================================
# Python busca módulos en: directorio actual, PYTHONPATH, instalación estándar.
# Para ver desde dónde se importa: print(modulo.__file__)

import sys
print("Rutas de búsqueda (primeras 3):", sys.path[:3])

"""
SIGUIENTE: 12_errores_excepciones.py — try, except y manejo de errores.
"""
