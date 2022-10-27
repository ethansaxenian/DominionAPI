import random
from typing import Optional

import deta

from core.utils import CardAsDict, case_insensitive


def get_all_cards(db: deta.Base) -> list[CardAsDict]:
    res = db.fetch()
    return res.items


def get_card_by_id(db: deta.Base, id: str) -> Optional[CardAsDict]:
    card = db.get(id)
    return card


def get_random_card(db: deta.Base) -> Optional[CardAsDict]:
    card = random.choice(get_all_cards(db))
    return card


def search_cards_with_query(
    db: deta.Base,
    name: Optional[str],
    expansion: Optional[str],
    card_types: list[str],
    coins: Optional[int],
    potions: Optional[int],
    debt: Optional[int],
    in_supply: Optional[bool],
) -> list[CardAsDict]:

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

    return cards


def post_card(db: deta.Base, new_card: CardAsDict) -> str:
    card = db.put(new_card)
    return card["key"]


def delete_card(db: deta.Base, id: str):
    db.delete(id)


def put_card(db: deta.Base, id: str, card: CardAsDict) -> Optional[Exception]:
    try:
        db.update(card, id)
    except Exception as e:
        return e
