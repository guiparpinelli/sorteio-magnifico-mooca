import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.router import api_router
from app.tests.session import TestingSessionLocal


@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def api_client():
    def _make_client():

        app = FastAPI()
        app.include_router(api_router, prefix="/api")

        client = TestClient(app)

        yield client

    yield _make_client
