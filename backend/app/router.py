from fastapi import APIRouter

from app.sorteio.api.urls import router as draw_urls


api_router = APIRouter()
api_router.include_router(draw_urls, prefix="/sorteio")
