from tinydb import TinyDB
from tinydb.table import Document

from magnifico import config


class Database:
    def __init__(self, db: str):
        self.db = TinyDB(f"{config.STORAGE}/{db}.json", sort_keys=True, indent=2)
        self.table = self.db.table(db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    def parse(self, payload: dict, doc_id: int) -> Document:
        return Document(payload, doc_id)

    def save(self, document: Document):
        self.table.insert(document)
