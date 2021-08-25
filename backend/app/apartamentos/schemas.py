from typing import List
from pydantic import BaseModel


class Apartamento(BaseModel):
    numero: int
    duas_vagas: bool


class Apartamentos(BaseModel):
    apartamentos: List[Apartamento]
