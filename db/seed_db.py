from core.utils import CardAsDict, case_insensitive
from db import Base, engine, get_db
from db import models

from deta import Deta


def seed_db(data: list[CardAsDict]):
    # sqlalchemy_db = next(get_db())

    deta = Deta("b03acyb3_g97LJtGhYxVZMBuVkjgYmJqKbqaKyvdp")
    db = deta.Base("dominion_db")

    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)

    for (key, card) in enumerate(data):
        print(f"Seeding {card['name']}...")
        # db_card = models.Card(
        #     **card,
        #     name_case_insensitive=case_insensitive(card["name"]),
        #     expansion_case_insensitive=case_insensitive(card["expansion"]),
        #     types_case_insensitive=[case_insensitive(t) for t in card["types"]],
        # )
        db.put(
            {
                **card,
                "key": str(key),
                "name_case_insensitive": case_insensitive(card["name"]),
                "expansion_case_insensitive": case_insensitive(card["expansion"]),
                "types_case_insensitive": [case_insensitive(t) for t in card["types"]],
            }
        )
        # sqlalchemy_db.add(db_card)
        # sqlalchemy_db.commit()
        # sqlalchemy_db.refresh(db_card)
