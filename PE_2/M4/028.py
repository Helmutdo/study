# PE_2/M4/028.py

# --- Patrones de Diseño: Observador (Observer Pattern) ---

# El patrón Observador define una relación de dependencia de uno a muchos
# entre objetos, de modo que cuando un objeto (el "sujeto" u "observable")
# cambia su estado, todos sus dependientes (los "observadores") son
# notificados y actualizados automáticamente.

# Es la base de muchos sistemas de "eventos" y "listeners".

# Componentes del patrón:
# 1.  **Sujeto (Subject/Observable)**: Mantiene una lista de observadores y
#     tiene métodos para añadir, eliminar y notificar a los observadores.
# 2.  **Observador (Observer)**: Define una interfaz de actualización para los
#     objetos que deben ser notificados de los cambios en un sujeto.

from abc import ABC, abstractmethod

# --- Interfaz del Sujeto ---
class ISubject(ABC):
    @abstractmethod
    def registrar_observador(self, observador):
        pass

    @abstractmethod
    def eliminar_observador(self, observador):
        pass

    @abstractmethod
    def notificar_observadores(self):
        pass

# --- Interfaz del Observador ---
class IObserver(ABC):
    @abstractmethod
    def actualizar(self, sujeto):
        """Recibe una notificación del sujeto."""
        pass

# --- Sujeto Concreto ---
# Este es el objeto que será "observado".

class SensorDeTemperatura(ISubject):
    _temperatura = 0
    _observadores = []

    def registrar_observador(self, observador):
        print(f"Sensor: Registrando al observador {observador.__class__.__name__}")
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        print(f"Sensor: Eliminando al observador {observador.__class__.__name__}")
        self._observadores.remove(observador)

    def notificar_observadores(self):
        print("\nSensor: Notificando a todos los observadores...")
        for observador in self._observadores:
            observador.actualizar(self)

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, nuevo_valor):
        """
        Cuando la temperatura cambia, se notifica a los observadores.
        """
        if self._temperatura != nuevo_valor:
            print(f"\n¡CAMBIO DE ESTADO! Nueva temperatura: {nuevo_valor}°C")
            self._temperatura = nuevo_valor
            self.notificar_observadores()


# --- Observadores Concretos ---
# Estos son los objetos que reaccionan a los cambios del sujeto.

class PantallaDigital(IObserver):
    def actualizar(self, sujeto):
        if isinstance(sujeto, SensorDeTemperatura):
            print(f"  [Pantalla Digital]: La temperatura actual es {sujeto.temperatura}°C")

class SistemaDeAlarma(IObserver):
    def __init__(self, umbral):
        self._umbral = umbral

    def actualizar(self, sujeto):
        if isinstance(sujeto, SensorDeTemperatura):
            if sujeto.temperatura > self._umbral:
                print(f"  [Alarma]: ¡ALERTA! Temperatura ({sujeto.temperatura}°C) ha superado el umbral de {self._umbral}°C!")
            else:
                print(f"  [Alarma]: Temperatura ({sujeto.temperatura}°C) dentro de los límites normales.")

class RegistradorDeDatos(IObserver):
    def actualizar(self, sujeto):
         if isinstance(sujeto, SensorDeTemperatura):
            print(f"  [Registrador]: Guardando en log... Nueva temperatura registrada: {sujeto.temperatura}°C")


# --- Demostración ---
# 1. Creamos el sujeto (el sensor)
sensor = SensorDeTemperatura()

# 2. Creamos los observadores
pantalla = PantallaDigital()
alarma = SistemaDeAlarma(umbral=30)
registrador = RegistradorDeDatos()

# 3. Registramos los observadores en el sujeto
sensor.registrar_observador(pantalla)
sensor.registrar_observador(alarma)
sensor.registrar_observador(registrador)

# 4. Cambiamos el estado del sujeto. Esto debería notificar a todos los observadores.
sensor.temperatura = 25
sensor.temperatura = 35 # Este cambio debería disparar la alarma

# 5. Eliminamos un observador
sensor.eliminar_observador(pantalla)

# 6. Cambiamos el estado de nuevo. Ahora la pantalla ya no será notificada.
sensor.temperatura = 28

# Este patrón es muy útil para construir sistemas desacoplados. El sensor no sabe
# qué es una "Pantalla" o una "Alarma", solo sabe que tiene una lista de objetos
# a los que notificar. De igual forma, los observadores no necesitan saber los
# detalles internos del sensor, solo reaccionan a sus notificaciones.
