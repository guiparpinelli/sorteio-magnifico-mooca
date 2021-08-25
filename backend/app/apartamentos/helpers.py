from app import constants
from app.apartamentos import schemas


def init_aparamentos() -> schemas.Apartamento:
    aps = schemas.Apartamentos(
        apartamentos=[
            schemas.Apartamento(numero=ap, duas_vagas=set_apartamento_com_duas_vagas(ap))
            for ap in constants.NUM_APARTAMENTOS
        ]
    )
    return aps


def set_apartamento_com_duas_vagas(ap: int) -> bool:
    return True if ap > 110 and not str(ap).endswith(("2", "5")) else False


def get_aps_duas_vagas(aps: schemas.Apartamentos) -> schemas.Apartamentos:
    return list(filter(lambda x: x.duas_vagas, aps))
