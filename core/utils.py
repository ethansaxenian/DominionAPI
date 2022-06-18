import re
from typing import Any


def case_insensitive(string: str):
    return re.sub(r"^\w\s", "", string.lower())


CardAsDict = dict[str, Any]
