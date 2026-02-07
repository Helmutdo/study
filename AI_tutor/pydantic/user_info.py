# ejemplo 06 de febero 2026 

from pydantic import BaseModel, Field

#basemodel es la clase base para crear modelos

#definimos el modelo de la respuesta
# el modelo es una clase que hereda de BaseModel
# Field es un decorador para definir los campos del modelo
# ge=0 es la restriccion para que la edad sea mayor o igual a 0
# le=120 es la restriccion para que la edad sea menor o igual a 120

class UserInfo(BaseModel):
    nombre : str
    edad : int = Field(ge=0, le=120)
    email : str 

#definimos la respuesta del modelo
# esta respuesta es un diccionario 
respuesta_modelo = {
    "nombre": "Juan",
    "edad": 30,
    "email": "juan@example.com"
}
#creamos una instancia del modelo con la respuesta
# ** es un operador para desempaquetar el diccionario
# la instancia es un objeto de la clase UserInfo
user = UserInfo(**respuesta_modelo)

#imprimimos el usuario
print(user)
#imprimimos el nombre del usuario
print(user.nombre)
#imprimimos la edad del usuario
print(user.edad)
#imprimimos el email del usuario
print(user.email)
