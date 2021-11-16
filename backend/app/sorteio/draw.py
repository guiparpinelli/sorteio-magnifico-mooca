from typing import Tuple
from random import choice, shuffle

from app.vagas.schemas import Vaga, Vagas
from app.vagas.helpers import get_index_vaga_vizinha
from app.apartamentos.schemas import Apartamentos


def atualizar_vagas_disponiveis(vagas: Vagas, sorteadas: Tuple[Vaga, Vaga]) -> Vagas:
    vaga_1, vaga_2 = sorteadas
    return list(filter(lambda x: x.numero not in [vaga_1.numero, vaga_2.numero], vagas))


def get_par_de_vagas(vagas: Vagas) -> Tuple[Vaga, Vaga]:
    sorteada = choice(vagas)
    index_vizinha = get_index_vaga_vizinha(sorteada, vagas.index(sorteada))
    vizinha = vagas[index_vizinha]
    return (sorteada, vizinha)


def sortear_duplas(vagas: Vagas):
    for vaga in vagas:
        sorteadas = get_par_de_vagas(vagas)


# definir apartamentos
## duplas cobertas -> sortear duplas descobertas
## duplas descobertas -> sortear duplas cobertas
