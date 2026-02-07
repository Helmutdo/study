# pydantic base model

# 🔹 Paso 1: Schema (contrato)
from pydantic import BaseModel

class Clima(BaseModel):
    temperatura: float
    humedad : int

# 🔹 Paso 2: Simular respuesta del modelo (JSON)
respuesta_modelo = {
    "temperatura": 20.0,
    #"temperatura": "calor", # el error es que la temperatura debe ser un float
    "humedad": 50
    }

# 🔹 Paso 3: Validación con Pydantic
clima = Clima(**respuesta_modelo)
print(clima)

print(respuesta_modelo)

