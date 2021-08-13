from pydantic import validator

from app import schemas

UM_A_SEIS = ("1", "2", "3", "4", "5", "6")


class Unidade(schemas.OrmBase):
    id: int
    numero: int
    dupla: bool

    @validator("numero", pre=True)
    def apartamentos(cls, v):
        if v < 11 or v > 276:
            raise ValueError("O numero dos apratamentos devem ser entre 11 e 276")
        if not str(v).endswith(UM_A_SEIS):
            raise ValueError("O numero do apartamento deve terminar entre 1 e 6")
