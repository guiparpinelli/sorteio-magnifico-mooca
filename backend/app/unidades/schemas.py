from typing import List
from pydantic import BaseModel


class Unidade(BaseModel):
    numero: int
    dupla: bool


class Unidades(BaseModel):
    unidades: List[Unidade]
