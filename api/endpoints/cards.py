import deta
from fastapi import APIRouter, Depends, HTTPException, Query, Security, status

from api.auth import get_api_key
from api.schemas import Card
from api.schemas.card import BaseCard
from core.utils import autofill_card_attrs
from db import delete_card, get_all_cards, get_card_by_id, get_db, post_card, put_card

router = APIRouter()


@router.get("/", response_model=list[Card])
def get_cards(
    db: deta.Base = Depends(get_db),
    page: int = Query(
        default=1,
        description="The page number to return.",
    ),
    size: int = Query(
        default=200,
        description="The page size.",
    ),
):
    cards = get_all_cards(db)

    return cards[size * (page - 1) : size * page]


@router.get("/{id}", response_model=Card)
def get_card(id: str, db: deta.Base = Depends(get_db)):
    card = get_card_by_id(db, id)

    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Card with id {id} not found"
        )

    return card


@router.post("/", response_model=str, dependencies=[Security(get_api_key)])
def add_card(card: BaseCard, db: deta.Base = Depends(get_db)):
    new_card = autofill_card_attrs(card)
    return post_card(db, new_card)


@router.delete("/", dependencies=[Security(get_api_key)])
def remove_card(id: str, db: deta.Base = Depends(get_db)):
    delete_card(db, id)
    raise HTTPException(
        status_code=status.HTTP_200_OK, detail=f"Card with id {id} deleted"
    )


@router.put("/{id}", dependencies=[Security(get_api_key)])
def update_card(id: str, card: BaseCard, db: deta.Base = Depends(get_db)):
    new_card = autofill_card_attrs(card)
    res = put_card(db, id, new_card)
    if res is not None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update card with id {id}",
        )
