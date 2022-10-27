from core.utils import CardAsDict, case_insensitive
from db import get_db
from tqdm import tqdm


def seed_db(data: list[CardAsDict]):
    deta_base = next(get_db())

    longest = len(max([card["name"] for card in data], key=len))
    pbar = tqdm(
        list(enumerate(data)),
        bar_format=f"{{desc:<{longest + 8}}} {{percentage:3.0f}}%|{{bar}}| {{n_fmt}}/{{total_fmt}}",
    )
    for (key, card) in pbar:
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
