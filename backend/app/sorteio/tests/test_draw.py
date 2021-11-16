from app.sorteio.draw import get_par_de_vagas


def test_foo(raw_vagas):
    """Testa se a função retorna o par de vagas correto."""
    vagas_duplas = list(filter(lambda x: x.dupla, raw_vagas))
