import os
from enum import Enum

from starlette.config import Config

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Env(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


config = Config(".env")

ENV = config("ENV", cast=Env, default=Env.DEV)
DEBUG = config("DEBUG", cast=bool, default=True)
STORAGE = config("DB_PATH", cast=str, default=os.path.join(BASEDIR, "db/storage"))
