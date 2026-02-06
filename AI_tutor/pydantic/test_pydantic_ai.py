from pydantic import BaseModel

class TestModel(BaseModel):
    value: int

print(TestModel(value=5))
