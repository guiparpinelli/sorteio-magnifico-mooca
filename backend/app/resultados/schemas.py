from datetime import date
from typing import Union
from pydantic import BaseModel

from app.vagas.schemas import Vaga
from app.unidades.schemas import Unidade


class Resultado(BaseModel):
    id: int
    ano: date.year
    resultado: Union[Vaga, Unidade]
