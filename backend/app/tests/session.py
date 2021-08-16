from sqlalchemy import create_engine, orm

from app import config as app_config

engine = create_engine(str(app_config.TEST_DATABASE_URL))
TestingSessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
