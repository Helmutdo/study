# desafio a, 06 de febero 2026 

# desafio A — tool calling correcto

from pydantic import BaseModel
from typing import Dict, Any

# 1️⃣ Schema: describe SOLO la llamada a la herramienta
class ToolCall(BaseModel):
    tool_name: str
    args: Dict[str, Any]

# 2️⃣ Herramienta real (código que SÍ se ejecuta)
def suma_numeros(num1: int, num2: int) -> int:
    return num1 + num2

# 3️⃣ Registro de herramientas disponibles
TOOLS = {
    "suma_numeros": suma_numeros
}

# 4️⃣ Respuesta simulada del modelo (JSON, no funciones)
respuesta_modelo = {
    "tool_name": "suma_numeros",
    "args": {
        "num1": 1,
        "num2": 2
    }
}

# 5️⃣ Validación con Pydantic
tool_call = ToolCall(**respuesta_modelo)

# 6️⃣ Ejecución REAL (la hace el sistema)
tool_func = TOOLS.get(tool_call.tool_name)

if not tool_func:
    raise ValueError("Herramienta no encontrada")

resultado = tool_func(**tool_call.args)

print("Resultado:", resultado)
