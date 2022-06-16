import asyncio
import json

from app.schemas.card import BaseCard

from core.config import get_settings
from firestore.init_db import db


async def seed(data: list[BaseCard]):
    for id, card in enumerate(data):
        await db.collection("cards").document(str(id)).set({**card, "id": id})


if __name__ == "__main__":
    settings = get_settings()

    with open(f"{settings.ROOT_DIR}/data/dominion_cards.json") as file:
        data = json.load(file)
        asyncio.run(seed(data))
