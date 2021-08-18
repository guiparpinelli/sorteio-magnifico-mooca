from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.vagas.schemas import Pisos
from app.db.session import Base


class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    piso = Column(Enum(Pisos))
    coberta = Column(Boolean)
    escriturada = Column(Boolean)
    dupla = Column(Boolean)
    unidade_id = Column(Integer, ForeignKey("unidades.numero"))

    unidade = relationship("Unidade", back_populates="vagas")

    def __repr__(self):
        return f"{self.numero} | {self.piso} | {self.coberta} | {self.escriturada} | {self.dupla} | {self.unidade_id}"
