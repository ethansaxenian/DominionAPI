from base64 import b64encode
from typing import Any

import requests

from api.schemas import BaseCard, CardCreate


def case_insensitive(string: str):
    return "".join(c for c in string if c.isalpha()).lower()


CardAsDict = dict[str, Any]


def autofill_card_attrs(card: BaseCard) -> CardCreate:
    new_card = CardCreate(
        **card.dict(),
        name_case_insensitive=case_insensitive(card.name),
        expansion_case_insensitive=case_insensitive(card.expansion),
        types_case_insensitive=[case_insensitive(t) for t in card.types],
    )
    if new_card.img_b64 is None:
        new_card.img_b64 = b64encode(requests.get(card.img_path).content).decode(
            "utf-8"
        )
    return new_card
