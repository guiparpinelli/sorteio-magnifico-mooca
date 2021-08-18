from datetime import date
from sqlalchemy import Column, Integer, Date

from app.db.session import Base


class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Date(date.year), unique=True)
    resultado = Column()

    def __repr__(self):
        return f"{self.ano} | {self.resultado}"
