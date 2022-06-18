from enum import Enum
from functools import cache
import os
from pydantic import BaseSettings, HttpUrl


class DBType(Enum):
    FIRESTORE = "firestore"
    SQLALCHEMY = "sqlalchemy"


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dominion API"
    PROJECT_DESCRIPTION: str = "An API for the game Dominion"
    API_PREFIX: str = "/api"
    ROOT_DIR: str = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    DATA_PATH: str = os.path.join(ROOT_DIR, "data/dominion_cards.json")
    AUTHOR_NAME: str = "Ethan Saxenian"
    AUTHOR_EMAIL: str = "ethansaxenian@gmail.com"
    LICENSE: str = "MIT"
    FIRESTORE_COLLECTION_NAME: str = "cards"
    FIRESTORE_PROJECT_ID: str
    FIRESTORE_PRIVATE_KEY_ID: str
    FIRESTORE_PRIVATE_KEY: str
    FIRESTORE_CLIENT_EMAIL: str
    FIRESTORE_TOKEN_URI: str
    CARD_LIST_URL: HttpUrl = "http://wiki.dominionstrategy.com/index.php/List_of_cards"
    DATABASE_TYPE: DBType
    DATABASE_URL: str = f"sqlite:///{os.path.join(ROOT_DIR, 'dominion.db')}"

    class Config:
        env_file = ".env"
        case_sensitive = True


@cache
def get_settings():
    return Settings()
