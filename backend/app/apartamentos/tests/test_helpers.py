from app.apartamentos import schemas
from app.apartamentos.helpers import set_apartamento_com_duas_vagas


def test_init_apartamentos_inicializa_aps_validos_entre_11_e_276(raw_apartamentos):
    assert isinstance(raw_apartamentos, schemas.Apartamentos)
    assert raw_apartamentos.apartamentos[0].numero == 11
    assert raw_apartamentos.apartamentos[-1].numero == 276


def test_set_duplas_retorna_false_para_aps_abaixo_do_110_ou_com_final_2_e_5():
    T = (
        (106, False),
        (111, True),
        (112, False),
        (113, True),
        (114, True),
        (115, False),
        (116, True),
        (271, True),
        (272, False),
        (273, True),
        (274, True),
        (275, False),
        (276, True),
    )
    for test in T:
        assert set_apartamento_com_duas_vagas(test[0]) == test[1], f"{test[0]} == {test[1]}"
