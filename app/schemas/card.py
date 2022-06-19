from typing import Optional
from pydantic import BaseModel, HttpUrl, constr
from .enums import Expansion, CardType


class BaseCard(BaseModel):
    name: str
    expansion: Expansion
    types: list[CardType]
    coins: Optional[int]
    potions: Optional[int]
    debt: Optional[int]
    text: str
    img_path: HttpUrl
    img_b64: Optional[constr(max_length=100000)]
    link: HttpUrl
    in_supply: bool


class Card(BaseCard):
    id: int

    class Config:
        orm_mode = True


class CardInDB(Card):
    name_case_insensitive: str
    expansion_case_insensitive: str
    types_case_insensitive: list[str]
