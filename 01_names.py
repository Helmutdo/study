from names_text import texto_crudo

nombres = texto_crudo.splitlines()
print(f'La lista de nombres contiene {len(nombres)} nombres')
#nombres_limpios = [nombre.strip() for nombre in nombres]
mayor = 0
for nombre in nombres:
    if len(nombre) > mayor:
        mayor = len(nombre)
        nombre_mayor = nombre
print(f'El nombre maoyr de la lista es {nombre_mayor} y tiene {mayor} caracteres')

#nombre_big = max(nombres, key=len)
nombre_small = min(nombres, key=len)
print(f'el nombre mas corto de la lista es {nombre_small} y tiene {len(nombre_small)} caracteres')

vocales = 'aeiou'
cuenta_nombres_vocal= 0
for nombre in nombres:
    if nombre[-1] in vocales:
        #print(f'El nombre{nombre} termina en vocal')
        cuenta_nombres_vocal += 1
print(f'La lista contiene {cuenta_nombres_vocal} nombres que terminan en vocal')

# nombres_vocal = [nombre for nombre in nombres if nombre[-1] in  vocales]
#print(len(nombres_vocal))

letra = 'n'
letra_in_nombre = [nombre_letra for nombre_letra in nombres if letra in nombre_letra]
print(len(letra_in_nombre))


suma = 0
for nombre in nombres:
    suma += len(nombre)

print(f'promedio de caracteres por nobmre es {int(suma/len(nombres))}')

promedio = sum(len(nombre) for nombre in nombres) / len(nombres)
print(promedio)

def contar_frecuencia_longitudes(nombres):
    frecuencias = {}
    for nombre in nombres:
        longitud = len(nombre)
        if longitud in frecuencias:
            frecuencias[longitud] += 1
        else:
            frecuencias[longitud] = 1
    return frecuencias

f = contar_frecuencia_longitudes(nombres)
f_ordered = sorted(f.items(), key= lambda x: x[1])

print(f)

# for longitud, frecuencia in f.items():
#     print(f'La longitud de {longitud} caracteres se repite en {frecuencia} nombres')

print(f_ordered)

# for longitud, frecuencia in f_ordered:
#     print(f'La longitud de {longitud} caracteres se repite en {frecuencia} nombres')