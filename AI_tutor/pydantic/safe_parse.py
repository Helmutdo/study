# ejemplo n2, 06 de febero 2026 

from pydantic import BaseModel, ValidationError

class Score(BaseModel):
    score : int

respuesta_modelo = {
    "score": "alto"
}

try: 
    instance_score = Score(**respuesta_modelo)
    print("Score válido:", instance_score.score)
except ValidationError as e:
    print("Salida invlida del modelo")
    print(e)
    print("Usando valor por defecto")
    instance_score = Score(score=0)

print("Score final:", instance_score.score)