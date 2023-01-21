from pathlib import PurePath
from typing import List

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

from ptm_torrent.onnx import (expectedOnnxHTMLPath, jsonMetadataPath,
                              rootHTMLPath)
from ptm_torrent.utils.fileSystem import saveJSON


def prepareData(dfs: List[DataFrame]) -> DataFrame:
    df: DataFrame
    for df in dfs:
        df.columns = [pair[0] for pair in df.columns]

    data: DataFrame = pandas.concat(objs=dfs, ignore_index=True)

    data["hfURLs"] = data[data.columns[-2:]].apply(
        lambda x: "".join(x.dropna().astype(str)), axis=1
    )

    return data


def extractData(row: Series) -> dict:
    modelClass: str = row["Model Class"][0]

    modelREADMEPath: str | None
    try:
        uri: PurePath = PurePath(row["Model Class"][1])
        modelREADMEPath: str = PurePath(
            f"{rootHTMLPath}/README_{uri.stem}.html"
        ).__str__()
    except TypeError:
        modelREADMEPath = None

    paper: str = row["Reference"][1]
    description: str = row["Description"][0]

    huggingFaceSpaceURL: str | None
    try:
        huggingFaceSpaceURL = row["hfURLs"][1]
    except IndexError:
        huggingFaceSpaceURL = None

    data: dict = {
        "ModelClass": modelClass,
        "ModelREADMEPath": modelREADMEPath,
        "Paper": paper,
        "Description": description,
        "HFSpaceURL": huggingFaceSpaceURL,
    }

    return data


def main() -> None:
    json: List[dict] = []

    tables: List[DataFrame] = pandas.read_html(
        io=expectedOnnxHTMLPath, extract_links="all"
    )

    data: DataFrame = prepareData(dfs=tables)
    dataSize: int = len(data)

    with Bar("Extracting data from HTML tables...", max=dataSize) as bar:
        idx: int
        for idx in range(dataSize):
            row: Series = data.iloc[idx]
            json.append(extractData(row))
            bar.next()

    saveJSON(json, filepath=PurePath(f"{jsonMetadataPath}/onnx_metadata.json"))


if __name__ == "__main__":
    main()
