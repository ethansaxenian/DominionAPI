from fastapi import APIRouter, Depends, HTTPException

from app.api.common import CommonParams, common_parameters
from app.schemas import Card
from core.utils import decode_str_list
from db import get_all_cards, get_card_by_id

router = APIRouter()


@router.get("/", response_model=list[Card])
def get_cards(commons: CommonParams = Depends(common_parameters)):
    cards = get_all_cards(commons.db)
    if not commons.include_b64:
        for card in cards:
            card.img_b64 = None
            card.types = decode_str_list(card.types)

    return cards


@router.get("/{id}", response_model=Card)
def get_card(id: int, commons: CommonParams = Depends(common_parameters)):
    card = get_card_by_id(commons.db, str(id))

    if card:
        card.types = decode_str_list(card.types)
        if not commons.include_b64:
            card.img_b64 = None
        return card
    else:
        raise HTTPException(status_code=404, detail=f"Card with id {id} not found")
