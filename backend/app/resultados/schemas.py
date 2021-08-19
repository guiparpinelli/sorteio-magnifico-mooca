import datetime
from typing import List
from pydantic import BaseModel, validator

from app.apartamentos.schemas import Apartamento


class Resultado(BaseModel):
    class Config:
        orm_mode = True

    id: int
    ano: int
    resultado: List[Apartamento]

    @validator("ano")
    def validar_ano(cls, v):
        if v < 2018 or v > datetime.datetime.now().year:
            raise ValueError("Ano inválido")
        return v
