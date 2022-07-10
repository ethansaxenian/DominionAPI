from typing import Any

from sqlmodel import Session

from core.utils import case_insensitive, encode_str_list
from db import Card, create_db_and_tables, drop_db_and_tables, engine


def seed_db(data: list[dict[str, Any]]):

    drop_db_and_tables()
    create_db_and_tables()

    with Session(engine) as session:

        for card in data:
            print(f"Seeding {card['name']}..")
            db_card = Card(
                **{k: v for k, v in card.items() if k != "types"},
                types=encode_str_list(card["types"]),
                name_case_insensitive=case_insensitive(card["name"]),
                expansion_case_insensitive=case_insensitive(card["expansion"]),
                types_case_insensitive=encode_str_list(
                    [case_insensitive(t) for t in card["types"]]
                ),
            )
            session.add(db_card)
            session.commit()
            session.refresh(db_card)
