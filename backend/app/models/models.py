from sqlalchemy import Column, Integer, Boolean, Enum, Date
from sqlalchemy.orm import relationship
from datetime import date

from app import schema
from app.db.base import Base


class Vaga(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    piso = Column(Enum(schema.Pisos))
    coberta = Column(Boolean)
    escriturada = Column(Boolean)
    dupla = Column(Boolean)

    def __repr__(self):
        return f"Vaga(id={self.id}, numero={self.numero}, piso={self.piso}, coberta={self.coberta}, reservada={self.escriturada}, dupla={self.dupla})"


class Unidades(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    dupla = Column(Boolean, viewonly=True)

    def __repr__(self):
        return f"Unidades(id={self.id}, numero={self.numero}, dupla={self.dupla}"


class Resultado(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Date(date.year), unique=True)
