import json
import urllib.request

from deta import Deta
from tqdm import tqdm

from core.config import get_settings
from core.utils import CardAsDict, case_insensitive
from db import Base, engine, get_db, models

deta = Deta(settings.DETA_BASE_PROJECT_KEY)

deta_drive = deta.Drive("dominion-images")


def seed_db(data: list[CardAsDict]):
    sqlalchemy_db = next(get_db())

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    longest = len(max([card["name"] for card in data], key=len))
    pbar = tqdm(
        list(enumerate(data)),
        bar_format=f"{{desc:<{longest + 9}}} {{percentage:3.0f}}%|{{bar}}| {{n_fmt}}/{{total_fmt}}",
    )
    for card in pbar:
        pbar.set_description(f"Seeding {card['name']}")
        db_card = models.Card(
            **card,
            name_case_insensitive=case_insensitive(card["name"]),
            expansion_case_insensitive=case_insensitive(card["expansion"]),
            types_case_insensitive=[case_insensitive(t) for t in card["types"]],
        )
        sqlalchemy_db.add(db_card)
        sqlalchemy_db.commit()
        sqlalchemy_db.refresh(db_card)

        # there has to be a better way to upload an image from a url
        img, _ = urllib.request.urlretrieve(
            card["img_path"], f"images/{card['name']}.jpg"
        )
        deta_drive.put(case_insensitive(card["name"]), path=img)


if __name__ == "__main__":
    settings = get_settings()

    with open(settings.DATA_PATH) as file:
        data = json.load(file)
        seed_db(data)
