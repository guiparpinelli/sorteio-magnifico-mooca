import uvicorn
from fastapi import FastAPI

from app.router import api_router


app = FastAPI()
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
