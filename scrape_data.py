import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from app.core.config import settings

NON_SUPPLY_TYPES = [
    "Ally",
    "Artifact",
    "Boon",
    "Event",
    "Heirloom",
    "Hex",
    "Landmark",
    "Prize",
    "Project",
    "Shelter",
    "Spirit",
    "State",
    "Way",
    "Zombie",
]


def get_cost(columns) -> dict[str, int | None]:
    images = columns[3].find_all("img")
    costs = [
        str(image)
        .removeprefix("<img alt=")
        .split('"')[1]
        .lower()
        .removesuffix("plus")
        .removesuffix("star")
        .removeprefix("$")
        for image in images
    ]
    cost: dict[str, int | None] = {"coins": None, "potions": None, "debt": None}
    for item in costs:
        if item == "p":
            cost["potions"] = 1
        elif item[-1] == "d":
            cost["debt"] = int(item[:-1])
        else:
            cost["coins"] = int(item)

    return cost


def get_text(columns) -> str:
    html_text = columns[4]
    for span in html_text.find_all("span", class_="coin-icon"):
        img = html_text.find("img", alt=True)
        span.replace_with(img["alt"])
    for span in html_text.find_all("span"):
        span.unwrap()
    for b in html_text.find_all("b"):
        b.unwrap()
    html_text.smooth()
    text = html_text.get_text(separator="\n", strip=True)

    return text


def get_image(columns) -> str:
    img_tag = str(columns[0].find("img"))
    img = img_tag[img_tag.find("src") + 4 : img_tag.find("width")].strip().strip('"')

    return f"http://wiki.dominionstrategy.com{img}"


def get_link(columns) -> str:
    link_tag = str(columns[0].find_all("a")[0])
    link = (
        link_tag[link_tag.find("href") + 5 : link_tag.find("title")].strip().strip('"')
    )

    return f"http://wiki.dominionstrategy.com{link}"


def get_card_data(soup: BeautifulSoup) -> list[dict[str, str | int | list[str] | bool]]:
    cards: list[dict[str, str | int | list[str] | bool]] = []

    table_rows = soup.find_all("table", class_="wikitable sortable")[0].find_all("tr")

    pbar = tqdm(table_rows[1:], bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")
    for row in pbar:
        columns = row.find_all("td")
        name: str = columns[0].find_all("a")[0].find_all("span")[0].text
        expansion: str = columns[1].find_all("a")[0].text
        types: list[str] = [word.strip() for word in columns[2].text.split("-")]
        cost = get_cost(columns)
        text = get_text(columns)
        img = get_image(columns)
        link = get_link(columns)
        pbar.set_description(f"Scraping {name}")
        cards.append(
            {
                "name": name,
                "expansion": expansion,
                "types": types,
                "coins": cost["coins"],
                "potions": cost["potions"],
                "debt": cost["debt"],
                "text": text,
                "img_path": img.replace("http://", "https://"),
                "link": link.replace("http://", "https://"),
                "in_supply": "this is not in the supply" not in text.lower()
                and all(t not in NON_SUPPLY_TYPES for t in types),
            }
        )

    return cards


def write_to_file(
    data: list[dict[str, str | int | list[str] | bool]], path: Path
) -> None:
    with path.open("w") as file:
        file.write(json.dumps(data, indent=2))


if __name__ == "__main__":
    page = requests.get(str(settings.CARD_LIST_URL))

    soup = BeautifulSoup(page.content, "html.parser")

    data = get_card_data(soup)

    write_to_file(data, settings.DATA_PATH)
