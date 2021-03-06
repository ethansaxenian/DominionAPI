from core.utils import CardAsDict, case_insensitive
from db import Base, engine, get_db
from db import models


def seed_db(data: list[CardAsDict]):
    sqlalchemy_db = next(get_db())

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    for card in data:
        print(f"Seeding {card['name']}..")
        db_card = models.Card(
            **card,
            name_case_insensitive=case_insensitive(card["name"]),
            expansion_case_insensitive=case_insensitive(card["expansion"]),
            types_case_insensitive=[case_insensitive(t) for t in card["types"]],
        )
        sqlalchemy_db.add(db_card)
        sqlalchemy_db.commit()
        sqlalchemy_db.refresh(db_card)
