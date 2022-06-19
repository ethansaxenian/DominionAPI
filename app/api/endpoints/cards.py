from fastapi import APIRouter, Depends, HTTPException

from app.api.common import CommonParams, common_parameters
from app.schemas import Card
from db import get_all_cards, get_card_by_id

router = APIRouter()


@router.get("/", response_model=list[Card])
async def get_cards(commons: CommonParams = Depends(common_parameters)):
    cards = await get_all_cards(commons.db)
    if not commons.include_b64:
        for card in cards:
            card.img_b64 = None
    return cards


@router.get("/{id}", response_model=Card)
async def get_card(id: int, commons: CommonParams = Depends(common_parameters)):
    card = await get_card_by_id(commons.db, str(id))

    if card:
        if not commons.include_b64:
            card.img_b64 = None
        return card
    else:
        raise HTTPException(status_code=404, detail=f"Card with id {id} not found")
