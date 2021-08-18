from sqlalchemy.orm import Session

from app.db.utils import get_db


class Base:
    def __init__(self, db: Session = None):
        self._session = db if db is not None else get_db()
