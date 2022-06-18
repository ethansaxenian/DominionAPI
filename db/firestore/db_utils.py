import random
from typing import Optional

from google.cloud.firestore_v1 import AsyncClient

from core.config import Settings
from core.utils import CardAsDict, case_insensitive


async def firestore_get_cards(db: AsyncClient, settings: Settings) -> list[CardAsDict]:
    docs = db.collection(settings.FIRESTORE_COLLECTION_NAME).stream()
    return [doc.to_dict() async for doc in docs]


async def firestore_get_card(
    db: AsyncClient, settings: Settings, id: str
) -> Optional[CardAsDict]:
    doc = await db.collection(settings.FIRESTORE_COLLECTION_NAME).document(id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None


async def firestore_get_random_card(
    db: AsyncClient, settings: Settings
) -> Optional[CardAsDict]:
    cards = await firestore_get_cards(db, settings)
    if cards:
        return random.choice(cards)
    else:
        return None


async def firestore_search_cards(
    db: AsyncClient,
    settings: Settings,
    name: Optional[str] = None,
    expansion: Optional[str] = None,
    card_type: Optional[str] = None,
    coins: Optional[int] = None,
    potions: Optional[int] = None,
    debt: Optional[int] = None,
    in_supply: Optional[bool] = None,
) -> list[CardAsDict]:
    cards_ref = db.collection(settings.FIRESTORE_COLLECTION_NAME)

    query = cards_ref
    if name:
        query = query.where("name_case_insensitive", "==", case_insensitive(name))
    if expansion:
        query = query.where(
            "expansion_case_insensitive", "==", case_insensitive(expansion)
        )
    if card_type:
        query = query.where(
            "types_case_insensitive", "array_contains", case_insensitive(card_type)
        )
    if coins:
        query = query.where("coins", "==", coins)
    if potions:
        query = query.where("potions", "==", potions)
    if debt:
        query = query.where("debt", "==", debt)
    if in_supply:
        query = query.where("in_supply", "==", in_supply)

    return [doc.to_dict() async for doc in query.stream()]
