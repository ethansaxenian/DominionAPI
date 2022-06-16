import re


def case_insensitive(string: str):
    return re.sub(r"^\w\s", "", string.lower())
