from typing import List, Optional
from pydantic import BaseModel, conlist

from app.vagas import schemas


class UnidadeBase(BaseModel):
    numero: int
    duas_vagas: bool


class Unidades(BaseModel):
    unidades: List[UnidadeBase]


class Unidade(UnidadeBase):
    class Config:
        orm_mode = True

    id: int
    vagas: Optional[conlist(item_type=List[schemas.Vaga], max_items=2)]
