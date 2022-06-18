from typing import Any


def case_insensitive(string: str):
    return "".join(c for c in string if c.isalpha()).lower()


CardAsDict = dict[str, Any]
