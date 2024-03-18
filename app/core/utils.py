from app.api.schemas.card import BaseCard, CardCreate


def case_insensitive(string: str) -> str:
    return "".join(c for c in string if c.isalpha()).lower()


def autofill_card_attrs(card: BaseCard) -> CardCreate:
    return CardCreate.model_validate(
        {
            **card.model_dump(),
            "name_case_insensitive": case_insensitive(card.name),
            "expansion_case_insensitive": case_insensitive(card.expansion),
            "types_case_insensitive": [case_insensitive(t) for t in card.types],
        }
    )
