from typing import Optional

from pydantic import BaseModel, HttpUrl

from .enums import CardType, Expansion


class BaseCard(BaseModel):
    name: str
    expansion: Expansion
    types: list[CardType]
    coins: Optional[int]
    potions: Optional[int]
    debt: Optional[int]
    text: str
    img_path: HttpUrl
    link: HttpUrl
    in_supply: bool


class CardCreate(BaseCard):
    name_case_insensitive: str
    expansion_case_insensitive: str
    types_case_insensitive: list[str]


class Card(BaseCard):
    key: str


class DBCard(Card, BaseCard):
    pass
