from countries import data_cruda as data

# data = data.splitlines()
# paises = []
# for pais in data:
#     pais = pais.split('-') 
#     pais[0] = pais[0].strip('* ') 
#     paises.append(pais)
# capitales = [pais[-1].strip() for pais in paises]
# print(capitales)

# 
data = [line.strip() for line in data.splitlines() if line.strip()] 
paises_capitales = []

for linea in data:
    partes = linea.split('-')
    if len(partes) >= 2:
        pais = partes[0].strip('* ')
        capital_str = partes[1].strip()
        # considerar múltiples capitales separadas por comas
        capitales_lista = [cap.strip() for cap in capital_str.split(',')]
        # si solo hay una capital, la guardamos como stringo sino como lista
        if len(capitales_lista) == 1:
            capital = capitales_lista[0]
        else:
            capital = capitales_lista
        paises_capitales.append({"pais": pais, "capital": capital})


# diccionario de paises y capitales
diccionario_paises = {item["pais"]: item["capital"] for item in paises_capitales}

# imprimir los paises del diccionario
# for pais, capital in diccionario_paises.items():
#    print(f'{pais} : {capital}')

count = 0
for pais in paises_capitales:
    print(f'{pais["pais"]} ')
    count += 1
#print(f'cantidad de paises: {count}')

# imprime los paises y capitales
for pais in paises_capitales:
    print(f'El pais es {pais["pais"]} y su capital es {pais["capital"]}')

def encontrar_longitud_nombre_pais_mas_largo(lista_paises):
    """Encuentra la longitud del nombre de país más largo en la lista."""
    max_longitud = 0
    for pais in lista_paises:
        if len(pais["pais"]) > max_longitud:
            max_longitud = len(pais["pais"])
    return max_longitud

def encontrar_paises_con_nombre_mas_largo(lista_paises, longitud_maxima):
    """Encuentra y devuelve una lista de países cuyo nombre tiene la longitud máxima."""
    paises_mas_largos = [pais["pais"] for pais in lista_paises if len(pais["pais"]) == longitud_maxima]
    return paises_mas_largos

longitud_maxima = encontrar_longitud_nombre_pais_mas_largo(paises_capitales)
paises_largos = encontrar_paises_con_nombre_mas_largo(paises_capitales, longitud_maxima)

print("País(es) con el nombre más largo:")
for pais in paises_largos:
    print(pais)