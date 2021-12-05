from itertools import chain
from typing import List

import attr

from magnifico.serializer import JSONMixIn
from magnifico.vagas.enums import Piso
from magnifico.vagas.enums import Tipo


TOTAL_VAGAS = 260
VAGAS_ESCRITURADAS = tuple(
    x for x in chain([43], range(101, 109), [181], range(230, 245, 2), range(245, 259))
)
VAGAS_DESCOBERTAS = tuple(x for x in chain(range(44, 101), range(217, 229)))
VAGAS_UNICAS = tuple(x for x in chain(range(43, 48), range(96, 111), [181, 182], range(195, 199)))


@attr.s(repr=False)
class Vaga(JSONMixIn):
    numero: int = attr.ib(converter=int)
    tipo: Tipo = attr.ib(init=False)
    piso: Piso = attr.ib(init=False)
    dupla: bool = attr.ib(init=False)
    escriturada: bool = attr.ib(init=False)
    vizinha: int = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.tipo = self.set_tipo()
        self.piso = self.set_piso()
        self.dupla: bool = self.is_dupla()
        self.escriturada: bool = self.is_escriturada()
        self.vizinha: int = self.set_vizinha()

    def __repr__(self) -> str:
        return f"Vaga(numero={self.numero}, tipo={self.tipo.name}, piso={self.piso.name})"

    def is_dupla(self) -> bool:
        return self.numero not in VAGAS_UNICAS

    def is_escriturada(self) -> bool:
        return self.numero in VAGAS_ESCRITURADAS

    def set_vizinha(self) -> bool:
        index = 1 if (self.numero < 48 or self.numero > 95) else -1
        return (self.numero - index) if self.numero % 2 == 0 else (self.numero + index)

    def set_piso(self) -> Piso:
        return Piso.Subsolo if self.numero < 216 else Piso.Terreo

    def set_tipo(self) -> Tipo:
        return Tipo.Coberta if self.numero not in VAGAS_DESCOBERTAS else Tipo.Descoberta

    @classmethod
    def create_vagas(cls) -> List["Vaga"]:
        return [cls(numero=n) for n in range(1, TOTAL_VAGAS + 1)]
