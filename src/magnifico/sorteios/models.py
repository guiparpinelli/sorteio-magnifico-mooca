from typing import List

import attr

from magnifico.apartamentos.models import Apartamento
from magnifico.serializer import JSONMixIn
from magnifico.vagas.models import Vaga


@attr.s
class Sorteado:
    apartamento: Apartamento = attr.ib(validator=attr.validators.instance_of(Apartamento))
    vagas: List[Vaga] = attr.ib(validator=attr.validators.instance_of(list), factory=list)


@attr.s
class Sorteio(JSONMixIn):
    ano: int = attr.ib(converter=int)
    resultado: List[Sorteado] = attr.ib(factory=list, validator=attr.validators.instance_of(list))

    def add(self, sorteado: Sorteado):
        self.resultado.append(sorteado)
