from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag

from ptm_torrent.onnx import expectedOnnxHTMLPath


def createSoup() -> BeautifulSoup:
    with open(expectedOnnxHTMLPath, "r") as htmlFile:
        soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")
        htmlFile.close()
    return soup


def getCategories(soup: BeautifulSoup) -> List[str]:
    categories: List[str] = []

    unorderedLists: ResultSet = soup.find_all(name="ul")
    unorderedLists = unorderedLists[0:3]

    tag: Tag
    for tag in unorderedLists:
        results: ResultSet = tag.findAll(name="a")

        result: Tag
        for result in results:
            categories.append(result.get(key="href")[1::])

    return categories


def main() -> None:
    soup: BeautifulSoup = createSoup()

    unorderedLists: ResultSet = soup.find_all(name="ul")
    unorderedLists = unorderedLists[0:3]

    categories: List[str] = getCategories(soup)
    print(categories)


if __name__ == "__main__":
    main()
