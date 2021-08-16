from app.db.base import Base

# from app.tests.conftest import db_session


def test_base_class_init_db_session(db_session):
    b = Base()
    assert b._session is not None
