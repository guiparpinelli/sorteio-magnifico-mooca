from pydantic import BaseModel

import enums


class Vaga(BaseModel):
    class Config:
        orm_mode = True

    id: int
    numero: int
    piso: enums.Pisos
    coberta: bool
    escriturada: bool
    dupla: bool
    unidade_id: int
