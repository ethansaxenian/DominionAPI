from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from api import schemas
from core.utils import CardAsDict, case_insensitive
from db import models


def get_all_cards(db: Session) -> list[CardAsDict]:
    cards = db.query(models.Card).all()
    return cards


def get_card_by_id(db: Session, id: str) -> Optional[CardAsDict]:
    card = db.query(models.Card).filter(models.Card.id == id).first()
    return card


def get_random_card(db: Session) -> Optional[CardAsDict]:
    card = db.query(models.Card).order_by(func.random()).first()
    return card


def search_cards_with_query(
    db: Session,
    is_postgress: bool,
    name: Optional[str],
    expansion: Optional[str],
    card_types: list[str],
    coins: Optional[int],
    potions: Optional[int],
    debt: Optional[int],
    in_supply: Optional[bool],
) -> list[CardAsDict]:

    cards = db.query(models.Card)

    if name is not None:
        cards = cards.filter(
            models.Card.name_case_insensitive == case_insensitive(name)
        )
    if expansion is not None:
        cards = cards.filter(
            models.Card.expansion_case_insensitive == case_insensitive(expansion)
        )
    for card_type in card_types:
        card_type_filter = (
            models.Card.types_case_insensitive.any(case_insensitive(card_type))
            if is_postgress
            else models.Card.types_case_insensitive.contains(
                case_insensitive(card_type)
            )
        )
        cards = cards.filter(card_type_filter)
    if coins is not None:
        cards = cards.filter(models.Card.coins == coins)
    if potions is not None:
        cards = cards.filter(models.Card.potions == potions)
    if debt is not None:
        cards = cards.filter(models.Card.debt == debt)
    if in_supply is not None:
        cards = cards.filter(models.Card.in_supply == in_supply)

    return cards.all()


def post_card(db: Session, card: schemas.CardCreate) -> int:
    new_card = models.Card(**card.dict())
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card.id


def delete_card(db: Session, id: str) -> schemas.CardCreate:
    card_to_remove = db.query(models.Card).filter(models.Card.id == id).first()
    db.delete(card_to_remove)
    db.commit()
    return card_to_remove


def put_card(db: Session, id: str, card: schemas.CardCreate):
    card_to_replace = db.query(models.Card).filter(models.Card.id == id).first()
    for k, v in card.dict().items():
        setattr(card_to_replace, k, v)
    db.commit()
    db.refresh(card_to_replace)
    return card_to_replace
