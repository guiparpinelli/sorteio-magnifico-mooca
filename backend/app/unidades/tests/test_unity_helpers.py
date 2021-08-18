from app.unidades import schemas
from app.unidades.helpers import set_unidades_com_duas_vagas


def test_init_unidades_inicializa_unidades_validas_entre_11_e_276(raw_unidades):
    assert isinstance(raw_unidades, schemas.Unidades)
    assert raw_unidades.unidades[0].numero == 11
    assert raw_unidades.unidades[-1].numero == 276


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
        assert set_unidades_com_duas_vagas(test[0]) == test[1], f"{test[0]} == {test[1]}"
