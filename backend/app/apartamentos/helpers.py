from app import constants
from app.apartamentos import schemas


def get_aparamentos() -> schemas.ApartamentoBase:
    aps = schemas.Apartamentos(
        apartamentos=[
            schemas.ApartamentoBase(numero=ap, duas_vagas=set_apartamento_com_duas_vagas(ap))
            for ap in constants.NUM_APARTAMENTOS
        ]
    )
    return aps


def set_apartamento_com_duas_vagas(ap: int) -> bool:
    return True if ap > 110 and not str(ap).endswith(("2", "5")) else False
