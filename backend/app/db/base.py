from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# metadata = MetaData()


# @as_declarative(metadata=metadata)
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
