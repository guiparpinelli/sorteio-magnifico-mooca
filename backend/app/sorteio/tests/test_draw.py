from app.sorteio.draw import Sorteio

s = Sorteio()


def test_sorteio_inicializa_listas_vazias():
    assert s._resultado == []
    assert s._vagas_disponiveis == []


# def test_foo(raw_vagas):
#     vagas_duplas = list(filter(lambda x: x.dupla, raw_vagas.vagas))
#     for _ in vagas_duplas:
#         resultado, idxs = s.sortear_duplas(vagas_duplas)
