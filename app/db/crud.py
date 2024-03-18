import random
from typing import Annotated

import deta
from deta.drive import DriveStreamingBody
from fastapi import Depends
from pydantic import ValidationError

from app.api.schemas import CardCreate, DBCard
from app.api.schemas.enums import CardType
from app.core.utils import case_insensitive

from .init_db import get_db, get_drive

DBType = Annotated[deta.Base, Depends(get_db)]
DriveType = Annotated[deta.Drive, Depends(get_drive)]


def get_all_cards(db: deta.Base) -> list[DBCard]:
    res = db.fetch()
    return [DBCard.model_validate(card) for card in res.items]


def get_card_by_id(db: deta.Base, id: str) -> DBCard | None:
    card = db.get(id)
    try:
        return DBCard.model_validate(card)
    except ValidationError:
        return None


def get_random_card(db: deta.Base) -> DBCard | None:
    card = random.choice(get_all_cards(db))
    try:
        return DBCard.model_validate(card)
    except ValidationError:
        return None


def search_cards_with_query(
    db: deta.Base,
    name: str | None,
    expansion: str | None,
    card_types: list[CardType],
    coins: int | None,
    potions: int | None,
    debt: int | None,
    in_supply: bool | None,
) -> list[DBCard]:
    query = {}

    if name is not None:
        query["name_case_insensitive?contains"] = case_insensitive(name)
    if expansion is not None:
        query["expansion_case_insensitive"] = case_insensitive(expansion)
    if coins is not None:
        query["coins"] = coins
    if potions is not None:
        query["potions"] = potions
    if debt is not None:
        query["debt"] = debt
    if in_supply is not None:
        query["in_supply"] = in_supply

    # handle type query with one value
    if len(card_types) == 1:
        query["types_case_insensitive?contains"] = case_insensitive(card_types[0])

    cards = db.fetch(query).items

    # handle query with multiple types
    if len(card_types) > 1:
        case_insensitive_type_query = {
            case_insensitive(card_type) for card_type in card_types
        }

        cards = [
            card
            for card in cards
            if set(card["types_case_insensitive"]) >= case_insensitive_type_query
        ]

    return [DBCard.model_validate(card) for card in cards]


def post_card(db: deta.Base, new_card: CardCreate) -> str:
    card = db.put(new_card.model_dump())
    return card.key


def delete_card(db: deta.Base, id: str) -> None:
    db.delete(id)


def put_card(db: deta.Base, id: str, card: CardCreate) -> Exception | None:
    try:
        db.update(card.model_dump(), id)
    except Exception as e:
        return e


def get_image_by_id(
    db: deta.Base, drive: deta.Drive, id: str
) -> DriveStreamingBody | None:
    if (card := get_card_by_id(db, id)) is None:
        return None

    return drive.get(f"{case_insensitive(card.name)}.png")
