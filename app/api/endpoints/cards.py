from base64 import b64encode

import requests
from fastapi import APIRouter, Depends, HTTPException, Security, status
from sqlalchemy.orm import Session

from app.api.common import CommonParams, common_parameters
from app.auth import get_api_key
from app.schemas import Card
from app.schemas.card import BaseCard, CardCreate
from core.utils import case_insensitive
from db import create_card, delete_card, get_all_cards, get_card_by_id, get_db

router = APIRouter()


@router.get("/", response_model=list[Card])
def get_cards(commons: CommonParams = Depends(common_parameters)):
    cards = get_all_cards(commons.db)
    if not commons.include_b64:
        for card in cards:
            card.img_b64 = None
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
    new_card = CardCreate(
        **card.dict(),
        name_case_insensitive=case_insensitive(card.name),
        expansion_case_insensitive=case_insensitive(card.expansion),
        types_case_insensitive=[case_insensitive(t) for t in card.types],
    )
    if new_card.img_b64 is None:
        new_card.img_b64 = b64encode(requests.get(card.img_path).content).decode(
            "utf-8"
        )
    return create_card(db, new_card)


@router.delete("/", response_model=Card, dependencies=[Security(get_api_key)])
def remove_card(id: int, db: Session = Depends(get_db)):
    return delete_card(db, str(id))
