from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, validate_call


class NumeroPositivo(BaseModel):
    numero: PositiveInt

@validate_call() # tem que colocar para o pydantic funcionar
def calculadora(x: NumeroPositivo, y: NumeroPositivo) -> NumeroPositivo:
    return x + y

print(calculadora(1, 5))
print(calculadora(1, 7))