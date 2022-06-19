from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from app.api.common import CommonParams, common_parameters
from app.schemas import Card
from db import get_random_card

router = APIRouter()


@router.get("/", response_model=Card)
async def random_card(commons: CommonParams = Depends(common_parameters)):
    card = await get_random_card(commons.db, commons.settings)

    if card:
        if not commons.include_b64:
            card.img_b64 = None
        return jsonable_encoder(card, exclude={"img_b64"} if not commons.include_b64 else {})
    else:
        raise HTTPException(status_code=404, detail="No cards found")
