#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 12: ERRORES Y EXCEPCIONES                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

Cuando algo falla, Python lanza una "excepción". Si no la capturas, el programa
termina. Con try/except puedes manejarlas y decidir qué hacer.
"""

# =============================================================================
# try / except BÁSICO
# =============================================================================
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# =============================================================================
# CAPTURAR LA EXCEPCIÓN (e)
# =============================================================================
try:
    n = int("no soy un número")
except ValueError as e:
    print(f"Error de valor: {e}")

# =============================================================================
# VARIOS except
# =============================================================================
try:
    # num = int("abc")
    # lst = [1, 2]; x = lst[10]
    d = {"a": 1}; x = d["b"]
except ValueError:
    print("Error de conversión.")
except IndexError:
    print("Índice fuera de rango.")
except KeyError:
    print("Clave no encontrada en el diccionario.")

# =============================================================================
# except MÚLTIPLES EN UNA LÍNEA
# =============================================================================
try:
    pass
except (TypeError, AttributeError) as e:
    print(f"Error de tipo o atributo: {e}")

# =============================================================================
# except GENÉRICO (evitar abusar)
# =============================================================================
try:
    # algo que puede fallar
    pass
except Exception as e:
    print(f"Algo falló: {e}")

# =============================================================================
# else Y finally
# =============================================================================
# else: se ejecuta si NO hubo excepción.
# finally: se ejecuta SIEMPRE (haya o no excepción). Útil para cerrar archivos, etc.

f = None
try:
    from pathlib import Path
    ruta = Path(__file__).parent / "ejemplo_lectura.txt"
    f = open(ruta, "r", encoding="utf-8")
    contenido = f.read()
except FileNotFoundError:
    print("Archivo no encontrado.")
else:
    print("Lectura correcta, longitud:", len(contenido))
finally:
    if f is not None and not f.closed:
        f.close()
    print("Bloque finally ejecutado.")

# =============================================================================
# LEVANTAR EXCEPCIONES: raise
# =============================================================================
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    dividir(10, 0)
except ValueError as e:
    print(e)

# =============================================================================
# EXCEPCIONES COMUNES
# =============================================================================
# TypeError, ValueError, KeyError, IndexError, FileNotFoundError,
# ZeroDivisionError, AttributeError, ImportError, etc.

"""
SIGUIENTE: 13_resumen.py — repaso y próximos pasos.
"""
