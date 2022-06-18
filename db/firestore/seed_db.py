from core.config import Settings
from core.utils import case_insensitive
from db.firestore import CardAsDict, firestore_db


async def seed_firestore(data: list[CardAsDict], settings: Settings):
    for id, card in enumerate(data):
        print(card["name"])
        await firestore_db.collection(settings.FIRESTORE_COLLECTION_NAME).document(
            str(id)
        ).set(
            {
                **card,
                "name_case_insensitive": case_insensitive(card["name"]),
                "expansion_case_insensitive": case_insensitive(card["expansion"]),
                "types_case_insensitive": [case_insensitive(t) for t in card["types"]],
                "id": id,
            }
        )
