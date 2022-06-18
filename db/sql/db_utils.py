from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from core.config import Settings
from core.utils import CardAsDict, case_insensitive
from db.sql import models


async def sqlalchemy_get_cards(db: Session, settings: Settings) -> list[CardAsDict]:
    cards = db.query(models.Card).all()
    return cards


async def sqlalchemy_get_card(
    db: Session, settings: Settings, id: str
) -> Optional[CardAsDict]:
    card = db.query(models.Card).filter(models.Card.id == id).first()
    return card


async def seqlalchemy_get_random_card(
    db: Session, settings: Settings
) -> Optional[CardAsDict]:
    card = db.query(models.Card).order_by(func.random()).first()
    return card


async def sqlalchemy_search_cards(
    db: Session,
    settings: Settings,
    name: Optional[str] = None,
    expansion: Optional[str] = None,
    card_type: Optional[str] = None,
    coins: Optional[int] = None,
    potions: Optional[int] = None,
    debt: Optional[int] = None,
    in_supply: Optional[bool] = None,
) -> list[CardAsDict]:
    if (
        not name
        and not expansion
        and not card_type
        and not coins
        and not potions
        and not debt
        and not in_supply
    ):
        return []

    cards = db.query(models.Card)
    if name:
        cards = cards.filter(
            models.Card.name_case_insensitive == case_insensitive(name)
        ).all()
    if expansion:
        cards = cards.filter(
            models.Card.expansion_case_insensitive == case_insensitive(expansion)
        ).all()
    if card_type:
        cards = cards.filter(
            models.Card.types_case_insensitive.contains(case_insensitive(card_type))
        ).all()
    if coins:
        cards = cards.filter(models.Card.coins == coins).all()
    if potions:
        cards = cards.filter(models.Card.potions == potions).all()
    if debt:
        cards = cards.filter(models.Card.debt == debt).all()
    if in_supply:
        cards = cards.filter(models.Card.in_supply == in_supply).all()

    return cards
