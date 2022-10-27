from sqlalchemy import Boolean, Column, Integer, JSON, String
from sqlalchemy.dialects.postgresql import ARRAY

from core.config import get_settings
from .init_db import Base

settings = get_settings()


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    name_case_insensitive = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    expansion_case_insensitive = Column(String, nullable=False)
    types = Column(ARRAY(String) if settings.using_postgres() else JSON, nullable=False)
    types_case_insensitive = Column(
        ARRAY(String) if settings.using_postgres() else JSON, nullable=False
    )
    coins = Column(Integer)
    potions = Column(Integer)
    debt = Column(Integer)
    text = Column(String, nullable=False)
    img_path = Column(String, nullable=False)
    img_b64 = Column(String, nullable=False)
    link = Column(String, nullable=False)
    in_supply = Column(Boolean, nullable=False)
