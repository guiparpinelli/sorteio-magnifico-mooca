from enum import Enum
from starlette.config import Config


class Env(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


config = Config(".env")

ENV = config("ENV", cast=Env)
DEBUG = config("DEBUG", cast=bool)
