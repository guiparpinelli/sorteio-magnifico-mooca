from enum import Enum
from typing import List
from pydantic import BaseModel, validator

from app import constants


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

    @validator("usuario", always=True)
    def usuario_existe(cls, v):
        if v not in constants.NUM_APARTAMENTOS:
            raise ValueError("Número de apartamento inválido")
        return v
