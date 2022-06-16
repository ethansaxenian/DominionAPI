from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.schemas import Card
from core.config import Settings, get_settings
from firestore import search_cards_with_query
from firestore.init_db import db

router = APIRouter()


@router.get("/", response_model=list[Card])
async def search_cards(
    settings: Settings = Depends(get_settings),
    name: Optional[str] = Query(default=None),
    expansion: Optional[str] = Query(default=None),
    card_type: Optional[str] = Query(default=None, alias="type"),
    coins: Optional[int] = Query(default=None),
    potions: Optional[int] = Query(default=None),
    debt: Optional[int] = Query(default=None),
):
    cards = await search_cards_with_query(db, settings, name, expansion, card_type, coins, potions, debt)

    if cards:
        return cards
    else:
        raise HTTPException(status_code=404, detail="No cards found")
