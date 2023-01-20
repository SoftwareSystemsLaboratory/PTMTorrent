from pathlib import PurePath
from typing import List, Tuple

from bs4 import BeautifulSoup, ResultSet, Tag

from ptm_torrent.onnx import expectedOnnxHTMLPath, rootHTMLPath


def createSoup() -> BeautifulSoup:
    with open(expectedOnnxHTMLPath, "r") as htmlFile:
        soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")
        htmlFile.close()
    return soup


def getCategories(soup: BeautifulSoup) -> List[str]:
    validCategories: List[str] = []

    categories: ResultSet = soup.find_all(name="a")

    category: Tag
    for category in categories:
        name: str | None = category.get(key="name")

        if name == None:
            continue

        validCategories.append(name)

    return validCategories


def getModelInformation(soup: BeautifulSoup, categories: List[str]) -> List[dict]:
    data: List[dict] = []
    paths: list = []

    tables: ResultSet = soup.find_all(name="table")

    categoryAmount: int = len(categories)
    tableAmount: int = len(tables)

    categories = categories[0 : tableAmount - categoryAmount]

    rawData: list[tuple[str, Tag]] = list(zip(categories, tables))

    pair: tuple[str, Tag]
    for pair in rawData:
        table: Tag = pair[1]

        thCount: int = len(table.find_all(name="th"))
        cells: ResultSet = table.find_all(name="td")

        if thCount == 4:
            cellGroupings: List[tuple[Tag, Tag]] = list(zip(*(iter(cells),) * 2))[::2]

        if thCount == 3:
            bigGroups: List[tuple[Tag, Tag]] = list(zip(*(iter(cells),) * 3))
            cellGroupings = [grouping[0:2] for grouping in bigGroups]

        grouping: Tuple[Tag, Tag]
        for grouping in cellGroupings:
            try:
                uri: PurePath = PurePath(grouping[0].find(name="a").get(key="href"))
                doi: str = grouping[1].find(name="a").get(key="href")
            except AttributeError:
                continue

            readmePath: PurePath = PurePath(f"{rootHTMLPath}/README_{uri.stem}.html")

            json: dict = {"category": pair[0], "readmePath": readmePath, "doi": doi}
            data.append(json)

    return data


def main() -> None:
    soup: BeautifulSoup = createSoup()

    unorderedLists: ResultSet = soup.find_all(name="ul")
    unorderedLists = unorderedLists[0:3]

    categories: List[str] = getCategories(soup)

    json: List[dict] = getModelInformation(soup, categories)


if __name__ == "__main__":
    main()
