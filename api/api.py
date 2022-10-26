from fastapi import APIRouter

from api.endpoints import search
from api.endpoints import cards, random

api_router = APIRouter()
api_router.include_router(cards.router, prefix="/cards")
api_router.include_router(search.router, prefix="/search")
api_router.include_router(random.router, prefix="/random")
