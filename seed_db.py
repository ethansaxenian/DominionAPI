import json

from core.config import get_settings
from db import seed_db

if __name__ == "__main__":
    settings = get_settings()

    with open(settings.DATA_PATH) as file:
        data = json.load(file)
        seed_db(data)
