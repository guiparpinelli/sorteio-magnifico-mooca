import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

# from sqlalchemy import create_engine, orm

# from app import config as app_config
from app.router import api_router
from app.vagas.helpers import init_vagas
from app.unidades.helpers import init_unidades


# engine = create_engine(str(app_config.TEST_DATABASE_URL))
# TestingSessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @pytest.fixture
# def db_session():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@pytest.fixture
def api_client():
    def _make_client():

        app = FastAPI()
        app.include_router(api_router, prefix="/api")

        client = TestClient(app)

        yield client

    yield _make_client


@pytest.fixture
def raw_vagas():
    v = init_vagas()
    return v


@pytest.fixture
def raw_unidades():
    u = init_unidades()
    return u