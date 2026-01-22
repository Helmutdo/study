#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  AI TUTOR - LECCIÓN 10: CLASES Y OBJETOS (POO Básica)                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

La programación orientada a objetos (POO) organiza el código en "clases"
(plantillas) e "instancias" (objetos concretos). Atributos guardan datos,
métodos definen comportamiento.
"""

# =============================================================================
# CLASE SIMPLE
# =============================================================================
class Perro:
    # Atributo de clase (compartido por todas las instancias)
    especie = "Canis lupus"

    def __init__(self, nombre, edad):
        """Constructor: se ejecuta al crear una instancia."""
        self.nombre = nombre  # atributos de instancia
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

    def info(self):
        return f"{self.nombre}, {self.edad} años"

# Crear instancias (objetos)
mi_perro = Perro("Max", 3)
tu_perro = Perro("Luna", 2)

print(mi_perro.nombre, mi_perro.edad)
print(mi_perro.ladrar())
print(tu_perro.info())
print(Perro.especie)

# =============================================================================
# self
# =============================================================================
# El primer parámetro de los métodos es siempre self (la instancia).
# Python lo pasa automáticamente; tú no lo pasas al llamar.

# =============================================================================
# HERENCIA
# =============================================================================
# Una clase puede heredar de otra y reutilizar o extender su comportamiento.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"

class Vaca(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Muu"

g = Gato("Felix")
v = Vaca("Clara")
print(g.hablar())
print(v.hablar())

# =============================================================================
# super() — LLAMAR AL PADRE
# =============================================================================
class PerroGuardian(Perro):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # llama al __init__ del padre
        self.raza = raza

    def ladrar(self):
        return super().ladrar() + " (¡Alerta!)"

pg = PerroGuardian("Rex", 4, "Pastor alemán")
print(pg.ladrar())
print(pg.raza)

# =============================================================================
# MÉTODOS ESPECIALES (dunders)
# =============================================================================
# __init__, __str__, __len__, etc. Dan comportamiento especial al objeto.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

p = Punto(3, 4)
print(p)  # usa __str__
print(repr(p))  # usa __repr__

"""
SIGUIENTE: 11_modulos_paquetes.py — import y organización del código.
"""
