from core.config import DBType, get_settings

settings = get_settings()

if settings.DB_TYPE == DBType.FIRESTORE:
    from .firestore.init_db import firestore_db as db
    from .firestore.db_utils import (
        firestore_get_cards as get_all_cards,
        firestore_get_card as get_card_by_id,
        firestore_search_cards as search_cards_with_query,
    )
    from .firestore.seed_db import seed_firestore as seed_db
else:
    raise ValueError("Unknown DB type")
