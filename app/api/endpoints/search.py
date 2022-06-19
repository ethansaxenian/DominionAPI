from typing import Optional

from fastapi import APIRouter, Depends, Query

from app.api.common import CommonParams, common_parameters
from app.schemas import Card
from db import search_cards_with_query

router = APIRouter()


@router.get("/", response_model=list[Card])
def search_cards(
    commons: CommonParams = Depends(common_parameters),
    name: Optional[str] = Query(
        default=None,
        description="A card name (case-insensitive). Any spaces and special characters are ignored",
    ),
    expansion: Optional[str] = Query(
        default=None,
        description="An expansion (case-insensitive). Any spaces and special characters are ignored",
    ),
    card_types: Optional[list[str]] = Query(
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
        commons.db,
        commons.settings.using_postgres(),
        name,
        expansion,
        card_types,
        coins,
        potions,
        debt,
        in_supply,
    )
    if not commons.include_b64:
        for card in cards:
            card.img_b64 = None
    return cards
