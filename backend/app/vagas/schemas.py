from enum import Enum
from typing import List
from pydantic import BaseModel


class Pisos(Enum):
    Subsolo = "Subsolo"
    Terreo = "Terreo"


class VagaBase(BaseModel):
    numero: int
    piso: Pisos
    coberta: bool
    escriturada: bool
    dupla: bool


class Vagas(BaseModel):
    vagas: List[VagaBase]


class Vaga(VagaBase):
    class Config:
        orm_mode = True

    id: int
    usuario: int
