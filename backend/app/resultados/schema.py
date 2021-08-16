from datetime import date
from typing import Union
from pydantic import BaseModel

from app.vagas import Vaga
from app.unidades import Unidade


class Resultado(BaseModel):
    class Config:
        orm_mode = True

    id: int
    ano: date.year
    resultado: Union[Vaga, Unidade]
