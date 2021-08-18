from app.db.base import Base


def test_base_class_init_db_session(db_session):
    b = Base()
    assert b._session is not None
