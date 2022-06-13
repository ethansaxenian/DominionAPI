from pydantic import BaseModel


class Card(BaseModel):
    id: int
    name: str
