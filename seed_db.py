import asyncio
import json
import sys

from core.config import get_settings
from firestore import seed_firestore


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: seed_db.py firestore")
        sys.exit(1)
    elif sys.argv[1] == "firestore":
        seed_func = seed_firestore
    else:
        print(f"Unknown seed function {sys.argv[1]}")
        sys.exit(1)

    settings = get_settings()

    with open(settings.DATA_PATH) as file:
        data = json.load(file)
        asyncio.run(seed_func(data, settings))
