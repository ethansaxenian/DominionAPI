from typing import Optional

from sqlmodel import Field, SQLModel


class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    name_case_insensitive: str
    expansion: str
    expansion_case_insensitive: str
    types: str
    types_case_insensitive: str
    coins: Optional[int]
    potions: Optional[int]
    debt: Optional[int]
    text: str
    img_path: str
    img_b64: str
    link: str
    in_supply: bool
