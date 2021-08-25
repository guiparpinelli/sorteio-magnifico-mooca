from app import constants
from app.vagas import schemas


def init_vagas() -> schemas.Vagas:
    vagas = schemas.Vagas(
        vagas=[
            schemas.Vaga(
                numero=num,
                piso=set_vagas_piso(num),
                coberta=set_vagas_cobertas(num),
                escriturada=set_vagas_escrituradas(num),
                dupla=set_vagas_duplas(num),
            )
            for num in constants.NUM_VAGAS
        ]
    )
    return vagas


def set_vagas_escrituradas(numero: int) -> bool:
    return True if numero in constants.VAGAS_ESCRITURADAS else False


def set_vagas_cobertas(numero: int) -> bool:
    return True if numero not in constants.VAGAS_DESCOBERTAS else False


def set_vagas_duplas(numero: int) -> bool:
    return True if numero not in constants.VAGAS_UNICAS else False


def set_vagas_piso(numero: int) -> bool:
    return "Subsolo" if numero < 216 else "Terreo"


def get_vagas_duplas(vagas: schemas.Vagas) -> schemas.Vagas:
    return list(filter(lambda x: x.dupla, vagas))


def get_vagas_cobertas(vagas: schemas.Vagas) -> schemas.Vagas:
    return list(filter(lambda x: x.coberta, vagas))


def get_vagas_descobertas(vagas: schemas.Vagas) -> schemas.Vagas:
    return list(filter(lambda x: not x.coberta, vagas))


def get_vagas_duplas_cobertas(vagas: schemas.Vagas) -> schemas.Vagas:
    return list(filter(lambda x: x.dupla and x.coberta, vagas))


def get_vagas_duplas_descobertas(vagas: schemas.Vagas) -> schemas.Vagas:
    return list(filter(lambda x: x.dupla and not x.coberta, vagas))


def get_index_vaga_vizinha(vaga: schemas.Vaga, index: int) -> int:
    dif = 1 if (vaga.numero < 48 or vaga.numero > 95) else -1
    return (index - dif) if vaga.numero % 2 == 0 else (index + dif)
