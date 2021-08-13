from fastapi import FastAPI

from app import models
from app.router import api_router
from app.db.session import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
