#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import List

import constants
from tinydb import TinyDB

db = TinyDB("db.json")


class Piso(str, Enum):
    Subsolo = "Subsolo"
    Terreo = "Terreo"


def is_escriturada(numero: int) -> bool:
    return numero in constants.VAGAS_ESCRITURADAS


def is_coberta(numero: int) -> bool:
    return numero not in constants.VAGAS_DESCOBERTAS


def is_dupla(numero: int) -> bool:
    return numero not in constants.VAGAS_UNICAS


def set_piso(numero: int) -> Piso:
    piso = Piso.Subsolo if numero < 216 else Piso.Terreo
    return piso.value


def set_vizinha(numero: int) -> int:
    if not is_dupla(numero):
        return

    index = 1 if (numero < 48 or numero > 95) else -1
    return (numero - index) if numero % 2 == 0 else (numero + index)


@dataclass(frozen=True)
class Vaga:
    numero: int
    piso: Piso
    coberta: bool
    escriturada: bool
    dupla: bool
    vizinha: int

    @classmethod
    def from_numero(cls, num: int) -> Vaga:
        return cls(
            numero=num,
            piso=set_piso(num),
            coberta=is_coberta(num),
            escriturada=is_escriturada(num),
            dupla=is_dupla(num),
            vizinha=set_vizinha(num),
        )


TOTAL_VAGAS = 261


@dataclass
class Vagas:
    disponiveis: List[Vaga] = field(default_factory=list)
    sorteadas: List[Vaga] = field(default_factory=list)

    @classmethod
    def new(cls) -> Vagas:
        return cls(disponiveis=[Vaga.from_numero(num=n) for n in range(1, TOTAL_VAGAS)])


class NumeroDeApartamentoInvalido(Exception):
    pass


def set_duas_vagas(numero: int) -> bool:
    if str(numero).endswith(("2", "5")):
        return False
    else:
        return True if numero > 110 else False


@dataclass(frozen=True)
class Apartamento:
    numero: int
    duas_vagas: bool
    vagas_atuais: List[Vaga] = field(default_factory=list)

    @classmethod
    def from_numero(cls, num: int) -> Apartamento:
        if not str(num).endswith(constants.UM_A_SEIS):
            raise NumeroDeApartamentoInvalido("O numero dos apartamentos terminam entre 1 e 6")
        return cls(numero=num, duas_vagas=set_duas_vagas(num))

    @classmethod
    def new_apartamentos(cls) -> List[Apartamento]:
        return [
            cls(numero=num, duas_vagas=set_duas_vagas(num)) for num in constants.TOTAL_APARTAMENTOS
        ]
