from app.vagas.enumerators import Pisos
from app.vagas.helpers import (
    set_vagas_cobertas,
    set_vagas_duplas,
    set_vagas_escrituradas,
    set_vagas_piso,
    get_vagas_cobertas,
    get_vagas_descobertas,
    get_vagas_duplas,
    get_vagas_duplas_cobertas,
    get_vagas_duplas_descobertas,
    get_index_vaga_vizinha,
)


def test_init_vagas_inicializa_vagas_validas_entre_1_e_260(raw_vagas):
    assert raw_vagas[0].numero == 1
    assert raw_vagas[-1].numero == 260


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
    T = ((100, Pisos.SUBSOLO), (215, Pisos.SUBSOLO), (216, Pisos.TERREO))
    for test in T:
        assert set_vagas_piso(test[0]) == test[1], f"{test[0]} == {test[1]}"


def test_sorteio_get_vagas_duplas_retorna_apenas_vagas_duplas(raw_vagas):
    vagas_duplas = list(filter(lambda x: x.dupla, raw_vagas))
    assert get_vagas_duplas(raw_vagas) == vagas_duplas


def test_sorteio_get_vagas_cobertas_retorna_apenas_vagas_cobertas(raw_vagas):
    vagas_cobertas = list(filter(lambda x: x.coberta, raw_vagas))
    assert get_vagas_cobertas(raw_vagas) == vagas_cobertas


def test_sorteio_get_vagas_descobertas_retorna_apenas_vagas_descobertas(raw_vagas):
    vagas_descobertas = list(filter(lambda x: not x.coberta, raw_vagas))
    assert get_vagas_descobertas(raw_vagas) == vagas_descobertas


def test_sorteio_get_vagas_duplas_cobertas_retorna_vagas_duplas_e_cobertas(raw_vagas):
    vagas_duplas_e_cobertas = list(filter(lambda x: x.dupla and x.coberta, raw_vagas))
    assert get_vagas_duplas_cobertas(raw_vagas) == vagas_duplas_e_cobertas


def test_sorteio_get_vagas_duplas_descobertas_retorna_vagas_duplas_e_descobertas(raw_vagas):
    vagas_duplas_e_descobertas = list(filter(lambda x: x.dupla and not x.coberta, raw_vagas))
    assert get_vagas_duplas_descobertas(raw_vagas) == vagas_duplas_e_descobertas


def test_sorteio_get_index_vaga_vizinha_retorna_index_vaga_vizinha_para_vagas_duplas(raw_vagas):
    vagas_duplas = list(filter(lambda x: x.dupla, raw_vagas))
    T = (
        (vagas_duplas[0], 0, vagas_duplas[1]),
        (vagas_duplas[1], 1, vagas_duplas[0]),
        (vagas_duplas[43], 43, vagas_duplas[42]),
        (vagas_duplas[89], 89, vagas_duplas[88]),
        (vagas_duplas[90], 90, vagas_duplas[91]),
    )
    for test in T:
        index_vizinha = get_index_vaga_vizinha(test[0], test[1])
        assert vagas_duplas[index_vizinha] == test[2], f"Vaga: {test[0]} | Vizinha: {test[2]}"
