from datetime import date
from typing import Union

from app import schemas


class Resultado(schemas.OrmBase):
    id: int
    ano: date.year
    resultado: Union[schemas.Vaga, schemas.Unidade]
