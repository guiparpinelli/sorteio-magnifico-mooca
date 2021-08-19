from app import constants
from app.vagas import schemas


def get_vagas() -> schemas.Vagas:
    vagas = schemas.Vagas(
        vagas=[
            schemas.VagaBase(
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
