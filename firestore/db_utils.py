from typing import Any, Optional

from google.cloud.firestore_v1 import AsyncClient

from core.config import Settings
from core.utils import case_insensitive

CardFromDB = dict[str, Any]


async def get_all_cards(db: AsyncClient, settings: Settings) -> list[CardFromDB]:
    docs = db.collection(settings.FIRESTORE_DOCUMENT_NAME).stream()
    return [doc.to_dict() async for doc in docs]


async def get_card_by_id(
    db: AsyncClient, settings: Settings, id: str
) -> Optional[CardFromDB]:
    doc = await db.collection(settings.FIRESTORE_DOCUMENT_NAME).document(id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None


async def search_cards_with_query(
    db: AsyncClient,
    settings: Settings,
    name: Optional[str] = None,
    expansion: Optional[str] = None,
    card_type: Optional[str] = None,
    coins: Optional[int] = None,
    potions: Optional[int] = None,
    debt: Optional[int] = None,
    in_supply: Optional[bool] = None,
) -> list[CardFromDB]:
    cards_ref = db.collection(settings.FIRESTORE_DOCUMENT_NAME)

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
