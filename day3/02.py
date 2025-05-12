# segundo ejercicio del dia 3


# ejemplo de uso de la funcion map"""

def map(funcion, iterable):
    """
    aplica la funcion a cada elemento del iterable
    """
    for i in iterable:
        yield funcion(i)
        # devuelve un generador
        # para obtener los valores se puede usar list(map(funcion, iterable))
        # la funcion yield sirve para devolver un valor y pausar la funcion
        # cuando se llama a la funcion de nuevo, se reanuda desde el punto donde se quedo
        # la funcion map devuelve un objeto iterable
        # que se puede conver en una lista o conjunto 

map(lambda x : x**2, [1, 2, 3, 4, 5])
# devuelve un generador
# un generador es un objeto iterable que se puede recorrer

list(map(lambda x : x**2, [1, 2, 3, 4, 5]))
