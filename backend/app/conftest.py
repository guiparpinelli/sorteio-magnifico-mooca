import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.router import api_router
from app.vagas.helpers import init_vagas
from app.apartamentos.helpers import init_aparamentos


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
    return v.vagas


@pytest.fixture
def raw_apartamentos():
    a = init_aparamentos()
    return a.apartamentos
