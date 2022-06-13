from fastapi import APIRouter

from app.api.endpoints import cards, random, search

api_router = APIRouter()
api_router.include_router(cards.router, prefix="/cards")
api_router.include_router(search.router, prefix="/search")
api_router.include_router(random.router, prefix="/random")
