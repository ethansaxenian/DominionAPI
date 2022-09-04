from functools import cache
import os
from typing import Optional

from pydantic import BaseSettings, HttpUrl

description = """
### An API for the game Dominion

<a href="https://github.com/ethansaxenian/DominionAPI" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40"/>
</a>
"""


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dominion API"
    PROJECT_DESCRIPTION: str = description
    API_PREFIX: str = "/api"
    ROOT_DIR: str = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    DATA_PATH: str = os.path.join(ROOT_DIR, "data/dominion_cards.json")
    AUTHOR_NAME: str = "Ethan Saxenian"
    AUTHOR_EMAIL: str = "ethansaxenian@gmail.com"
    LICENSE: str = "MIT"
    CARD_LIST_URL: HttpUrl = "http://wiki.dominionstrategy.com/index.php/List_of_cards"
    DATABASE_URL: str = f"sqlite:///{os.path.join(ROOT_DIR, 'dominion.db')}"
    API_KEY: Optional[str]
    API_KEY_NAME: str = "api_key"
    RENDER_DEPLOY_KEY: Optional[str]
    RENDER_SERVICE_ID: Optional[str]

    class Config:
        env_file = ".env"
        case_sensitive = True

    def using_postgres(self):
        return self.DATABASE_URL.startswith("postgres")


@cache
def get_settings():
    return Settings()
