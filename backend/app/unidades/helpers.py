from app.unidades import schemas

UM_A_SEIS = tuple([str(x) for x in range(1, 7)])
APARTAMENTOS = tuple([x for x in range(11, 277) if str(x).endswith(UM_A_SEIS)])


def init_unidades() -> schemas.Unidades:
    unidades = schemas.Unidades(
        unidades=[
            schemas.Unidade(numero=ap, dupla=set_unidades_com_duas_vagas(ap)) for ap in APARTAMENTOS
        ]
    )
    return unidades


def set_unidades_com_duas_vagas(ap: int) -> bool:
    return True if ap > 110 and not str(ap).endswith(("2", "5")) else False
