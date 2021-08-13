from app import schemas


class Vaga(schemas.OrmBase):
    id: int
    numero: int
    piso: schemas.Pisos
    coberta: bool
    escriturada: bool
    dupla: bool
    unidade_id: int
