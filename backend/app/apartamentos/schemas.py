from typing import List, Tuple
from pydantic import BaseModel, validator

from app.vagas import schemas


class ApartamentoBase(BaseModel):
    numero: int
    duas_vagas: bool


class Apartamentos(BaseModel):
    unidades: List[ApartamentoBase]


class Apartamento(ApartamentoBase):
    class Config:
        orm_mode = True

    id: int
    vagas: Tuple[schemas.VagaBase]

    @validator("vagas", always=True)
    def foo(cls, v, values):
        if values["duas_vagas"] and len(v) > 2:
            raise ValueError("Limite de até 2 vagas.")
        if not values["duas_vagas"] and len(v) > 1:
            raise ValueError("Limite de até 1 vaga.")
        return v
