from typing import Any

from api.schemas import BaseCard


def case_insensitive(string: str):
    return "".join(c for c in string if c.isalpha()).lower()


CardAsDict = dict[str, Any]


def autofill_card_attrs(card: BaseCard) -> CardAsDict:
    return {
        **card.dict(),
        "name_case_insensitive": case_insensitive(card.name),
        "expansion_case_insensitive": case_insensitive(card.expansion),
        "types_case_insensitive": [case_insensitive(t) for t in card.types],
    }
