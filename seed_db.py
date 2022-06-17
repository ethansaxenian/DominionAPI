import asyncio
import json

from core.config import Settings, get_settings
from core.utils import case_insensitive
from firestore import db, CardAsDict


async def seed(data: list[CardAsDict], settings: Settings):
    for id, card in enumerate(data):
        print(card["name"])
        await db.collection(settings.FIRESTORE_DOCUMENT_NAME).document(str(id)).set(
            {
                **card,
                "name_case_insensitive": case_insensitive(card["name"]),
                "expansion_case_insensitive": case_insensitive(card["expansion"]),
                "types_case_insensitive": [case_insensitive(t) for t in card["types"]],
                "id": id,
            }
        )


if __name__ == "__main__":
    settings = get_settings()

    with open(f"{settings.ROOT_DIR}/data/dominion_cards.json") as file:
        data = json.load(file)
        asyncio.run(seed(data, settings))
