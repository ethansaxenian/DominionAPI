import json

from core.config import settings
from db import seed_db

if __name__ == "__main__":
    with open(settings.DATA_PATH) as file:
        data = json.load(file)
        seed_db(data)
