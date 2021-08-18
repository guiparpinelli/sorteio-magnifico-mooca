from enum import Enum
from typing import List
from pydantic import BaseModel


class Pisos(Enum):
    Subsolo = "Subsolo"
    Terreo = "Terreo"


class Vaga(BaseModel):
    numero: int
    piso: Pisos
    coberta: bool
    escriturada: bool
    dupla: bool


class Vagas(BaseModel):
    vagas: List[Vaga]
