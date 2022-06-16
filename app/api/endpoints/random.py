import random

from fastapi import APIRouter, Depends, HTTPException

from app.schemas import Card
from core.config import Settings, get_settings
from firestore import db, get_all_cards

router = APIRouter()


@router.get("/", response_model=Card)
async def get_random_card(settings: Settings = Depends(get_settings)):
    cards = await get_all_cards(db, settings)
    try:
        return random.choice(cards)
    except IndexError:
        raise HTTPException(status_code=404, detail="No cards found")
