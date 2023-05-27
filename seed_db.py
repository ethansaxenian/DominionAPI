import json
import urllib.request
from typing import Any

from deta import Deta
from tqdm import tqdm

from app.core.config import settings
from app.core.utils import case_insensitive
from app.db import get_db

deta = Deta(settings.DETA_PROJECT_KEY)

deta_drive = deta.Drive(settings.DETA_DRIVE_NAME)


def seed_db(data: list[dict[str, Any]]):
    deta_base = next(get_db())

    longest = len(max([card["name"] for card in data], key=len))
    pbar = tqdm(
        list(enumerate(data)),
        bar_format=f"{{desc:<{longest + 9}}} {{percentage:3.0f}}%|{{bar}}| {{n_fmt}}/{{total_fmt}}",
    )
    for key, card in pbar:
        pbar.set_description(f"Seeding {card['name']}")
        deta_base.put(
            {
                **card,
                "key": str(key),
                "name_case_insensitive": case_insensitive(card["name"]),
                "expansion_case_insensitive": case_insensitive(card["expansion"]),
                "types_case_insensitive": [case_insensitive(t) for t in card["types"]],
            }
        )

        # there has to be a better way to upload an image from a url
        img, _ = urllib.request.urlretrieve(card["img_path"], f"tmp/{card['name']}.png")
        deta_drive.put(f'{case_insensitive(card["name"])}.png', path=img)


if __name__ == "__main__":
    with settings.DATA_PATH.open() as file:
        data = json.load(file)
        seed_db(data)
