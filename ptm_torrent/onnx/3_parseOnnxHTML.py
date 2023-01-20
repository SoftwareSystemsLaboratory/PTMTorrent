from collections import namedtuple
from pathlib import PurePath
from typing import List, Tuple, Type

from bs4 import BeautifulSoup, ResultSet, Tag
from progress.bar import Bar

from ptm_torrent.onnx import (expectedOnnxHTMLPath, jsonMetadataPath,
                              rootHTMLPath)
from ptm_torrent.utils.fileSystem import saveJSON

TableCell = namedtuple(
    typename="TableCell",
    field_names=[
        "id",
        "Model",
        "ModelREADMEURI",
        "PaperURL",
        "Description",
        "HuggingFaceURL",
        "Category",
    ],
    defaults=[None, None, None, None, None, None, None],
)


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


def convertFourColumn(
    group: Tuple[Tag, Tag, Tag, Tag] | Tuple[Tag, Tag, Tag], category: str, id: int
) -> Type[tuple]:
    modelName: str = group[0].text.strip()
    paperURL: str = group[1].find(name="a").get(key="href")
    description: str = group[2].text.strip()

    modelREADMEPath: str | None
    try:
        uri: PurePath = PurePath(group[0].find(name="a").get(key="href"))
        modelREADMEPath: str = PurePath(
            f"{rootHTMLPath}/README_{uri.stem}.html"
        ).__str__()
    except AttributeError:
        modelREADMEPath = None

    hfURL: str | None
    if len(group) == 4:
        try:
            hfURL = group[3].find(name="a").get(key="href")
        except AttributeError:
            hfURL = None

    else:
        hfURL = None

    return TableCell(
        id=id,
        Model=modelName,
        ModelREADMEURI=modelREADMEPath,
        PaperURL=paperURL,
        Description=description,
        HuggingFaceURL=hfURL,
        Category=category,
    )


def getModelInformation(soup: BeautifulSoup, categories: List[str]) -> List[dict]:
    data: List[dict] = []
    id: int = 0

    tables: ResultSet = soup.find_all(name="table")

    categoryAmount: int = len(categories)
    tableAmount: int = len(tables)

    categories = categories[0 : tableAmount - categoryAmount]

    rawData: List[Tuple[str, Tag]] = list(zip(categories, tables))

    with Bar(
        f"Creating JSON from {expectedOnnxHTMLPath} tables...", max=len(tables)
    ) as bar:
        pair: Tuple[str, Tag]
        for pair in rawData:
            table: Tag = pair[1]

            thCount: int = len(table.find_all(name="th"))
            cells: ResultSet = table.find_all(name="td")

            if thCount == 4:
                cellGroupings: List[Tuple[Tag, Tag, Tag, Tag]] = list(
                    zip(*(iter(cells),) * 4)
                )

            if thCount == 3:
                cellGroupings: List[Tuple[Tag, Tag, Tag]] = list(
                    zip(*(iter(cells),) * 3)
                )

            group: Tuple[Tag, Tag, Tag, Tag] | Tuple[Tag, Tag, Tag]
            for group in cellGroupings:
                dataTuple: Type[tuple] = convertFourColumn(
                    group=group, category=pair[0], id=id
                )
                id += 1

                json: dict = dataTuple._asdict()
                data.append(json)

            bar.next()

    return data


def main() -> None:
    jsonFilepath: PurePath = PurePath(f"{jsonMetadataPath}/onnx_metadata.json")
    soup: BeautifulSoup = createSoup()

    unorderedLists: ResultSet = soup.find_all(name="ul")
    unorderedLists = unorderedLists[0:3]

    categories: List[str] = getCategories(soup)

    json: List[dict] = getModelInformation(soup, categories)
    saveJSON(json=json, filepath=jsonFilepath)


if __name__ == "__main__":
    main()
