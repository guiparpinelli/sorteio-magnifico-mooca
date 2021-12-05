from typing import List

import attr

from magnifico.serializer import JSONMixIn

UM_A_SEIS = tuple("1 2 3 4 5 6".split())
APARTAMENTOS = tuple(x for x in range(11, 277) if str(x).endswith(UM_A_SEIS))


@attr.s
class Apartamento(JSONMixIn):
    numero: int = attr.ib(converter=int)
    duas_vagas: bool = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.duas_vagas = self.set_duas_vagas()

    @numero.validator
    def check_numero(self, attr, value):
        if not str(value).endswith(UM_A_SEIS):
            raise ValueError(f"Número {value} inválido. Os números devem terminar entre 1 e 6.")

    def set_duas_vagas(self) -> bool:
        if str(self.numero).endswith(("2", "5")):
            return False
        else:
            return True if self.numero > 110 else False

    @classmethod
    def create_aps(cls) -> List["Apartamento"]:
        return [cls(numero=n) for n in APARTAMENTOS]
