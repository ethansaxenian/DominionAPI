from typing import Optional, Union

from fastapi import APIRouter, Depends, Query
from google.cloud.firestore_v1 import AsyncClient
from sqlalchemy.orm import Session

from app.schemas import Card
from core.config import Settings, get_settings
from db import get_db, search_cards_with_query

router = APIRouter()


@router.get("/", response_model=list[Card])
async def search_cards(
    settings: Settings = Depends(get_settings),
    db: Union[Session, AsyncClient] = Depends(get_db),
    name: Optional[str] = Query(default=None),
    expansion: Optional[str] = Query(default=None),
    card_type: Optional[str] = Query(default=None, alias="type"),
    coins: Optional[int] = Query(default=None),
    potions: Optional[int] = Query(default=None),
    debt: Optional[int] = Query(default=None),
    in_supply: Optional[bool] = Query(default=None, alias="in-supply"),
):
    return await search_cards_with_query(
        db, settings, name, expansion, card_type, coins, potions, debt, in_supply
    )
