from typing import Optional
from pydantic import BaseModel, HttpUrl
from .enums import Expansion, CardType


class BaseCard(BaseModel):
    name: str
    expansion: Expansion
    types: list[CardType]
    coins: Optional[int]
    potions: Optional[int]
    debt: Optional[int]
    text: str
    img: HttpUrl
    link: HttpUrl


class Card(BaseCard):
    id: int


class CardInDB(Card):
    name_case_insensitive: str
    expansion_case_insensitive: str
    types_case_insensitive: list[str]
