from typing import Optional

import deta
from fastapi import APIRouter, Depends, Query

from api.schemas import Card, CardType, Expansion
from db import get_db, search_cards_with_query

router = APIRouter()


@router.get("/", response_model=list[Card])
def search_cards(
    db: deta.Base = Depends(get_db),
    name: Optional[str] = Query(
        default=None,
        description="A card name (case-insensitive). Any spaces and special characters are ignored",
    ),
    expansion: Optional[Expansion] = Query(
        default=None,
        description="An expansion (case-insensitive). Any spaces and special characters are ignored",
    ),
    card_types: Optional[list[CardType]] = Query(
        default=[],
        alias="type",
        description="A card type (case-insensitive). Any spaces and special characters are ignored",
    ),
    coins: Optional[int] = Query(
        default=None, description="The amount of coins in a card's cost."
    ),
    potions: Optional[int] = Query(
        default=None, description="The amount of potions in a card's cost."
    ),
    debt: Optional[int] = Query(
        default=None, description="The amount of debt in a card's cost."
    ),
    in_supply: Optional[bool] = Query(
        default=None,
        alias="in-supply",
        description="Whether the card is in the supply.",
    ),
):
    cards = search_cards_with_query(
        db,
        name,
        expansion,
        card_types,
        coins,
        potions,
        debt,
        in_supply,
    )
    return cards
