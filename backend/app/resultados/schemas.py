import datetime
from typing import Union
from pydantic import BaseModel, validator

from app.vagas.schemas import Vaga
from app.unidades.schemas import Unidade


class Resultado(BaseModel):
    class Config:
        orm_mode = True

    id: int
    ano: int
    resultado: Union[Vaga, Unidade]

    @validator("ano")
    def foo(cls, v):
        if v < 2018 or v > datetime.datetime.now().year:
            raise ValueError("Ano inválido")
        return v
