import datetime
from typing import List
from pydantic import BaseModel, validator


class Resultado(BaseModel):
    id: int
    ano: int
    resultado: str

    @validator("ano")
    def validar_ano(cls, v):
        if v < 2018 or v > datetime.datetime.now().year:
            raise ValueError("Ano inválido")
        return v
