import requests
from bs4 import BeautifulSoup
import json


def get_cost(columns):
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
    cost = {"coins": None, "potions": None, "debt": None}
    for item in costs:
        if item == "p":
            cost["potions"] = 1
        elif item[-1] == "d":
            cost["debt"] = int(item[:-1])
        else:
            cost["coins"] = int(item)

    return cost


def get_text(columns):
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


def get_image(columns):
    img_tag = str(columns[0].find("img"))
    img = img_tag[img_tag.find("src") + 4 : img_tag.find("width")].strip().strip('"')

    return f"http://wiki.dominionstrategy.com{img}"


def get_link(columns):
    link_tag = str(columns[0].find_all("a")[0])
    link = (
        link_tag[link_tag.find("href") + 5 : link_tag.find("title")].strip().strip('"')
    )

    return f"http://wiki.dominionstrategy.com{link}"


def get_card_data(soup):
    cards = []

    table_rows = soup.find_all("table", class_="wikitable sortable")[0].find_all("tr")

    for row in table_rows[1:]:
        columns = row.find_all("td")
        name = columns[0].find_all("a")[0].find_all("span")[0].text
        expansion = columns[1].find_all("a")[0].text
        types = [word.strip() for word in columns[2].text.split("-")]
        cost = get_cost(columns)
        text = get_text(columns)
        img = get_image(columns)
        link = get_link(columns)
        cards.append(
            {
                "name": name,
                "expansion": expansion,
                "types": types,
                "coins": cost["coins"],
                "potions": cost["potions"],
                "debt": cost["debt"],
                "text": text,
                "img": img,
                "link": link,
            }
        )

    return cards


def write_to_file(data, path):
    with open(path, "w") as file:
        file.write(json.dumps(data, indent=2))


if __name__ == "__main__":
    URL = "http://wiki.dominionstrategy.com/index.php/List_of_cards"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    data = get_card_data(soup)
    write_to_file(data, "./data/dominion_cards.json")
