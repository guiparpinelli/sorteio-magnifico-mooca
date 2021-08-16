from sqlalchemy import Column, Integer, Boolean, Date
from sqlalchemy.orm import relationship

from app.db.session import Base


class Unidade(Base):
    __tablename__ = "unidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    dupla = Column(Boolean, viewonly=True)

    vagas = relationship("Vaga", back_populates="unidade")

    def __repr__(self):
        return f"{self.numero} | {self.dupla} | {self.vaga.numero}"
