from fastapi import APIRouter, Depends, HTTPException, status

from api.common import CommonParams, common_parameters
from api.schemas import Card
from db import get_random_card

router = APIRouter()


@router.get("/", response_model=Card)
def random_card(commons: CommonParams = Depends(common_parameters)):
    card = get_random_card(commons.db)

    if card:
        if not commons.include_b64:
            card.img_b64 = None
        return card
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No cards found"
        )
