palabras = ["Manzana", "banana", "Kiwi", "Naranja", "uva"]

# ordena la lista en orden alfabetico sin importar mayusculas o minusculas
palabras_order = sorted(palabras,  key = lambda s: s.lower())


# ahora hacemos lo mismo pero en orden inverso
palabras_order = sorted(palabras, key = lambda s: s.lower(), reverse=True)


# ordenamos por longitud de la palabra
palabras_order = sorted(palabras, key = lambda s: len(s))


# ordenamos por numero de vocales
# itera como palabra completa y devuelve la cantidad de vocales
# en la palabra, luego ordena por esa cantidad de vocales
def contar_vocales(palabra):
    vocales = 'aeiouAEIOU'
    return sum(1 for letra in palabra if letra in vocales)

# contar vocales en una list
def contar_vocales_lista(palabras):
    return [contar_vocales(palabra) for palabra in palabras]
print(contar_vocales_lista(palabras))