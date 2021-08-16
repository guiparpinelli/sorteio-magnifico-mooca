import databases
from enum import Enum
from starlette.config import Config


class Env(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


config = Config(".env")

ENV = config("ENV", cast=Env)
DEBUG = config("DEBUG", cast=bool)
TEST_DATABASE_URL = config(
    "TEST_DATABASE_URL", cast=databases.DatabaseURL, default="sqlite:///:memory:"
)
