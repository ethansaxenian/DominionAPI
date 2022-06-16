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
