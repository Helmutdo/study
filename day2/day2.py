# day 2 first file !

# determinemos los factores de un numero como numeros enteros

def factores(num):
    """Devuelve los factores de un numero como numeros enteros"""
    return [i for i in range(1, num + 1) if num % i == 0]   

factores_10 = factores(150)

print(factores_10)