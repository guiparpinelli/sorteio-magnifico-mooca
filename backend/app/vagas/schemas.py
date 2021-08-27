from typing import List
from pydantic import BaseModel

from app.vagas.enumerators import Pisos


class Vaga(BaseModel):
    numero: int
    piso: Pisos
    coberta: bool
    escriturada: bool
    dupla: bool


class Vagas(BaseModel):
    vagas: List[Vaga]
