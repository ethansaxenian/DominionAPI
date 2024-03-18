from typing import Annotated

from fastapi import APIRouter, Query

from app.api.schemas import CardType, Expansion
from app.api.schemas.card import DBCard
from app.db.crud import DBType, search_cards_with_query

router = APIRouter()


@router.get("/")
def search_cards(
    db: DBType,
    name: Annotated[
        str | None,
        Query(
            description="A card name (case-insensitive). Any spaces and special characters are ignored",
        ),
    ] = None,
    expansion: Annotated[
        Expansion | None,
        Query(
            description="An expansion (case-insensitive). Any spaces and special characters are ignored",
        ),
    ] = None,
    card_types: Annotated[
        list[CardType] | None,
        Query(
            alias="type",
            description="A card type (case-insensitive). Any spaces and special characters are ignored",
        ),
    ] = None,
    coins: Annotated[
        int | None,
        Query(description="The amount of coins in a card's cost."),
    ] = None,
    potions: Annotated[
        int | None, Query(description="The amount of potions in a card's cost.")
    ] = None,
    debt: Annotated[
        int | None,
        Query(description="The amount of debt in a card's cost."),
    ] = None,
    in_supply: Annotated[
        bool | None,
        Query(
            alias="in-supply",
            description="Whether the card is in the supply.",
        ),
    ] = None,
) -> list[DBCard]:
    cards = search_cards_with_query(
        db,
        name,
        expansion,
        card_types or [],
        coins,
        potions,
        debt,
        in_supply,
    )
    return cards
