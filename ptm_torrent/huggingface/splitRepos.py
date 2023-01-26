from typing import List

import pandas
import numpy as np
from pandas import DataFrame
from progress.bar import Bar
from progress.spinner import Spinner

import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneRepo


def readJSONData(json: dict) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data...") as spinner:
        obj: dict
        for obj in json:
            data.append(f"https://huggingface.co/{obj['id']}")
            spinner.next()

    return data


def shrinkDataFrame(df: DataFrame, shrinkage: float = 0.1) -> DataFrame:
    if shrinkage >= 1:
        return df

    dfSize: int = len(df)
    lastRow: int = int(dfSize * shrinkage)

    return df.iloc[0:lastRow, :]


def main(shrinkage: float = 0.1) -> None:
    if testForFile(path=hf.huggingface_HubMetadataPath) == False:
        return False

    print(f"Loading {hf.huggingface_HubMetadataPath} into DataFrame...")
    df: DataFrame = pandas.read_json(hf.huggingface_HubMetadataPath)

    print(f"Sorting DataFrame rows by download...")
    df.sort_values(by="downloads", ascending=False, inplace=True)
    df.reset_index(inplace=True)

    print(f"Reducing the size of the DataFrame by {shrinkage * 100}%...")
    df = shrinkDataFrame(df, shrinkage)

    urls: List[str] = [f"https://huggingface.co/{id}" for id in df["id"]]
    split_urls = map(lambda x: x.tolist(), np.array_split(urls, 100))

    for i, split_url in enumerate(split_urls):
        with open(f"./split_urls/split_url_{i}.txt", "w", newline="\n") as f:
            f.writelines([url + "\n" for url in split_url])


if __name__ == "__main__":
    main()
