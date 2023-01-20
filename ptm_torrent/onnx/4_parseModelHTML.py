from pathlib import PurePath
from typing import List

import pandas
from bs4 import BeautifulSoup, ResultSet, Tag
from pandas import DataFrame
from progress.bar import Bar

from ptm_torrent.onnx import expectedOnnxMetadataJSONPath
from ptm_torrent.utils.fileSystem import readJSON


def getTable(soup: BeautifulSoup) -> ResultSet:
    return soup.find_all(name="table")


def main() -> None:
    onnxJSON: List[dict] = readJSON(expectedOnnxMetadataJSONPath)

    readmePaths: List[PurePath] = [
        PurePath(data["ModelREADMEURI"])
        for data in onnxJSON
        if data["ModelREADMEURI"] != None
    ]

    with Bar(
        "Finding model specific information from README files...", max=len(readmePaths)
    ) as bar:

        readmePath: PurePath
        for readmePath in readmePaths:
            print(readmePath)
            with open(readmePath, "r") as readme:
                soup: BeautifulSoup = BeautifulSoup(markup=readme, features="lxml")
                readme.close()

            table: ResultSet = getTable(soup)
            tag: Tag
            for tag in table:
                headers: List[str] = [th.text.strip() for th in tag.find_all(name="th")]

                cells: ResultSet = tag.find_all(name="td")
                for cell in cells:
                    print(cell)
                    input()

                input()

            bar.next()


if __name__ == "__main__":
    main()
