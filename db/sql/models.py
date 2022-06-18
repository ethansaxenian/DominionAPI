from sqlalchemy import ARRAY, Boolean, Column, Integer, JSON, String

from .init_db import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    name_case_insensitive = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    expansion_case_insensitive = Column(String, nullable=False)
    types = Column(JSON, nullable=False)
    types_case_insensitive = Column(JSON, nullable=False)
    coins = Column(Integer)
    potions = Column(Integer)
    debt = Column(Integer)
    text = Column(String, nullable=False)
    img = Column(String, nullable=False)
    link = Column(String, nullable=False)
    in_supply = Column(Boolean, nullable=False)
