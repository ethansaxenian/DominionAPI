from fastapi import APIRouter, Depends, HTTPException

from app.api.common import CommonParams, common_parameters
from app.schemas import Card
from core.utils import decode_str_list
from db import get_random_card

router = APIRouter()


@router.get("/", response_model=Card)
def random_card(commons: CommonParams = Depends(common_parameters)):
    card = get_random_card(commons.db)

    if card:
        card.types = decode_str_list(card.types)
        if not commons.include_b64:
            card.img_b64 = None
        return card
    else:
        raise HTTPException(status_code=404, detail="No cards found")
