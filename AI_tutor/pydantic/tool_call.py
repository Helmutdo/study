# ejemplo n3, 06 de febero 2026 

from pydantic import BaseModel
from typing import Dict, Any

# 1️⃣ Schema del tool call
class ToolCall(BaseModel):
    tool_name: str
    args: Dict[str, Any]

# 2️⃣ Herramientas reales
def get_weather(city: str) -> dict:
    return {
        "city": city,
        "temperature": 22,
        "humidity": 60
    }

TOOLS = {
    "get_weather": get_weather
}

# 3️⃣ Respuesta simulada del modelo
respuesta_modelo = {
    "tool_name": "get_weather",
    "args": {
        "city": "Santiago"
    }
}

# 4️⃣ Validación
tool_call = ToolCall(**respuesta_modelo)

# 5️⃣ Ejecución REAL (esto es CLAVE)
tool_func = TOOLS.get(tool_call.tool_name)

if tool_func:
    result = tool_func(**tool_call.args)
    print("Resultado de la herramienta:", result)
else:
    print("Herramienta no encontrada")
