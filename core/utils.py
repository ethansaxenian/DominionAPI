def case_insensitive(string: str):
    return "".join(c for c in string if c.isalpha()).lower()


def encode_str_list(strs: list[str]) -> str:
    return ",".join(strs)


def decode_str_list(str: str) -> list[str]:
    return str.split(",")
