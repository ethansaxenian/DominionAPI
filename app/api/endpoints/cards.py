from fastapi import APIRouter, HTTPException, Security, status

from app.api.auth.api_key import get_api_key
from app.api.schemas.card import BaseCard, Card
from app.core.utils import autofill_card_attrs
from app.db.crud import (
    DBType,
    delete_card,
    get_all_cards,
    get_card_by_id,
    post_card,
    put_card,
)

router = APIRouter()


@router.get("/")
def get_cards(db: DBType) -> list[Card]:
    cards = get_all_cards(db)

    return cards


@router.get("/{id}")
def get_card(id: str, db: DBType) -> Card:
    card = get_card_by_id(db, id)

    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Card with id {id} not found"
        )

    return card


@router.post("/", dependencies=[Security(get_api_key)])
def add_card(card: BaseCard, db: DBType) -> str:
    new_card = autofill_card_attrs(card)
    return post_card(db, new_card)


@router.delete("/", dependencies=[Security(get_api_key)])
def remove_card(id: str, db: DBType):
    delete_card(db, id)
    raise HTTPException(
        status_code=status.HTTP_200_OK, detail=f"Card with id {id} deleted"
    )


@router.put("/{id}", dependencies=[Security(get_api_key)])
def update_card(id: str, card: BaseCard, db: DBType):
    new_card = autofill_card_attrs(card)
    res = put_card(db, id, new_card)
    if res is not None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update card with id {id}",
        )
