# Respuestas estructuradas

Temas: **Pydantic AI**, **Google Gemini API**, variables de entorno (`.env` / `.venv`), **system prompt**.

## Setup

```bash
# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# Copiar y rellenar API key
cp .env.example .env
# Editar .env y poner tu GEMINI_API_KEY (https://aistudio.google.com/apikey)
```

## Carga de variables (.env y sistema)

- **`.venv`**: carpeta del entorno virtual (no guarda variables por defecto).
- **`.env`**: archivo con variables (API key, etc.). No se sube a git.
- **`python-dotenv`**: en el código se usa `load_dotenv()` para cargar `.env`; si no existe, se usan las variables ya definidas en el **sistema** (export en la shell, etc.).

El script `01_ejemplo_gemini.py` carga primero `.env` y luego usa `GEMINI_API_KEY` o `GOOGLE_API_KEY`.

## Ejemplo mínimo (google-genai)

```python
from google import genai

client = genai.Client()  # usa GEMINI_API_KEY del entorno si existe
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=input(),
)
print(response.text)
```

En este repo el ejemplo completo está en `01_ejemplo_gemini.py`: carga `.env`, lee el **system prompt** desde `system_prompt.txt` y genera contenido con Gemini.

## Archivos

| Archivo              | Descripción                          |
|----------------------|--------------------------------------|
| `requirements.txt`   | pydantic-ai, google-genai, python-dotenv |
| `.env.example`       | Plantilla para API key               |
| `system_prompt.txt`  | System prompt por defecto             |
| `01_ejemplo_gemini.py` | Ejemplo con Client + .env + system prompt |
