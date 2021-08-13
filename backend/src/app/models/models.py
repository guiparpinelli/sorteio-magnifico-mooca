from sqlalchemy import Column, Integer, Boolean, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from app import schemas
from app.db.base import Base


class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    piso = Column(Enum(schemas.Pisos))
    coberta = Column(Boolean)
    escriturada = Column(Boolean)
    dupla = Column(Boolean)
    unidade_id = Column(Integer, ForeignKey("unidade.numero"))

    unidade = relationship("Unidade", back_populates="vagas")

    def __repr__(self):
        return f"{self.numero} | {self.piso} | {self.coberta} | {self.escriturada} | {self.dupla} | {self.unidade_id}"


class Unidade(Base):
    __tablename__ = "unidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    dupla = Column(Boolean, viewonly=True)

    vagas = relationship("Vaga", back_populates="unidade")

    def __repr__(self):
        return f"{self.numero} | {self.dupla} | {self.vaga.numero}"


class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Date(date.year), unique=True)
    resultado = Column()

    def __repr__(self):
        return f"{self.ano} | {self.resultado}"
