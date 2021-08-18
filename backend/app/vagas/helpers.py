import itertools

from app.vagas import schemas

VAGAS = tuple([x for x in range(1, 261)])
ESCRITURADAS = frozenset(
    [x for x in itertools.chain([43], range(101, 109), [181], range(230, 245, 2), range(245, 259))]
)
DESCOBERTAS = frozenset([x for x in itertools.chain(range(44, 101), range(217, 229))])
VAGAS_UNICAS = frozenset(
    [x for x in itertools.chain(range(43, 48), range(96, 111), [181, 182], range(195, 199))]
)


def init_vagas() -> schemas.Vagas:
    vagas = schemas.Vagas(
        vagas=[
            schemas.VagaBase(
                numero=num,
                piso=set_vagas_piso(num),
                coberta=set_vagas_cobertas(num),
                escriturada=set_vagas_escrituradas(num),
                dupla=set_vagas_duplas(num),
            )
            for num in VAGAS
        ]
    )
    return vagas


def set_vagas_escrituradas(numero: int) -> bool:
    return True if numero in ESCRITURADAS else False


def set_vagas_cobertas(numero: int) -> bool:
    return True if numero not in DESCOBERTAS else False


def set_vagas_duplas(numero: int) -> bool:
    return True if numero not in VAGAS_UNICAS else False


def set_vagas_piso(numero: int) -> bool:
    return "Subsolo" if numero < 216 else "Terreo"
