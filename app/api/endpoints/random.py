from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from google.cloud.firestore_v1 import AsyncClient
from sqlalchemy.orm import Session

from app.schemas import Card
from core.config import Settings, get_settings
from db import get_db, get_random_card

router = APIRouter()


@router.get("/", response_model=Card)
async def random_card(
    settings: Settings = Depends(get_settings),
    db: Union[Session, AsyncClient] = Depends(get_db),
):
    card = await get_random_card(db, settings)

    if card:
        return card
    else:
        raise HTTPException(status_code=404, detail="No cards found")
