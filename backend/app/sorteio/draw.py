from random import choice, shuffle

from app.vagas.schemas import Vaga, Vagas
from app.vagas.helpers import get_index_vaga_vizinha
from app.apartamentos.schemas import Apartamentos


class Sorteio:
    def __init__(self):
        self._resultado = []
        self._vagas_disponiveis = []

    @staticmethod
    def sortear_duplas(vagas: Vagas):
        # setar vagas disponiveis para vagas duplas
        # setar apartamentos concorrendo a vagas disponiveis
        # sortear vagas
        # retornar resultado
        sorteada = choice(vagas)
        index_vizinha = get_index_vaga_vizinha(sorteada, vagas.index(sorteada))
        vizinha = vagas[index_vizinha]
        return (sorteada, vizinha), (vagas.index(sorteada), index_vizinha)
