from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Security, status
from sqlalchemy.orm import Session

from app.api.common import CommonParams, common_parameters
from app.auth import get_api_key
from app.schemas import Card
from app.schemas.card import BaseCard
from core.utils import autofill_card_attrs
from db import post_card, delete_card, get_all_cards, get_card_by_id, get_db, put_card

router = APIRouter()


@router.get("/", response_model=list[Card])
def get_cards(
    commons: CommonParams = Depends(common_parameters),
    page: Optional[int] = Query(
        default=None,
        description="The page number to return.",
    ),
    size: int = Query(
        default=100,
        description="The page size.",
    ),
):
    cards = get_all_cards(commons.db)
    if not commons.include_b64:
        for card in cards:
            card.img_b64 = None

    if page is not None:
        return cards[size * (page - 1) : size * page]
    else:
        return cards


@router.get("/{id}", response_model=Card)
def get_card(id: int, commons: CommonParams = Depends(common_parameters)):
    card = get_card_by_id(commons.db, str(id))

    if card:
        if not commons.include_b64:
            card.img_b64 = None
        return card
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Card with id {id} not found"
        )


@router.post("/", response_model=int, dependencies=[Security(get_api_key)])
def add_card(card: BaseCard, db: Session = Depends(get_db)):
    new_card = autofill_card_attrs(card)
    return post_card(db, new_card)


@router.delete("/", response_model=Card, dependencies=[Security(get_api_key)])
def remove_card(id: int, db: Session = Depends(get_db)):
    return delete_card(db, str(id))


@router.put("/{id}", response_model=Card, dependencies=[Security(get_api_key)])
def update_card(id: int, card: BaseCard, db: Session = Depends(get_db)):
    new_card = autofill_card_attrs(card)
    return put_card(db, str(id), new_card)
