from pathlib import Path

from pydantic import HttpUrl, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict

description = """
### An API for Dominion card data

<a href="https://github.com/ethansaxenian/DominionAPI" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40"/>
</a>
"""

url_adapter: TypeAdapter[HttpUrl] = TypeAdapter(HttpUrl)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dominion API"
    PROJECT_DESCRIPTION: str = description
    API_PREFIX: str = "/api"
    ROOT_DIR: Path = Path(__file__).resolve().parent.parent
    DATA_PATH: Path = Path(ROOT_DIR.parent, "data", "dominion_cards.json")
    AUTHOR_NAME: str = "Ethan Saxenian"
    AUTHOR_EMAIL: str = "ethansaxenian+github@proton.me"
    LICENSE: str = "MIT"
    CARD_LIST_URL: HttpUrl = url_adapter.validate_strings(
        "http://wiki.dominionstrategy.com/index.php/List_of_cards"
    )
    API_KEY: str | None
    API_KEY_NAME: str = "api_key"
    DETA_PROJECT_KEY: str
    DETA_BASE_NAME: str = "dominion-db"
    DETA_DRIVE_NAME: str = "dominion-images"

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, validate_default=True
    )


settings = Settings()
