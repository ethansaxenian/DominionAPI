from functools import cache
import os
from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dominion API"
    PROJECT_DESCRIPTION: str = "An API for the game Dominion"
    API_PREFIX: str = "/api"
    PROJECT_ID: str
    ROOT_DIR: str = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    DATA_PATH: str = os.path.join(ROOT_DIR, "data/dominion_cards.json")
    AUTHOR_NAME: str = "Ethan Saxenian"
    AUTHOR_EMAIL: str = "ethansaxenian@gmail.com"
    LICENSE: str = "MIT"
    FIRESTORE_DOCUMENT_NAME: str = "cards"
    GOOGLE_APPLICATION_CREDENTIALS: str
    CARD_LIST_URL: HttpUrl = "http://wiki.dominionstrategy.com/index.php/List_of_cards"

    class Config:
        env_file = ".env"
        case_sensitive = True


@cache
def get_settings():
    return Settings()
