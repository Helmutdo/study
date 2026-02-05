"""
Ejemplo de respuesta estructurada con Google Gemini.
Carga variables desde .env (.venv es el entorno virtual; las vars se cargan con python-dotenv).
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Cargar .env desde esta carpeta (o desde la raíz del proyecto)
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)
# Opcional: cargar también desde sistema si no hay .env
load_dotenv(override=False)

# API key: google-genai usa GEMINI_API_KEY; Pydantic AI suele usar GOOGLE_API_KEY (misma key)
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise SystemExit("Falta GEMINI_API_KEY o GOOGLE_API_KEY en .env o en el sistema.")

# System prompt desde archivo
SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "system_prompt.txt"
if SYSTEM_PROMPT_PATH.exists():
    system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()
else:
    system_prompt = "Responde de forma clara y estructurada."


def main() -> None:
    client = genai.Client(api_key=api_key)
    user_input = input("Tu mensaje: ").strip() or "Explica en una frase qué es Python."
    contents = f"{system_prompt}\n\nUsuario: {user_input}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
    )
    print(response.text or "(sin texto en la respuesta)")


if __name__ == "__main__":
    main()
