from fastapi import APIRouter, Depends, HTTPException

from app.schemas import Card
from core.config import Settings, get_settings
from db import db, get_all_cards, get_card_by_id

router = APIRouter()


@router.get("/", response_model=list[Card])
async def get_cards(settings: Settings = Depends(get_settings)):
    return await get_all_cards(db, settings)


@router.get("/{id}", response_model=Card)
async def get_card(id: int, settings: Settings = Depends(get_settings)):
    card = await get_card_by_id(db, settings, str(id))

    if card:
        return card
    else:
        raise HTTPException(status_code=404, detail=f"Card with id {id} not found")
