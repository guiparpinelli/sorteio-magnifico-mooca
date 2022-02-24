from enum import Enum


class Tipo(str, Enum):
    Coberta = "Coberta"
    Descoberta = "Descoberta"


class Piso(str, Enum):
    Subsolo = "Subsolo"
    Terreo = "Terreo"
