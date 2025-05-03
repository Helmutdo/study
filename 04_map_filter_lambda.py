from countries_data import paises_capitales

# paises nueva lista en mayusculas con map()

paises_mayuscula = list(map(lambda pais: pais["pais"].upper(), paises_capitales))
print(paises_mayuscula)

def contar_letras(pais):
    """cuenta las letras de un pais"""
    return len(pais["pais"])

def contar_letras_lista(paises):
    return sum(map(lambda pais: len(pais["pais"]), paises))

print(contar_letras_lista(paises_capitales))