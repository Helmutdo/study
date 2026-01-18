
# PE_2/M4/026.py

# --- Patrones de Diseño: Singleton ---

# Un patrón de diseño es una solución reutilizable a un problema común en el diseño de software.
# No es una librería o un código final, sino una plantilla o descripción de cómo resolver un problema.

# El patrón Singleton asegura que una clase solo tenga una única instancia en toda la aplicación
# y proporciona un punto de acceso global a dicha instancia.

# ¿Cuándo es útil?
# - Para gestionar un recurso compartido, como una conexión a base de datos, un gestor de logging,
#   o un objeto de configuración que debe ser el mismo en todo el sistema.
# - Cuando tener más de una instancia podría llevar a resultados incorrectos o a un estado inconsistente.

# --- Implementación de Singleton usando un decorador ---
# Esta es una forma bastante "pythónica" de implementarlo.

def singleton(cls):
    """Decorador que convierte una clase en un Singleton."""
    instancias = {} # Diccionario para almacenar la única instancia de cada clase singleton

    def obtener_instancia(*args, **kwargs):
        # Si la clase aún no está en nuestro diccionario de instancias...
        if cls not in instancias:
            # ...la creamos y la guardamos.
            instancias[cls] = cls(*args, **kwargs)
            print(f"--- Creando la única instancia de {cls.__name__} ---")
        else:
            print(f"--- Devolviendo la instancia existente de {cls.__name__} ---")
        # Devolvemos la instancia (nueva o existente).
        return instancias[cls]
    
    return obtener_instancia


# --- Usando el decorador Singleton ---

@singleton
class GestorDeConfiguracion:
    def __init__(self):
        # Simulamos la carga de una configuración costosa
        self.config = {
            "url_base": "https://api.miempresa.com",
            "api_key": "ABC123XYZ789",
            "timeout": 30
        }
    
    def obtener_config(self, clave):
        return self.config.get(clave)

@singleton
class GestorDeLogs:
    def __init__(self, fichero_log):
        self.fichero_log = fichero_log
        print(f"El gestor de logs escribirá en {self.fichero_log}")

    def log(self, mensaje):
        print(f"LOG: {mensaje}")


# --- Verificando el comportamiento del Singleton ---

print("Primer intento de obtener el gestor de configuración:")
config1 = GestorDeConfiguracion()

print("\nSegundo intento de obtener el gestor de configuración:")
config2 = GestorDeConfiguracion()

# Comprobamos si ambos objetos son en realidad el mismo
print(f"\n¿Son config1 y config2 el mismo objeto? {config1 is config2}") # Debería ser True

# Usamos una de las variables para acceder a la configuración
print(f"API Key obtenida de config1: {config1.obtener_config('api_key')}")

# Modificamos el estado a través de una variable...
config2.config["timeout"] = 60
print("Timeout modificado a través de config2.")

# ...y el cambio se refleja en la otra, porque son el mismo objeto.
print(f"Nuevo timeout obtenido de config1: {config1.obtener_config('timeout')}")


print("\n--- Probando con otra clase Singleton ---")
# El decorador mantiene las instancias separadas para cada clase
log1 = GestorDeLogs("app.log")
log2 = GestorDeLogs("otro_fichero.log") # El argumento se ignora porque la instancia ya existe

print(f"¿Son log1 y log2 el mismo objeto? {log1 is log2}")
print(f"Fichero de log usado: {log1.fichero_log}") # Sigue siendo "app.log"


# --- Consideraciones sobre Singleton ---
# Aunque puede ser útil, el patrón Singleton a menudo es criticado porque:
# - Introduce un estado global en la aplicación, lo que puede hacer que el código sea más
#   difícil de razonar y de probar (testing).
# - Viola el Principio de Responsabilidad Única (una clase debería hacer una cosa, no dos:
#   hacer su trabajo Y asegurarse de que solo hay una instancia de sí misma).
# - Puede ocultar dependencias. En lugar de pasar un objeto de configuración explícitamente
#   a las funciones que lo necesitan (inyección de dependencias), se accede a él globalmente,
#   lo que hace que el flujo del programa sea menos claro.

# A menudo, la Inyección de Dependencias es considerada una alternativa mejor y más flexible.
