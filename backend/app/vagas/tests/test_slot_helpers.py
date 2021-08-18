from app.vagas.schemas import Vagas

from app.vagas.helpers import (
    init_vagas,
    set_vagas_cobertas,
    set_vagas_duplas,
    set_vagas_escrituradas,
    set_vagas_piso,
)


def test_set_vagas_escrituradas_retorna_true_se_o_numero_estiver_na_constante_escrituradas():
    T = (
        (42, False),
        (43, True),
        (44, False),
        (100, False),
        (101, True),
        (108, True),
        (109, False),
        (180, False),
        (181, True),
        (182, False),
        (229, False),
        (230, True),
        (231, False),
        (232, True),
        (242, True),
        (243, False),
        (244, True),
        (245, True),
        (258, True),
        (259, False),
    )
    for test in T:
        assert set_vagas_escrituradas(test[0]) == test[1], f"{test[0]} == {test[1]}"


def test_set_vagas_cobertas_retorna_true_se_numero_nao_estiver_na_constante_descobertas():
    T = (
        (43, True),
        (44, False),
        (100, False),
        (101, True),
        (216, True),
        (217, False),
        (228, False),
        (229, True),
    )
    for test in T:
        assert set_vagas_cobertas(test[0]) == test[1], f"{test[0]} == {test[1]}"


def test_set_vagas_duplas_retorna_true_se_numero_nao_estiver_na_constante_vagas_unicas():
    T = (
        (42, True),
        (43, False),
        (47, False),
        (48, True),
        (95, True),
        (96, False),
        (110, False),
        (111, True),
        (180, True),
        (181, False),
        (182, False),
        (183, True),
        (194, True),
        (195, False),
        (198, False),
        (199, True),
    )
    for test in T:
        assert set_vagas_duplas(test[0]) == test[1], f"{test[0]} == {test[1]}"


def test_set_vagas_piso_retorna_subsolo_se_numero_for_menor_que_216():
    T = ((100, "Subsolo"), (215, "Subsolo"), (216, "Terreo"))
    for test in T:
        assert set_vagas_piso(test[0]) == test[1], f"{test[0]} == {test[1]}"


def test_init_vagas_inicializa_vagas_validas_entre_1_e_260():
    u = init_vagas()
    assert isinstance(u, Vagas)
    assert u.vagas[0].numero == 1
    assert u.vagas[-1].numero == 260
