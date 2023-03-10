from pathlib import PurePath
from typing import List

import pandas
from bs4 import BeautifulSoup, ResultSet, Tag
from pandas import DataFrame, Series
from progress.bar import Bar

import ptm_torrent.onnxmodelzoo as omz
from ptm_torrent.utils.fileSystem import readHTML, saveJSON


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


def prepareData(dfs: List[DataFrame], categories: List[str]) -> DataFrame:
    df: DataFrame
    for df in dfs:
        df.columns = [pair[0] for pair in df.columns]
        df["Category"] = categories.pop(0)

    data: DataFrame = pandas.concat(objs=dfs, ignore_index=True)

    data["hfURLs"] = data[data.columns[-3:-2]].apply(lambda x: x.dropna(), axis=1)

    return data


def extractData(row: Series, id: int) -> dict:
    modelClass: str = row["Model Class"][0]

    modelREADMEPath: str | None
    uri: str | None
    try:
        uri = PurePath(row["Model Class"][1])
        modelREADMEPath: str = (
            f"{omz.onnxmodelzoo_ModelHTMLPath}/README_{uri.stem}.html".__str__()
        )
        uri = uri.__str__()
    except TypeError:
        uri = None
        modelREADMEPath = None

    paper: str = row["Reference"][1]
    description: str = row["Description"][0]

    huggingFaceSpaceURL: str | None
    try:
        huggingFaceSpaceURL = row["hfURLs"][1]
    except TypeError:
        huggingFaceSpaceURL = None

    category: str = row["Category"]

    data: dict = {
        "id": id,
        "ModelClass": modelClass,
        "ModelREADMEPath": modelREADMEPath,
        "RepoREADMEPath": uri,
        "Paper": paper,
        "Description": description,
        "HFSpaceURL": huggingFaceSpaceURL,
        "Category": category,
    }

    return data


def main() -> None:
    json: List[dict] = []

    soup: BeautifulSoup = readHTML(htmlFilePath=omz.onnxmodelzoo_HubHTMLMetadataPath)
    categories: List[str] = getCategories(soup)

    tables: List[DataFrame] = pandas.read_html(
        io=omz.onnxmodelzoo_HubHTMLMetadataPath, extract_links="all"
    )

    categories = categories[0 : len(tables) - len(categories)]

    data: DataFrame = prepareData(dfs=tables, categories=categories)
    dataSize: int = len(data)

    with Bar("Extracting data from HTML tables...", max=dataSize) as bar:
        idx: int
        for idx in range(dataSize):
            row: Series = data.iloc[idx]
            json.append(extractData(row, id=idx))
            bar.next()

    saveJSON(json, filepath=omz.onnxmodelzoo_HubJSONMetadataPath)


if __name__ == "__main__":
    main()
