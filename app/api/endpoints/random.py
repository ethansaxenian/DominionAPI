import random

from fastapi import APIRouter, Depends, HTTPException

from app.schemas import Card
from core.config import Settings, get_settings
from db.init_db import db

router = APIRouter()


@router.get("/", response_model=Card)
async def get_random_card(settings: Settings = Depends(get_settings)):
    docs = db.collection(settings.FIRESTORE_DOCUMENT_NAME).stream()
    cards = [doc.to_dict() async for doc in docs]
    try:
        return random.choice(cards)
    except IndexError:
        raise HTTPException(status_code=404, detail="No cards found")
