from functools import cache
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Dominion API"
    PROJECT_DESCRIPTION: str = "An API for the game Dominion"
    API_PREFIX: str = "/api"
    PROJECT_ID: str
    ROOT_DIR: str = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    AUTHOR_NAME: str = "Ethan Saxenian"
    AUTHOR_EMAIL: str = "ethansaxenian@gmail.com"
    LICENSE: str = "MIT"
    FIRESTORE_DOCUMENT_NAME: str = "cards"

    class Config:
        env_file = ".env"
        case_sensitive = True


@cache
def get_settings():
    return Settings()
