from typing import Optional

from sqlalchemy import func
from sqlmodel import Session, select

from core.utils import case_insensitive, decode_str_list
from db import Card, models


def get_all_cards(db: Session) -> list[Card]:
    cards = select(Card)
    return db.exec(cards).all()


def get_card_by_id(db: Session, id: str) -> Optional[Card]:
    card = db.get(Card, id)
    return card


def get_random_card(db: Session) -> Optional[Card]:
    card = select(models.Card).order_by(func.random())
    return db.exec(card).first()


def search_cards_with_query(
    db: Session,
    name: Optional[str],
    expansion: Optional[str],
    card_types: list[str],
    coins: Optional[int],
    potions: Optional[int],
    debt: Optional[int],
    in_supply: Optional[bool],
) -> list[Card]:

    cards = select(Card)

    if name is not None:
        cards = cards.where(Card.name_case_insensitive == case_insensitive(name))
    if expansion is not None:
        cards = cards.where(
            Card.expansion_case_insensitive == case_insensitive(expansion)
        )
    for card_type in card_types:
        # TODO: fix this
        cards = cards.where(case_insensitive(card_type) in decode_str_list(Card.types_case_insensitive))
    if coins is not None:
        cards = cards.where(Card.coins == coins)
    if potions is not None:
        cards = cards.where(Card.potions == potions)
    if debt is not None:
        cards = cards.where(Card.debt == debt)
    if in_supply is not None:
        cards = cards.where(Card.in_supply == in_supply)

    return db.exec(cards).all()
